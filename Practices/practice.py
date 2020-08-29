a = 2
print(a + 1)

if a == 1:
    print("inamo")#inamo
elif a == 2:
    print(a)
else:   
    print("error")

"""
mamamoweidwje
iweodiwednwie
dowidwide
"""

print(a)

c,d,b = "kenneth","rexelle","eros"

if c == "kenneth":
    print(d)
print(b)

q = w = e = "pogi ako"

print(q,w,e)

f = c + b

print(f)

x = "awesome"

def myfunc():
   global x
   x = "qwerty"
y = "qwet"
print("Python is " + y)

myfunc()


l = 1j
print(type(l))


import random

print(random.randrange(1,11))

t = """qweroplsa
askdsvbvb
asdcfesedg
"""

print(t)

myname = "Kenneth Lester De Guzman"

print(myname.replace("e", "i"))

print(10 > 10)

a = 10
b = 11

if b > a:
    print("hahaha")
else:
    print("hkakakak")

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

  x = 200
print(isinstance(x, int))

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[5] = "prutas"

for x in thislist:
    print(x)

thislist.insert(1,"kimi")



thislist.pop(4)


thislist.clear()
print(thislist)

thislist.insert(1,"kimi")
print(thislist)

copylist = thislist.copy()
print(copylist)

for qwe in copylist:
    print(qwe)

together = thislist + copylist
print(together)

i = 1
while i < 6:
  print(i)
  i += 1

i = 1
j = 0
k = 1
s = 0
n = 0

n = input("input a num: ")
b = int(n)

while b >= i:
    print(b)
    if i == 3:
        break
    i += 1

for x in "banan":
    print(x)

# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
    
