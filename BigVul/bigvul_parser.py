import csv

import pandas as pd

#Path to BigVul Dataset
file = "Dataset/MSR_data_cleaned.csv"
#How many rows we are going to read at a time
#Optimizing performance
chunks = 25000


