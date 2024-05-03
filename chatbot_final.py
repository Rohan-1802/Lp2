
def greet(bot_name, birth_year):
    print("Hello! My name is {0}.".format(bot_name)) 
    print("I was created in {0}.".format(birth_year))
def remind_name():
    print('Please, remind me your name.')
    name = input()
    print("What a great name you have, {0}!".format(name))
def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.') 
    rem3 = int(input())
    rem5 = int(input()) 
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105 
    if age >= 18 :
        print("Your age is {0}; eligible for voting".format(age))
    else:
        print("Your age is {0}; is not eligible for voting".format(age))
    return
def test():
    print("Let's test your democratic knowledge.")
    print("Among the below-given countries, which country has the highest support for democracy?")
    print("1. India")
    print("2. Nepal") 
    print("3. Bangladesh") 
    print("4. Pakistan") 
    answer = 1
    guess = int(input())
    if guess==1:
        print("Your answer is right , India has the higgest support for democracy \n")
    while guess != answer:
        print("Please, try again.")
        guess = int(input()) 
    print("Who is President of India") 
    print("1.Pranav Mukharji") 
    print("2.Droupadi Murmu") 
    print("3.Ramnath Kovind") 
    print("4.Venkeya Naidu")
    answer2 = 2
    guess2 = int(input())
    if guess2==2:
        print("Your answer is right ,Droupadi Murmu is the president of India")
    while guess2!= answer2:
        print("Please, try again.")
        guess2 = int(input())
    print('Completed, have a nice day!') 
    print('.	')
    
def end():
    print('Congratulations, have a nice day!') 
    print('.	')
    
greet('TE-Chatbot', '2022') # change it as you need 
remind_name()
guess_age() 
test()
end()