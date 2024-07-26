import pandas
from sklearn import linear_model
import matplotlib.pyplot as plt

data_frame = pandas.read_csv("data.csv")

X = data_frame[['Weight', 'Volume']]
y = data_frame['CO2']

regressor = linear_model.LinearRegression()
regressor.fit(X, y)

fig, ax1 = plt.subplots()

ax1.scatter(X['Weight'], y)
ax1.set_xlabel('X1')
ax1.set_ylabel('Y')

ax1.scatter(X['Volume'], y)
# ax2.set_xlabel('X2')

y_predictions = []
n = len(X['Weight'])

for i in range(n):
    prediction = regressor.predict([[X['Weight'][i], X['Volume'][i]]])
    y_predictions.append(prediction)

print(y_predictions)
ax1.plot(X['Weight'], y_predictions)

plt.show()