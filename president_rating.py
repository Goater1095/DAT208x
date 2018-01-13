import matplotlib.pyplot as plt
import numpy as np
rating =  [68.5,67.8,67.2,70.3,70.1,71.6,73.0,71.5,70.8,69.5]
date=[10.2,10.3,10.4,11.1,11.2,11.3,11.4,11.5,12.1,12.2]
plt.fill_between(date,rating,0,color='green')
plt.xlabel('year')
plt.ylabel('rating')
plt.title('president rating')
plt.show()
