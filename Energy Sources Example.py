import matplotlib.pyplot as plt

x = 'Solar', 'Wind', 'Gas', 'Oil', 'Coal', 'Biofuel'
y = [5,6,15,22,24,8]

#plt.style.use('ggplot')
#plt.bar(x,y,color='green', width = 0.5)

explode = (0, 0.1, 0, 0, 0, 0)
fig1, ax1 = plt.subplots()
ax1.pie(y, explode=explode, labels=x, autopct='%.2f')
ax1.axis('equal')

plt.xlabel("Energy Source")
plt.ylabel("Energy Output (GJ)")
plt.title("Energy Output From Various Fuel Sources")

plt.show()