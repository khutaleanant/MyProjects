import matplotlib
matplotlib.use('Agg') # this code is use for to save particular out put file in particular location.

import matplotlib.pyplot as plt
labels=["Mango","Apple","Banana","Grapes"]
sizes=[20,30,40,10]
colors=["red","blue","green","yellow"]
explode=(0.1,0,0,0)

plt.pie(sizes,labels=labels,colors=colors,explode=explode,autopct="%1.1f%%",startangle=140,shadow=True)
plt.title("Fruit Distribution")
# plt.show()

plt.savefig("Piechart.png")
