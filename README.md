![ui](https://github.com/Madhur-01/Loan-Status-Prediction/assets/108746195/9d90de32-55a7-43cd-82bf-b33e764cead7)
In this project I build and deployed a UI website using Python Flask Server and Streamlit. I analysed various Machine Learning algorithms to predict loan status of a new applicant using various background informations about the applicant and deployed the best one.Parameters like credit score, loan amount, lifestyle, career, income and assets are the deciding factors in getting the loan approval.

Several collections of data from past loan applicants use different features to decide the loan status. A machine learning model can look at this data, which could be static or time-series, and give a probability estimate of whether this loan will be approved.

For this project, I choose the dataset from the Loan Prediction Competition on Kaggle. It has 12 features, one target variable, and 614 samples. The features include Income, Loan Amount, Credit History, Gender, Marital Status, Education, Dependents, and others. This straightforward dataset will be a good measure of finding which ML models work the best.

As opposed to deep learning, traditional machine learning algorithms give a more generalized performance across datasets. I attempted to observe this further in end-to-end implementation of loan prediction machine learning project -

# Machine Learning Solution Approaches for Loan Prediction

1. Support Vector Machine (Classifier) : Support Vector Machine (SVM) is a supervised machine learning algorithm that generates a hyperplane (a decision boundary) to separate classes even in a high-dimensional vector space. SVM is particularly useful in loan prediction because this task usually has several features that need to be considered for the final decision.

2. XGBoost : "Boosting" is a method that combines individual models in an ensemble manner to gain higher performance gain.Extreme Gradient Boost (XGBoost) is an improvement over Gradient Boost and is very popular in binary classification algorithms. The decision trees are built in parallel in XGBoost than in series, giving it an edge over normal Decision Trees and Boosting algorithms.

3. Random Forest Classifier : The random forest algorithm improves the flexibility and decision-making capacity of individual trees.Since we know the fundamentals of decision trees and how they choose features based on information gain, random forests would incorporate these benefits to give superior performance.


 # Results

 1. XGBoost : On testing, I fond that the final binary classification accuracy is around 78.9%. It had a more balanced performance. it found some importance in Property area, loan amount, co-applicant income, dependents, and marital status  in the prediction. However, credit history remains the most crucial feature in determining loan status.

 2. Random Forest Classifier : The test accuracy is around 78%. Credit history, loan amount, and applicant income greatly influence the final decision. For instance, applicants with very high incomes and co-applicant income with a good credit history have an excellent chance of getting loan approval.

 3. Support Vector Classification : the model performed best on a linear kernel with regularization factor C as 1.0 and produced a test score of 78.9%.

 4. Decision Tree : Test accuracy for the decision tree is around 78%. Most other features added little to no influence over the final prediction. This hints at a problem which resulted in most of our models performing similarly. One of the features is significantly more important than the rest, and thus, it biases the loan prediction model performance.

After this analysis I decided to deploy Random Forest Classifier as it accounts all the parameters. 
From this project we can conclude that SVM, XGBoost, and Random Forest are some of the best performing ML models for performing loan prediction and building a loan prediction machine learning project.
