
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB


class Algo:
    test_df = pd.read_csv("test.csv")
    train_df = pd.read_csv("train.csv")

    def processing(self, algo_name, pclass, sex, sibling, embark):
        p_class = int(pclass)
        gender = 0 if sex == 'Male' else 1
        sib = int(sibling)
        emb = 0
        if embark == 'S':
            emb = 0
        elif embark == 'C':
            emb = 1
        else:
            emb = 2

        self.train_df = self.train_df.drop(['PassengerId'], axis=1)
        common_value = 'S'
        data = [self.train_df, self.test_df]
        for dataset in data:
            dataset['Embarked'] = dataset['Embarked'].fillna(common_value)

        genders = {"male": 0, "female": 1}
        data = [self.train_df, self.test_df]
        for dataset in data:
            dataset['Sex'] = dataset['Sex'].map(genders)

        ports = {"S": 0, "C": 1, "Q": 2}
        data = [self.train_df, self.test_df]
        for dataset in data:
            dataset['Embarked'] = dataset['Embarked'].map(ports)

        X_train = self.train_df.drop("Survived", axis=1)
        Y_train = self.train_df["Survived"]
        X_test = self.test_df.drop("PassengerId", axis=1).copy()
        X_test = X_test.drop('Sibling', axis=1).copy()
        if algo_name == 'knn':
            knn = KNeighborsClassifier(n_neighbors=3)
            knn.fit(X_train, Y_train)
            Y_pred = knn.predict([[p_class, gender, sib, emb]])
            return Y_pred[0]

        elif algo_name == 'gnb':
            gaussian = GaussianNB()
            gaussian.fit(X_train, Y_train)
            Y_pred = gaussian.predict([[p_class, gender, sib, emb]])
            return Y_pred[0]

        elif algo_name == 'decision tree':
            decision_tree = DecisionTreeClassifier()
            decision_tree.fit(X_train, Y_train)
            Y_pred = decision_tree.predict([[p_class, gender, sib, emb]])
            return Y_pred[0]

        elif algo_name == 'random forest':
            random_forest = RandomForestClassifier(n_estimators=100)
            random_forest.fit(X_train, Y_train)
            Y_prediction = random_forest.predict([[p_class, gender, sib, emb]])
            return Y_prediction[0]

        else:
            logreg = LogisticRegression()
            logreg.fit(X_train, Y_train)
            Y_pred = logreg.predict([[p_class, gender, sib, emb]])
            return Y_pred[0]
