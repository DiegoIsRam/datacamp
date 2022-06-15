# baseball is available as a regular list of lists
# updated is available as 2D numpy array

# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)
print(f" Se imprime el array np_baseball : {np_baseball}")
print(f"Se imprime el array updated : Updated {updated}")
# Print out addition of np_baseball and updated
print(f"Se imprime la suma de los dos np_baseball + updated: {np_baseball+updated}")

# Create numpy array: conversion
conversion=np.array([0.0254,0.453592,1])

# Print out product of np_baseball and conversion
print(f"La multiplicacion final es:{np_baseball*conversion}")