#!/usr/bin/env python
# coding: utf-8

# # 1. Dice Roll Stimulator

# In[1]:


import random;
while int(input('Press 1 to roll the dice or 0 to exit:\n')): print(random.randint(1,6))


# # 2. Rock, paper & scissors game

# the goal is to create a command-line game where a user is given a chance to choose between rock, paper, and scissors and is the user wins the score is added, and at the end when the user finishes the game the score is shown to the user.

# In[3]:


import random
choices = ["Rock", "Paper", "Scissors"]
computer = random.choices(choices)
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("Rock, Paper or Scissors?").capitalize()
    ## conditions of rock, paper and scissors
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", players)
            cpu_score+=1
        else:
            print("You win!", player, "smashes", computer)
            player_score+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            cpu_score+=1
        else:
            print("You win!", player, "covers", computer)
            player_score+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            cpu_score+=1
        else:
            print("You win!", player, "cut", computer)
            player_score+=1
    elif player=='E':
        print("Final scores:")
        print(f"CPU:{cpu_score}")
        print(f"Player:{player_score}")
        break
    else:
        print("That's not a valid play. Check you spelling!")
    computer = random.choice(choices)


# # 3. Random Password Generator 

# create a program that takes the length of the password and generates a random password of the same length

# hint: create a string of numbers+capital letters+lower case letters+special characters. Take a random sample from the string of a length given by the user.

# In[5]:


import random
passlen = int(input("Enter the length of password"))
s="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s,passlen))
print (p)


# # 4. mad libs generator 

# the task is to generate a random and unique story by adding the input given by ther user.

# In[6]:


color = input("Enter a color:")
pluralNoun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")
print("Roses are", color)
print(pluralNoun + "are blue")
print("I love", celebrity)


# # 5. Guess the number game

# In this game, the task is to create a script that generates a random number between a range if the user guesses the number right in three chance then user wins otherwise user loss. 

# hint: to generate a number user random number and using a loop gives the user only three chances to guess and according to the user's guess print a satisfactory output.

# In[1]:


import random
number = random.randint(1,10)
for i in range(0,3):
    user = int(input("guess the number"))
    if user == number:
        print("Hurray!!")
        print(f"you guessed the number right it's {number}")
        break
    elif user>number:
        print("Your guess is too high")
    elif user<number:
        print("Your guess is to low.")
else:
    print(f"Nice Try!, but the number is {number}")


# # 6. story generator 

# the task is to generate a random story every time user runs the program. 
# hint: random module can be used to select random parts of the story stored in different lists. 

# In[3]:


import random
when = ['A few years ago', 'Yesterday', 'Last Night', 'A long time ago', 'On 20th Jan']
who = ['a rabbit', ' an elephant', 'a mouse', 'a turtle', 'a cat']
name = ['Ali', 'Miriam', 'daniel', 'Hoouk', 'Starwalker']
residence = ['Barcelona', 'India', 'Germany', 'Venice', 'England']
went = ['cinema', 'university', 'seminar', 'school', 'laundry']
happened = ['made a lot of friends', 'Eats a burger', 'found a secret key', 'solved a misery', 'wrote a book']
print(random.choice(when) + ' , ' + random.choice(who) + ' that lived in' + random.choice(residence) + 
      ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))


# # 7. Email slicer program

# python script that can fetch the username and domain name from the email. Hint divide the email into two strings using @ as divider 

# In[1]:


#get the user's email address
email = input("what is your email address?: ").strip()
#slice out the user name
user_name = email[:email.index("@")]
#slice out the domain name
domain_name = email[email.index("@")+1:]
#format message 
res = f"Your username is '{user_name}' and your domain name is '{domain_name}'"
#display the result message
print(res)


# # 8. automating emails

# the task is to write a python script using which you can send emails. 
# Hint - email library can be used to send emails. 

# In[4]:


