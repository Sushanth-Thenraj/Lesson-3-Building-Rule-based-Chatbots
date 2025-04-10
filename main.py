#name the file as main.py , uncomment the imports and basic functions, complete  the code by writing remainig functions 

import re, random
from colorama import Fore, init

# # Initialize colorama (autoreset ensures each print resets after use)
init(autoreset=True)

# # Destination & joke data
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}
jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

# # Helper function to normalize user input (remove extra spaces, make lowercase)
def normalize_input(text):
     return re.sub(r"\s+", " ", text.strip().lower())

# Provide travel recommendations (recursive if user rejects suggestions)

def recommend():
     print(f"{Fore.CYAN}Chatbot: Beaches, Mountains or Cities?")
     preference= input(f"{Fore.YELLOW}You: ").lower()
     preference= normalize_input(preference)

     if preference in destinations:
          suggestion= random.choice(destinations[preference])
          print(f"{Fore.CYAN}Chatbot: How about {suggestion}")
          answer= input("Do you like it? [Y/N]").lower()

          if answer== "yes":
               print(f"{Fore.GREEN}Chatbot: Awesome! Enjoy {suggestion}!")
          elif answer== "no":
               print(f"{Fore.RED}Chatbot: I'll give you another suggestion.")  
               recommend()
          else:
               print(f"{Fore.RED}Chatbot: How about another suggestion.")
               recommend()
     else:
          print(f"{Fore.YELLOW}Chatbot: I don't think I have that type of destination...")                 

# Offer packing tips based on user’s destination and duration


# Tell a random joke

# Display help menu

# Main chat loop

# Run the chatbot
if __name__ == "__main__":
    chat()
