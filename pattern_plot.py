import pandas as pd
import numpy as np
import re
import decimal
import matplotlib.pyplot as plt
# read CSV file using pandas
df = pd.read_csv('floats.csv', header=None)
df2 = pd.read_csv('floats2.csv', header=None)


f = []
for i in range(len(df)):
    k = []
    for j in range(25):
        a=df[0][i].split("\n")[j]
        numbers = re.findall(r'\d+\.\d+e[\+-]\d+', a)
        for z in range(3):
            numbers[z]=float(numbers[z])
        k.append(numbers)
    f.append(k)
    
f2 = []
for i in range(len(df2)):
    k2 = []
    for j in range(25):
        a2=df2[0][i].split("\n")[j]
        numbers2 = re.findall(r'\d+\.\d+e[\+-]\d+', a2)
        for z in range(3):
            numbers2[z]=float(numbers2[z])
        k2.append(numbers2)
    f2.append(k2)
    
    
# create 25 subplots
fig, axs = plt.subplots(5, 5, figsize=(15, 15))

# flatten the axes array to make it easier to loop through
axs = axs.flatten()

# loop through the keypoints and plot the x and y values on separate subplots
for keypoints in f:
    for i in range(len(keypoints)):
        x = keypoints[i][0]
        y = keypoints[i][1]
        axs[i].scatter(x, y, marker='o', color='red')
        axs[i].set_title(f"Keypoint {i+1}")
        axs[i].set_xlabel("X")
        axs[i].set_ylabel("Y")
        axs[i].set_xlim([0, 1600])
        axs[i].set_ylim([0, 1200])
        
for keypoints in f2:
    for i in range(len(keypoints)):
        x = keypoints[i][0]
        y = keypoints[i][1]
        axs[i].scatter(x, y, marker='o', color='blue')

    


# adjust the spacing between the subplots
plt.tight_layout()

# display the plot
plt.show()