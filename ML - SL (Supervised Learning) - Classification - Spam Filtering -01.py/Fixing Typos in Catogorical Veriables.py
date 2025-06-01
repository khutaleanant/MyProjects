import pandas as pd

DATASET={"Gender":["Male","MALE","male","M","female","Fem","Female"]}

DATAFRAME=pd.DataFrame(DATASET)

DATAFRAME["Gender"]=DATAFRAME["Gender"].replace({"Male":"Male","male":"Male","M":"Male","MALE":"Male","female":"Female","Fem":"Female","Female":"Female"})

DATAFRAME.to_csv("Corrrected Dataset.csv")