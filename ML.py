import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import mysql.connector as mariadb

class Machine_Learning:
    
    
    def __init__(self):

      
        self.df=pd.read_csv("titanic3.csv")
        self.null=0
        self.data=0
        self.not_null=0
        self.valor_null=0
        self.valor_notnull=0
        self.clean1=0
        self.clean2=0
        self.clean3=0
        self.clean4=0
        self.clean5=0
        self.clean6=0
        self.clean7=0
        self.dummy=0
        self.dummy2=0
        self.var_name=0
        self.df2=0
        self.df3=0
        self.df4=0
        self.df5=0
        self.p1=0
        self.p2=0
        self.p3=0
        self.p4=0
        
        
    def parametros(self):
        
        pd.set_option('display.width', 320)
        print(self.df.shape)
        print(self.df.columns.values.tolist())
        print(self.df.describe())
        print(self.df.dtypes)
        print("\n\n")
        
    def MissingValues(self):
        
        self.null=pd.isnull(self.df["body"])
        print(self.null)
        print("\n\nXXXXXXXXXXXXXXXXXXXXXXXX\n\n")
        self.not_null=pd.notnull(self.df["body"])
        print(self.not_null)
        
    def valores(self):
        
        self.valor_null=pd.isnull(self.df["body"]).values.ravel().sum()
        print(self.valor_null)
        self.valor_notnull=pd.notnull(self.df["body"]).values.ravel().sum()
        print(self.valor_notnull)
        
    def borrados(self):
        
        self.clean1=self.df.dropna(axis=0,how="all")
        print(self.clean1)
        print("X"*20)
        self.clean2=self.df.dropna(axis=0,how='any')
        print(self.clean2)
        print("X"*20)
    
    def computo_valores_faltantes(self):
        
        self.clean3=self.df.fillna(0)
        print(self.clean3)
        print("X"*40)
        self.clean4=self.df.fillna("Desconicido")
        print(self.clean4)
    
    def computo_columna(self):
        
        print("X"*30)
        self.clean5=self.df["body"].fillna(0)
        print(self.clean5)
        print("X"*30)
        self.clean7=self.df["home.dest"].fillna("Desconocido")
        print(self.clean7)
        
    def computo_variables(self):
        
        self.p1=pd.isnull(self.df["age"]).values.ravel().sum()
        print("La cantidad de valores--->{}".format(self.p1))
        self.p2=self.df["age"].fillna(self.df["age"].mean())
        print(self.df)
        print(self.p2)
        
    def generacion_dummy(self):
        
        self.dummy=pd.get_dummies(self.df["sex"],prefix="sex")
        print(self.dummy)
        print("X"*30)
        self.df2=self.df.drop(["sex"],axis=1)
        print(self.df.columns.values.tolist())
        print(self.df2.columns.values.tolist())
        self.df3=pd.concat([self.df2,self.dummy],axis=1)
        print("X"*30) 
        print(self.df3)
        
    def generacion_dataset(self,df,var_name):
        
        self.dummy2=pd.get_dummies(self.df[var_name],prefix=self.var_name)
        self.df5=self.df.drop(self.var_name,axis=1)
        self.df5=pd.concat([self.df5,self.dummy2])
        
        print(self.df5)
        
        
        
'''
p=Machine_Learning()
p.parametros()
p.MissingValues()
p.valores()
p.borrados()
p.computo_valores_faltantes()
p.computo_columna()
p.computo_variables()
p.generacion_dummy()
print("XXXXXXXXX"*70)
p.generacion_dataset(df,"sex")
'''
