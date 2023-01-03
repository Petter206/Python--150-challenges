#001 and 002
#firstname = input("Enter your first name: ")
#surname = input("Enter your surname: ")
#print("hello", firstname + "", surname)

#003
#print("What do you call a bear with no teeth?\nA gummy bear!")

#004
#number1 = input("Enter first value: ")
#number2 = input("Enter second value: ")
#print(number1 + number2) #make into an int and try the difference, look at answers for tips

#005
#num1 = int(input("please enter your first number: "))
#num2 = int(input("please enter your second number: "))
#num3 = int(input("please enter your third number: "))
#answer = (num1 + num2)* num3
#print("the answer is", answer)

#006
#start_slices = int(input("How many slices did you start with? "))
#slices_consoomed = int(input("How many slices have you eaten? "))
#answer = start_slices - slices_consoomed
#print("You have consoomed", answer, "slices off pizza") 

#007
#Name = input("Enter your name: ")
#Age = int(input("Enter your age: "))
#new_age = Age + 1
#print(Name, "next birthday you will be", new_age) 

#008
#total_price = int(input("How much was the bill?: "))
#num_dinner = int(input("How many dinners did you have?: "))
#price = (total_price/num_dinner) 
#print("Each person should pay", price)

#009
#days = int(input("How many days? "))
#hours = int(days * 24)
#minutes = int(hours * 60)
#seconds = int(minutes * 60)
#print("There are", hours, "hours", minutes, "minutes", "and", seconds, "seconds", "in", days, "days")

#010
#kilograms = int(input("How many kilograms? "))
#pounds = kilograms*2.204
#print(kilograms, "Is", pounds, "pounds")

#011
#num1 = int(input("Enter a number over 100: "))
#num2 = int(input("Enter a number under 10: "))
#result = num1/num2
#print(num1, "fits into", num2, result, "times")

#012
#num1 = int(input("Enter a number: "))
#num2 = int(input("Enter a second number: "))
#if num1 > num2:
   # print(num2, num1)
#else:
   # print(num1, num2)

#013
#num = int(input("Enter a number that is under 20: "))
#if num >=20:
    #print("Too high")
#elif num < 20:
    #print("Thank you")

#014
#num = int(input("Enter a number between 10 and 20: "))
#if num >= 10 and num <= 20:
    #print("Thank you") 
#else:
    #print("Incorrect answer")

#015
#colour = input("Your favorite colour: ")
#if colour == "red" or colour == "RED" or colour == "Red":
    #print("I like red too: ")
#else:
  #   print("I dont like", colour, "I prefer red")

#016
#Rain = input("Is it raining? ")
#Rain = str.lower(Rain)
#if Rain == "yes":
    #windy = input("Is it windy? ")
    #windy = str.lower(windy)
    #if windy == "yes":
      #  print("It is too windy for an umbrella")
   # else: print("Bring an umbrella")
#else: print("Have a nice day")

#017
#Age = int(input("How old are you? "))
#if Age >= 18:
    #print("You can vote")
#if Age == 17:
   # print("You can drive")
#if Age == 16:
  #  print("You can buy a lottery ticket")
#if Age < 16:
    #print("You can go trick or treating")

#018
#num = int(input("Enter a number: "))
#if num <10:
 #   print("Too low")
#elif num >=10 and num <=20:
   # print("Correct")
#else: print("Too high")

#019
#num = int(input("Enter 1,2 or 3: "))
#if num == 1:
  #  print("Thank you")
#elif num == 2:
    #print("Well done")
#elif num == 3:
   # print("Correct")
#else:
    #print("Error message")

#020
#name = input("Enter your first name: ")
#length = len(name)
#print(length)

#021
#first_name = input("Enter your first name: ")
#sur_name = input("Enter your surname: ")
#name = (first_name + " " + sur_name)
#Length = len(name)
#Length = str(Length)
#print(name + " has " + Length + " characters")

#022
#first_name = input("Enter your first name in lower case: ")
#sur_name = input("Enter your surname in lower case: ")
#first_name = first_name.title()
#sur_name = sur_name.title()
#name = first_name + " " + sur_name 
#print(name)

#023
#rhyme = input("Enter the first line of a nursery rhime: ")
#rhyme = len(rhyme)
#print(rhyme)
#starting_number = int(input("Enter a starting number: "))
#ending_number = int(input("Enter an ending number: "))
#part = (rhyme [starting_number:ending_number])
#print(part)

#024
#word = input("Enter a word: ")
#word = word.upper()
#print(word)

#025
#name = (input("Enter your first name: "))
#if len(name) >= 5:
    #print(name)
