* Problem: Given n points (x<sub>i</sub>, y<sub>i</sub>), we want to predict what **y** would be for any **new x**.
* Solution: Find a **linear regression predictor/function** that fit(拟合) or approximate(逼近) existing data.
  
  * y = k <sup>**.**</sup> x + b 
* Optimization: The find the best fit of **k** and **b**, we need to define a loss/cost function
  * Loss function: Loss =  （ Σ(y<sub>i</sub> - y)<sup>2 </sup>)<sup>1/2</sup> = ( Σ(y<sub>i</sub> - k <sup>**.**</sup> x<sub>i</sub> + b)<sup>2</sup> )<sup>1/2</sup>     Note: **Loss is in terms of y, x is set the same.**
    * Explanation: The representation is **Root Square Error**
    * Another representation is **Mean Square Error**: 1/n  <sup>**.**</sup> ( Σ(y<sub>i</sub> - y)<sup>2 </sup>)
  * Then the goal to find the best fit linear function has been translated to find the k and b so that the loss function can be the **smallest**. 
  * Obviously, loss function is two variable quadratic equation (二元二次方程) It has a curve plot. When the derivative of Loss function is equal to 0, that point will make the loss function reach the lowest value.  So the problem becomes computing the derivative when its value is 0.
  * Algorithm: 
    * gradient descent: because it is difficult to compute two partial derivative = 0 (相当于求解两个二元一次方程):
    
      * d<sub>y</sub>/d<sub>k</sub> = Σ 2/n <sup>**.**</sup> x (y<sub>i</sub> - y) = Σ 2/n <sup>**.**</sup> x (y<sub>i</sub> - (kx + b)) = 0
      * d<sub>y</sub>/d<sub>b</sub> = Σ 2/n <sup>**.**</sup> (y<sub>i</sub> - y) =  Σ 2/n <sup>**.**</sup> (y<sub>i</sub> - (kx + b)) = 0
    
       So we will have to approximate to it by finding a starting point, and then minus the   distance = derivative <sup>**.**</sup>α, since this function will converge, we know this will get to the bottom eventually. (k 和 b 是平面上的纵横轴，每次k 和 b 都向球心方向收敛，收敛的距离就是derivative <sup>**.**</sup>α)
    
      * ​	For liner predictor function y = kx + b:
        * ​	k = k - α <sup>**.**</sup> d<sub>y</sub>/d<sub>k</sub> = k - α  <sup>**.**</sup> Σ 2/n <sup>**.**</sup> x (y<sub>i</sub> - y) = k - α  <sup>**.**</sup>  Σ 2/n <sup>**.**</sup> x (y<sub>i</sub> - (kx + b))
        * ​    b = k - α <sup>**.**</sup> d<sub>y</sub>/d<sub>b</sub> = k - α  <sup>**.**</sup> Σ 2/n <sup>**.**</sup> (y<sub>i</sub> - y) = k - α  <sup>**.**</sup>  Σ 2/n <sup>**.**</sup> (y<sub>i</sub> - (kx + b))
    
    * stochastic gradient descent

