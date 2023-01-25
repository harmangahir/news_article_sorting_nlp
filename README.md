# News Article Sorting
## Problem Statement:
In today’s world, data is power. With News companies having terabytes of data stored in servers, everyone is in the quest to discover insights that add value to the organization. With various examples to quote in which analytics is being used to drive actions, one that stands out is news article classification.
Nowadays on the Internet there are a lot of sources that generate immense amounts of daily news. In addition, the demand for information by users has been growing continuously, so it is crucial that the news is classified to allow users to access the information of interest quickly and effectively. This way, the machine learning model for automated news classification could be used to identify topics of untracked news and/or make individual suggestions based on the user’s prior interests.

## Approach: 
Techniques like clustering and associating rule-based algorithms can be applied to group together similar text. The ML algorithms learn the mapping function between the text and the tags based on already categorized data. Algorithms such as SVM, Neural Networks, Random Forest are commonly used for text classification.

## Results: 
For a given news article, the system should be able to classify them according to various categories like Finance, Sports etc.
You have to build a solution that should recognize and classify the news articles based on their labels.

## Dataset:
Dataset Link:Link


## Project Evaluation metrics:
## Code: 
• You are supposed to write a code in a modular fashion 
• Safe: It can be used without causing harm. 
• Testable: It can be tested at the code level. 
• Maintainable: It can be maintained, even as your codebase grows. 
• Portable: It works the same in every environment (operating system) 
• You have to maintain your code on GitHub. 
• You have to keep your GitHub repo public so that anyone can check your code. 
• Proper readme file you have to maintain for any project development. 
• You should include basic workflow and execution of the entire project in the readme file on GitHub • Follow the coding standards: https://www.python.org/dev/peps/pep-0008/


## Database:
• You are supposed to use a given dataset for this project which is a Cassandra database. • https://astra.dev/ineuron
Cloud:
• You can use any cloud platform for this entire solution hosting like AWS, Azure or GCP
API Details or User Interface:
• You have to expose your complete solution as an API or try to create a user interface for your model testing. Anything will be fine for us.

## Logging:
• Logging is a must for every action performed by your code use the python logging library for this.


### Software and tools requirements

1. [Github Account](https://github.com)
2. [VS Code IDE](https://code.visualstudio.com)
3. [Heroku Account](https://heroku.com)
4. [GitCLI](https://cli.github.com/)

### Purposed Solution
A BBC labelled public dataset of 1490 stories is utilised for prediction using several algorithms. I applied following ML and DL models for prediction:
1. [Multinomial Naive Bayes]
2. [Bernoulli Naive Bayes]
3. [Complement Naive Bayes]
4. [K-Nearest Neighbour]
5. [Stochastic Gradient Descent]
6. [Logistic Regression]

Despite above, three deep learning models applied:
1. [LSTM]
2. [Bi-Directional LSTM]
3. [Gated Recurrent Unit]

 Almost every algorithm is greater than 90% accurate. We employ the Complement Naive Bayes model in the test because it has strong precision (more than 95%), recall (more than 98%), and f1-score (more than 97%) for each class, giving an accuracy of 98%.