# Exercise-01b-Guessing-Game
Exercise for MSCH-C220, 27 August 2020

This exercise is an opportunity for you to create a (simple) game in Python. I understand that this might feel intimidating, but we will take time in class (and elsewhere) to explain every line of this program in a way that you can (hopefully) understand.

First, Fork the repository. When that process has completed, make sure that the top of the repository reads [your username]/Exercise-01b-Guessing-Game. 

*Edit the LICENSE and replace BL-MSCH-C220-F20 with your full name.* Commit your changes.

Press the green "Code" button and select "Open in GitHub Desktop". Allow the browser to open (or install) GitHub Desktop. Once GitHub Desktop has loaded, you should see a window labeled "Clone a Repository" asking you for a Local Path on your computer where the project should be copied. Choose a location where you will keep the repositories for this class (a C220 folder off your Desktop would be fine). Make sure the Local Path ends with "Exercise-01b-Guessing-Game" and then press the "Clone" button. GitHub Desktop will now download a copy of the repository to the location you indicated.

Open Visual Studio Code, and select File->Open. Navigate to the repository folder you just cloned, select the folder, and press "Open".

In the far right (black) panel of the window, you should see five icons. The top one is File Explorer. If that is selected, you should see five files listed: .gitignore, LICENSE, main.py, main2.py, README.md.

Open main.py. If you haven't already installed the Python plugin, do so now.

Copy the following code, and paste it after the lines that already appear in that file:
```
number = 5
guess = input("Guess a number from 1 to 10: ")
guess = int(guess)
if guess == number:
    print("Great job! You got it!")
else:
    print("Sorry, better luck next time.")
    print("The number was " + str(number))
```

Run the program by pressing the green button. Click in the bottom panel, so it accepts your input, and answer 5. Then press the trash can icon and run it again. Answer a value other than 5. Do you understand what is happening? What happens if you type something that is not a number?

This isn't a very fun game; how could you make it more interesting? For extra credit, work with main2.py to see if you can make it into more of a game. Add some personality and features. See if you can prevent the player from generating an error when they type something that is not a number.

Hint, to assign a random number to a variable, type:
```
number = random.randrange(1,10)
```

Save these files and quit Visual Studio Code. In GitHub Desktop, you should now see main.py and main2.py (if you did the extra credit) highlighted. Add a Summary message at the bottom of that panel, and push the "Commit to master" button. On the right side of the top, black panel, you should see a button labeled "Push origin". Press that now.

If you return to and refresh your GitHub repository page, you should now see that your files have been changed (with a new date).

Now edit the README.md file. When you have finished editing, commit your changes, and then turn in the URL of the main repository page (https://github.com/[username]/Exercise-01b-Guessing-Game) on Canvas.

The final state of the file should be as follows (replacing my information with yours):

# Exercise-01b-Guessing-Game
Exercise for MSCH-C220, 27 August 2020

Two versions of a guessing game, written in Python

## Implementation
Built using Visual Studio Code and Python 3.8.5

## References
None

## Future Development
None

## Created by 
Sonny Kim
