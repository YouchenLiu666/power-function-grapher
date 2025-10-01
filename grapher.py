import matplotlib.pyplot as plt
import numpy as np

def plot_power_function(a=1,n=2):
    x=np.linspace(-20,20,100)
    y=a*(x**n)
    plt.plot(x,y,label=f'y={a}*x^{n}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Power Function Plotter')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_power_function()