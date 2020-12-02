import sys
from time import sleep

print('''
RATE US >>>

How was your experience with AI arduino.
''')

b = ('''
Please write -->
1 for 'Terible' 🤬

2 for 'Bad' 😡

3 for 'Ok' 😐

4 for 'Nice' 😀

5 for 'Wow' 😎
''')

a = input(b)

if "1" in a:
    print("Ok, I will surely keep that in mind and work on the AI.")

elif "2" in a:
    print("Ok, I will work on the AI.")

elif "3" in a:
    print("Well, sure I will work on the AI.")

elif "4" in a:
    print("Thanks, buddy!")

elif "5" in a:
    print("Well, nailed it. Thanks a lot!")

else:
    print(b)

print("Want to send a note to the developer?")
develop = input('''
<--------------- NOTE -------------->
Please write your review here.

To exit this review write --> exit
''')

if "exit" in develop:
    sys.exit()

print('You wrote - ' + (develop))
print("We will send it to our developer. To contact him personally send him a E mail on --> arduinoboy.vbps@gmail.com")
sleep(25)
