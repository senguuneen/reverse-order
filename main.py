def count_digits(number):
    count = 0
    while number > 0:
        number = number // 10
        count += 1
    return count

user_input = int(input("Enter a number: "))

if user_input == 0:
    print("The total number of digits is 1.")
else:
    total_digits = count_digits(user_input)
    print(f"The total number of digits is: {total_digits}")
