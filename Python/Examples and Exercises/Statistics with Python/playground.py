from scipy.stats import norm, poisson
from math import sqrt

mu = 100
sigma = 15
n = 30

z_score = (95 - 100) / (sigma / sqrt(n))
p = norm.cdf(z_score)

print(p)