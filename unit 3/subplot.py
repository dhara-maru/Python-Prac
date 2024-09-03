import matplotlib.pyplot as plt
import numpy as np

def create_subplot_graph():
    # Generating random data for the scatter plot
    x_data_scatter = np.random.rand(50)
    y_data_scatter = np.random.rand(50)

    # Generating random data for the bar plot
    categories = ['A', 'B', 'C', 'D', 'E']
    values_bar = np.random.randint(1, 10, len(categories))

    # Creating subplots
    plt.figure(figsize=(10, 5))

    # Scatter plot (subplot 1)
    plt.subplot(1, 2, 1)
    plt.scatter(x_data_scatter, y_data_scatter, color='blue', marker='o')
    plt.title('Scatter Plot')

    # Bar plot (subplot 2)
    plt.subplot(1, 2, 2)
    plt.bar(categories, values_bar, color='green')
    plt.title('Bar Plot')

    # Adjust layout to prevent overlapping
    plt.tight_layout()

    # Display the plot
    plt.show()

# Call the function to create and display the graph with subplots
create_subplot_graph()
