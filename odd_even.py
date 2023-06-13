odd_count = 0
even_count = 0

user_input = input("Enter a list of numbers (separated by spaces): ")

numbers = user_input.split()

for num in numbers:
    num = int(num)

    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
        
print("Odd count:", odd_count)
print("Even count:", even_count)

