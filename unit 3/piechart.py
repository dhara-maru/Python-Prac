import matplotlib.pyplot as plt
import numpy as np

def create_food_pie_chart():
    # Sample data for different types of food
    food_types = ['Pizza', 'Burger', 'Pasta', 'Salad', 'Sushi']
    food_percentages = np.random.rand(len(food_types))

    # Creating the pie chart with different colors for each food type
    plt.pie(food_percentages, labels=food_types, autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'gold', 'lightblue', 'palegreen', 'lightcyan'])

    # Adding title
    plt.title('Random Food Distribution')

    # Display the plot
    plt.show()

# Call the function to create and display the pie chart
create_food_pie_chart()
