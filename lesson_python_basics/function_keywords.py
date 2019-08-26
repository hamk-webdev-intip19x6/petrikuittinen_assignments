def ask(question, choices, correct, retries=2):
    i = 1
    print(question)
    for c in choices:
        print(i, c)
        i += 1
    while retries>0:
        try:
            guess = int(input("?"))
        except ValueError:
            continue
        if guess==correct:
            print("right")
            break
        print("wrong guess")
        retries -= 1
    else:
        print("the correct reply was", correct, choices[correct-1])

ask("What is the capital of Australia?", \
    ("London", "Sydney", "Canberra", "Victoria"), 3)
ask("When Finland gained independence?", \
    ("1900", "1917", "1919", "1939"), 2, 1)
ask("How to delete a variable in Python?", \
    ("delete", "del", "remove", "destroy"), \
    retries=3, correct=2)

