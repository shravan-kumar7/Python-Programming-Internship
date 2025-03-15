def count_words(text):
    words = text.split()
    return len(words)

def main():
    user_input = input("Enter a sentence or paragraph: ").strip()
    
    if not user_input:
        print("Error: Input cannot be empty. Please enter some text.")
        return
    
    word_count = count_words(user_input)
    print(f"Word Count: {word_count}")

if __name__ == "__main__":
    main()
