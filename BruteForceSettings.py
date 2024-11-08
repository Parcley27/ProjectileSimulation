import math
import csv

def calculateInitialVelocity(height):
    # Calculate initial velocity required to reach height h from height x
    g = -9.81  # gravitational acceleration in m/s^2
    initialVelocity = math.sqrt(-2 * g * height)
    return initialVelocity

def calculateDistance(initialVelocity, angle, initialHeight):
    # Convert the angle to radians
    angleRadians = math.radians(angle)
    
    # Define gravitational acceleration (m/s^2)
    g = 9.81
    
    # Calculate the horizontal and vertical components of the initial velocity
    v_x = initialVelocity * math.cos(angleRadians)
    v_y = initialVelocity * math.sin(angleRadians)
    
    # Calculate the time of flight
    # Using the quadratic formula to solve for time t when the projectile hits the ground (y = 0)
    discriminant = v_y**2 + 2 * g * initialHeight
    if discriminant < 0:
        return None  # No real solution, meaning the projectile doesn't reach ground level
    
    t_flight = (v_y + math.sqrt(discriminant)) / g
    
    # Calculate the horizontal distance
    distance = v_x * t_flight
    return distance

def main():
    heights = [0.40, 0.76, 1.14, 1.65, 1.84]
    initialHeight = 0.26  # Starting height of the marble in m
    
    # Open a CSV file to write the results
    with open('power_angle_distance.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Power Setting", "Angle (degrees)", "Distance (meters)"])
        
        # Loop through each power setting and angle, calculating distances
        for powerSetting in range(1, len(heights) + 1):
            height = heights[powerSetting - 1]
            initialVelocity = calculateInitialVelocity(height)
            
            for angle in range(0, 91):  # Angles from 0 to 90 degrees
                distance = calculateDistance(initialVelocity, angle, initialHeight)
                if distance is not None:
                    writer.writerow([powerSetting, angle, f"{distance:.2f}"])
    
    print("Write Success! Lookup table updated")

# Run the main function to output all data into a CSV file
main()
