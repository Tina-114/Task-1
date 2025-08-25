def reverse_string(input_string):
    return input_string[::-1]

def is_palindrome(input_string):
    cleaned_string = input_string.lower().replace(" ", "")
    return cleaned_string == cleaned_string[::-1]

if __name__ == "__main__":
    text = input("Enter a string to reverse: ")
    reversed_text = reverse_string(text)
    print(f"Reversed string: {reversed_text}")
    
    text = input("\nEnter a string to check if it's a palindrome: ")
    if is_palindrome(text):
        print(f"\"{text}\" is a palindrome.")
    else:
        print(f"\"{text}\" is not a palindrome.")
    
    print("\nExamples of palindromes:")
    examples = ["radar", "level", "A man a plan a canal Panama", "Was it a car or a cat I saw"]
    for example in examples:
        print(f"\"{example}\" -> {is_palindrome(example)}")