# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs=areas[0:6]

# Use slicing to create upstairs
upstairs=areas[6:10]
upstairs2=areas[-4:]

# Print out downstairs and upstairs
print(downstairs, upstairs)
print("la segunda forma de almacenar los ultimos 4 valores de la lista ",upstairs2)