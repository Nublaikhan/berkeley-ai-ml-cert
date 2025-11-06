
Executive Summary:
  I have completed my evaluation of vehicle data.  I believe that I have found some key vehicle features
that will aid you in tailoring your inventory to maximize sales potential.  In short, I've found that the
main driver of pricing are three features. The age of the vehicle, the drive train, and the manufacturer.
Below is a summary of the work done.

Jupyter Notebook Link:
https://github.com/Nublaikhan/berkeley-ai-ml-cert/blob/main/assignment_11_1/prompt_II.ipynb

Data Understanding:
The first task was to get to know the data.  We needed to see what vehicle features were in the data. We
needed to check the quality of the data as well.  I created some visualizations to aid in this understanding.
There were missing data items as well as some outlying data points that needed to be remedied.  In most cases,
you remove these and that is what I did.

Data Preparation:
Here I needed to manipulate the categorical data by changing the text into numeric items so the tools I was
using could 'crunch the numbers' on this data.  I removed the features with significant data missing.  Then
I created some new features like 'age' along side of the year of the vehicle.  I ended up coming back to this
phase of the work to put the pricing data on a logarithmic scale because the model I was working with was
better able to find a fit to the data.  I had to create a few visualizations to see this and that's why I
had to loop back around.  Here I then removed outlying data.  This data was skewing the statistics and made
it difficult to fit a model to this problem.  This is perfectly normal to do.

At this point, I ran an analysis to determine which features really contained most of the information.  This
is what led me to 'age', 'drive', and 'manufacturer'.  Using this knowledge I limited the dataset to these
features to speed up calculations later on.

Modeling:
As I stated above, I had to loop back after a while due to poor model performance.  I couldn't get a model
to predict pricing very well so I had to go back and take a look at the data.  This is when I applied the
logarithmic scale to the pricing data.  From here, I optimized multiple models and chose the best of the
three I looked at.  I picked a Linear Regression model as it had the lowest error in our test data set.

Evaluation:
After evaluation of the models via a method called cross validation, I've found that the models I generated
weren't quite as accurate as we would want.  I need to go back and take another look at my data Preparation
stage to  determine if there are other transformations I can apply to increase the accuracy of the models.

Deployment:
I wouldn't recommend we use this model yet.  Give me some more time and I'll improve the accuracy.




