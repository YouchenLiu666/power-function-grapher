import matplotlib.pyplot as plt
import numpy as np
import logging

logging.basicConfig(filename="grapher.log",level=logging.INFO)

def log_action(a,n,filesaved,filename='power_plot.png'):
    if filesaved:
        logging.info(f"Plotted power function with a={a}, n={n}, file saved: {filename}")
    else:       
        logging.info(f"Plotted power function with a={a}, n={n}, file saved: {filesaved}")


def plot_power_function(a=1,n=2,save_to_file=False,filename='power_plot.png'):
    x=np.linspace(-20,20,100)
    y=a*(x**n)
    plt.plot(x,y,label=f'y={a}*x^{n}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Power Function Plotter')
    plt.legend()
    plt.grid(True)
    
    if save_to_file:
        plt.savefig(filename)
        print(f"Plot saved as {filename}")
    log_action(a,n,save_to_file,filename)    
    plt.show()
    
    

if __name__ == "__main__":
    try:
        a = int(input("Enter coefficient a (integer): "))
        n = int(input("Enter power n (integer): "))
        save_to_file = input("Save plot to file? (y/n): ").strip().lower() == 'y'
        plot_power_function(a, n,save_to_file)
    except ValueError:
        print("Please enter valid integers!")