#else:
    #surname = (input("Enter your surname: "))
    #print(name + surname)

#026
#word = input("Enter a word: ")
#first = word[0]
#length = len(word)
#rest = word[1-length]
#if first != "a" and first != "e" and first != "i" and first != "o" and first != "u" and first != "y":
   # newword = rest + first + "ay"
   # print(newword)
#else:
    #print(word + "way")

#027
#import math
#num = float(input("Enter a number with lots of decimal places: "))
#print(num*2)

#028
#import math
#num = float(input("Enter a number with lots of decimal places: "))
#print(round (num, 2))

#029
#import math
#num = int(input("Enter an interger over 500: "))
#num = math.sqrt(num)
#print(round(num, 2))

#030
#import math
#print(round(math.pi, 5))

#031
#import math
#radius = int(input("Enter the radius of a circle: "))
#area = (radius**2)*math.pi
#print(area)

#032
#import math
#radius = int(input("Enter the radius of the cylinder: "))
#area = (radius**2)*math.pi
#height = int(input("Enter the height of the cylinder: "))
#volume = area*height
#print(round(volume, 3))

#033
#num_1 = int(input("Enter number the first number: "))
#num_2 =int(input("Enter the second number: "))
#new_num = num_1//num_2
#remainder = num_1%num_2
#print(num_1, "divided by", num_2, "is", new_num, "with", remainder, "remaining")

#034
#print("1) Square")
#print("2) Triangle")
#print("             ")
#num = int(input("Enter a number: "))
#if num == 1:
  #  lengthS = int(input("Enter the length of one of the sides: "))
   # area1 = lengthS*lengthS
  #  print("The area is: ", area1)
#elif num == 2:
   # base = int(input("Enter the base of the triangel: "))
    #height = int(input("Enter the height of the triangel: "))
    #area2 = (base*height)//2
    #print("The area is: ", area2)
#else:
  #  print("Error 69420, must enter 1 or 2") 

#035
#name = input("Enter your name: ")
#for i in range(0,3):
  #print(name)

#036
#name = (input("Enter your name: "))
#num = int(input("Enter a number: "))
#for i in range(0,num):
 # print(name)

#037
#name = input("Enter your name: ")
#for i in name:
  #print(i)

#038
#num = int(input("Enter a number: "))
#name = input("Enter your name: ")
#for x in range(0,num):
  #for i in name:
    #print(i)

#039
#num = int(input("Enter a number between 1 and 12: "))
#for i in range(1,13):
  #answer = i*num
 #print(answer)

#040
#num = int(input("Enter a number below 50: "))
#for i in (50,num):
  #print(i)

#041
#name = input("Enter your name: ")
#num = int(input("Enter a number: "))
#if num < 10:
  #for i in range(0,num):
    #print(name)
#else: 
  #for i in range(1,4):
    #print("Too high")

#042
#total = int(0)
#for i in range(1,5):
  #number = int(input("Enter a number: "))
  #x = input("Do want to include the number? y/n ")
  #if x == "y":
    #newnum = total + number
#print(newnum)

#043
#ud = input("Count up or down? ")
#if ud == "up":
  #num1 = int(input("Enter the top number: "))
  #for i in range(1,num1+1):
    #print(i)
#if ud == "down":
  #num2 = int(input("Enter a number below 20: "))
  #for i in range(20,num2-1, -1):
    #print(i)
#elif ud != "up" or "down":
  #print("I do not understand!!")

#044
#people = int(input("How many people do you want to invite? "))
#if people < 10:
  #for i in range(0,people):
    #name = input("Enter their name: ")
    #print(name, " has been invited:")
#if people >= 10:
  #print("Too many people")

#045
#total = 0
#while total <= 50:
  #num = int(input("Enter a number: "))
  #total = total+num
  #print("The total is ", total)

#046
#number = 0
#while number <=5:
  #num2 = int(input("Enter a number: "))
  #number = num2
#if number > 5:
  #print("The last number you entered was a", number)

#047
#num1 = int(input("Enter a number: "))
#again = "y"
#total = num1
#while again =="y":
  #num2 = int(input("Enter another number: "))
  #total = total+num2
  #again = input("Do you want to enter another number? y/n ")
#print(total)

#048
#again = "yes"
#total = 0
#while again == "yes":
    #name = input("Who do you want to invite? ")
    #print(name, "was invited")
    #total = total+1
    #again = input("Do you want to invite somebody else? ")
#print(total, "people will be attending the party")

