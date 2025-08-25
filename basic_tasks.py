def sum_two_numbers(num1, num2):
    return num1 + num2

def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    
    return fib_sequence

if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"Sum: {sum_two_numbers(num1, num2)}")
    
    num = int(input("\nEnter a number to check if it's odd or even: "))
    print(f"Result: {check_odd_even(num)}")
    
    num = int(input("\nEnter a number to calculate its factorial: "))
    print(f"Factorial: {calculate_factorial(num)}")
    
    n = int(input("\nEnter how many Fibonacci numbers to generate: "))
    print(f"Fibonacci Sequence: {generate_fibonacci(n)}")