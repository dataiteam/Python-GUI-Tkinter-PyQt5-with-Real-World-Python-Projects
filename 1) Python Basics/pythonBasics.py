print("Hello World1!")
print("Hello World2!")
print("Hello World3!")
print("Hello World4!")

# %%
print("Hello World5!")
print("Hello World6!")

# %%

# section3, this is my first coding experience
# *************************************************************** !!
print("Hello World7!")
print("Hello World8!")

# %% data types

a = 4 # integer 
b = 8
c = 3.14 # float
type(a)

d = a+b+c
print(d)

# string
string1 = "Hello"

string2 = "World"

print(string1)
print(string2)

string3 = string1 + " " + string2
print(string3)

string3[4] # Hello World

string3[0:5]

bool1 = True
bool2 = False

#%%  lists ve dictionaries

list1= ["milk","orange", "fish", "water"]

list1[0]
list1[-1]
list1[1:3]

list1[1] = "coffee"

len(list1)

list1.append("orange")

list1.remove("orange")


list1.insert(1,"orange")


list1.pop(0)

list2 = [1,5,6,7,23,4,5,5,5]
list2.sort()

list2.count(5)

# dictionary

dict1 = {"country":"Spain",
        "city":"Madrid",
        "year":1964}

x = dict1["city"]
y = dict1.get("city")

dict1["city"] = "Barcelona"

len(dict1)

dict1.values()
dict1.keys()


dict1["food"] = "pizza"

dict1.pop("city")

# %% if/else, for and while loops

a = 23
b = 55

if a<b:
    print("a is smaller than b")
elif a>b:
    print("a is bigger than b")
else:
    print("a == b ")


c = 33

if a<b and c<b:
    print("yes")

list1= ["milk","orange", "fish", "water"]

if "coffee" in list1:
    print("milk is in list")
else:
    print("not in list")

# for 
list1= ["milk","orange", "fish", "water"]   

for i in list1:
    print(i)

dict1 = {"country":"Spain",
        "city":"Madrid",
        "year":1964}

for i in dict1:
    print(i)

for i in dict1.values():
    print(i)


for i in list1:
    print(i)
    if i == "fish":
        print("i find {}".format(i))
        break
    else:
        continue

# list1= ["milk","orange", "fish", "water"]
        
for i in range(len(list1)):
    print(list1[i])


city = ["paris","new york"]
country = ["france","usa"]

z = zip(city,country)
for i in z:
    print(i)

# while

c = 1
while c < 6:
    print(c)
    c += 1 # c = c + 1

c = 1
while c < 6:
    print(c)
    if c == 3:
        break
    c += 1

# %% functions
    
def summation(x,y):
    z = x+y
    print(z)
    return z

def square(x):
    z = x*x
    print(z)

w = summation(4,5) 
   
square(w)

def sayHi():
    print("hi")


sayHi()

def areaCircle(r, pi = 3.14):
    print(pi*r*r)
    
areaCircle(4, 5)

areaCircle(5)


# lambda
x = lambda a : a + 10
x(4)

x = lambda a,b : a*b + 10
x(2,3)

def toString():
    pass


# %% class (oop)
    
class Circle:
    
    global pi
    pi = 3.14
    
    # constructor
    def __init__(self,name,r):
        self.class_name = name
        self.class_r = r
        
    def toString(self):
        print(self.class_name)
        print(self.class_r)
        
    def findArea(self):
        area = pi*self.class_r*self.class_r
        print(area)
        
    def setName(self,name):
        self.class_name = name
    
    def getName(self):
        print(self.class_name)
        return self.class_name
        
    def emp(self):
        pass
        
        
c1 = Circle("s1",2)

c1.toString()
c1.findArea()


c1.setName("s2")
name = c1.getName()



# %% module < package < library

import numpy # module
a = numpy.array([1,2,3])

numpy.mean(a)

c = numpy.random.randint(3)

from numpy import random

import numpy as np

a = np.array([1,2,3])


# %% numpy

import numpy as np

arr = np.array([[1,2,3],[4,5,6]])

print(arr.shape)
print(type(arr))
print(arr.ndim)
print(arr.size)
print(arr.dtype)

# indexing
arr[0,0]
arr[1,1]
arr[1,-1]

arr[1,:]

# math
a = np.array([1,2,3,4,5])
a+1
a-3
a*3
a**2

# mean, std, max min
a = np.array([1,2,3,4,5])
np.mean(a)
np.std(a)
np.max(a)
np.min(a)

# create array
g = np.arange(1,100)
g2 = g.reshape((3,-1))

# allacotion

z = np.zeros([5,5])
z[2,1] = 5

#liste = []
#liste.append(5)

# concat
x = np.array([1,2,3])
y = np.array([3,2,1])

np.concatenate([x,y])

# random

a = np.random.randint(10,size = (5,5))
b = np.random.randint(10,size = 5)
np.argmax(b)


# %% pandas
import pandas as pd

# series
s = pd.Series([1,2,3,4,5])

# data frame

dictionary = {"country": ["Turkey", "Russia", "France", "China", "South Africa","Spain"],
              "capital": ["Ankara", "Moscow", "Paris", "Beijing", "Pretoria","Madrid"],
              "area":    [5.5, 17.1, 4.1, 9.2, 1.5, 4],
              "population": [80 , 150, 80, 1500, 50,70] }

data = pd.DataFrame(dictionary)
print(data)

data.head()
data.tail()
data.info()

data.to_csv("data.txt")
data1 = pd.read_csv("data.txt")

# indexing
# iloc ,loc
data1.iloc[3,4]
data1.iloc[:,2]
# loc
data1.loc[:,"country"]
data1 = data1.iloc[:,1:]

# filter
filter1 = data.loc[:,"population"] > 100
data2 = data1[filter1]

# numpy
n = data1.as_matrix()

n = data1.values

# save pickle
data.to_pickle("data_pickle.pkl")
data_p = pd.read_pickle("data_pickle.pkl")

# list comprehension
data.population = [ i + 10 for i in data.population]

# drop
df = data.drop(["area"],axis = 1)

# https://www.kaggle.com/kanncaa1/data-sciencetutorial-for-beginners


# %% matplotlib

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)
y = np.linspace(-5,5,100)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y, color = "red", linewidth = 1)
ax.scatter(x,y, color = "green", marker = "*")

plt.xlabel("x")
plt.ylabel("y")
plt.title("x vs y")
plt.savefig("x_y.png")
plt.show()

# seaborn

import seaborn as sns
a = np.random.randint(5,size = 1000)

plt.figure()
sns.countplot(a)

# https://www.kaggle.com/kanncaa1/seaborn-tutorial-for-beginners

# %% random
import random

random.seed(2)

a = random.random()
b = random.uniform(1,10)
c = random.randint(1,10)
d = random.randrange(0,101,2)

# %% i/o

save_txt = "hello world"
text_file = open("save_string.txt","w")
text_file.write(save_txt)
text_file.close()

# load
load_file = open("save_string.txt","r")
print(load_file.read())

# %% common mistakes
"""
1) import
2) array creation
3) return
4) indentation
5) remember figure()
"""

#if True:
#    print("12")
















































