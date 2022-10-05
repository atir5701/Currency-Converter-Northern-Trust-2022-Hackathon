import streamlit as st
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def convert(curr1, curr2, amount, total):
    data1 = list(total[curr1])
    data2 = list(total[curr2])
    data1 = data1[-1]
    data2 = data2[-1]
    rate = data2 / data1
    net = rate * amount
    print("Converted ammount from " + curr1 + " to " + curr2 + " is : " + str(net))



df11 = pd.read_csv("Exchange_Rate_Report_2022.csv")
curr1 = 'Indian rupee   (INR)                     '
curr2 = 'U.K. pound   (GBP)                     '
amount = int(input("Enter the total Amount : "))

convert(curr1, curr2, amount, df11)
