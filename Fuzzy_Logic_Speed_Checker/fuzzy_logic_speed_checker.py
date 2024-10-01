#Implementation of Assign_No_1 with detailed explanation
#Real-Life Applications:

#Fuzzy logic has a wide range of applications in various domains, including:
#Control systems: Fuzzy logic controllers can be used in washing machines, robots, and other systems to make decisions based on imprecise or subjective inputs, leading to smoother and more adaptable control behaviors.
#Image processing: Fuzzy logic can be applied to tasks like image segmentation and edge detection, where decisions about pixel membership in specific regions can benefit from fuzzy logic's ability to handle ambiguity.
#Expert systems: Fuzzy logic can be used to model expert knowledge in areas like medical diagnosis or financial forecasting, where human experts often rely on imprecise rules and experience rather than strictly defined algorithms.

import numpy as np
#Provides numerical computation capabilities essential for defining and manipulating arrays (used for the speed universe of discourse)

import skfuzzy as fuzz
#Offers fuzzy logic tools, including membership function creation and fuzzy rule systems (used to define speed categories based on fuzzy logic)

import matplotlib.pyplot as plt
#Facilitates visualization of the defined membership functions and input speed line (used to create the plot)


# Define the universe of discourse (speed range)
speed = np.arange(0, 141, 1)
#creates a NumPy array speed containing integers from 0 to 140 (inclusive) with a step size of 1.
#This represents the possible range of car speeds in kilometers per hour (km/h) that our fuzzy system will consider


# Membership functions
extremely_slow = fuzz.trapmf(speed, [0, 0, 10, 20])
slow = fuzz.trapmf(speed, [10, 20, 30, 40])
fast = fuzz.trapmf(speed, [30, 40, 60, 70])
very_fast = fuzz.trapmf(speed, [60, 70, 100, 110])
extremely_fast = fuzz.trapmf(speed, [100, 110, 140, 150])
#fuzz.trapmf(speed, [a, b, c, d]) defines a trapezoidal membership function for the speed array with parameters a, b, c, and d. These parameters represent the following:
#a, b: The left and right endpoints of the flat (horizontal) part of the trapezoid, indicating full membership (degree of truth equal to 1).
#c, d: The left and right shoulders of the trapezoid, where the membership degree gradually increases or decreases from 0 to 1.
#Each function defines a fuzzy set representing a car speed category:
#extremely_slow: Cars traveling very slowly (0-20 km/h).
#slow: Cars moving at a slow pace (10-40 km/h).
#fast: Cars going at a moderate speed (30-70 km/h).
#very_fast: Cars traveling quite fast (60-110 km/h).
#extremely_fast: Cars exceeding the usual speed limit (100-140+ km/h)


# Plotting the membership functions
plt.figure(figsize=(12, 6)) #creates a plotting figure with a specified width (12) and height (6) in inches
plt.plot(speed, extremely_slow, label='Extremely Slow') #and similar lines plot each membership function along the speed axis (x-axis), with corresponding labels for clarity
plt.plot(speed, slow, label='Slow')
plt.plot(speed, fast, label='Fast')
plt.plot(speed, very_fast, label='Very Fast')
plt.plot(speed, extremely_fast, label='Extremely Fast')

# Adding the input speed line
input_speed = 65 #user will input here the speed of the bike or vehicle
plt.axvline(x=input_speed, color='r', linestyle='--', label=f'Input Speed = {input_speed} km/h')
#plt.axvline() is a Matplotlib function used to plot a vertical line on a graph

#Parameters:
#x: The x-coordinate of the vertical line. In this case, it's set to input_speed, which represents the speed value that we want to visualize.
#color: The color of the line. Here, it's specified as 'r', which stands for red.
#linestyle: The style of the line. 'dashed' is used to create a dashed line.
#label: A label associated with the line, which will be displayed in the legend. The label is formatted as f'Input Speed = {input_speed} km/h', where input_speed is replaced with the actual value of the input speed.

#Purpose:
#This line of code adds a vertical line to the plot, indicating the input speed value. This helps visually identify the position of the input speed within the range of possible speeds defined by the membership functions.

#Example:
#If input_speed is 12, the line will be drawn at the x-coordinate of 12, and the label will read "Input Speed = 12 km/h".
#In the context of the given code:
#The line is added to the plot after the membership functions have been plotted.
#It serves as a visual aid to help understand the relationship between the input speed and the membership values assigned to different speed categories.
#By comparing the position of the vertical line with the membership functions, we can see which categories the input speed belongs to and to what degree


# Labeling the plot
plt.xlabel('Speed (km/h)')
plt.ylabel('Membership')
plt.title('Membership Functions for Speed')
plt.legend()

# Calculate membership function values for input speed
extreme_slow_membership = extremely_slow[int(input_speed)]
slow_membership = slow[int(input_speed)]
fast_membership = fast[int(input_speed)]
very_fast_membership = very_fast[int(input_speed)]
extreme_fast_membership = extremely_fast[int(input_speed)]
#This block calculates the degree of membership (between 0 and 1) for the input speed in each fuzzy set.
#int(input_speed) converts the input speed from a floating-point number to an integer index.
#This is necessary because the membership functions (extremely_slow, slow, etc.) are NumPy arrays, and array indexing requires integers.
#Each line accesses the value at the corresponding index (int(input_speed)) in the respective membership function array.
#This value represents the degree of membership of the input speed in that particular fuzzy set


# Print membership function values
print(f"Input speed: {input_speed} km/h")
print("Membership Values:")
print(f"Extremely Slow: {extreme_slow_membership}")
print(f"Slow: {slow_membership}")
print(f"Fast: {fast_membership}")
print(f"Very Fast: {very_fast_membership}")
print(f"Extremely Fast: {extreme_fast_membership}")
#This code prints the input speed and the calculated membership values for each fuzzy set.
#It provides a clear summary of how much the input speed belongs to each speed category based on the fuzzy logic definitions


plt.show()
#plt.show() is a function in the matplotlib.pyplot library that displays any plots or figures created during a Python session
#This single line plays a crucial role in making the results of your plotting code visible on the screen.
#Without it, any plots you create using Matplotlib functions like plt.plot(), plt.xlabel(), etc.
#would remain hidden in the background and wouldn't be displayed to the user.


#Summary:
#The combined code demonstrates how fuzzy logic can be used to categorize real-world data (car speed in this case)
#with flexible boundaries and varying degrees of membership.
#This approach is particularly useful when the classification of data isn't entirely
#crisp or binary (e.g., a car can be considered "slow" to some degree even if it's not extremely slow)
