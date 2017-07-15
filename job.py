
start = '''

You are driving home from working overtime at a job that you absolutely hate. You need to home by 8 pm for a dinner with your new boss. You have the option of taking the normal route or a shortcut.

'''
normal = '''
You decide to take the normal route and you get into a car crash with someone. No one is hurt but your car is badly damaged. Now you walk to the nearest bus stop. An hour passed and no bus is coming. You have the option to wait or call an uber. Type 'wait' to wait or type 'uber' to call an uber.
'''
shortcut = '''
You choose to take the shortcut and the police chases you thinking you are dirivng a getaway car for a bank robbery. You have an option to keep going or to explain to the cops. Type 'go' to keep going or type 'talk' to explain
'''

wait = '''
The bus comes 3 hours later. You missed your dinner and you did not get the job.

'''

uber = '''
You get on the uber with a driver that takes the long cut. The driver makes extra turns so the bill goes up. Your bill ends up being $500 and you are 10 minutes late to the dinner. However, you still get the job.
'''

go = '''
You keep driving faster in the hopes of escaping the cops. Unfortunately, you are not fast enough and you get a speeding ticket after you explain that you did not take part in the robbery. You come home late and miss the dinner. You did not get the new job.
'''

talk = '''
You talk with the cops and explain that you did not take part in the robbery. The cops understand and let you go. You continue to make your way to dinner and you get the job.
'''

print(start)




print("Type 'normal' to take the normal route or 'shortcut' to take the shortcut")
done= False
while not done:
    answer1 = input()


    if answer1 == "normal":
        print (normal)

        done1=False
        while not done1:
            answer2=input()
            if answer2 =="wait":
                print (wait)
                done=True
                done1=True
            elif answer2 =="uber":
                print (uber)
                done=True
                done1=True
            else:
                print ("Please type one of the options")
    elif answer1 == "shortcut":
        print(shortcut)

        done1=False
        while not done1:
            answer2=input()
            if answer2 =="go":
                print (go)
                done=True
                done1=True
            elif answer2 =="talk":
                print (talk)
                done=True
                done1=True
            else:
                print ("Please type one of the options")

    else:
        print ("Please type one of the options")
