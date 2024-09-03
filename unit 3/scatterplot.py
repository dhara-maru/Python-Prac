import matplotlib.pyplot as plt
import numpy as np

def create_movie_scatter_plot():
    # Generating random data for the scatter plot
    num_movies = 50
    box_office_revenue = np.random.uniform(50, 500, num_movies)  # Random revenue between 50 and 500 million
    audience_ratings = np.random.uniform(0, 10, num_movies)  # Random ratings between 0 and 10

    # Creating the scatter plot with different colors for X and Y
    plt.scatter(box_office_revenue, audience_ratings, color='blue', marker='o', s=50, alpha=0.7, label='Movies')
    plt.scatter(np.mean(box_office_revenue), np.mean(audience_ratings), color='red', marker='x', s=100, label='Mean')

    # Adding labels and title
    plt.xlabel('Box Office Revenue (in million $)')
    plt.ylabel('Audience Ratings')
    plt.title('Movie Scatter Plot')

    # Display the legend
    plt.legend()

    # Display the plot
    plt.show()

# Call the function to create and display the scatter plot
create_movie_scatter_plot()
