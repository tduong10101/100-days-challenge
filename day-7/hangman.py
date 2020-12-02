#Step 1 
import random
import hangman_art
import hangman_words
word_list = hangman_words.word_list
print(hangman_art.logo)
word = random.choice(word_list)
stages = hangman_art.stages
lives = len(stages) - 1
dword = []
for i in range(len(word)):
    dword.append("_")
endmessage = ""
gameover = False
print(' '.join(dword))
while not gameover:
    guess = None
    if not gameover:
        while not guess:
            guess = input("Guess a letter: ").lower()
            if len(guess) > 1:
                guess = None
                print("Invalid input! Please try again.")
        if guess not in word:
            print(f"You guessed {guess} and it's not in the word. You lose a life.")        
            lives -= 1
            if lives == 0:
                gameover = True
                print("You Lose.")
            
        else:
            if guess in dword:
                print(f"You have already guessed {guess}")
            else:
                for i in range(len(word)):                    
                    if word[i] == guess:
                        dword[i] = guess
    
    print(' '.join(dword))
    
    if "_" not in dword:
        gameover = True
        print("You Win.")

    if lives < len(stages) - 1:
        print(stages[lives])
    
           
    
