import json
import time
from PIL import Image

start = time.time()

def showInstructions():
    # Print a main menu and the commands
    print('''
            Stuck In Time
            =============''')
    time.sleep(1)
    print('''
    You suddenly wake up. You see that you are stranded in a forest, on an abandoned planet with your co-pilot.
    This could only mean one thing. . . ''')
    time.sleep(2)
    print('''
    You failed your mission. You seem to be somewhere in the future.
    But you don't know which planet you are on.
    What you do know is that the planet has suffered destruction.''')
    time.sleep(2)
    print('''
    Your spaceship has been damaged. To go back to your time you need to find materials to fix it.
    Solve the questions and find an escape.''')
    time.sleep(3)
    print('''
            R U L E S
         READ CAREFULLY''')
    time.sleep(2)
    print('''
    Every written answer is to be in small letters (with no extra spaces)
    Every numerical is to be written to the third decimal point
    Mention the SI units wherever applicable (with a space between the answer)
    Be as accurate with the answers as possible!! ''')
    time.sleep(3)
    print('''
    You have only 3 attempts to answer the quetion.
    Scoring method:
        Correct answer on first attempt gets 5 points
        Correct answer on second attempt gets 3 points
        Correct answer on third attempt gets 0 points
        Incorrect answer after 3 attempts loses -2 points''')
    time.sleep(5)
    print('''
    Answer after the prompt ">> "
    Commands:
        go [direction]
        [answer]
''')
    time.sleep(3)

# Ask the player their name
name = input("  What is your name, Captain? ")
showInstructions()
points =0
time_taken =0
gamedata ={
        "playername": name,
        "playerscore": points,
        "playertime": time_taken}
with open("gamedata.json", "w") as f:
    json.dump(gamedata, f)


# Code to check the answer.
def Check_Answer(Correct_Answer, Dialogue):
    attempt =0
    with open("gamedata.json", "r") as file:
        gamedata = json.load(file)
        points =gamedata["playerscore"]
    while True:
        Answer =input(">> ")
        if Answer == Correct_Answer and attempt==0:
            time.sleep(1)
            print("            You answered correctly.")
            points = points + 5
            gamedata["playerscore"] = points
            with open("gamedata.json", "w") as file:
                json.dump(gamedata, file)
            time.sleep(1)
            print("            ", Dialogue)
            time.sleep(2)
            Display_Marks(points)
            #go to next level if answer is correct
            break
        elif Answer == Correct_Answer and attempt==1:
            time.sleep(1)
            print("            You answered correctly.")
            points = points + 3
            gamedata["playerscore"] = points
            with open("gamedata.json", "w") as file:
                json.dump(gamedata, file)
            time.sleep(1)
            print("            ", Dialogue)
            time.sleep(2)
            Display_Marks(points)
            #go to next level if answer is correct
            break
        elif Answer == Correct_Answer and attempt==2:
            time.sleep(1)
            print("            You answered correctly.")
            points = points + 0
            gamedata["playerscore"] = points
            with open("gamedata.json", "w") as file:
                json.dump(gamedata, file)
            time.sleep(1)
            print("            ", Dialogue)
            time.sleep(2)
            Display_Marks(points)
            #go to next level if answer is correct
            break
        elif attempt ==3:
            time.sleep(1)
            print("            You failed to answer within 3 attempts. ")
            time.sleep(1)
            print("            The correct answer was,")
            time.sleep(1)
            print('"', Correct_Answer, '"')
            points = points - 2
            gamedata["playerscore"] = points
            with open("gamedata.json", "w") as file:
                json.dump(gamedata, file)
            time.sleep(1)
            print("            ", Dialogue)
            time.sleep(2)
            Display_Marks(points)
            #go to next level
            break
        else:
            #repeat code
            print("            Incorrect answer try again.")
            attempt = attempt+1

