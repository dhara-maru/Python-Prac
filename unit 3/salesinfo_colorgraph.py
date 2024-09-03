import matplotlib.pyplot as plt

def display_sales_info():
    # Data for the plot
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    book_sales = [15, 22, 18, 25, 20]
    movie_sales = [10, 18, 14, 20, 16]

    # Plotting the data with different colors for book and movie sales
    plt.plot(months, book_sales, linewidth=5, color='blue', label='Book Sales')
    plt.plot(months, movie_sales, linewidth=5, color='orange', label='Movie Sales')

    # Adding labels and title
    plt.xlabel('Months')
    plt.ylabel('Number of Sales')
    plt.title('Book and Movie Sales Info')

    # Display grid lines
    plt.grid(True)

    # Display the legend
    plt.legend()

    # Display the plot
    plt.show()

# Call the function to display the sales information
display_sales_info()
