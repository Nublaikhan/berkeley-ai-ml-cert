import csv, random, zipfile
import numpy as np

base_rows = [
    # Name,             Type,                               freq_Hz,    pw_s,   mod,    enc,                    pri_s,  amp_dB, band
    ["EWGuard_01",      "Early-warning",                    1.375e9,    7.2e-6, "FM",   "Linear FM (chirp)",    2.3e-3, -18.4,  "L" ],
    ["EWGuard_02",      "Early-warning",                    2.89e9,     5.9e-6, "PM",   "Barker code",          1.8e-3, -12.1,  "S" ],
    ["AirScan_01",      "Air-surveillance",                 1.92e9,     3.4e-6, "AM",   "Unmodulated pulse",    1.1e-3, -8.7,   "L" ],
    ["AirScan_02",      "Air-surveillance",                 3.45e9,     9.5e-6, "FM",   "Linear FM (chirp)",    9.0e-4, -22.3,  "S" ],
    ["TrackLock_01",    "Tracking / fire-control",          9.45e9,     1.1e-6, "PM",   "Phase-coded",          4.5e-4, 3.6,    "X" ],
    ["TrackLock_02",    "Tracking / fire-control",          13.8e9,     8.8e-6, "FM",   "Linear FM (chirp)",    7.2e-4, -5.2,   "Ku"],
    ["MissileGuide_01", "Missile guidance / illumination",  10.2e9,     6.0e-6, "AM",   "Unmodulated CW pulse", 3.1e-4, 9.7,    "X" ],
    ["MissileGuide_02", "Missile guidance / illumination",  15.4e9,     2.3e-6, "PM",   "Barker code",          2.8e-4, -1.9,   "Ku"],
    ["CBRadar_01",      "Counter-battery",                  9.1e9,      4.7e-6, "FM",   "Linear FM (chirp)",    1.6e-3, -27.5,  "X" ],
    ["CBRadar_02",      "Counter-battery",                  5.6e9,      8.2e-6, "PM",   "Phase-coded",          1.2e-3, -15.3,  "C" ],
    ["GroundWatch_01",  "Ground-surveillance",              3.2e9,      5.1e-6, "AM",   "Unmodulated pulse",    1.0e-3, -32.8,  "S" ],
    ["GroundWatch_02",  "Ground-surveillance",              9.7e9,      6.9e-6, "FM",   "Linear FM (chirp)",    8.8e-4, -24.6,  "X" ],
    ["NavSeaScan_01",   "Naval surface-search",             9.3e9,      2.9e-6, "AM",   "Unmodulated pulse",    6.0e-4, -11.0,  "X" ],
    ["NavSeaScan_02",   "Naval surface-search",             9.9e9,      7.6e-6, "FM",   "Linear FM (chirp)",    7.5e-4, -6.4,   "X" ],
    ["AEWWatch_01",     "Airborne early-warning",           1.36e9,     9.9e-6, "PM",   "Phase-coded",          2.0e-3, -19.8,  "L" ],
    ["AEWWatch_02",     "Airborne early-warning",           3.0e9,      6.4e-6, "FM",   "Linear FM (chirp)",    1.7e-3, -14.2,  "S" ],
    ["FighterAESA_01",  "Fighter multi-mode",               10.8e9,     1.9e-6, "PM",   "Polyphase code",       5.0e-4, 12.5,   "X" ],
    ["FighterAESA_02",  "Fighter multi-mode",               11.6e9,     7.1e-6, "FM",   "Linear FM (chirp)",    4.2e-4, 6.1,    "X" ],
    ["SARMapper_01",    "SAR / imaging",                    9.65e9,     8.7e-6, "FM",   "Linear FM (chirp)",    1.4e-3, -21.7,  "X" ],
    ["SARMapper_02",    "SAR / imaging",                    35.2e9,     2.7e-6, "PM",   "Phase-coded",          9.5e-4, -29.9,  "Ka"],
]

mods = ["AM","FM","PM"]
encodings = [
    "Unmodulated pulse",
    "Linear FM (chirp)",
    "Barker code",
    "Phase-coded",
    "Polyphase code",
    "Unmodulated CW pulse"
]

def band_from_freq(f):
    ghz = f / 1e9
    if 1.0 <= ghz < 2.0: return "L"
    if 2.0 <= ghz < 4.0: return "S"
    if 4.0 <= ghz < 8.0: return "C"
    if 8.0 <= ghz < 12.0: return "X"
    if 12.0 <= ghz < 18.0: return "Ku"
    if 27.0 <= ghz < 40.0: return "Ka"
    return None  # or clip/skip

with open("radar_dataset_200k.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["Name","Type","Frequency","Pulse Width","Modulation","Encoding","PRI","Amplitude","Band"])
    N = 200_000
    for i in range(N):
        base = random.choice(base_rows)
        name, rtype, f0, pw0, m0, e0, pri0, a0, b0 = base

        # Gaussian noise (tune sigmas as desired)
        f = np.random.normal(f0, f0*0.002)          # 0.2% std dev
        pw = np.random.normal(pw0, pw0*0.05)        # 5% std dev
        pri = np.random.normal(pri0, pri0*0.05)     # 5% std dev

        # Optionally constrain PRI to be positive
        if pri <= 0:
            pri = pri0

        # Occasionally change modulation and or encoding (e.g., 10% chance each)
        mod = m0
        if random.random() < 0.1:
            mod = random.choice(mods)

        enc = e0
        if random.random() < 0.1:
            enc = random.choice(encodings)

        # Update band if frequency crosses boundary
        band = band_from_freq(f)
        if band is None:
            # fall back to original
            f = f0
            band = b0

        # Random amplitude
        amp = random.uniform(-50.0, 30.0)

        w.writerow([name, rtype, f, pw, mod, enc, pri, amp, band])

with zipfile.ZipFile("radar_dataset_200k.zip","w",compression=zipfile.ZIP_DEFLATED) as z:
    z.write("radar_dataset_200k.csv")
