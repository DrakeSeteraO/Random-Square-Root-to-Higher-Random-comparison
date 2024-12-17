from random import random
from math import floor
import matplotlib.pyplot as plt

def main():
    columns = int(input('How many columns would you like?'))
    amount = int(input('How many random numbers do you want to generate?'))
    
    higher_D = [0] * columns
    sqrt_D = [0] * columns
    
    for _ in range(amount):
        a = random()
        b = random()
        temp = a
        if a < b:
            temp = b
        temp = floor(temp * columns)
        higher_D[temp] += 1
        
        c = random()
        c = c ** (1/2)
        c = floor(c * columns)
        sqrt_D[c] += 1

    num_range = 0
    range_names = list()
    for _ in range(columns):
        range_names.append(f'{num_range} to {num_range + (1/columns)}')
        num_range += 1 / columns
    
    fig, axs = plt.subplots(1,2)
    fig.set_size_inches(10,5)

    
    axs[0].bar(range_names, higher_D, align='edge',width=1)
    axs[0].set_xticklabels([])
    axs[0].title.set_text('Higher of 2 random float')
    
    axs[1].bar(range_names, sqrt_D, align='edge',width=1)
    axs[1].set_xticklabels([])
    axs[1].title.set_text('Square root of random float')

    plt.show()


if __name__ == '__main__':
    main()