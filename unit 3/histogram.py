import matplotlib.pyplot as plt
import numpy as np

def create_histogram():
    # Generating random data for the histogram
    data = np.random.normal(0, 1, 1000)

    # Creating the histogram
    plt.hist(data, bins=30, color='skyblue', edgecolor='black')

    # Adding labels and title
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram Example')

    # Display the plot
    plt.show()

# Call the function to create and display the histogram
create_histogram()
