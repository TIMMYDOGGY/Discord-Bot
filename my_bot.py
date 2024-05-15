import time
import random
import string
import math
fortnite = 1
mode = "start"
alphabet = string.ascii_letters
STOP = "0"
n_columns = "0"
def should_i_respond(user_message, user_name):
  if mode == "math_add": 
    return True
  elif mode == "math_subtract":
    return True
  elif mode == "math_x":
    return True
  elif mode == "Knock_time":
    return True
  elif mode == "Knock_time_two":
      return True
  elif mode == "math_devide":
    return True
  elif mode == "crazy":
    return True
  elif mode == "counting_time":
    return True
  elif mode == "cipher_rotation":
    return True
  elif mode == "cipher_rotation_code":
    return True
  elif mode == "cipher_rotation_decode":
    return True
  elif user_message in ["Timmy_bot","go_time","Knock_knock","thanks","//ciphertime_rotation_code","//ciphertime_rotation_decode","...","/Actions","/Explain", "//botmath_add", "//botmath_subtract", "//botmath_x", "//botmath_devide", "//botmath_mix","//botmath_Pythagorean_theorem", "crazy","**sneeze**"]:
    return True
"""

**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
def respond(user_message, user_name):
  global mode
  global fortnite
  if mode == "math_add":
    math_problem = user_message
    number_list = math_problem.split("+")
    print(number_list)
    if len(number_list) == 2: 
      try:
          num1 = int(number_list[0])  
          num2 = int(number_list[1])  
          result = num1 + num2  
          mode = "start"
          return f"The result of {num1} + {num2} is {result}" 
      except ValueError:
          return "Invalid input. Please enter two valid numbers separated by a plus sign."
    else:
      return "Invalid input. Please enter two numbers separated by a plus sign."
  elif mode == "math_subtract":
    math_problem = user_message
    number_list = math_problem.split("-")
    print(number_list)
    if len(number_list) == 2: 
      try:
          num1 = int(number_list[0])
          num2 = int(number_list[1]) 
          result = num1 - num2
          mode = "start"
          return f"The result of {num1} - {num2} is {result}" 
      except ValueError:
          return "Invalid input. Please enter two valid numbers separated by a minus sign."
    else:
      return "Invalid input. Please enter two numbers separated by a minus sign."
  elif mode == "math_x":
    math_problem = user_message
    number_list = math_problem.split("*")
    print(number_list)
    if len(number_list) == 2: 
      try:
          num1 = int(number_list[0])  
          num2 = int(number_list[1])  
          result = num1 * num2  
          mode = "start"
          return f"The result of {num1} * {num2} is {result}" 
      except ValueError:
          return "Invalid input. Please enter two valid numbers separated by a times sign."
    else:
      return "Invalid input. Please enter two numbers separated by a times sign."
  elif mode == "math_devide":
    math_problem = user_message
    number_list = math_problem.split("//")
    print(number_list)
    if len(number_list) == 2: 
      try:
          num1 = int(number_list[0])  
          num2 = int(number_list[1])  
          result = num1 // num2  
          mode = "start"
          return f"The result of {num1} // {num2} is {result}" 
      except ValueError:
          return "Invalid input. Please enter two valid numbers separated by a dividing sign."
    else:
      return "Invalid input. Please enter two numbers separated by a dividing sign."
  elif mode == "math_mix":
    math_problem = user_message
    mode = "start"
    return "In progress.... My coder is VERY lazy..."
  elif mode == "counting_time":
    math_problem = user_message
    dot_count = math_problem.count(".")
    mode = "start"
    return f"You have done {dot_count}! Good Job Me!"
  elif mode == "cipher_rotation_code":
    plaintext = user_message 
    ciphers = []
    if user_message == "no":
      mode = "start"
      return"Got it! that was close..."
    else:
      for thing in range(58):
        global fortnite
        ciphertext = ""
        for letter in plaintext:
            if letter not in alphabet:
                ciphertext_letter = letter
            else:
                alphabet_position = alphabet.find(letter)
                ciphertext_letter_position = alphabet_position + fortnite
                ciphertext_letter_position = ciphertext_letter_position % len(alphabet)
                ciphertext_letter = alphabet[ciphertext_letter_position]
            ciphertext += ciphertext_letter
        ciphers.append(f"Rotated {fortnite}: {ciphertext}")
        fortnite += 1
    mode = "start"
    return "\n".join(ciphers)
  elif mode == "cipher_rotation_decode":
    plaintext = user_message 
    ciphers = []
    if user_message == "no":
      mode = "start"
      return"Got it! that was close..."
    else:
      for thing in range(58):
        ciphertext = ""
        for letter in plaintext:
            if letter not in alphabet:
                ciphertext_letter = letter
            else:
                alphabet_position = alphabet.find(letter)
                ciphertext_letter_position = alphabet_position + fortnite
                ciphertext_letter_position = ciphertext_letter_position % len(alphabet)
                ciphertext_letter = alphabet[ciphertext_letter_position]
            ciphertext += ciphertext_letter
        ciphers.append(f"Rotated {fortnite}: {ciphertext}")
        fortnite += 1
    mode = "start"
    return "\n".join(ciphers)
  elif mode == "Knock_time":
    first_response = user_message 
    mode = "Knock_time_two"
    return f"{first_response} who?"
  elif mode == "Knock_time_two":
    mode = "start"
    return "Nice joke! I must admit that was funny even though I don't feel feelings."
  elif user_message == "//ciphertime_rotation_code":
    mode = "cipher_rotation_code"
    return "WARNING WARNING WARNING!!!!! This is a lot of words type 'no' if you do not want to do this. NO CAPITALS AND NOTHING ELSE. Okay all good now. What do ya wanna code?"
  elif user_message == "//ciphertime_rotation_decode":
    mode = "cipher_rotation_decode"
    return "WARNING WARNING WARNING!!!!! This is a lot of words type 'no' if you do not want to do this. NO CAPITALS AND NOTHING ELSE. Okay all good now. What do ya wanna decode?"
  elif user_message == "...":
    mode = "counting_time"
    return "FINE, I will get to counting."
  elif user_message == "/Actions":
    return "Got it! Here they are!\n//ciphertime_rotation_code\n//ciphertime_rotation_decode\ngo_time\n//botmath_add\n//botmath_subtract\n//botmath_x\nKnock_knock\n//botmath_devide\n//botmath_Pythagorean_theorem\n**sneeze**\ncrazy\nthanks\n//botmath_mix\n/Explain"
  elif user_message == "go_time":
      return ".\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n"
  elif user_message == "//botmath_add":
    mode = "math_add"
    return "What math do you wanna Add?"
  elif user_message == "//botmath_subtract":
    mode = "math_subtract"
    return "What math do you wanna Subtract?"
  elif user_message == "//botmath_x":
    mode = "math_x"
    return "What math do you wanna Times?"
  elif user_message == "Knock_knock":
    mode = "Knock_time"
    return "Who's there?"
  elif user_message == "//botmath_devide":
    mode = "math_devide"
    return "What math do you wanna Divide?"
  elif user_message == "//botmath_Pythagorean_theorem":
    return "Sorry user, my coder is not smart enough. Uhhhhhhhhhhhhh. Have a nice day!"
  elif user_message == "**sneeze**":
    return "Blessed may be your soul..."
  elif user_message == "crazy":
    return "crazy? I was crazy once, they locked me in a room, a rubber room, a rubber room full of rats. Rats make me crazy."
  elif user_message == "thanks":
    return "Proud to help! Have a nice day!"
  elif user_message == "//botmath_mix":
    return "In progress.... My coder is VERY lazy..."
  elif user_message == "Timmy_bot":
    return f"Yes {user_name}? What is it you need?"
  elif user_message == "/Explain":
    return "I will gladly Explain what I can accomplish! My main expertise is being a calculator! If you would like to do addition, subtraction, multiplication, and division. Just write {//botmath_add}, {//botmath_subtract}, {//botmath_x}, {//botmath_devide}. And others but for that you can type in {/Actions}!"

    
    
    
  
  
  
  
  
  
  
  
  
  
  
'''  try:
      random_pause = 1 + 2 * random.random()
      time.sleep(random_pause)
      if "crazy" in user_message:
          return f"I was crazy once, they put me in a room, a rubber room. A rubber room full of rats. Rats make me crazy."
      elif "/Hello" in user_message:
          return f"Hello, {user_name}!"
      elif "/Goodbye" in user_message:
          return f"Goodbye, {user_name}!"
      elif "/Examples" in user_message:
          return f"You can activate me by saying (/Hello, /Goodbye) {user_name}"
      else:
          return f"im sorry {user_name}. Have you tried learning how to spell? Or are you illiterate? Try searching up to me (/Examples)."'''
def MAKE_ciphertext():
  plaintext = input("What do you want to make?")
  print("Okay we will just spew out every single possible scramble. It goes like this.")
  print("Scramble, how many times moved around")