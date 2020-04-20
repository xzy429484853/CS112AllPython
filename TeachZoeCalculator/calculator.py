numbers = []
actions = []
allowedActions = ["+", "-", "*", "/", "h"]
currentAnswer = None
active = True


def getHistory():
    history = ""
    for index, value in enumerate(numbers):
        # print(index, value)
        # if index
        if index != len(actions):
            history += str(value) + " " + actions[index] + " "
        else:
            history += str(value) + " "
    return history

while active:
    if numbers:
        action = input("Please choose one(+, -, *, /, ^, h (history): ")
        if action not in allowedActions:
            print("Invalid action, please try again...")
            continue
        else:
            if action == "h":
                l = getHistory()
                print(l + "= " + str(currentAnswer))
            else:
                actions.append(action)

        # take user input for number

    try:
        inp = float(input("->  "))
    except:
        print("That is an invalid number, please try again.")
        continue


    if currentAnswer != None:
        if actions[-1] == "+":
            currentAnswer += inp
        elif actions[-1] == "-":
            currentAnswer -= inp
        elif actions[-1] == "*":
            currentAnswer *= inp
        elif actions[-1] == "/":
            currentAnswer = currentAnswer / inp
    else:
        currentAnswer = inp
    if currentAnswer != None:
        print("->> " + str(currentAnswer))

    numbers.append(currentAnswer)
