from random import randrange

def startGame():
    a = ["happy","ball","egg"]
    tries = []

    word = a[randrange(0,len(a))]

    d = {}

    for l in word:
        if l in d:
            d[l]=d[l]+1
        else: d[l]=1
        
    print("welcome to the game of hangman, guess the word in 6 attempts and you win! Best of luck!")
    
    for letter in word:
        tries.append('_')

    lives = 6
    guess = len(word)
    
    hangman_stages = {
    0: """
       +---+
           |
           |
           |
          ===""",
    1: """
       +---+
       O   |
           |
           |
          ===""",
    2: """
       +---+
       O   |
       |   |
           |
          ===""",
    3: """
       +---+
       O   |
      /|   |
           |
          ===""",
    4: """
       +---+
       O   |
      /|\\  |
           |
          ===""",
    5: """
       +---+
       O   |
      /|\\  |
      /    |
          ===""",
    6: """
       +---+
       O   |
      /|\\  |
      / \\  |
          ==="""
}


    while True:
        rightguess = False

        print(tries)

        

        l = input("enter a letter: ")[0]

        if l in d:
            if d[l]==0:
                lives = lives - 1
                
            else:
                
                for i,j in enumerate(word):
                    if(j==l and d[l]!=0 and tries[i]=='_'):
                        tries[i]=l
                        guess -=1
                        if guess == 0:
                            print(tries)
                            print("you win!")
                            return
                        break

                d[l]=d[l]-1

                rightguess = True
        if not rightguess:
            lives=lives-1
            if lives==0:
                print("sorry you lose")
                return
            print("offo! wrong guess!")
            print(hangman_stages[lives])
        else:
            
            print('woohoo! right guess')


            




startGame()


