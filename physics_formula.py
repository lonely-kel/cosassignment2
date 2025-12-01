print("=== PHYSICS FORMULA CALCULATOR ===")
print("Choose a formula to calculate:")
print("1. Speed = Distance / Time")
print("2. Force = Mass * Acceleration")
print("3. Pressure = Force / Area")
print("4. Work Done = Force * Distance")
print("5. Kinetic Energy = 0.5 * Mass * Velocity^2")
choice = int(input("Enter your choice (1-5): "))

# Speed formula

if choice == 1:
    distance = float(input("Enter distance (m): "))
    time = float(input("Enter time (s): "))
    speed = distance / time
    print("Speed =", speed, "m/s")

# Force formula

elif choice == 2:
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s^2): "))
    force = mass * acceleration
    print("Force =", force, "N")

# Pressure formula

elif choice == 3:
    force = float(input("Enter force (N): "))
    area = float(input("Enter area (m^2): "))
    pressure = force / area
    print("Pressure =", pressure, "Pa")

# Work Done formula

elif choice == 4:
    force = float(input("Enter force (N): "))
    distance = float(input("Enter distance (m): "))
    work = force * distance
    print("Work Done =", work, "J")

# Kinetic Energy formula

elif choice == 5:
    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))
    ke = 0.5 * mass * (velocity ** 2)
    print("Kinetic Energy =", ke, "J")
else:
    print("Invalid choice. Please run the program again.")

