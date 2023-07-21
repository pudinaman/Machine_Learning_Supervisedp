import numpy as np
import matplotlib.pyplot as plt
x_train=np.array([1.0,2.0])
y_train=np.array([300.0,500.0])
print(f"x_train={x_train}")
print(f"y_train={y_train}")
m=x_train.shape[0]
print(f"number o ftraining examples is {m}")
l=len(x_train)
i=0
x_i=x_train[i]
y_i=y_train[i]
print(f"(x^({i}),y^({i}))=({x_i},{y_i})")
#plot data points
plt.scatter(x_train,y_train,marker='x',c='r')
#set the title
plt.title("housing Price")
#set y_axis_label
plt.ylabel("Price (in 1000s of dollars)")
#set x_label
plt.xlabel("Size(1000 sqft)")
plt.show()
