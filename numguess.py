secret_num = 0

while True:
    try:
        val = int(input("Guess the num: "))

        if val < secret_num:
            print("too low")
        elif val > secret_num:
            print("too hifgh")
        else:
            print("Correct")
            break
    except ValueError:
        print("enter a number")



