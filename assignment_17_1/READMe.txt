Jupyter Notebook:
https://github.com/Nublaikhan/berkeley-ai-ml-cert/blob/main/assignment_17_1/prompt_III.ipynb

Summary of Findings:
Business Understanding:
The goal here is to train a model that can accurately predict if a bank marketing solicitation will bring a client to subscribing to a term deposit.  I will evaluate multiple models to determine the best selection.

Data Understanding:
The data being utilized for this investigation is from a Portuguese banking institution.  There are 16 features and one target in this data.  Many of the features are categorical and will need some transformation before being used.  The target is a simple 'yes' or 'no' to if the client subscribed a term deposit.

Data Preparation:
I need to transform the categorical data.  I decided to utilize a OneHotEncoder for the categorical data.  This will create a new column for each category and then place a 1 in the column for the actual category and then a zero in all other created columns.  This expanded our number of features to 57.  For all of the numeric features, I used a StandardScaler to normalize the data.  For the target column, I transformed 'yes' to 1 and 'no' to 0.

Modeling:
I am going to evaluate LogisticRegression, KNearestNeighbors, DecisionTree, and SVM classifiers.  To begin, I needed to get a baseline measurement on accuracy.  I decided to use the DummyClassifier for this purpose.  The baseline accuracy score came out to be 88.7%.

Next we took a look at the LogisticRegression classifier.  Using just the default parameters, we trained the model and obtained its accuracy score.  This model's accuracy turned out to be 91.3%.

Then I evaluated a KNearestNeighbors classifier.  Using just the default parameters, I obtained an accuracy score of 90.5%.

The DecisionTree classifier was evaluated next with default parameters.  Its accuracy score was 89.2%.

Lastly, I evaluated a SVM classifier using default parameters.  The default accuracy score was 91.1%

These default scores gave me a good starting point to improve upon.  Next I needed to tune the hyperparameters for each model to try and improve accuracy.  I used GridSearchCV to search over many combinations of hyperparameters and to perform cross-validation of the generated model.

I will refer to the Jupyter Notebook link at the top of this document for the hyperparameters searched through.  I will just give the results of the search here.  Each grid search took quite a bit of time relative to the single model training time.  This is due to the grid search number of parameters, parameter values, and the cross validation of each generated model.

The LogisticRegression search ended up returning the default parameters as the best model.  In turn, the search provided no improvement in accuracy (91.3%).

The KNearestNeighbors search returned a new model but the accuracy score was slightly worse than the default parameters.  The reason behind this is likely due to the parameter search resolution not being fine grained enough to obtain a better model.  The accuracy of the found model was 90.3%

The DecisionTree search returned a slightly better model than the default parameters.  The returned model obtained a 90.7% accuracy score with a 1.5% increase.

The SVM search returned a model that performed almost as good as the default parameter model.  The grid search took a very long time but that was expected as this data set was quite large.  The accuracy score of this model was 91.1%.

Evaluation:
When I took a look at the confusion matricies, I began to think about which incorrect classification is worse for the bank.  False positives will cause some extra work for marketers in extra calls and follow-ups.  The likely worse situation is a false negative.  This would be a client that would subscribe a term deposit but the model said they wouldn't.  This would cause lost business.  Looking at each model's accuracy and false negatives, I would say that a LogisticRegression model would best fit this data.  It has the highest accuracy and the lowest false negative counts.

Next Steps:
If I had more time for fine grained grid searches, I would return to the modeling phase and narrow my grid searches.  I would also head back to the data preparation phase and try to reduce the dimensionality of the data.  This would help with some training times.  A principal component analysis could aid in retaining variance in the data and reduce the number of features.


