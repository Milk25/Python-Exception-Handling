def get_number_of_servings(prompt):
    while True:
        try:
            servings = int(input(prompt))
            if servings <= 0:
                print("Number of servings must be a positive integer.")
            else:
                return servings
        except ValueError:
            print("Invalid input! Please enter a valid number for servings.")

def main():
    try:
        original_servings = get_number_of_servings("Enter the original number of servings: ")
        new_servings = get_number_of_servings("Enter the number of servings you wish to make: ")
        print("Original servings:", original_servings)
        print("Desired servings:", new_servings)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
    
    




def get_number_of_servings(prompt):
    while True:
        try:
            servings = int(input(prompt))
            if servings <= 0:
                print("Number of servings must be a positive integer.")
            else:
                return servings
        except ValueError:
            print("Invalid input! Please enter a valid number for servings.")

def main():
    try:
        original_servings = get_number_of_servings("Enter the original number of servings: ")
        new_servings = get_number_of_servings("Enter the number of servings you wish to make: ")
        print("Original servings:", original_servings)
        print("Desired servings:", new_servings)
        
        try:
            adjustment_factor = new_servings / original_servings
            print("Adjustment factor:", adjustment_factor)
            
            # Display adjusted recipe quantities
            print("Adjusted recipe quantities:")
            # Your recipe adjustment logic goes here
            
        except ZeroDivisionError:
            print("Error: The original number of servings cannot be zero.")
        except ArithmeticError as e:
            print("Arithmetic error occurred:", e)
        except Exception as e:
            print("An error occurred:", e)
    finally:
        print("Enjoy your cooking!")

if __name__ == "__main__":
    main()
