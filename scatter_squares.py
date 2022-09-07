import matplotlib.pyplot as plt

x = range(1,1001)
y = [x_val**2 for x_val in x]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.scatter(x,y,c='red',s=10)
# ax.scatter(x,y,c=(0,0.8,0),s=10)
ax.scatter(x,y,c=y,cmap=plt.cm.Blues,s=10)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both',which='major', labelsize=14)

#Set the range for the axis
ax.axis([0,1100,0,1100000])

# plt.show()
plt.savefig('squares_plot', bbox_inches='tight')