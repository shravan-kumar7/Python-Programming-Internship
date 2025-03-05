import random
import string

adjectives = ["Happy", "Brave", "Curious", "Energetic", "Graceful", "Mysterious", "Vivid", "Bold", "Serene", "Zesty",
              "Clever", "Gentle", "Radiant", "Fierce", "Joyful", "Lively", "Nimble", "Witty", "Charming", "Dynamic"]

nouns = ["Tiger", "Dragon", "Phoenix", "Panther", "Eagle", "Wolf", "Falcon", "Leopard", "Shark", "Lion",
         "Cobra", "Griffin", "Hawk", "Jaguar", "Bear", "Cheetah", "Viper", "Raven", "Bison", "Kraken"]

def generate_username(add_numbers=False, add_special=False, count=1):
    usernames = []
    special_chars = "!@#$%^&*"
    
    for _ in range(count):
    
        adj = random.choice(adjectives)
        noun = random.choice(nouns)
        username = adj + noun
        
        if add_numbers:
            username += str(random.randint(0, 999))
            
        if add_special:
            username += random.choice(special_chars)
            
        usernames.append(username)
    
    return usernames

def save_to_file(usernames):
    try:
        with open("usernames.txt", "a") as file:
            for username in usernames:
                file.write(username + "\n")
        print(f"Saved {len(usernames)} username(s) to usernames.txt")
    except Exception as e:
        print(f"Error saving to file: {e}")

def main():
    print("Welcome to Random Username Generator!")
    
    while True:
        try:
            count = int(input("How many usernames to generate? (1-10): "))
            if count < 1 or count > 10:
                print("Please enter a number between 1 and 10")
                continue
                
            numbers = input("Include numbers? (y/n): ").lower() == 'y'
            special = input("Include special characters? (y/n): ").lower() == 'y'
            save = input("Save to file? (y/n): ").lower() == 'y'
            
            usernames = generate_username(numbers, special, count)
            
            print("\nGenerated Usernames:")
            for i, username in enumerate(usernames, 1):
                print(f"{i}. {username}")
            
            if save:
                save_to_file(usernames)
            
            again = input("\nGenerate more usernames? (y/n): ").lower()
            if again != 'y':
                break
                
        except ValueError:
            print("Please enter a valid number")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    print("Thank you for using Random Username Generator!")

if __name__ == "__main__":
    main()