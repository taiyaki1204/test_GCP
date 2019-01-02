#
# titanic ssiviar research
#
import pandas as pd
import numpy as np

TRAIN_DATA = '../input/train.csv'
TEST_DATA = '../input/test.csv'

train = pd.read_csv(TRAIN_DATA)
test = pd.read_csv(TEST_DATA)

###################################################
# data clean:lostdata fill, exchange category data
####################################################

#data replace
##fill lost data as age median
train["Age"] = train["Age"].fillna(train["Age"].median())
##fill lost data as manay data
train["Embarked"] = train["Embarked"].fillna("S")
##Cabin not use

#excahnge category data
train["Sex"] = train["Sex"].map({"male" : 0, "female" : 1})
train["Embarked"] = train["Embarked"].map({"S" : 0, "C" : 1, "Q" : 2})

#data replace
##fill lost data as age median
test["Age"] = test["Age"].fillna(test["Age"].median())
##fill lost data as fare median
test["Fare"] = test["Fare"].fillna(test["Fare"].median())
##Cabin not use

#excahnge category data
test["Sex"] = test["Sex"].map({"male" : 0, "female" : 1})
test["Embarked"] = test["Embarked"].map({"S" : 0, "C" : 1, "Q" : 2})

#show train data
print('=== train ============================================================')
print('headの確認==>\n', train.head())
#show test data
print('=== test ============================================================')
print('headの確認==>\n', test.head())


###################################################
# create decide tree
####################################################

from sklearn import tree

#get train's purpose num and explain num 
target = train["Survived"].values
features_one = train[["Pclass", "Sex", "Age", "Fare"]].values

#create decide tree
my_tree_one = tree.DecisionTreeClassifier()
my_tree_one = my_tree_one.fit(features_one, target)

#get test's explain num
test_features = test[["Pclass", "Sex", "Age", "Fare"]].values

#predict by my_tree_one using test explain num
my_prediction = my_tree_one.predict(test_features)

#show predict data
print('=== predict ============================================================')
print('predictの確認==>\n', my_prediction.shape)
print('predictの確認==>\n', my_prediction)

#Get PassengerId
PassengerId = np.array(test["PassengerId"]).astype(int)

#input PassengerId and my_prediction
my_solution = pd.DataFrame(my_prediction, PassengerId, columns = ["Survived"])

#write as my_tree_one.csv
my_solution.to_csv("my_tree_one.csv", index_label = ["PassengerId"])


