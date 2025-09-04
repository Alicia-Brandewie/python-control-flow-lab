# # Exercise 1: Vowel or Consonant
# #
# # Write a Python function named `check_letter` that determines if a given letter
# # is a vowel or a consonant.
# #
# # Requirements:
# # - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# # - It should handle both uppercase and lowercase letters.
# # - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# # - If the letter is a consonant, print: "The letter x is a consonant."
# # - Replace 'x' with the actual letter entered by the user.
# #
# # Hints:
# # - Use the `input()` function to capture user input.
# # - Utilize the `in` operator to check for vowels.
# # # - Ensure to provide feedback for non-alphabetical or invalid entries.

# def check_letter():
#     # Your control flow logic goes here

#     letter = input('Enter a single letter, upper or lower case, to determine its case: ').lower()
#     vowel_tuple = ('a', 'e', 'i', 'o', 'u')
#     consonant_tuple = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
#     if letter in vowel_tuple:
#         print(f'The letter {letter} is a vowel.')
#     elif letter in consonant_tuple:
#         print(f'The letter {letter} is a consonant.')
#     else:
#         print('Invalid.')
        


# # Call the function
# check_letter()



# # Exercise 2: Old enough to vote?
# #
# # Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# # Fill in the logic to perform the eligibility check inside the function.
# #
# # Function Details:
# # - Prompt the user to input their age: "Please enter your age: "
# # - Validate the input to ensure the age is a possible value (no negative numbers).
# # - Determine if the user is eligible to vote. Set a variable for the voting age.
# # - Print a message indicating whether the user is eligible to vote based on the entered age.
# #
# # Hints:
# # - Use the `input()` function to capture the user's age.
# # - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# # - Use a conditional statement to check if the age meets the minimum voting age requirement.

# def check_voting_eligibility():
#     # Your control flow logic goes here
#     age = input('Please enter your age in years: ')

#     if type(age) == str or float:
#         num_age = int(age, 0)
#         if num_age >= 18:
#             print('You are eligible to vote.')
#         elif num_age <= 17:
#             print('You are not eligible to vote.') 
#     elif type(age) == float:
#         round_age = int(age, 0)
#         if round_age >= 18:
#             print('You are eligible to vote.')
#         elif round_age<= 17:
#             print('You are not eligible to vote.') 
#     else:     
#         print('Input not valid. Please enter a number.') 



def check_voting_eligibility():
    try:
        age_input = input("Please enter your age: ")
        age = float(age_input)

        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
        elif age >= 18:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for age.")



# Call the function
check_voting_eligibility()
# works with int but NOT with floats
# ValueError: invalid literal for int() with base 0: '45.5' for BOTH line 79 '== str or float' OR line 79 '== str' and 85 '== float'






# # Exercise 3: Calculate Dog Years
# #
# # Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# # Fill in the logic to perform the calculation inside the function.
# #
# # Function Details:
# # - Prompt the user to enter a dog's age: "Input a dog's age: "
# # - Calculate the dog's age in dog years:
# #      - The first two years of the dog's life count as 10 dog years each.
# #      - Each subsequent year counts as 7 dog years.
# # - Print the calculated age: "The dog's age in dog years is xx."
# # - Replace 'xx' with the calculated dog years.
# #
# # Hints:
# # - Use the `input()` function to capture user input.
# # - Convert the string input to an integer using `int()`.
# # # - Apply conditional logic to perform the correct age calculation based on the dog's age.

# def calculate_dog_years():
#     # Your control flow logic goes here
#     age = input("Input a dog's age: ")

#     int_age = int(age, 0)
#     if int_age <= 2:
#         print(f"The dog's age in dog years is {int_age * 10}.")
#     elif int_age >= 3:
#         print(f"The dog's age in dog years is {(int_age -2) * 7 +20}")

# # Call the function
# calculate_dog_years()


# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

# def weather_advice():
#     # Your control flow logic goes here
#     cold = input("Is it cold?(yes/no)")
#     raining = input("Is it raining?(yes/no)")

#     if cold == 'yes' and raining == 'yes':
#         print("Wear a waterproof coat.")

#     elif cold == 'yes' and raining != 'yes':
#         print("Wear a warm coat.")

#     elif cold != 'yes' and raining == 'yes':
#         print("Carry an umbrella.")

#     elif cold != 'yes' and raining != 'yes':
#         print("Wear light clothing.")



# # Call the function
# weather_advice()
# #WORKS


# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

# def determine_season():
#     # Your control flow logic goes here
#     month = input('Enter the month of the year as three characters (ie: Jan - Dec): ').lower()
#     day = input('Enter the day(numeral) of the month: ')

#     winter_tuple = ('dec', 'jan', 'feb', 'mar')
#     spring_tuple =('mar', 'apr', 'may', 'jun')
#     summer_tuple = ('jun', 'jul', 'aug', 'sep')
#     fall_tuple = ('sep', 'oct', 'nov' ,'dec')

#     int_day = int(day, 0)

#     for month in winter_tuple:
#         if (month == 'dec' and day >= 21) or (month == 'jan' or 'feb' ) or (month == 'mar' and  day <= 19):
#             season = 'Winter'

#     # season = (
#     #     if (month == 'dec' and day >= 21) or (month == 'jan' or 'feb' ) or (month == 'mar' and  day <= 19):
#     #         return 'Winter'
#     #     if (month == 'mar' and day >= 20) or (month == 'apr' or 'may' ) or (month == 'jun' and  day <= 20):
#     #         return 'Spring'
#     #     if (month == 'jun' and day >= 21) or (month == 'jul' or 'aug' ) or (month == 'sep' and  day <= 21):
#     #         return 'Summer'
#     #     if (month == 'sep' and day >= 22) or (month == 'oct' or 'nov' ) or (month == 'dec' and  day <= 20):                                              
#     #         return 'Fall'
#     # )
#         print(f'{month} {day} is in {season}.')

# # Call the function
# determine_season()
#LOST IN THE SAUCE


def determine_season():
    month_input = input("Enter the month of the year (Jan - Dec): ").strip().capitalize()
    day_input = input("Enter the day of the month: ").strip()

    # Validate day input
    try:
        day = int(day_input)
        if day < 1 or day > 31:
            print("Invalid day. Please enter a number between 1 and 31.")
            return
    except ValueError:
        print("Invalid input. Please enter a numeric value for the day.")
        return

    # Normalize month input
    month = month_input.lower()

    # Determine season
    if (month == 'dec' and day >= 21) or month in ('jan', 'feb') or (month == 'mar' and day <= 19):
        season = 'Winter'
    elif (month == 'mar' and day >= 20) or month in ('apr', 'may') or (month == 'jun' and day <= 20):
        season = 'Spring'
    elif (month == 'jun' and day >= 21) or month in ('jul', 'aug') or (month == 'sep' and day <= 21):
        season = 'Summer'
    elif (month == 'sep' and day >= 22) or month in ('oct', 'nov') or (month == 'dec' and day <= 20):
        season = 'Fall'
    else:
        print("Invalid date or month format.")
        return
    print(f"{month_input} {day} is in {season}.")

# Call the function
determine_season()