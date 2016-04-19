import numpy as np
import matplotlib.pyplot as plt

def gradientDescent(x, y, theta, alpha, m, numIterations):
    cost_history=[]
    xTrans = x.transpose()
    for i in range(0, numIterations):
        hypothesis = np.dot(x, theta)
        loss = hypothesis - y
        # avg cost per example (the 2 in 2*m doesn't really matter here.
        # But to be consistent with the gradient, I include it)
        cost = np.sum(loss ** 2) / (2 * m)
        cost_history.append(cost)
        print("Iteration %d | Cost: %f" % (i, cost))
        # avg gradient per example
        gradient = np.dot(xTrans, loss) / m
        # update
        theta = theta - alpha * gradient
    return theta, cost_history

def plot_cost(plt,cost_history):
    xs=range(len(cost_history))
    plt.plot(xs,cost_history,color='b')
    plt.ylim(0, max(cost_history))
    plt.title('Cost function vs. number of iterations')
    plt.xlabel('Number of iterations')
    plt.ylabel('Cost function')
    plt.show()


# Test - generate 100 points with a bit of noise
from sklearn.datasets.samples_generator import make_regression
nsamples=100
x, y = make_regression(nsamples, n_features=1, n_informative=1, 
                        random_state=0, noise=5) 
x = np.c_[ np.ones(nsamples), x] # insert column of ones
m, n = np.shape(x)
theta=np.random.random(n)
alpha = 0.01
numIterations= 500
theta, cost_history = gradientDescent(x, y, theta, alpha, m, numIterations)

print(theta)
plt.figure(0)
plot_cost(plt,cost_history) #check that cost function converges to min

predictions=np.dot(x,theta)
xs=[val[1] for val in x]   
plt.figure(1)
plt.scatter(xs,y,color='b',label='Data')
plt.plot(xs,predictions,color='r',linewidth=1,label='Linear regression')
plt.legend(loc=2)
plt.xlabel('x')
plt.ylabel('y')
plt.figure(1)