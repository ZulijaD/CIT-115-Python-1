# Prompt for the person's name
str_name = input("Enter the person's name for the Grade Analyzer: ")

# Prompt for 4 test scores and validate input
try:
    int_score1 = int(input("Enter test score 1 (whole number only): "))
    int_score2 = int(input("Enter test score 2 (whole number only): "))
    int_score3 = int(input("Enter test score 3 (whole number only): "))
    int_score4 = int(input("Enter test score 4 (whole number only): "))
except ValueError:
    print("Invalid input. Please enter whole numbers only.")
    exit()

# Ensure all scores are non-negative
if int_score1 < 0 or int_score2 < 0 or int_score3 < 0 or int_score4 < 0:
    print("Test scores must be greater than 0.")
    exit()

# Prompt for whether to drop the lowest grade
str_drop_lowest = input("Drop the lowest grade? (Enter Y or N): ").upper()

if str_drop_lowest not in ["Y", "N"]:
    print("Enter Y or N to Drop the Lowest Grade.")
    exit()

# Calculate the average based on dropping the lowest grade or not
flt_average = 0.0
if str_drop_lowest == "Y":
    # Find the lowest score manually without using min() or lists
    if int_score1 <= int_score2 and int_score1 <= int_score3 and int_score1 <= int_score4:
        flt_average = (int_score2 + int_score3 + int_score4) / 3
    elif int_score2 <= int_score1 and int_score2 <= int_score3 and int_score2 <= int_score4:
        flt_average = (int_score1 + int_score3 + int_score4) / 3
    elif int_score3 <= int_score1 and int_score3 <= int_score2 and int_score3 <= int_score4:
        flt_average = (int_score1 + int_score2 + int_score4) / 3
    else:
        flt_average = (int_score1 + int_score2 + int_score3) / 3
else:
    # Average all four test scores
    flt_average = (int_score1 + int_score2 + int_score3 + int_score4) / 4

# Determine the letter grade based on the average
str_letter_grade = ""
if flt_average >= 97.0:
    str_letter_grade = "A+"
elif 94.0 <= flt_average < 97.0:
    str_letter_grade = "A"
elif 90.0 <= flt_average < 94.0:
    str_letter_grade = "A-"
elif 87.0 <= flt_average < 90.0:
    str_letter_grade = "B+"
elif 84.0 <= flt_average < 87.0:
    str_letter_grade = "B"
elif 80.0 <= flt_average < 84.0:
    str_letter_grade = "B-"
elif 77.0 <= flt_average < 80.0:
    str_letter_grade = "C+"
elif 74.0 <= flt_average < 77.0:
    str_letter_grade = "C"
elif 70.0 <= flt_average < 74.0:
    str_letter_grade = "C-"
elif 67.0 <= flt_average < 70.0:
    str_letter_grade = "D+"
elif 64.0 <= flt_average < 67.0:
    str_letter_grade = "D"
elif 60.0 <= flt_average < 64.0:
    str_letter_grade = "D-"
else:
    str_letter_grade = "F"

# Output the results
print(f"\nName: {str_name}")
print(f"Average: {flt_average:.1f}")
print(f"Letter Grade: {str_letter_grade}")
