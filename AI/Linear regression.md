* Problem: Given n points (x<sub>i</sub>, y<sub>i</sub>), we want to predict what **y** would be for any **new x**.
* Solution: Find a **linear regression predictor/function** that fit(拟合) or approximate(逼近) existing data.
  * y = k <sup>**.**</sup> x + b 
* Optimization: The find the best fit of **k** and **b**, we need to define a loss/cost function
  * Loss function: Loss =  （ Σ(y<sub>i</sub> - y)<sup>2 </sup>)<sup>1/2</sup> = ( Σ(y<sub>i</sub> - k <sup>**.**</sup> x<sub>i</sub> + b)<sup>2</sup> )<sup>1/2</sup> 
    * Explanation: The representation is **Root Square Error**
    * Another representation is **Mean Square Error**: 1/n  <sup>**.**</sup> ( Σ(y<sub>i</sub> - y)<sup>2 </sup>)
  * Then the goal to find the best fit linear function has been translated to find the k and b so that the loss function can be the **smallest**. 
  * Obviously, loss function is quadratic equation with two unknowns.(二元二次方程) It has a curve plot. When the derivative of Loss function is equal to 0, that point will make the loss function reach the lowest value.  So the problem becomes computing the derivative when its value is 0.
  * Algorithm: 
    * gradient descent: because it is difficult to compute derivative = 0. we will have to approximate to it.
    * stochastic gradient descent

