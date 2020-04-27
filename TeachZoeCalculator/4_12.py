a = True
while a:
    try:
        number1 = float(input("please type your number in here "))
        number2 = float(input("please type your another number in here "))
    except:
        print("An exception occurred")
        continue
    print("here is the choice for action")
    print("+")
    print("-")
    print("*")
    print("/")
    symbol = input("please choose your action here ")
    # This does x
    if symbol == "+":
        answer = float(number1) + float(number2)
        print("you have " + str(answer) + " now ")
    elif symbol == "-":
        answer = float(number1) - float(number2)
        print("you have " + str(answer) + " now ")
    elif symbol == "/":
        if  number2 == 0:
            print("An exception occurred")
            continue
        answer = float(number1) / float(number2)
        print("you have" + str(answer) + "now")
    elif symbol == "*":
        answer = float(number1) * float(number2)
        print("you have" + str(answer) + "now")
    else:
        print("a wrong choice")
    action = input("if you want to continue, hit enter; if not, type 00")
    a = false
    print("good bye!")












