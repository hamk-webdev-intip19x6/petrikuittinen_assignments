def ask(question, choices, correct, retries=2):
    print(question)
    for i, choice in enumerate(choices, start=1):
        print(i, choice)
    while retries > 0:
        try:
            guess = int(input("?"))
        except ValueError:
            continue
        if guess == correct:
            print("Correct!")
            break
        print("Wrong guess")
        retries -= 1
    else:
        print("The correct reply was choice", correct, "=", choices[correct - 1])

ask("What is the capital of Australia?", \
    ("London", "Sydney", "Canberra", "Victoria"), 3)
ask("When Finland gained independence?", \
    ("1900", "1917", "1919", "1939"), 2, 1)
ask(question = "What is the chemical symbol of Iron?", \
    correct=1, choices=("Fe", "R", "Ir", "I"))
ask(question="How to delete a variable in Python?", \
    retries=3, choices=("delete", "del", "remove", "destroy"), 2)
ask("How to delete a variable in Python?", \
    ("delete", "del", "remove", "destroy"), \
    retries=3, correct=2)
