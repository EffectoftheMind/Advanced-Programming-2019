import math
import matplotlib.pyplot as plt

#Sqrt Graph
x = []
y = []

for i in range(1, 100):
    x.append(i)
for i in x:
    j = math.sqrt(i)
    y.append(j)

plt.title('Square Roots Graph')
plt.plot(x, y)
plt.show()

#Single Int. Graph
x = []
y = []
for i in range(1,100):
    x.append(i)
for i in x:
    y.append(i)
 
plt.title('Int. Graph')
plt.plot(x, y)
plt.show()

#Squared Nums Graph
x = []
y = []

for i in range(1, 100):
    x.append(i)
for i in x:
    j = i**2
    y.append(j)
    
plt.title('Squared Numbers Graph')
plt.plot(x, y)
plt.show()

#Cubed Nums Graph
x = []
y = []

for i in range(1, 100):
    x.append(i)
for i in x:
    j = i**3
    y.append(j)
    
plt.title('Cubed Numbers Graph')
plt.plot(x, y)
plt.show()

#2^n Graph
x = []
y = []

for i in range(1, 100):
    x.append(i)
for i in x:
    j = 2**i
    y.append(j)
    
plt.title('2^n Graph')
plt.plot(x, y)
plt.show()

#Factorial Graph
x = []
y = []

for i in range(1, 100):
    x.append(i)
    j = math.factorial(i)
    y.append(j)
    
plt.title('Factorials Graph')
plt.plot(x, y)
plt.show()

#Log Graph 1
x = []
y = []

for i in range(1,100):
    x.append(i)
for i in x:
    j = i * math.log(i,2)
    y.append(j)
    
plt.title('Log Graph 1')
plt.plot(x, y)
plt.show()

#Log Graph 2
x = []
y = []

for i in range(1,100):
    x.append(i)
for i in x:
    j = math.log(i, 2)
    y.append(j)
    
plt.title('Log Graph 2')
plt.plot(x, y)
plt.show()

#Sine Graph
x = []
y = []

for i in range(1, 100):
	x.append(i)
for i in x:
	j = math.sin(i)
	y.append(j)

plt.title('Sin Wave')
plt.plot(x, y)
plt.show()

#Cosine Graph
x = []
y = []
for i in range(1,100):
    x.append(i)
    
for i in x:
    j = math.cos(i)
    y.append(j)
    
plt.title('Cos Wave')
plt.plot(x,y)
plt.show()

#Tangent Wave
x = []
y = []

for i in range(1, 100):
    x.append(i)
    
for i in x:
    j=math.tan(i)
    y.append(j)

plt.title('Tan Wave')
plt.plot(x,y)
plt.show()

#Poly-Graph 1
x = []
y = []

for i in range(1,100):
    x.append(i)
for i in x:
    j = i**2+3*i-9
    y.append(j)
    
plt.title('Polynomial Graph 1')
plt.plot(x,y)
plt.show()

#Poly-Graph 2
x = []
y = []

for i in range(1,100):
    x.append(i)
for i in x:
    j = i**-5
    y.append(j)
    
plt.title('Polynomial Graph 2')
plt.plot(x,y)
plt.show()

#Poly-Graph 3
x = []
y = []

for i in range(1,100):
    x.append(i)
for i in x:
    j = math.sqrt(i)+3 * math.sqrt(i)-3
    y.append(j)
    
plt.title('Polynomial Graph 3')
plt.plot(x,y)
plt.show()
