points = [(1, 651), (2, 762), (3, 856), (4, 1063), (5, 1190), (6, 1298), (7, 1421), (8, 1440), (9, 1518)]

# Training function/model
def f(x, k, b):
    return k * x + b

# Loss/cost function ( in terms of y )
def loss(points, k, b):

    loss = 0
    n = len(points)
    for point in points:
        loss += (point[1] - k * point[0] - b) ** 2
    return loss/n

# partial derivative
def k_partial_derivative(points, k, b):
    # -2x(y - (kx + b))
    derivative = 0
    n = len(points)
    for point in points:
        derivative += (-2/n) * (point[1] - k * point[0] - b) * point[0]
    return derivative

def b_partial_derivative(points, k, b):
    # -2(y - (kx + b))
    derivative = 0
    n = len(points)
    for point in points:
        derivative += (-2/n) * (point[1] - k * point[0] - b)
    return derivative

def gradient_descent(points):

    k = 1
    b = 100
    # alpha has to be very small, otherwise, k/b will jump around, and the loss function will not converge
    alpha = 0.01

    for i in range(0, 10000):
        k -= alpha * k_partial_derivative(points, k, b)
        b -= alpha * b_partial_derivative(points, k, b)

        print(k, end=", ")
        print(b, end="; Loss: ")
        print(loss(points, k, b))


gradient_descent(points)