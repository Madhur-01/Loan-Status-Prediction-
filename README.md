# Loan-Status-Prediction-
In this project I analysied various Machine Learning algorithms to predict loan status of a new applicant using various background informations about the applicant.Parameters like credit score, loan amount, lifestyle, career, income and assets are the deciding factors in getting the loan approval.

Several collections of data from past loan applicants use different features to decide the loan status. A machine learning model can look at this data, which could be static or time-series, and give a probability estimate of whether this loan will be approved.

For this project, we choose the dataset from the Loan Prediction Competition on Kaggle. It has 12 features, one target variable, and 614 samples. The features include Income, Loan Amount, Credit History, Gender, Marital Status, Education, Dependents, and others. This straightforward dataset will be a good measure of finding which ML models work the best.

As opposed to deep learning, traditional machine learning algorithms give a more generalized performance across datasets. I attempted to observe this further in end-to-end implementation of loan prediction machine learning project -

1. Support Vector Machine (Classifier) : Support Vector Machine (SVM) is a supervised machine learning algorithm that generates a hyperplane (a decision boundary) to separate classes even in a high-dimensional vector space. SVM is particularly useful in loan prediction because this task usually has several features that need to be considered for the final decision.

2. XGBoost : "Boosting" is a method that combines individual models in an ensemble manner to gain higher performance gain.Extreme Gradient Boost (XGBoost) is an improvement over Gradient Boost and is very popular in binary classification algorithms. The decision trees are built in parallel in XGBoost than in series, giving it an edge over normal Decision Trees and Boosting algorithms.

3. Random Forest Classifier : The random forest algorithm improves the flexibility and decision-making capacity of individual trees.Since we know the fundamentals of decision trees and how they choose features based on information gain, random forests would incorporate these benefits to give superior performance.
