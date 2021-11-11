import matplotlib.pyplot as plt

def display(x, y):
    fig, ax = plt.subplots()
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.plot(x, y)
    plt.show()

def run():
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    display(x, y)

run()
