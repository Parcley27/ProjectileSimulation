import math
import csv

# Initial parameters
# Local gravity in m/s^2
gravity = 9.81

# Launch starting height in m
initialHeight = 0.26 # Change as needed

# Projectile max height at each power level
heights = [0.40, 0.76, 1.14, 1.65, 1.84] # Change as needed

# Min and max search angles
minAngle = 0
maxAngle = 90

# Average real disntance loss in m
realGains = 0.05

def calculateInitialVelocity(height):
    initialVelocity = math.sqrt(-2 * -gravity * height)

    return initialVelocity

def calculateDistance(initialVelocity, angle, initialHeight):
    radianAngle = math.radians(angle)
    
    xVelocity = initialVelocity * math.cos(radianAngle)
    yVelocity = initialVelocity * math.sin(radianAngle)
    
    discriminant = yVelocity ** 2 + 2 * gravity * initialHeight
    
    flightTime = (yVelocity + math.sqrt(discriminant)) / gravity
    
    distance = (xVelocity * flightTime) + realGains

    return distance

with open("PowerAngleDistance.csv", mode = "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(["Power Setting", "Angle (degrees)", "Distance (meters)"])
    
    for powerSetting in range(1, len(heights) + 1):
        height = heights[powerSetting - 1]
        initialVelocity = calculateInitialVelocity(height)
        
        for angle in range(0, maxAngle + 1):
            distance = calculateDistance(initialVelocity, angle, initialHeight)

            writer.writerow([powerSetting, angle, f"{distance:.2f}"])

print("Write Success! Lookup table updated")
