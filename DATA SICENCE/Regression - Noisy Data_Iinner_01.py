# Lasso Regression (L1 Regulization)
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Genrate Synthetic data

np.random.seed(10)
DATA1=np.random.rand(100,1)*10   # independent Veriable
DATA2=3*DATA1+7+np.random.rand(100,1)   #independent Veriable with Noise

# Split the dataset
DATA1_train,DATA1_test,DATA2_train,DATA2_test=train_test_split(DATA1,DATA2,test_size=0.3,random_state=42)

# fit the liner Regression model

Model=LinearRegression()
Model.fit(DATA1_train,DATA2_train)

# Make Predictions

DATA2_pred=Model.predict(DATA1_test)

# Evaluate the model

mse=mean_squared_error(DATA2_test,DATA2_pred)

print("mean squared error = ",mse)


# plot the results 
plt.scatter(DATA1_test,DATA2_test,color="blue",label="Acutal Data")
plt.plot(DATA1_test,DATA2_pred,color="red",label="Fitted Line")
plt.legend()
plt.show()