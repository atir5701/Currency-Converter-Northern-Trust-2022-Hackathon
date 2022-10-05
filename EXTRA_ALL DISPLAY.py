import streamlit as st
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px

df1=pd.read_csv("Exchange_Rate_Report_2012.csv")
df2=pd.read_csv("Exchange_Rate_Report_2013.csv")
df3=pd.read_csv("Exchange_Rate_Report_2014.csv")
df4=pd.read_csv("Exchange_Rate_Report_2015.csv")
df5=pd.read_csv("Exchange_Rate_Report_2016.csv")
df6=pd.read_csv("Exchange_Rate_Report_2017.csv")
df7=pd.read_csv("Exchange_Rate_Report_2018.csv")
df8=pd.read_csv("Exchange_Rate_Report_2019.csv")
df9=pd.read_csv("Exchange_Rate_Report_2020.csv")
df10=pd.read_csv("Exchange_Rate_Report_2021.csv")
df11=pd.read_csv("Exchange_Rate_Report_2022.csv")

df1=df1.fillna(method="bfill")
df2=df2.fillna(method="bfill")
df3=df3.fillna(method="bfill")
df4=df4.fillna(method="bfill")
df5=df5.fillna(method="bfill")
df6=df6.fillna(method="bfill")
df7=df7.fillna(method="bfill")
df8=df8.fillna(method="bfill")
df9=df9.fillna(method="bfill")
df10=df10.fillna(method="bfill")
df11=df11.fillna(method="bfill")

curr1 = 'Indian rupee   (INR)                     '
curr2 = 'U.K. pound   (GBP)                     '


# print("For year 2012 : ")
# data1=np.array(list(df1[curr1]))
# data2=np.array(list(df1[curr2]))
# print("Average Exchange Rate : "+str((np.mean(data2))/np.mean(data1)))
#
# print("For year 2013 : ")
# data1=np.array(list(df2[curr1]))
# data2=np.array(list(df2[curr2]))
# print("Average Exchange Rate : "+str((np.mean(data2))/np.mean(data1)))
#
# print("For year 2014 : ")
# data1=np.array(list(df3[curr1]))
# data2=np.array(list(df3[curr2]))
# print("Average Exchange Rate : "+str((np.mean(data2))/np.mean(data1)))
#
# print("For year 2015 : ")
# data1=np.array(list(df4[curr1]))
# data2=np.array(list(df4[curr2]))
# print("Average Exchange Rate : "+str((np.mean(data2))/np.mean(data1)))
#
# print("For year 2016 : ")
# data1=np.array(list(df5[curr1]))
# data2=np.array(list(df5[curr2]))
# print("Average Exchange Rate : "+str((np.mean(data2))/np.mean(data1)))
#
# print("For year 2017 : ")
# data1=np.array(list(df6[curr1]))
# data2=np.array(list(df6[curr2]))
# print("Average Exchange Rate : "+str((np.mean(data2))/np.mean(data1)))
#
# print("For year 2018 : ")
# data1=np.array(list(df7[curr1]))
# data2=np.array(list(df7[curr2]))
# print("Average Exchange Rate : "+str((np.mean(data2))/np.mean(data1)))
#
# print("For year 2019 : ")
# data1=np.array(list(df8[curr1]))
# data2=np.array(list(df8[curr2]))
# print("Average Exchange Rate : "+str((np.mean(data2))/np.mean(data1)))
#
# print("For year 2020 : ")
# data1=np.array(list(df9[curr1]))
# data2=np.array(list(df9[curr2]))
# print("Average Exchange Rate : "+str((np.mean(data2))/np.mean(data1)))
#
# print("For year 2021 : ")
# data1=np.array(list(df10[curr1]))
# data2=np.array(list(df10[curr2]))
# print("Average Exchange Rate : "+str((np.mean(data2))/np.mean(data1)))

print("For year 2022 : ")
data1=list(df11[curr1])
data2=list(df11[curr2])
data1=data1[-1]
data2=data2[-1]
curr1=' '.join(curr1.strip(" "))
curr2=' '.join(curr2.strip(" "))

print("Exchange rate of  "+curr1+"  to  "+curr2+" is :  "+str(data2/data1))


