# Radar classification on processed RF signals

**Neil Hamilton Jr**

## Executive Summary
**Overview and Goals:** There is a need in the defense sector to have quick responses to incoming threats.  The goal here is to be able to determine what a threat is quickly and provide guidance on how to respond or provide an automated response.  I was to build a model that can be trained to take features pulled from a signal processed RF signature.  When a new signature is received, the model can then classify it accurately.

**Results:** During this project I was able to build a model that could very accurately predict what type of radar the data represented.  There's a caveat in that the data the model was trained on was synthetic.  The model was able to hit more than a 99% accuracy.  What this project did provide was a blueprint to creating a model that could train on real world data and provide reasonable predictions.

**Future Work:** The future work here is to build up a more complex synthetic data set prior to gaining access to real world data.  There are many more radars than the 20 I included for this data set.  Many new radars include advanced features that will need to be included in the synthetic data set.

## Project Goal
The project goal was to provide the blueprint to generating a model to predict a radar type based on various extracted features from the raw RF signature.

## Exploratory Data Analysis (EDA)
This phase of the project is to inspect, clean, and transform the data in preparation for modeling.  After the data prep, various models will be tested to determine the final model to use for the evaluation.  The EDA notebook can be found [here](Capstone_EDA.ipynb).

### Data
Here the data set was generated.  The main reason for this was that real data is not publicly accessable.  I discussed my project with an industry expert and he helped me structure the synthetic data to be representative of what real world data would provide.  The data is limited to 24 radars and 10 different types.

The process to generate the dataset is to run the python function generate_radar_dataset found in the python file ([data/CapstoneDataGenerator.py](data/CapstoneDataGenerator.py)).

Example call from Capstone_EDA.ipynb:
import data.CapstoneDataGenerator as cdg
cdg.generate_radar_dataset(200000, "data/radar_dataset_200k.zip", 42)

### Data Preparation
This dataset didn't have any missing or NaN fields because I generated the data.  However, this would be the first step when working with real world data.

**Transformations:** The transformations utilized were a standard scaler and a label encoder.  The scaler is used to normalize the numeric data which aids models accuracy.  The label encoder is to take object type columns and enumerate unique values to a number.  This allows one to use many functions to visualize or evaluate models (e.g. corr()).

### Initial Modeling
As part of the EDA I wanted to find my model selection for the dataset.  I tried multiple models and grid searched the hyperparameters to find the ideal settings for each model type.

**NOTE:** The grid searches took a long time to complete.

**Baseline Model**
Here I utilized the sklearn provided DummyClassifier.  This is a simple model that essentially randomly selects a class and provides a baseline score to compare other models to.

**Linear Regression** The linear regression model performed well with accuracy scores in the high 90s.  The grid search found the best parameters as follows:
- C = 1.0
- fit_intercept = True
- max_iter = 200

**Decision Tree** The decision tree perfomed a small amount better than the Linear Regression.  The grid search found the best parameters as follows:
- max_depth = None
- min_samples_leaf = 1
- min_samples_split = 2

This model performed well enough but I decided to apply a boosting technique on it as well to see if I could squeeze out more performance.

**Boosted Decision Tree** For the boosted tree model, I wrapped a decision tree base model with an AdaBoostClassifier.  This boosting will create many weak decision trees but combines all their results to produce a stronger model.  The grid search provided the following best parameters:
- max_depth = 5
- min_samples_leaf = 4
- min_samples_split = 5
- learning_rate = 0.1
- n_estimators = 200

This model performed just as good as the decision tree.  It is interesting to note that the hyperparameters for the decision trees are quite different from the decision tree alone.  However, the boosting method creates many weak models and these parameters would create a small trees.

**Random Forest** This was the best performing model by a small margin.  The main reason I selected this model was the training times.  The boosted decision tree took a very long time and the random forest model alone is simpler to implement.  The grid search for this model produced these best parameters:
- max_depth = None
- min_samples_leaf = 1
- min_samples_split = 2
- n_estimators = 500

I took this model into evaluation to interpret the results and contemplate future enhancements and next steps.

## Evaluation
The evaluation phase setup was exactly the same as during the EDA.  There was the data preparation and transformations.  After that, I collected some statistics and provided some model interpretation techniques.

**Statistics:** For the statistics, I ran the classification_report.  This model acheived the following weighted average results:
- precision - 0.9991
- recall - 0.9990
- f1-score - 0.9991

This data set was quite balanced so the f1-score is not as important.  With this application, I would say both false negatives and positives are equally bad.  If I were to choose, I'd say that false negatives are a bit worse. This means that the recall score should be maximized.  For this data, the model is performing well.

These scores feel much higher than likely due to the generated data set with a limited number of unique radars.  Again also no advanced radar techniques.

**Additional Testing** Here I generated some new samples and tested the model against new data.  Here the model perfomed well and correctly classified all 100 samples.

**Feature Importance** I checked the feature importance to determine how the model was working under the hood.  For this model the following importances were found:
       Feature  Importance
0    Frequency    0.249654
1    Bandwidth    0.184461
5          PRI    0.182907
2  Pulse Width    0.179050
7         Band    0.107248
4     Encoding    0.058769
3   Modulation    0.037057
6    Amplitude    0.000854

These importances make sense to me.  I would have expected frequency to be the most important.  Bandwidth was a bit unexpected, but PRI and pulse width were expected to be near the top of importance.

**Permutation Importance** Here we want to look at how the accuracy of the model decreases if a features values are shuffled around.  Here we didn't see a large decrease in the accuracy score over each feature.  This means that the features are mostly independent and that there are likely other features that can predict the correct class.

Frequency   - 1.14256250e-01
Bandwidth   - 1.85107500e-01
Pulse Width - 1.89475625e-01
Modulation  - 1.56250000e-04
Encoding    - 7.88750000e-04
PRI         - 2.17790000e-01
Amplitude   - 1.58750000e-04
Band        - 9.50181250e-02

## Links to Project Files

Data - See Data section on how to run the data generation script

[EDA](Capstone_EDA.ipynb)

[Evaluation](Capstone_Evaluation.ipynb)