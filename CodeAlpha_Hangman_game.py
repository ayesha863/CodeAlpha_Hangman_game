
#import random module for selecting the word

import random as ram

lis=["ayesha","zainab","muneeb","akram","chair","table","cot","jasmine","pillow",
     "bed","barbie","cavin","jain","mandir","zain"]

#choice function for selecting the word from the given list

randWord=ram.choice(lis)  

#loops for finding guessing word

#loop so that user can guess more than once if loose

found=True

for j in range(0,3):

    guessLetter=input("\nEnter the letter you guess:")
    found=False
   
    for i in range(len(randWord)):

        if randWord[i]==guessLetter:
            
            print("Congratulation you guess the correct letter in the word")
            print("\n And the word is:"+randWord)

            found=True

            break

    if found==True:    #if the player found the word
        break

    if found==False:
        print("\nSorry man you lost the game>>>>...")  
        print("\n\nWant to try again:")

        #if the player doesnt guess the word

    if j==2:
        print("\nSorry you can't try now\nYou looooooseeee.........\n\nGame Over")
        break