# Code to calculate marks
def Display_Marks(points):
    time.sleep(1)
    print(' ---------------------------')
    time.sleep(1)
    print(" ",name, "your score is", points)
    time.sleep(1)
    print(' ---------------------------\n')
    time.sleep(1)

# Code to calculate time
def Update_Time(Total_Time):
    with open("gamedata.json", "r") as file:
        gamedata = json.load(file)
    time.sleep(1)
    print(' ---------------------------')
    time.sleep(1)
    gamedata["playertime"] = Total_Time
    with open("gamedata.json", "w") as file:
        json.dump(gamedata, file)
    print(" time taken to finish the game by", name, "is \n", Total_Time, " seconds.")
    time.sleep(1)
    print(' ---------------------------\n')
    time.sleep(1)

# Circuit Question
def Question_3():
    print("""
        The circuit has a part which comprises of a set of resistors and a bulb.
        You have a few cells to make up a battery. The bulb has a rating of (60W, 12V).
        Calculate the voltage of the battery tht you would need to provide,
        if the bulb still has to dissipate 60W of power.
        Given R = 1 ohm.
        (Hint: Remember that the voltage will be distributed across the resistors too.)
        """)
    img = Image.open(r"Final_Circuit.jpg")
    img.show()
    

# Final Question
def Dialogue_7():
    print("""    Now it all makes sense. The ship in the wormhole, which was about to crash into you,
    W A S   Y O U !!""")
    time.sleep(2)
    print("""
    It has always been you.""")
    time.sleep(1)
    print("""
    You caused yourself to go into the future""")
    time.sleep(1)
    print("""
    You crashed with yourself""")
    time.sleep(1)
    print("""
    While you where having this epiphany, the box slips from your hand and starts to hover.
    You notice your spaceship becoming smaller and smaller. """)
    time.sleep(2)
    print("""
    Wait!
    Its not your spaceship anymore. It looks more like those capsules!
    Thats why they looked so fimiliar!!""")
    time.sleep(2)
    print("""
    Suddenly the capsule starts to accelerate... Faster and faster, till you fell weightless.
    Now you completely understand!""")
    time.sleep(3)
    print("""
    Or do you? \n\n""")
    time.sleep(3)


####################################################################################################################################################################

## The main code
            
def showStatus():
    time.sleep(1)
    # Print the player's current status
    print(' ---------------------------')
    time.sleep(1)
    print(' Welcome ', name)
    time.sleep(1)
    print(' Let the adventure begin!')
    time.sleep(1)
    print(' ---------------------------')
    time.sleep(2)


# Loop forever
while True:
    points =0
    showStatus()

####################################################################################################################################################################

# Code about each level.

## Level 1
    while True:
        Question ="""
        What is the frequency of the sound, which you inquire about?
        (Hint: Answer in Hz)
        """
        Correct_Answer = "29565 Hz"
        Dialogue = """
            "You are on the heavenly planet of Vignar, in the year 7093.
            The distruction you see is due to a Great War which happened here.
            We are investigators amongst the people who survived.
            After what happened here, we need faith to carry on living.
            There exists a temple, north from here. The answer to your questions lie there.
            Only the worthy can enter. Good luck."  \n"""
        print("""    You and your co-pilot decide to look around to find ANY remains of life.
    You take your highly advanced bikes and a device which collects data through signals.
    While moving through the forest, your device detects two types of signals.
    One, infrared signatures of life by your thermal scanner and the second, an unexplainable sound,
    coming from the same direction. \n""")
        time.sleep(3)
        print("  What do you do? ([go towards] or [go away] from the sound) \n")
        move = ''
        while move =='':
            move = input('>> ')
        move = move.lower().split()
        if move[0] == 'go':
            if move[1] == 'away':
                time.sleep(1)
                print("\n  Don't be scared.")
                time.sleep(1)
            elif move[1] == 'towards':
                time.sleep(1)
                print("""\n    You move towards the signal at a speed of 18km/h. To get an idea of what could be making the sound,
    you try to measure its frequency, which comes out to be approximately 30 KHz
    On your way you come across a group of humanoids.
    You move closer towards them and notice that they are Avasapiens, like you. """)
                time.sleep(1)
                print("""
    You decide to go talk to them. You realized that they speak a language which is familiar to you.
    When you approach them, they seem surprised.""")
                time.sleep(1)
                print("""
    You ask them who they are, tell them about the signal you are receiving
    and ask them if they could tell you where it is coming from and also where you are.
    They don’t trust you. They say,  """)
                time.sleep(2)
                print("\n        \"If you want to know about the signal, you need to answer the following question.\" ")
                time.sleep(1)
                print ('        ', Question)
                time.sleep(1)
                print("    You know that, based on the composition of your environment, the speed of sound is 340 m/s \n ")
                #Check answer from function
                Check_Answer(Correct_Answer, Dialogue)
                break
            else:
                print('\n  You can\'t go that way! \n')
        else:
            time.sleep(1)
            print("\n  Incorrect set of input, try again. \n")
            time.sleep(1)

