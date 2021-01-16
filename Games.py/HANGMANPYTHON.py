import random

def get_word():
   words = ("cat" , "dog", "python" , "snake")
   return random.choice(words)

def play_game() :
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   word = get_word()
   letters_guessed = ()
   tries = 10
   guessed = False

   print("the word contains" , len(word) , "letters.")
   print(len(word) * "*")
   while guessed == False and tries > 0 :
       print("you have" + str(tries) + "tries" )
       guess = input ("please enter one letter or the full word.") . lower()
       #1  - user inputs a letter
       if len (guess) == 1 :
           if guess not in alphabet :
               print ("you have not entered a letter.")
           elif guess in letters_guessed:
               print ("you have guessed that number before.")
           elif guess not in word:
               print ( "sorry, that letter is not part of the word : ( " )
               letters_guessed.append (guess)
               tries -= 1
           elif guess in word:
               print("well done that letter exists in the word!")
               letters_guessed.append (guess)
           else:
               print("no idea why we get this message , it should be investigated!")    
      #2 -  user inputs the full word
       elif len (guess) == len(word) :
           if guess == word :
               print("well done you have guessed the word right")
               guessed = True
           else:
               print("sorry that was not the word we were looking for")
               tries -= 1
            
      #3 - user inputs letters where the total number of letters =/= total number of letters in the word.
       else:
          print("the length of your guess is not the same as the length of the word we\"re looking for.")

       status = ""
       if gussed == False:
           for letter in word:
               if letter in letters_guessed:
                   status +=  letter
               else:
                       status += "*"
           print (status)
       if status == word:
           print ("Well done , you have guesed the word")
           guessed = True
       elif tries == 0:
           print ("You have run out of gusess and you haven\'t gussed the world.")
           
           
          
          

          
