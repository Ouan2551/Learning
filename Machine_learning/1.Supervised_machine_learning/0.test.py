import matplotlib.pyplot as plt

def onclick(event):
    print(f"Clicked at x={event.xdata}, y={event.ydata}")

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])

cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