#049
#compnum = 50
#guess = int(input("Guess the number: "))
#count = 1
#while guess != compnum:
  #if guess < compnum:
    #print("Too low")
  #else:
    #print("Too high")
  #count = count+1
  #guess = int(input("Guess the number: "))
#print("Well done, you took", count, "attempts")

#050
#number = int(input("Enter a number between 10 and 20: "))
#while number > 20 or number < 10:
    #if number > 20:
        #print("Too high")
    #if number < 10:
        #print("Too low")
    #number = int(input("Try again: "))
#print("Thank you")

#051
#num = 10
#while num > 0:
    #print("There are", num, "green bottles hanging on the wall", num, "green bottles hanging on the wall", "and if one green bottle accidentally falls")
    #num = num - 1
    #guess = int(input("How many green bottles are hanging on the wall? "))
    #if guess == num:
        #print("There will be", num, "green bottles hanging on the wall")
    #else:
        #while guess != num:
            #guess = int(input("No, try again: "))
#else: 
  #print("There are no more green bottles hanging on the wall")

#052
#import random
#num = random.randint(1,100)
#print(num)

#053
#import random
#fruit = random.choice(["Apple", "Kiwi", "Mango", "Banana", "Lemon"])
#print(fruit)

#054
#import random
#side = random.choice(["heads", "tails"])
#guess = input("Heads or tails): ")
#if guess == side:
  #print("You win")
#else:
  #print("Bad luck")
#print("The computer selected", side)

#055
#import random
#number = random.randint(1, 5)
#guess = int(input("Guess a number between 1 and 5: "))
#if guess == number:
  #print("Well done")
#else:
  #if number < guess:
    #print("Too high")
  #if number > guess:
    #print("Too low")
  #guess = int(input("Pick a second number between 1 and five: "))
  #if guess == number:
    #print("Correct")
  #else:
    #print("You lose")

#056
#import random
#number = random.randint(1,10)
#guess = int(input("Guess the number: "))
#while guess != number:
  #guess = int(input("Guess the number: "))

#057
#import random
#number = random.randint(1,10)
#guess = int(input("Guess the number: "))
#while guess != number:
  #if guess > number:
    #print("Too high")
  #elif guess < number:
    #print("Too low")
  #guess = int(input("Guess the number: "))

#058
#import random
#score = 0
#for i in range(1,6):
  #num1 = random.randint(1,50)
  #num2 = random.randint(1,50)
  #question = num1 + num2
  #print(num1,"+",num2)
  #answer = int(input("What is the answer? "))
  #if answer == question:
   #score = score +1 
#print("You got", score, "out of 5")

#059
#import random
#color = random.choice(["green", "blue","red", "purple", "yellow" ])
#print("green", "blue", "red", "purple", "yellow")
#retry = True
#while retry == True:
  #choice = input("Pick a colour: ")
  #if color == choice:
    #print("Well done")
  #else:
    #if color == "green":
      #print("I bet youre green with envy")
    #if color == "blue":
      #print("You are probably feeling blue right now")
    #if color == "red":
      #print("I bet youre red with anger")
    #if color == "purple":
      #print("You are probably purple")
    #if color == "yellow":
      #print("Youre probably listening to the epice song yellow")
#if color != choice:
  #retry = True
#else:
  #retry = False

#60
#import turtle
#for i in range(0,4):
  #turtle.forward(100)
  #turtle.right(90)
#turtle.exitonclick    

#61
#import turtle
#for i in range(0,3):
  #turtle.forward(100)
  #turtle.left(120)
#turtle.exitonclick()

#62
#import turtle
#for i in range(0,360):
  #turtle.forward(1)
  #turtle.right(1)

#63
#import turtle
#turtle.color("black", "red")
#turtle.begin_fill()

#69
#countries_tuple = ("Djibouti", "Sweden", "United Kingdom", "China", "Chad")
#print(countries_tuple)
#country = input("Choose a country: ")
#print(countries_tuple.index(country))

#70
#countries_tuple = ("Djibouti", "Sweden", "United Kingdom", "China", "Chad")
#print(countries_tuple)
#country = input("Choose a country: ")
#print(countries_tuple.index(country))
#num = int(input("Enter a number: "))
#print(countries_tuple[num])

#71
#sports_list = ["Football", "Cricket"]
#sports_list.append(input("What is your favorite sport? "))
#sports_list.sort()
#print(sports_list)

#72
#subjects_list = ["History", "Math", "Geography", "P.E", "Biology", "Society studies"]
#print(subjects_list)
#remove = input("Which subject do you dislike? ")
#remove = subjects_list.index(remove)
#del subjects_list[remove]
#print(subjects_list)

