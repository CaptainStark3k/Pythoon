import random

num = random.randint(1, 10)

for i in range(10):
    try:
        unum = int(input("Enter a number between 1 to 10: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if 1 <= unum <= 10:
        if unum > num:
            print("The number is smaller than the number you entered.")
        elif unum < num:
            print("The number is bigger than the number you entered.")
        else:
            print("🎉 Found the number!")
            break
    else:
        print("Please enter a number between 1 to 10.")
else:
    print("😢 You couldn't guess the number. It was", num)
