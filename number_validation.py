def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    return armstrong_sum == number

def explain_armstrong_calculation(number):
    num_str = str(number)
    num_digits = len(num_str)
    
    calculation = " + ".join([f"{digit}^{num_digits}" for digit in num_str])
    result = " + ".join([f"{int(digit) ** num_digits}" for digit in num_str])
    total = sum(int(digit) ** num_digits for digit in num_str)
    
    explanation = f"{calculation} = {result} = {total}"
    
    if total == number:
        return f"{number} is an Armstrong number because {explanation}"
    else:
        return f"{number} is not an Armstrong number because {explanation} ≠ {number}"

if __name__ == "__main__":
    year = int(input("Enter a year to check if it's a leap year: "))
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
    print("Note: A year is a leap year if divisible by 4 but not by 100, unless it's also divisible by 400.")
    
    number = int(input("\nEnter a number to check if it's an Armstrong number: "))
    if is_armstrong_number(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")
    
    print(explain_armstrong_calculation(number))
    
    print("\nExamples of Armstrong numbers:")
    armstrong_examples = [153, 370, 371, 407]
    for example in armstrong_examples:
        print(explain_armstrong_calculation(example))