import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression

x = [[6], [8], [10], [14], [18]]
y = [[7], [9], [13], [17.5], [18]]
model = LinearRegression()
model.fit(x,y)

plt.figure()
plt.title('Pizza price statistics')
plt.xlabel('Diameter (inches)')
plt.ylabel('Price (dollars)')
plt.plot(x,y,'.')
plt.plot(x,model.predict(x),'--')
plt.axis([0,25,0,25])
plt.grid(True)
plt.show()

print ("Predicted price = ",model.predict([[21]]))
