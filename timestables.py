'''Program to practise times tables. Allows the user to '''


import random
import time

def number_answer():
    while True:
        try:
            number = int(input("> "))
            break
        except:
            print("Invalid input, please try again")

    return number

def letter_input(letter_list):
    while True:
        ans = str(input("> ")).lower()
        if ans in letter_list:
            break
        else:
            print("Invalid input, please try again")

    return ans



print("Hello, welcome to Times Table Trainer!\n"  \
     +"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


while True:
    print("Which Times Table do you want to Practice? (enter a number)")
    num_1 = number_answer()
    print("What number to go up to?")
    num_2 = number_answer()
    
    table = []
    for i in range(1,num_2+1):
        table.append((num_1, i, num_1*i))
    
    random.shuffle(table)
    incorrect_list = []
    start_time = time.time()
    
    while len(table) > 0:
        test_1, test_2, real_ans = table[0]
        print("\n"+str(len(table)),"questions to go.")
        print("What is",test_1,"×",test_2,"?")
        user_ans = number_answer()

        if user_ans == real_ans:
            print("Correct!")
        else:
            print("Incorrect - the answer was",real_ans)
            table.append(table[0])
            incorrect_list.append(str(test_1)+" × "+str(test_2)+" = "+str(real_ans))

        del table[0]


    completion_time = time.time() - start_time
    mins = int(completion_time/60)
    secs = int(completion_time - mins*60)
    num_incorrect = len(incorrect_list)
    min_text, sec_text, ans_text = "minutes", "seconds", "answers"
    if mins == 1:
        min_text = "minute"
    if secs == 1:
        sec_text = "second"
    if num_incorrect == 1:
        ans_text = "answer"

    print("\nCompleted in", mins, min_text,"and", secs, sec_text+"!")
    print("With",num_incorrect,"incorrect",ans_text+"!")
    if num_incorrect > 0:
        print("These were:")
        for entry in incorrect_list:
            print(entry)


    print("\nDo you want to go again? (y/n)")
    answer = letter_input(['y','n'])
    if answer == "y":
        print("\n~~~~~~~"       \
             +"\nNew Run"       \
             +"\n~~~~~~~\n")
        continue
    else:
        print("Goodbye!")
        break
     
    
        
