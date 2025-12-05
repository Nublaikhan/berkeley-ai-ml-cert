This investigation was to explore the possibility of creating a model that can classify an RF signal source.
I scoured around for data source and ended up finding some data on kaggle at this location
(https://www.kaggle.com/datasets/suraj520/rf-signal-data).  The evaluation of the data and model generation are
done in this jupyter notebook found here (https://github.com/Nublaikhan/berkeley-ai-ml-cert/tree/main/capstone).

The data looked good at the start.  There were clear RF features for each device type.  I started to clean the
data so that I could perform some analysis.  I performed some LabelEncoder transformations on all the categorical
data.  Some of the NaN data I replaced with either 0 or a category 'None'.  When investigating the I/Q data, I
needed to do some serious conversions to split out all the samples into their own columns.  I scaled the data
performed a principal component analysis to determine how many features I'd need to retain the most variance. It
turns out that there is almost no variance in the data for the device types.

I went ahead and I tested out some models to see what I could see.  I tried some of the basics, LogisticRegression
and DecisionTree.  The accuracy of both of them was around %50.  This make sense given the lack of any variance
between the device types.  I tried some ensemble techniques to see if I could gain anything due to the low
variance.  The AdaBoost and RandomForest classifiers provided no gains.  I've come to the conclusion that this
dataset is too uniform between device types.

Next steps are to find a better set of data that contains some variance between device types.  