import numpy as np 
import sys

a=[1,2,3,4,5,6]
b= [55,8,64,1,35,78,45,66]

people =[
       {"name":'alex','age':'20'},
       {"name":'bob','age':'10'},
       {"name":'alan','age':'30'}
       ]

# def countnum(x,y):
#     assert x>0 and y>0,"參數要大於0"
#     return x+y

# print(countnum(0,2))

def first(fn):
    def w():
        print("hi i'm")
        fn()
        print("nice to see you!")
    return w

@first
def myname():
    # print(f"alex i'm {age} years old")
    print('alex')


myname()