#73
#food_dictionary = {}
#food1 = input("Enter a food you like: ")
#food_dictionary[1] = food1
#food2 = input("Enter a food you like: ")
#food_dictionary[2] = food2
#food3 = input("Enter a food you like: ")
#food_dictionary[3] = food3
#food4 = input("Enter a food you like: ")
#food_dictionary[4] = food4
#print(food_dictionary)
#dislike = int(input("Which food food do you want to remove? "))
#del food_dictionary[dislike]
#print(sorted(food_dictionary.values()))

#74
#colours_list = ["Red", "Blue", "Pink", "Purple", "Orange", "Yellow", "Green", "Brown", "Black", "White"]
#startnum = int(input("Enter a starting number between 0 and 4: "))
#endnum = int(input("Enter an ending number between 5 and 9: "))
#print(colours_list[startnum:endnum])

#75
#number_list = [123, 442, 982, 326]
#for i in number_list:
  #print(i)
#usernum = int(input("Enter a three digit number: "))
#if usernum in number_list:
  #print(number_list.index(usernum))
#else:
  #print("That is not in the list")

#76
#name1 = input("Who do you want to invite to your party? ")
#name2 = input("Invite a second person to your party: ")
#name3 = input("Invite a third person to your party: ")
#guest_list = [name1, name2, name3]
#again = input("Do you want to invite another person to your party? y/n ")
#while again == "y":
  #guest_list.append(input("Who do you want to invite? "))
  #again = input("Do you want to invite anoyher person to your party? y/n ")
#print("You have invited", len(guest_list), "people to your party")

#77
#name1 = input("Who do you want to invite to your party? ")
#name2 = input("Invite a second person to your party: ")
#name3 = input("Invite a third person to your party: ")
#guest_list = [name1, name2, name3]
#again = input("Do you want to invite another person to your party? y/n ")
#while again == "y":
  #guest_list.append(input("Who do you want to invite? "))
  #again = input("Do you want to invite anoyher person to your party? y/n ")#print("You have invited", len(guest_list), "people to your party")
#print(guest_list)
#nameselection = input("Enter a name on the list: ")
#print(guest_list.index(nameselection))
#remove = input("Do you still want that person to come to your party?: ")
#if remove == "no":
  #guest_list.remove(nameselection)
  #print(guest_list)

#78
#programs_list = ["Breaking bad", "Better Call Saul", "The Big Bang", "AmongusTV"]
#print(programs_list)
#newshow = input("Enter another show: ")
#position = int(input("Enter the position on the index: "))
#programs_list.insert(position, newshow)
#print(programs_list)

#79
#nums = []
#for i in range(0,3):
  #num = input("Enter a number: ")
  #nums.append(num)
  #print(nums)
#keepitem = input("Do you want to keep your last number saved? ")
#if keepitem == "no":
  #nums.remove(num)
#print(nums)

#80
#first_name = input("Enter your first name: ")
#print("Your first name has", len(first_name), "characters")
#surname = input("Enter your surname: ")
#print("Your surname has", len(surname), "characters")
#print("Your full name is", first_name, surname)
#full_name = first_name +" " + surname
#letters = len(full_name)
#print("Your full name has", letters, "characters")

#81
#subject = input("Enter your favorite school subject: ")
#for letter in subject:
  #print(letter, end="-")

#82
#poem = ("What is the world, O soldiers? "
#"It is I: "
#"I, this incessant snow, "
#"This northern sky; "
#"Soldiers, this solitude through which we go "
#"is I.")
#print(poem)
#start_point = int(input("Enter a starting number: "))
#end_point = int(input("Enter an ending number: "))
#print(poem[start_point:end_point])

#83
#word = input("Type any word in upper case: ")
#retry = False
#if word.isupper():
  #print("Thank you")
#else:
  #retry = True
#while retry == True:
  #word = input("Try again: ")
  #if word.isupper():
    #retry = False
    #print("Thank you")

#84
#postcode = input("Enter your postcode: ")
#scode = postcode[0:2]
#scode = scode.upper()
#print(scode)

#85
#name = input("Enter your name: ")
#count = 0
#for x in name:
  #if x in name == "a" or x ==  "e" or x == "i" or x == "o" or x == "u":
    #count = count + 1
#print("You have", count, "vowels in your name")

#86
#password = input("Choose a password: ")
#confirm = input("Confirm your password: ")
#if password == confirm:
  #print("Thank you")
#elif password != confirm and password.lower() == confirm.lower():
  #print("Passwords must be in the same case")
#else:
  #print("Incorrect")
