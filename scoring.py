import numpy as np
import pandas as pd
import json
import csv
#import openpose as op

with open('Cloud.txt') as f:
    temp = f.read()

temp = temp.replace('  ', '')
temp = temp.replace('][', '],[')
temp = temp.replace(' ', ',')
temp = temp.replace('\n\n', ',')
temp = temp.replace('\n', ',')
temp = temp.replace(',,', ',')
temp = '[' + temp + ']'

text_file = open('test1.txt', 'w')
n = text_file.write(temp)
text_file.close()
   
with open('test1.txt') as file:
    lst = json.load(file)

with open('Yusam.txt') as f:
    temp = f.read()

temp = temp.replace('  ', '')
temp = temp.replace('][', '],[')
temp = temp.replace(' ', ',')
temp = temp.replace('\n\n', ',')
temp = temp.replace('\n', ',')
temp = temp.replace(',,', ',')
temp = '[' + temp + ']'

text_file = open('test2.txt', 'w')
n = text_file.write(temp)
text_file.close()
   
with open('test2.txt') as file:
    lst = json.load(file)

with open('test1.txt', 'r') as file:
    data = file.read()
cloud = eval(data)
with open('test2.txt', 'r') as file:
    data = file.read()
yusam = eval(data)

yusam1 = [[j for k in i for j in k] for i in yusam]
cloud1 = [[j for k in i for j in k] for i in cloud]

cloud_df = pd.DataFrame(cloud1)
yusam_df = pd.DataFrame(yusam1)
cloud_df = cloud_df.iloc[:, 0:26]
yusam_df = yusam_df.iloc[:, 0:26]
def calculate_points(df1, df2):
    # Define the point system constants
    X_THRESHOLD_1 = 5
    X_THRESHOLD_2 = 10
    X_THRESHOLD_3 = 20
    Y_THRESHOLD_1 = 5
    Y_THRESHOLD_2 = 10
    Y_THRESHOLD_3 = 20
    PROBABILITY_THRESHOLD = 0.4

    # Define a variable to store the total points
    total_points = 0

    # Loop through each row and column in the dataframes
    for i in range(len(df1)):
        for j in range(len(df1.columns)):
            # Skip comparison if either df1 or df2 has a None value for the joint location
            if df1.iloc[i, j] is None or df2.iloc[i, j] is None:
                continue

            # Check if the probability is greater than the threshold
            if df1.iloc[i, j][2] >= PROBABILITY_THRESHOLD and df2.iloc[i, j][2] >= PROBABILITY_THRESHOLD:

                # Calculate the difference in x and y coordinates
                x_diff = abs(df1.iloc[i, j][0] - df2.iloc[i, j][0])
                y_diff = abs(df1.iloc[i, j][1] - df2.iloc[i, j][1])

                # Check if the difference in x and y coordinates falls within the thresholds and add points accordingly
                if x_diff <= X_THRESHOLD_1 and -X_THRESHOLD_1 <= x_diff:
                    total_points += 2
                elif x_diff <= X_THRESHOLD_2 and -X_THRESHOLD_2 <= x_diff:
                    total_points += 1
                elif x_diff <= X_THRESHOLD_3 and -X_THRESHOLD_3 <= x_diff:
                    total_points += 0.5

                if y_diff <= Y_THRESHOLD_1 and -Y_THRESHOLD_1 <= y_diff:
                    total_points += 2
                elif y_diff <= Y_THRESHOLD_2 and -Y_THRESHOLD_2 <= y_diff:
                    total_points += 1
                elif y_diff <= Y_THRESHOLD_3 and -Y_THRESHOLD_3 <= y_diff:
                    total_points += 0.5

    # Return the total points
    return total_points
calculate_points(cloud_df, yusam_df)