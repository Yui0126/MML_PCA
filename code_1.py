#%%
import math

set = [1,2,3,2]

mu = (1+2+3+2+1)/5
var = ((1-mu)**2+(2-mu)**2+(3-mu)**2+(2-mu)**2+(1-mu)**2)/5

print(mu,var)

newnum = []

for i in set:
    newnum.append((i)+1)

sum = 0

for i in newnum:
    sum = sum + i

newmu = sum/4

print(newmu)

su = 0

for i in newnum:
    su = su + (i-newmu)**2

newvar = su/4

print(newvar)

#%%

import math

data = [1,2,3,2]

mul = []

for i in data:
    mul.append((i)*2)

print(mul)

sum = 0

for i in mul:
    sum = sum + i

print(sum)

mu = sum/4
print(mu)

print("sqrt is", math.sqrt(mu))

su = 0

for i in mul:
    su = su + (i-mu)**2

newvar = su/4
print(newvar)

# %%
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

# The datatset to be plotted. You can add and remove points 
# from the array to create a dataset with cov(x, y) != 0
data = np.array([[1,1],
                [-3,-3],
                [2,2],
                [0,2],
                [-2,0],
                [1,3],
                [4,4]])
mean_data = np.mean(data, axis=0)
# The following two lines will generate a plot similar to the figures above.
# create_plot(data)
plt.show()
# %%
