# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
#Las siguientes formas de copiar una lista permiten que no modifiquemos la lista original
areas_copy = list(areas)
areas_copy_2=areas[:]
# Change areas_copy
areas_copy[0] = 5.0
areas_copy_2[0] =True
# Print areas
print(areas,areas_copy,areas_copy_2)