## Level 2
    while True:
        Riddle ="""
        I have 3 kids, you know them all, 
        I keep 1 with myself, 2 in the hall,
        The one with me is rigid, we can't change him now, 
        I have ambitions, to the 3rd, the world will bow, 
        The middle one gets influenced by the rigid one, and can ruin the the third,
        Though if I focus on the middle one, the third will fly higher than a bird.
        What am I? \n"""
        Correct_Answer = "time"
        Dialogue = """\n    The gate opens and you enter. \n"""
        print("""    You follow the directions, and arrive at the temple.
    You and your co-pilot start looking for ways to enter. Your co-pilot discovers a hidden gate with an inscription on it.
    It reads, """)
        time.sleep(2)
        print("\n        \"To enter the temple, prove your worth. Answer the riddle, and commence forth.\" ")
        time.sleep(2)
        print('        ', Riddle)
        time.sleep(2)
        Check_Answer(Correct_Answer, Dialogue)
        break
    
## Level 3
    while True:
        Correct_Answer = "21.166 V"
        Dialogue = """
        The bulb in the circuit start to glow. You hear a gears turning inside the well.
        A capsule appears in the well. It looks very familiar but you can’t make out what it is. \n"""
        print("""    You enter a dusty temple, full of cobwebs.
    The insides of the temple look similar to an abandoned facility. There is a well there too.
    You see a skeleton on the floor. You think, """)
        time.sleep(1)
        print("""\n          "The outcome of the war huh? I wonder what this facility was used for." \n""")
        time.sleep(2)
        print("""    You look around to find a control unit, which could allow you to access the machines there.
    You find a box which contains a broken circuit.""")
        time.sleep(2)
        print("""\n          "I wonder what this does." \n""")
        time.sleep(2)
        print("""    Your co-pilot calls you across the temple and says,""")
        time.sleep(1)
        print("""\n          "I think the box is connected to this well. Lets try to fix it!
           Maybe something might happen?" """)
        time.sleep(2)
        Question_3()
        time.sleep(1)
        Check_Answer(Correct_Answer, Dialogue)
        break

