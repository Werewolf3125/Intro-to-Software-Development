# Day 3 Calculate Grade Nested if
# Note: User will input a score and the program will
# output a grade (A - F) on a 10 point scale
# Joseph Hollenbach 1/27/2021
# J. Treacy - added code to validate correct 0-100 range input
# as well as numeric digits input
# Define module
def main():

    go_again: str = 'y'
    while go_again == 'y':
        # Get test score from user
        scoreSt = input('Please enter your score (0-100): ')
        # check if valid digits Convert score to integer number
        if not (scoreSt.isdigit()):
            grade = "Invalid Numeric Integer Score input"
        else:
            score = int(scoreSt) # valid so convert and continue
            # Determine letter grade
            if score > 100:
                grade = "Invalid score too high "
            elif score >= 90:
                grade = 'A'
            elif score >= 80:
                grade = 'B'
            elif score >= 70:
                grade = 'C'
            elif score >= 60:
                grade = 'D'
            elif score >= 0:
                grade = 'F'
            else:
                grade = "Invalid score too low "
        # Output letter grade based on score
        print('Your score earns grade: ' + grade) # concatenate string type
        go_again = input('Do you want to enter another score? (y/n): ')

# Execute main module
main()