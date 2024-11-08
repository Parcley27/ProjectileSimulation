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

def searchForPowerAngleSetting(targetDistance, csvFilePath='power_angle_distance.csv', tolerance=0.05):
    # Open and read the CSV file
    with open(csvFilePath, mode='r') as file:
        reader = csv.DictReader(file)
        
        # Search for the first row where the distance is within the tolerance of the target
        for row in reader:
            distance = float(row["Distance (meters)"])
            
            if abs(distance - targetDistance) <= tolerance:
                # Matching row found
                powerSetting = row["Power Setting"]
                angle = row["Angle (degrees)"]
                print(f"To reach {targetDistance} meters, use power setting {powerSetting} and launch angle {angle} degrees.")
                return
        
        # If no match found
        print("No solution found with the available power settings and angles.")

def main():
    heights = [0.40, 0.76, 1.14, 1.65, 1.84]
    initialHeight = 0.26  # Starting height of the marble in m

    print("Choose an option:")
    print("1. Calculate the distance for a given angle and power setting.")
    print("2. Find the power setting and angle for a specific target distance.")
    print("3. Exit the program.")

    choice = int(input("Enter your choice (1, 2, or 3): "))

    if choice == 1:
        angle = float(input("Enter the launch angle in degrees (0 = flat): "))
        powerSetting = int(input("Enter the power setting (1 to 5): "))

        # Get the corresponding height for the power setting
        if powerSetting < 1 or powerSetting > len(heights):
            print("Invalid power setting.")
            return

        height = heights[powerSetting - 1]
        initialVelocity = calculateInitialVelocity(height)
        distance = calculateDistance(initialVelocity, angle, initialHeight)
        print(f"The marble travels {distance:.2f} meters.")
    
    elif choice == 2:
        targetDistance = float(input("Enter the target distance in meters: "))
        searchForPowerAngleSetting(targetDistance)
    
    elif choice == 3:
        print("Goodbye!")
        exit()
    
    else:
        print("Invalid choice.")

while True:
    print("")
    main()
