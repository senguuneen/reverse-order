import math

def count_digits(number):
    if number == 0:
        return 1
    elif number < 0:
        number = abs(number)
    return int(math.log10(number)) + 1

def main():
    user_input = input("Enter a number: ")
    
    try:
        number = float(user_input)
        digits = count_digits(abs(number)) if not isinstance(number, bool) else 1
        print(f"✨ Total digits in the number: {digits} ✨")
    except ValueError:
        print("⚠️ Invalid input! Please enter a valid number. ⚠️")

if __name__ == "__main__":
    main()
