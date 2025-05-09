from pyexpat import model
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,confusion_matrix

DataFrame=pd.read_csv("C:\Data Science Programs Practice\Company Workforce Forcasating - Empolyee Attrition.csv")

DataFrame_Encoded = pd.get_dummies(DataFrame.drop(["Employee ID"],axis=1),drop_first=True)


# Split features and target
X=DataFrame_Encoded.drop("Attrition_Stayed",axis=1)
y=DataFrame_Encoded["Attrition_Stayed"]

#Train-Test split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

#Train model
model=RandomForestClassifier
model.fit(X_train,y_train)

#Predicut and Evaluate 
y_pred=model.predict(X_test)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
