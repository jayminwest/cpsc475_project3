'''
Jaymin West
CPSC475
Project 3
9/19/2022

This program uses the code from the given "Eliza.py" program and
    adjusts it so that it is more comprehensive and responsive to 
    the user input. The technique used is Regular Expressions. 
'''


import sys
import re

def doreply(instr):
    instr = instr.lower()
    
    # Provided Criteria:
    if re.search(r'^hello|hi$', instr):
        return 'Hi there!'
    if re.search(r'\W(hate|despise|loathe)\W', instr):
        return 'Wow! Those are some strong feelings you have! Tell me more...'
    if re.search(r"^(are|aren't|what|where|who|when|is|isn't|why|how)\W", instr):
        return 'good question!'
    
    # --- Added Criteria ---
    
    # 1. Recognizing Pronouns: 
    if re.search(r"he|him|she|her|they|them", instr):
        return "Tell me more about them..."
    # 2. Determining if user "wants to" commit arson
    if re.search(r"want to", instr) and re.search(r"burn|arson|fire|destroy", instr):
        return "Wowza! That seems a bit extreme...\nSpeaking of extreme, what's your favorite animal?"
    # 3. Reacting to user talking about their pet (hopefully pet gopher)
    if re.search(r"dog|cat|lizard|gopher|pet", instr):
        return "Aw I love animals! Tell me more about that animal..."
    # 4. Figuring out if patient is in school 
    if re.search(r"in school", instr):
        print("Oh you're in school, what is your major?")
        instr = input()
        # 5. When patients says their major isn't computer science, it suggests they change 
        if not re.search(r"Computer Science|comp sci|computer science", instr):
            print("Interesting! Have you ever though of switching to Computer Science?")
    # 6. Searching if patient is talking about money
    if re.search(r"rich|poor|wealthy|bankrupt|money|income", instr):
        print("Interesting, do you think about money a lot?")
        instr = input()
        # 7. If the user is thinking about money
        if re.search("yes|Yes|constantly", instr):
            print("Are you in massive debt?")
            instr = input()
            # 8. If the user is in debt
            if re.search("yes|Yes", instr):
                print("Oh no! I would suggest disappearing to a cabin in the woods. How does that make you feel?")
                instr = input()
                # 9. If the user likes the idea of moving into the woods"
                if re.search("good|Good|Great|okay", instr):
                    return "Great! Enjoy nature!"
                if re.search("Bad|bad|not good", instr):
                    return "I think you're making the wrong call but okay. Anything else I should know about you?"

    # 10. 


    return "That's very good to know.\nTell more more about yourself..."

def main():
    print ("Welcome! How may I help you? (type \"bye\" to quit.)\n")
    while True:
        # Read user's input
        instr = input("Patient: ")
        instr = instr.lower()

        if re.search(r'\bbye\b', instr):
            print ("Nice chatting with you!\n")
            return 0
        
        print (doreply(instr))
        
        print()

if __name__ == "__main__":
    sys.exit(main())