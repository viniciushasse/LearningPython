numbers = []
print ("Type how many numbers you want, when you are done type done and I will show you the largest and the smallest among them")

while True:
    user_input = input("What number do you want ? ")
    if user_input == 'done':
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. PLease type a number or 'done' if you are finished.")

if numbers:
    print("The largest number is: ", max(numbers))
    print("The smallest number is: ", min(numbers))
else:
    print("No numbers where entered.")