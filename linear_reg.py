import matplotlib.pyplot as plt
from scipy import stats
import random
# -----------------------------------------------------------------------------
# Linear Regression
#
# Builds up a linear regression model using random data points in order to 
# demonstrate how to make basic predictions.
#
# Usage:
#   $ python linear_reg.py
# -----------------------------------------------------------------------------
# Main driver function. 
def main():
    # Data point arrays.
    x = []
    y = []

    # Set number of data points.
    n = 20

    # Generate and add random x,y data points.
    for i in range(n):
        x_value = random.randint(0,10)
        y_value = random.randint(0,10)*i
        x.append(x_value)
        y.append(y_value)

    # Get the stats using linear regression.
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

    # Generates and returns a prediction given an x value. 
    # Uses the equation y = mx + b.
    def get_prediction(x):
        prediction = slope * x + intercept
        return prediction   

    # Assigns a list of predictions using the get_prediction function and x values.
    model = list(map(get_prediction, x))

    # Plots the data points.
    plt.scatter(x,y)

    # Plots the prediction model.
    plt.plot(x, model)

    # Make and display a prediction with an x value of 5.
    predict_me = 5
    prediction = get_prediction(predict_me)
    print(f"At", predict_me, "the prediction is", prediction)

    # Graph display.
    plt.show()

# Pushing the big red button. 
if __name__ == "__main__":
    main()