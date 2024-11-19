import math
import csv

# Initial parameters
# Local gravity in m/s^2
gravity = 9.81

# Launch starting height in m
initialHeight = 0.26 # Change as needed

# Projectile max height at each power level
heights = [0.40, 0.76, 1.14, 1.65, 1.84] # Change as needed

# Average real disntance loss in m
realGains = 0.05

# Brute force file name
bruteForce = "BruteForceSettings.py"

def calculateInitialVelocity(maxHeight):
    initialVelocity = math.sqrt(-2 * -gravity * maxHeight)

    return initialVelocity

def calculateFlight(initialVelocity, angle, initialHeight):
    radianAngle = math.radians(angle)
        
    xVelocity = initialVelocity * math.cos(radianAngle)
    yVelocity = initialVelocity * math.sin(radianAngle)
    
    discriminant = yVelocity ** 2 + 2 * gravity * initialHeight
    
    flightTime = (yVelocity + math.sqrt(discriminant)) / gravity
    
    distance = (xVelocity * flightTime) + realGains

    return (distance, flightTime)

def searchForAngleAndPowerSettings(targetDistance, shortTolerance = 0.05, longTolerance = 0.1):
    csvFilePath = "PowerAngleDistance.csv"

    with open(csvFilePath, mode='r') as file:
        reader = csv.DictReader(file)
        
        # Use the first row where the distance matches within tolerance
        # Lower/less extreme settings should be more precise
        for row in reader:
            distance = float(row["Distance (meters)"])
            
            if (targetDistance - shortTolerance) <= distance <= (targetDistance + longTolerance):
                powerSetting = row["Power Setting"]
                angle = row["Angle (degrees)"]

                return (angle, powerSetting)
        
        # If no match found
        print("No solution found with the available power settings and angles.")

def mainLoop():
    print("Choose an option:")
    print("1. Calculate the distance for a given angle and power setting.")
    print("2. Find the power setting and angle for a specific target distance.")
    print("3. Exit the program.")

    choice = int(input("Enter your choice (1, 2, or 3): "))

    print()

    if choice == 1:
        angle = float(input("Enter the launch angle in degrees (0 = flat, 90 = up): "))
        powerSetting = int(input(f"""Enter the power setting (1 to {len(heights)}: """))

        if powerSetting < 1 or powerSetting > len(heights):
            print("Invalid power setting.")
            return

        height = heights[powerSetting - 1]
        initialVelocity = calculateInitialVelocity(height)

        flightProfile = calculateFlight(initialVelocity, angle, initialHeight)
        flightDistance = round(flightProfile[0], 2)
        flightTime = round(flightProfile[1], 2)

        print(f"""\nThe projectile travels {flightDistance} meters over {flightTime}s.""")
    
    elif choice == 2:
        targetDistance = float(input("Enter the target distance in meters: "))

        launchParameters = searchForAngleAndPowerSettings(targetDistance, 0.00, 0.05)
        launchAngle = launchParameters[0]
        launchPower = launchParameters[1]

        print(f"To reach {targetDistance} meters, launch at {launchAngle} degrees and use power setting {launchPower}.")

    
    elif choice == 3:
        print("Goodbye!")
        exit()
    
    else:
        print("Invalid choice, please try again.")

with open(bruteForce) as scriptFile:
    code = scriptFile.read()
    exec(code)

while True:
    print("")
    mainLoop()
