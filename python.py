# Chapter 1- (Variables and Data types) 

print("Hello world") # print string statement
print(24) # print integer value
name = "Piyush"
age = 19
price = 23.54                                           # Outputs-
age2 = age + 2
print(name)                                             #Piyush
print(age)                                              #19
print(price)                                            #23.54 
print(age2)                                             #21
print("my name is:",name)
print("my age is:",age)
print("price of book:",price)
print("my friends age is:",age2)

# Type of data types
a = None
old = False
print(type(name))
print(type(age))
print(type(price))
print(type(age2))
print(type(a))
print(type(old))

# Print sum and difference
A = 14
B = 5
sum = A+B
diff = A-B
print(sum) # print(A+B)
print(diff) # print(A-B)
# Type of operators

# Arithmetic operators - (+,-,*,/,%,**)
C = 20
D = 10
print(C-D)
print(C+D)
print(C*D)
print(C/D)
print(C%D)
print(C**D)

# Relational operators - (==,!=,>,<,=<,=>)
print(C==D)
print(C!=D)
print(C>=D)
print(C<=D)
print(C<D)
print(C>D)

# Assigment operators - (=,+=,-=,*=,/=,%=,**=)
num = 20
num = num + 10  # num += 10
print("num:",num)
number = 30
number += 10  # number-=, number*=, number%=, number/=, etc
print(" number:",number)

# logical operators - (not,or,and)
print(not False)
print(not True)
E = 40
F = 20
print(not(E>F))
print(not False)
val1 = True
val2 = True
print("and operator:",val1 and val2)
print("or operator:",val1 or val2)
val3 = True
val4 = False
print("and operator:",val3 and val4)
print("or operator:",val3 or val4)
val5 = False
val6 = False
print("or operator:",val5 or val6)
print("and operator:",val5 and val6)
G = 50
H = 30
print("or operator:",(G==H) or (G>H))

# Type conversion (Automatic conversition)
I = 3
J = 4.34
sum = I + J
print(sum)
K = "4"
L = 5.65
print(type(K))
         # print(K+L)   Output- Error

# Type casting (Manualy conversition)
a = int("3")
b = 6.34
print(type(a))
print(a+b)
c = float("7")
d = 3.45
print(type(c))
print(c-d)
e = 7.23
e = str(e)
print(type(e))

# Input in python-     input()
NAME=input("Enter your name:")
print("Welcome",NAME)
Val = input("Enter some value:")
print(type(Val),Val)
value = int(input("Enter some value 1:"))
print(type(value),value)
value2  = float(input("Enter some value 2:"))
print(type(value2),value2)
Name1 = input("Enter your name1:") 
Age3 = input ("Enter age3:")
Marks = input("Enter your marks:")
print("Welcome",Name1)
print("Age3=",Age3)
print("Marks=",Marks)

# Let's Practice

# Write a program to input 2 numbers and print their sum.
first = int(input("Enter first number:"))
second = int(input("Enter second number:"))
print("sum=",first + second)

# Write a program to input side of a square and print area.
side = float(input("Enter square side:"))
print("area=",side*side)

# Write a program to input 2 floating point number and print their average.
f = float(input("Enter first:"))
g = float(input("Enter second:"))
print("avg=",(f+g)/2)

# Write a program to input 2 integer numbers, h and i and print True if h is greater than or equal to i. if not print False.
h = int(input("Enter first no. :"))
i = int(input("Enter second no. :"))
print(h>=i)

# Chapter 2- (Strings and Conditional statement)

# concatenation-
str1 = "hello"
str2 = "world"
conc = str1 + str2
print("concatenation:",conc) # print(str1 + str2)

# Escape sequence characters -  (\n,\t)      \n = next line ,  \t = tab space
str3 = "This is a string.\n we are creating it in python"
str4 = "This is a string.\t we are creating it in python"
print("\n escape sequence characters:",str3)
print("\t escape sequence characters:",str4)
string = str3 + " " + str4
print("If we want to give space between two string:",string)

# Length of string -       len(str)
str5 = "apna college"
length = len(str5)
print(length)      # print(len(str5))
print("length of string 4:",len(str4))
str6 = "apna"
str7 = "college"
final = str6 + str7
print("length of string 6:",len(str6))
print("length of string 7:",len(str7))
print("concatenation:",final)
print("length of final length:",len(final))

# Indexing - 

str8 = "APNA COLLEGE"
Chhar = str8[8]
Chhar1 = str8[1]
Chhar2 = str8[2]
Chhar3 = str8[4]
Chhar4 = str8[7]
print("Indexing of string 8 in python:",Chhar)
print(Chhar1)
print(Chhar2)
print(Chhar3)
print(Chhar4)

# Slicing - Accessing parts of a string
   # Breakdown the string in different parts is called slicing
str9 = "Hello world"
sli = str9[0:4]
sli1 = str9[3:7]
sli2 = str9[ :10]
sli3 = str9[1: ]
sli4 = str9[6:10]
print("Slicing of string 9 in python:",sli)
print(sli1)
print(sli2)
print(sli3)
print(sli4)