## Level 4
    while True:
        Riddle ="""
        Time has come, you have to be wise,
        You don't want to go where the end lies,
        The things you see from now on will be a surprise,
        If you choose the right way, someone dies,
        Choose the direction to see the skies, 
        To seek the answers, you have to...? """
        Correct_Answer = "rise"
        Dialogue = """\n    The capsule opens and your hurry inside. \n
            “Just take me away from here”  \n
    you say as the capsule closes behind you. \n"""
        print("""    Your co-pilot throws a coin in the well as a joke, but you don't hear the sound of the coin hitting the floor.
    Instead, the same coin falls on your head from above.""")
        time.sleep(1)
        print("\n        \"Weird\" \n")
        time.sleep(2)
        print("""    You need to find out what this "well" is. You need to know what's going on! \n""")
        time.sleep(1)
        print("""    You step into the capsule. Your co-pilot is left behind as a safety measure.
    The capsule closes shut behind you and you begin to descend faster and faster till you feel weightless. \n""")
        time.sleep(2)
        print("""    You seem to come across some kind of highway, made out of stars? It leads to various paths.
    Wait... Is this a wormhole??
    Before you can make sense of anything, you collapse.\n""")
        time.sleep(3)
        print("""    You wake up after a while to find yourself in the temple. But something seems strange.
    The temple seems relatively new. \n""")
        time.sleep(2)
        print("""    You go out of the temple to see the planet full of life. People are running here and there.
    They seem to be distressed. The temple seems to be marked with yellow tape and "do not enter" signs all around it. \n""")
        time.sleep(2)
        print("""    You know what’s happening. You’ve come back into the past. A time just before the Great War.
    You hear people screaming, """)
        time.sleep(1)
        print("\n        \"The aliens are here! Run!\" \n")
        time.sleep(2)
        print("""    You think, """)
        time.sleep(1)
        print("\n        \"An alien invasion? Is this because of the new wormhole?\" \n")
        time.sleep(1)
        print("""    You need to get out of here. You run towards the capsule but it’s gone!!
    You look around the temple for any sign of the capsule and find another circuit box.
    You summon the capsule, but it wont open! \n""")
        time.sleep(1)
        print("""    You see a hologram displaying the following message: \n""")
        time.sleep(1)
        print('        ', Riddle)
        time.sleep(1)
        print("\n        \"Oh god oh god, I need to hurry\" \n")
        Check_Answer(Correct_Answer, Dialogue)
        break

## Level 5
    while True:
        Question1 ="""
        In the presence of gravity (as the only force operating),
        what type of path should I take to minimise travel time
        so I can save my life and get away as fast as I can? """
        Question2 ="""        Give the general equation. \n"""
        Correct_Answer1 = "cycloid"
        Correct_Answer2 = "sinx/(y^0.5)=constant"
        Hint = """
            Hint:
            Sometimes the answer isn't as straightforward as it seems.\n"""
        Dialogue1 = "\n        You can hear the sound of the spiders getting closer. \n"
        Dialogue2 = """\n    Just before the spiders could reach you, you jump.
    Lucky, you find another capsule at the end of the path. You get into it as fast as you can and wizz away into time. \n"""
        print("""    The capsule roars and starts to ascend, faster and faster.
    Suddenly everything becomes quiet. A little too quiet.
    The capsule opens and you step out to see the temple in a hideous condition. \n""")
        time.sleep(2)
        print("""    Everything has changed. Plant life has overpowered human-made structures.
    You go outside. The air is fresh, you are encompassed by greenery, the planet seems calm and relaxed.
    There is no sign of human life what-so-ever.\n""")
        time.sleep(2)
        print("""    Your bike is inside the temple, but it looks broken
    You move to see your co-pilots corpse in the temple, or rather just his skeleton. \n
        "Sorry friend"\n""")
        time.sleep(2)
        print("""    Suddenly, you hear something rustling in the forest. Something huge.
    You run back inside the temple to take cover. Just then a cluster of spiders,
    about 10 feet tall, walked out into the open. """)
        time.sleep(2)
        print("""\n        "If these creatures have evolved to be like this, I must be around a million years ahead in the future.
        I need to get back!
        Wait... If I'm years into the future, how can his corpse be here? And how is my bike still here?
        In fact, how is the whole lab here? Did the whole place travel through time??"  \n""")
        time.sleep(1)
        print("""    You start to panic. You try to run towards the capsule, but you trip on something and fall.""")
        time.sleep(1)
        print("\n        *T H U D* \n")
        time.sleep(1)
        print("""    You know you messed up. You know they heard you.
    Without looking back, you start to run. You enter the temple and notice there are two paths in front of you.
    One which led somewhere inside the temple and one going straight down like a fall of doom.
    Your bike won't start. And there are so many paths in front of you. \n""")
        time.sleep(2)
        print("  What do you do? ([go inside] or [go down]) \n")
        move = ''
        while move =='':
            move = input('>> ')
        move = move.lower().split()
        if move[0] == 'go':
            if move[1] == 'inside':
                time.sleep(1)
                print("""\n    You know you can't go inside the temple, or you'll be trapped.
    Think. T H I N K. \n""")
                time.sleep(1)
            elif move[1] == 'down':
                time.sleep(1)
                print("\n        \"Okay, I just need to calculate the situation correctly.\" ")
                time.sleep(1)
                print('        ', Question1)
                time.sleep(3)
                print(Hint)
                time.sleep(2)
                Check_Answer(Correct_Answer1, Dialogue1)
                time.sleep(3)
                print('        ', Question2)
                time.sleep(3)
                Check_Answer(Correct_Answer2, Dialogue2)
                time.sleep(3)
                break
            else:
                print('\n  You can\'t go that way! \n')
                time.sleep(1)
        else:
            time.sleep(1)
            print("\n  Incorrect set of input, try again. \n")
            time.sleep(1)

