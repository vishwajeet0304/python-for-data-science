
# Student Marks Calculator

# Accept marks from the user
maths = float(input("Enter Mathematics marks: "))
cs = float(input("Enter Computer Science marks: "))
statistics = float(input("Enter Statistics marks: "))
english = float(input("Enter English marks: "))
physics = float(input("Enter Physics marks: "))

# Calculate total marks
total = maths + cs + statistics + english + physics

# Calculate average marks
average = total / 5

# Calculate percentage
percentage = (total / 500) * 100

# Display results
print("\n--- Student Result ---")
print("Total Marks:", total, "/ 500")
print("Average Marks:", average)
print("Percentage:", percentage, "%")
