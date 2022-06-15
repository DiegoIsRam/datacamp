# np_baseball is available

# Import numpy
import numpy as np

# Create np_height_in from np_baseball
np_height_in=np.array(np_baseball[:,0])
print(f"El numpy array principal es: {np_height_in}")
# Print out the mean of np_height_in
print(np.mean(np_height_in))
enmedio=round(len(np_height_in)/2)
print("La mitad de los datos es: ", enmedio)
# Print out the median of np_height_in
print(f"The median data is: {np_height_in[enmedio+1]}")
print(np.median(np_height_in))