## Level 6
    while True:
        Question ="""
        You find the following data,
        Density of planet- 6x10^12 kg/km^3 
        Diameter of planet- 15000km
        Calculate the escape velocity.
        (Hint: Answer in km/s) \n """
        Correct_Answer = "13.732 km/s"
        Dialogue = """\n    You calculate the escape velocity and start to go towards the spaceship.
    Then you remember that the capsule is still there!
    You notice a box which seems to be powering it. You take it with you to study it.
    Maybe you can prevent the future you saw from happening.
    You configure your spaceship. It comes to life! 100. 1000. 100000 meters away from the ground. You did it! You escaped the planet.\n"""
        print("""    You are shaking from fear. You just escaped death. \n
        "I just want to go home" \n
    You start dreaming about your home on Xenerth, warm food, clean clothes and a warm bed.
    You start to drift off to sleep, to a place full of hope and love. \n""")
        time.sleep(2)
        print("""    The capsule stops with a thud. You wake up abruptly. The capsule opens and you step out.
    Surprisingly, this time the capsule doesn’t disappear.\n""")
        time.sleep(2)
        print("""    You notice your surroundings. You are in the temple, but this time it looks more like a laboratory. \n
        "How is this possible?"  \n
    You try to look for answers. \n""")
        time.sleep(2)
        print("""    Then it strikes you. This isn’t a temple! This is one of MEMES labs!
    You notice computers collecting data about the planet and its surroundings.
    You read the date, \n
        "28th July 6420"\n""")
        time.sleep(2)
        print("""    This is it! You have arrived 2 days before you were supposed to leave your planet for the mission.
    This is your chance to go back home! To save everyone. \n""")
        time.sleep(2)
        print("""    You hear voices of people outside the temple.
    One thing you wonder is that, """)
        time.sleep(1)
        print("""
        "Were the scientists here trying to create a wormhole covertly?"
        Should I tell them about the future invasion?
        What if they capture me instead?! """)
        time.sleep(3)
        print("""
    You need to find a spaceship in the facility, before someone finds you.
    You need to inform your people about this mess.
    All you need to do is collect data about the planet, calculate the escape velocity and go home.\n""")
        time.sleep(2)
        print("""    You check the computers and find out the radius of the planet as well as its gravitational energy.""")
        time.sleep(1)
        print('        ', Question)
        time.sleep(1)
        Check_Answer(Correct_Answer, Dialogue)
        break

