# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 12:54:17 2025

@author: jsata
"""
#python--version
print("Hello World!")

x=5
y=6
z=x+y
print(z)
print (z*12)
a="Aahi is good"
print(a)
print(f"x={x} and y={y} ")
def add(x, y):
    return x + y# indented block defines a function
n=add(9,12)
print(n)
def print_message():
    print("A message")
print_message()

def demonstrateIndents():
    # An indented block
    if True:
        # Another indented block
        print("Hello")
    elif False:
        pass
    else:
        pass
# Code that is not part of the function
demonstrateIndents()
import math

print(math.ceil(4.9)) # The ceiling function
print(math.exp(1)) # Calculates e^1
print(math.log(256, 16)) # Calculates the base-16 logarithm of 256
print(math.sin(2*math.pi)) # Calculates the sine of 2π radians
print(math.asin(0)) # Calculate the arcsin of 0
print(math.atan2(5, 4)) # Computes the angle of the point (4, 5) with respect to the origin
print(math.degrees(2*math.pi)) # Converts 2π radians to degrees
print(math.radians(180)) # Converts 180 degrees to radians
print(math.sinh(1)) # Computes the hyperbolic sine
print(math.erf(1)) # Computes the error function from statistics



import cmath
x = cmath.sqrt(cmath.sqrt(-1))
print(cmath.polar(x)) # Converts a Python complex number into polar form
print(cmath.exp(x)) # Calculates e^x
print(cmath.cos(x)) # Calculates the cosine of x



import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.bar(x, y)


#df = pd.read_csv('https://lib.stat.cmu.edu/datasets/boston')
#df.head()

#import pandas as pd
#from sklearn.datasets import load_boston

# Load the dataset
from sklearn.datasets import fetch_california_housing

california_housing = fetch_california_housing()

print(california_housing.DESCR)
housing_data = fetch_california_housing()
housing_df = pd.DataFrame(data=housing_data.data, columns=housing_data.feature_names)
housing_df['MedHouseVal'] = housing_data.target  # Add the target variable
print(housing_df.head())
