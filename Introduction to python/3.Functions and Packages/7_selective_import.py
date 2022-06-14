# Definition of radius
r = 192500

# Import radians function of math package
from math import radians as rad


# Travel distance of Moon over 12 degrees. Store in dist.
phi=rad(12)
dist=r*phi

# Print out dist
print(dist)
