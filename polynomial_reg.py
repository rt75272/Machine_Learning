import matplotlib.pyplot as plt
import random
import numpy
# -----------------------------------------------------------------------------
# Polynomial Regression
#
# Builds up a polynomial regression model using random data points in order to 
# demonstrate how to make basic predictions.
#
# Model Equation:
#   y = b_0 + (b_1 * x_1) + (b_2 * x_2^2) + ... + (b_n * x_n^n)
#
# Usage:
#   $ python polynomial_reg.py
# -----------------------------------------------------------------------------
# Main driver function.
def main():
    # Set domain.
    MAX_X = 20

    # Data point arrays.
    x = []
    y = []

    # Set number of data points.
    n = 20

    # Generate and add random x,y data points.
    for i in range(n):
        x_value = random.randint(0, MAX_X)
        y_value = random.randint(0, 100)
        x.append(x_value)
        y.append(y_value)

    # Setup a polynomial model object.
    # With degree set to 3:
    #   y = b_0 + (b_1 * x_1) + (b_2 * x_2^2) + (b_3 * x_3^3)  
    model = numpy.poly1d(numpy.polyfit(x=x, y=y, deg=3))

    # Generate a array of floats to be our display line. 
    # x-values.
    line = numpy.linspace(start=0, stop=MAX_X, num=MAX_X)

    # Plot original data points.
    plt.scatter(x, y)

    # Fitted prediction line. 
    # y-values.
    fitted_line = model(line)

    # Get a single prediction.
    get_prediction(model)

    # Plot the fitted line of polynomial regression.
    plt.plot(line, fitted_line)
    plt.show()

# Get prediction given an x value.
# Default x value equals 10.
def get_prediction(model, x=10):
    # Assign x value.
    predict_me = x
    # Get the prediction from the model.
    prediction = model(predict_me)
    print(f"At x = 10 the prediction is", prediction)
    return prediction

# Pushing the big red button.
if __name__ == "__main__":
    main()