## Level 7
    while True:
        Riddle ="""
        The end is closer the you think,
        Pay attention, try not to blink,
        What might have triggered the deja vu,
        Could have begun through you,
        Although the beginning is redundant on a predestined path,
        It feels like you control your actions from the start,
        Now it all comes full cirlce and things make sense,
        You realize there isn't a clear distinction of tense."""
        Hint ="""
        The more you seek the end, the closer you get to the beginning,
        If you think about it, I’m brimming with the same happenings,
        4 letters I have and I have no start to my structure,
        I am the very thing by which your story is manufactured.
        What am I?  \n"""
        Correct_Answer = "loop"
        print("""    You’re in outer space. You are heading home. You recall all the past events.  """)
        time.sleep(1)
        print("""\n          "What a crazy journey." \n""")
        time.sleep(2)
        print("""    You entered the wormhole without a problem. Just as you were starting to relax,
    you notice a spaceship coming towards you. The weird thing is that the spaceship looked familiar.
    Wait, isn’t that your spaceship?  \n """)
        time.sleep(2)
        print("            .")
        time.sleep(2)
        print("            .")
        time.sleep(2)
        print("            .")
        time.sleep(2)
        print("        C R A S H  \n")
        time.sleep(3)
        print("""    Lucky, you were able to change your trajectory and prevent a head on collision.
    But none-the-less your spaceship has faced some damage. You exit the wormhole to try and stabilize your ship.\n""")
        time.sleep(2)
        print("""    While fixing te ship, the circuit box which you took from Vignar starts to glow.
    It displays a hologram reading,""")
        time.sleep(2)
        print('        ', Riddle)
        time.sleep(5)
        print("\n        \"Huh? What a weird riddle.\" ")
        time.sleep(2)
        print('        ', Hint)
        x = True
        while x ==True:
            attempt =0
            with open("gamedata.json", "r") as file:
                gamedata = json.load(file)
                points =gamedata["playerscore"]
            while True:
                Answer =input(">> ")
                if Answer ==Correct_Answer and attempt==0:
                    time.sleep(1)
                    print("            You answered correctly.")
                    points = points + 5
                    gamedata["playerscore"] = points
                    with open("gamedata.json", "w") as file:
                        json.dump(gamedata, file)
                    time.sleep(1)
                    print("            "), Dialogue_7()
                    time.sleep(2)
                    Display_Marks(points)
                    x = False
                    #go to next level if answer is correct
                    break
                elif Answer ==Correct_Answer and attempt==1:
                    time.sleep(1)
                    print("            You answered correctly.")
                    points = points + 3
                    gamedata["playerscore"] = points
                    with open("gamedata.json", "w") as file:
                        json.dump(gamedata, file)
                    time.sleep(1)
                    print("            "), Dialogue_7()
                    time.sleep(2)
                    Display_Marks(points)
                    x = False
                    #go to next level if answer is correct
                    break
                elif Answer ==Correct_Answer and attempt==2:
                    time.sleep(1)
                    print("            You answered correctly.")
                    points = points + 0
                    gamedata["playerscore"] = points
                    with open("gamedata.json", "w") as file:
                        json.dump(gamedata, file)
                    time.sleep(1)
                    print("            "), Dialogue_7()
                    time.sleep(2)
                    Display_Marks(points)
                    x = False
                    #go to next level if answer is correct
                    break
                elif attempt ==3:
                    time.sleep(1)
                    print("            You failed to answer within 3 attempts. ")
                    time.sleep(1)
                    print("            The correct answer was,")
                    time.sleep(1)
                    print('"', Correct_Answer, '"')
                    points = points - 2
                    gamedata["playerscore"] = points
                    with open("gamedata.json", "w") as file:
                        json.dump(gamedata, file)
                    time.sleep(1)
                    print("            "), Dialogue_7()
                    time.sleep(2)
                    Display_Marks(points)
                    x = False
                    #go to next level
                    break
                else:
                    #repeat code
                    print("            Incorrect answer try again.")
                    attempt = attempt+1
        break
    break
    
####################################################################################################################################################################
end = time.time()
Total_Time = end-start
Update_Time(Total_Time)
time.sleep(1)
print("""
          A wormhole is speculated to have been created on Vignar.
          You and your co-pilot have been selected to investigate.
          Good luck!!""")
time.sleep(30)
