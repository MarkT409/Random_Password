import random

# Declaring possible symbols
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!@#$%^&*()_+"

# Gathering input for desired password length
print("\tWelcome to Random Password Generator!")
length = input("How Many Character Password would you like?: ")
length_int = int(length)
pass_length = length.ljust(length_int, " ")
pass_length_int = int(pass_length)

# Gathering data for desired password make up
# choice = input("How do you want your Password composed of? \n1. Letters \n2. Numbers \n3. Symbols \n4. All Three\n").split(',')

#Returning random password @ requested length, turning into str from list
all_chars = letters + numbers + symbols

pass_list = random.choices(all_chars, k=pass_length_int)
password = ''.join(map(str, pass_list))
print(f"\nYour {pass_length_int} Character Password: {password}")

if pass_length_int <= 8:
    print("""\n*TIP: Passwords under 8 characters are deemed unsafe and can be cracked in under 5 minutes*
      ** Recommended Password Length: 14+ Characters **""")
