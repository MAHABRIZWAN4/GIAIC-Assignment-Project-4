# Write a simple joke bot. The bot starts by asking the user what they want. However, your program will only respond to one response: Joke.

# If the user enters Joke then we will print out a single joke. Each time the joke is always the same:


print("Basic ==> 00_joke_bot")

PROMPT:str = "What do you want ? "
JOKE:str = "Why don't Skeleton fight each other ? \nBecause they don't have the guts. 😂🤣"
SORRY:str = "Sorry I only tell jokes"

def main():
    user_input = input(PROMPT)
    user_input = user_input.strip().lower()

    if "joke" in user_input:
        print(JOKE)
    else:
        print(SORRY)


if __name__ == "__main__":
    main()
