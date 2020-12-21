#Created by : Yassine
import getpass 
import re
from draw import *
word_to_guess = getpass.getpass('Enter the word you want : ')
underscores = '_' * len(word_to_guess)
count = 0 
duplicate = []
guessed = False
attempt = 7
print(empty) #from draw.py file
print(underscores)
while True:
    if underscores == word_to_guess or guessed:
      print('WINNER !!')
      break
    if count == 7:#from draw.py file
      print(n_7)
      print(f'Looser ! :( ')
      print(f'The word was : "{word_to_guess.upper()}"')
      break
    while True:
      user_letter = input("Guess the letter or the word : ").lower()
      if user_letter == '':
        print('Please enter a letter or a word !')
        continue
      if not re.match("^[a-z]*$", user_letter):
        print("Error! Only letters a-z allowed!")
        continue
      if len(user_letter) == 1 :
        is_letter = True
        break
      if len(user_letter) > 1 :
        is_letter = False
        user_answer = user_letter
        break
      else:
        break
    if is_letter and user_letter in word_to_guess:
      print(f'The letter {user_letter} is in the word')
      if word_to_guess.count(user_letter) == 1:
        letter_index = word_to_guess.find(user_letter)
        underscores = underscores[0:letter_index] + str(user_letter) + underscores[letter_index+1:]
        print(underscores.upper())
      else:
        for (index,letter) in enumerate(list(word_to_guess)):#storing index of duplicated letters in a list
          if user_letter == letter:
            duplicate.append(index)
        if word_to_guess.count(user_letter) >= 2:#replacing all the duplicated letters in the word
          temporary = list(underscores)
          for y in temporary:
            for x in duplicate:
              if temporary[x] == '_':
                temporary[x] = user_letter
          underscores = "".join(temporary)
        print(underscores.upper())
    if not is_letter:
      if user_answer == word_to_guess:
          guessed = True
      else:
        print(f'"{user_answer}" Wrong answer ! ')
        count += 1

    if user_letter not in word_to_guess :
      print(f'The letter {user_letter} does not exist in the word ')
      count += 1
    if count == 1:
      print(n_1,f'{attempt - count} Attempts left !')
    if count == 2:
      print(n_2,f'{attempt - count} Attempts left !')
    if count == 3:
      print(n_3,f'{attempt - count} Attempts left !')
    if count == 4:
      print(n_4,f'{attempt - count} Attempts left !')
    if count == 5:
      print(n_5,f'{attempt - count} Attempts left !')
    if count == 6:
      print(n_6,f'{attempt - count} Attempt left !')
    

            
        
    
    
    
    
    
    
    
    
