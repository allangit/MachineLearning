import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import mysql.connector as mariadb


pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 70)


class Carga:
     
    def __init__(self):
        
        self.figure=0
        self.axs=0
        self.ax=0
        self.desired=0
        self.all_columns=0
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

class data_Wranglig:
    
    def __init__(self):
        
        self.df=pd.read_csv("Customer Churn Model.txt")
    
        self.df2=0
        self.df3=0
        self.df4=0
        self.df5=0
        self.all_columns=0
        self.sublist=0
        self.x=0
        self.data1=0
        self.data2=0
        self.data3=0
        self.data4=0
        
        
    def conjunto1(self):
        
        print(self.df.columns.values.tolist())
        self.df2=self.df['Account Length']
        print(self.df2)  
        
    def conjunto2(self):
        
        self.df3=self.df[['Account Length', 'Phone', 'Eve Charge', 'Day Calls']]
        print(self.df3)
        print("X"*40)
        
    def conjunto3(self):
        
        self.desired=['Account Length', 'Area Code', 'Phone', 'Day Calls']
        self.df4=self.df[self.desired]
        print(self.df4)
        
    def conjunto4(self):
        
        self.all_columns=self.df.columns.values.tolist()
        self.sublist=[self.x for self.x in self.all_columns if self.x not in self.desired]
        print(self.sublist)
        
    def filtrado1(self):
        
        print(self.df[1:25])
        print(self.df[20:35])
        print(self.df[200:])
        
    def filtrado2(self):
        
        self.data2=self.df[self.df["Day Mins"] > 350]
        print(self.data2)
        
        
        
        

        
data=data_Wranglig()
data.conjunto1()
data.conjunto2()
data.conjunto3()
data.conjunto4()
data.filtrado1()
data.filtrado2()
        
        