import smtplib
from email.message import EmailMessage
email = EmailMessage() ## creating an object for EmailMessage
email['from'] = 'xyz name' ##Person who is sending
email['to'] = 'xyz id' ##whom we are sending
email['subject'] = 'xyz subject' ##subject of email
email.set_content("Xyz content of email") ##content of email
with smtplib.SMTP(host='smtp.gmail.com',port=587)as smtp:
## sending request to server
     smtp.ehlo()  ##server object
smtp.starttls()   ##used to send data between server and client
smtp.login("email_id","Password") ##login id and password of gmail
smtp.send_message(email)  ##sending email
print("email send")  ##printing success message 


# # 9. Acronym

# python script that generates an acronym word from a given sentence. hint: you can use split and indexing to fetch the first word and then combine it. 

# In[5]:


text = str(input("Enter a string\n"))
text = text.split()
acronym = ""
for i in text:
    acronym = acronym+str(i[0]).upper()
print(acronym)


# # 10. text-based adventure

# python script that takes the user on a fun adventure by choosing different options for the path. 

# In[6]:


name = str(input("Enter your name\n"))
print(f"{name} you are stuck in a forest. your task is to get out from the forest without dieing")
print("you are walking threw forest and suddenly a wolf comes in your way. now you have two option")
print("1.run 2.climb the nearest tree")
user = int(input("Choose one option 1 or 2"))
if user==1:
    print("you died!!")
elif user==2:
    print("you survived!!")
else:
    print("incorrect input")
## add a loop and increase the story as much as you can


# # 11. Hangman
# task is to create a simple command-line hangman game. Hint create a list of secret words and randomly pick a word. now represents each word as _ and give user chances to guess the word if the user guesses the word right then replace _ with the word.

# In[4]:


import time
import random
name = input("what is your name? ")
print ("Start guessing...\n")
time.sleep(0.5)
## a list of secret words
words = ['python','programming','treasure','creative','medium','horror']
word = random.choice(words)
guesses = ''
turns = 5
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print (char,end="")
        else:
            print ("_",end=""),
            failed += 1
    if failed == 0:
        print ("\nYou won")
        break
    guess = input("\nguess a character:")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("\nWrong")
        print("\nYou have", + turns, 'more guesses')
        if turns == 0:
            print ("\nYou Lose")


# # 12. Alarm Clock
# hint: use the date-time module to create an alarm clock and play sound library for playing alarm sound.

# In[2]:


pip install playsound


# In[3]:


from datetime import datetime
from playsound import playsound
alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_seconds=alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Setting up alarm..")
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if(alarm_period==current_period):
        if(alarm_hour==current_hour):
            if(alarm_minute==current_minute):
                if(alarm_seconds==current_seconds):
                    print("Wake Up!")
                    playsound('audio.mp3') #download the alarm sound from link
                    break


# # 13. Audio Book
# python script that can be used to convert a pdf inot an audiobook.
# hint take help of pyttsx3 library to convert text into speech.
# installation: pyttsx3, PyPDF2

# In[5]:


pip install pyttsx3


# In[6]:


import pyttsx3, PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('file.pdf', 'rb'))
speaker = pyttsx3.init()
for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()


# # 15. face detection
# script that can detect faces in an image and save all the faces in a folder HInt: haar cascade classifier can be used to detect the faces. it returns coordinates of the faces, using those faces can be saved as a file. 

# In[7]:


import cv2
#load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# read the input image
img = cv2.imread('images/img0.jpg')
#convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#detect faces
faces = face_cascade.detectMultiScale(gray, 1.3, 4)
# draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y),(x+w, y+h), (255, 0, 0), 2)
    crop_face = img[y:y + h, x:x + w]
    cv2.imwriter(str(w) + str(h) + '_faces.jpg', crop_faces)
#display the output 
cv2.imshow('img', img)
cv2.imshow("imgcropped",crop_face)
cv2.waitKey()


# In[ ]:




