import matplotlib.pyplot as plt

#,x-coordinate of left side of the bar
left = [1,2,3,4,5]

#height of the bar
height = [10,24,36,40,5]

#label for bars
tick_label = ['one','two','three','four','five']

#plotting a bar chart
plt.bar (left, height, tick_label=tick_label,
	    width = 0.8, color = ['red','green'])

#naming the x-axis
plt.xlabel ('x - axis')
#naming the y-axis
plt.ylabel ('y - axis')
#plot tittle
plt.title('My bar chart')

#function to show the plot
plt.show()