# Implement the helper function make_sentence(word, part_of_speech) which will take a string word and an integer part_of_speech as parameters and, depending on the part of speech, place the word into one of three sentence templates (or one from your imagination!):


print("Step 06_FUNCTIONS ==> 08_sentence_generator")


def make_sentence(word, part_of_speech):
    if part_of_speech == 0:  # Noun
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:  # Verb
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:  # Adjective
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Invalid part of speech! Please enter 0, 1, or 2.")  

def main():
    word = input("\033[34mPlease type a noun, verb, or adjective: \033[0m")  
    part_of_speech = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))  # User input for part of speech
    
    make_sentence(word, part_of_speech)  

if __name__ == '__main__':
    main()
