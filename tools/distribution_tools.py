#Author: Ronnie Ankner
# 2/5/2020
# Purpose: create tools to estimate and work with random variable distributions
#	- Parzen Window Density Estimation from random samples
#	- Inverse CDF creation from arbitrary density
#	- Inverse interpolation of CDF for random variable creation

import numpy
import matplotlib as plt

#============ Parzen Window ==================
#============ CDF Creation ===================
# Input: Probability density function 2xn array with X values and corresponding probabilities
# Output: 1x1000 array where key is analog value [0,1] times 1000 and value of that key is X value of CDF
# For example: CDF is represented as F(X) = U, inverse F^-1(U) = X
# if F^-1(0.230) = 120 then out[230] = 120

#============ Inverse Interpolation ==========
