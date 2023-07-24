import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import mysql.connector as mariadb
'''
class Carga:
     
    def __init__(self):
        
        self.figure=0
        self.axs=0
        self.ax=0
        self.df=pd.read_csv("Customer Churn Model.txt")
        print(self.df)
        
    def plots(self):
        
        self.df.plot(kind="scatter", x="Day Mins", y="Day Charge")
        plt.show()
    
    def plots2(self):
        
        self.figure,self.axs=plt.subplots(2,2, sharey=True,sharex=True)
        self.df.plot(kind="scatter",x="Day Mins", y="Day Charge", ax=self.axs[0][0])
        self.df.plot(kind="scatter",x="Night Mins", y="Night Charge", ax=self.axs[0][1])
        self.df.plot(kind="scatter",x="Day Calls", y="Day Charge", ax=self.axs[1][0])
        self.df.plot(kind="scatter",x="Day Mins", y="Day Charge", ax=self.axs[0][0])
        plt.show()
'''
class data_Wranglig:
    
    def __init__(self):
        
        self.df=pd.read_csv("Customer Churn Model.txt")
    
        self.df2=0
        self.df3=0
        self.df4=0
        self.df5=0
        
        
    def conjuntoDatos(self):
        
        print(self.df.columns.values.tolist())
        self.df2=self.df['Account Length']
        print(self.df2)
        

        
data=data_Wranglig()
data.conjuntoDatos()        
        
        
        