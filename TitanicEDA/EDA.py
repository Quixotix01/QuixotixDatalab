import numpy as np
import pandas as pd
df= pd.read_csv(r"C:\Users\Surendar\Desktop\TitanicEDA\TitanicEDA\train.csv")
df_test=pd.read_csv(r"C:\Users\Surendar\Desktop\TitanicEDA\TitanicEDA\test.csv")


##pd.set_option('display.max_columns', None)
##print(df)

"""# **EDA**"""

print(df.info())

print(df.head(10))

print(df.tail(10))

print(df.columns)

print(df.shape)

print(df.duplicated().sum())

print(df.isnull().sum())

import matplotlib.pyplot as plt
import missingno as ms

ms.bar(df,figsize = (10,5),color="tomato")
plt.title("Bar plot showing missing data values", size = 15,c="r")
plt.show()


df.drop(['Cabin'], axis=1, inplace=True)

print(df.shape)

print(df["Embarked"].unique())

print(df["Embarked"].value_counts())

df["Embarked"]=df["Embarked"].fillna("S")

print(df["Embarked"].value_counts())



print(df["Age"].value_counts())

print(df["Age"].mean())

print(df["Age"].median())

print(df["Age"].mode().value_counts())

print(df.describe().astype(int))


df["Age"] = df["Age"].fillna(df["Age"].mean())

print(df["Age"].isnull().sum())


import matplotlib.pyplot as plt
import missingno as ms

ms.bar(df,figsize = (10,5),color="tomato")
plt.title("Bar plot showing missing data values", size = 15,c="r")
plt.show()


print(df.isnull().sum())


print(df["Survived"].value_counts())

import matplotlib.pyplot as plt
import seaborn as sns

sns.countplot(x="Survived", data=df)
plt.title("count of passengers who survived")
plt.show()

print(df["Sex"].value_counts())

fig,axes = plt.subplots(1,2,figsize=(5,3))
df["Sex"].value_counts().plot(kind="bar", ax=axes[1], color =['DarkRed','indianred'])
df["Sex"].value_counts().plot(kind="pie",ax=axes[0],autopct='%0.1f' ,colormap="Reds")
plt.show()

sns.catplot(x="Sex",hue="Survived", kind="count",data=df,height=3)
plt.show()



sns.countplot(x="Pclass", hue="Survived", data=df, palette="Reds",)
plt.show()


# dropping irelevant columns in train dataset

df.drop(["Name","Ticket","PassengerId"],axis=1,inplace=True)
df.head()


# Encode categorical variables in the training dataset
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

df['Sex'] = le.fit_transform(df['Sex'])
df['Embarked'] = le.fit_transform(df['Embarked'])



#print(df.corr())



# Handle missing values in the training dataset
df["Embarked"] = df["Embarked"].fillna("S")
df["Age"] = df["Age"].fillna(df["Age"].mean())
#df["Fare"] = df["Fare"].fillna(df["Fare"].mean())

print(df)

# Split the data into features and target
X = df.drop("Survived", axis=1)
y = df["Survived"]

# Split data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train.shape, X_test.shape)
print(y_train.shape, y_test.shape)

# Handle missing values in the test dataset
df_test["Age"] = df_test["Age"].fillna(df["Age"].mean())
df_test["Fare"] = df_test["Fare"].fillna(df_test["Fare"].mean())

# Encode categorical variables in the test dataset
df_test['Sex'] = le.fit_transform(df_test['Sex'])
df_test['Embarked'] = le.fit_transform(df_test['Embarked'].fillna("S"))

# Dropping irrelevant columns in the test dataset
X_test = df_test.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Initialize the Logistic Regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Predict on the validation set
#y_pred = model.predict(X_test)

# Calculate the accuracy score
#accuracy = accuracy_score(y_test, y_pred)
#print(f"Accuracy on validation set: {accuracy:.4f}")


# Predict on the test set
predictions = model.predict(X_test)

# Create a DataFrame to save the results
output = pd.DataFrame({'PassengerId': df_test['PassengerId'], 'Survived': predictions})

# Save the predictions to a CSV file
output.to_csv(r"C:\Users\Surendar\Desktop\TitanicEDA\TitanicEDA\submission.csv", index=False)

print("Predictions have been saved to submission.csv")

