def madlibs():
    print("Hurray🤩 LET'S PLAY WITH MADLIBS! FILL IN THE BLANKS WITH YOUR OWN WORDS ")

    name = input("Give me a name : ")
    place = input("Give me a place name : ")
    funny_adjective = input("Give me a funny adjective : ")
    random_object = input("Give me a random object : ")
    animal = input("Give me a name of animal : ")
    action_verb = input("Give me a action verb : ")
    funny_exclamation = input("Give me a funny exclamation : ")
    
    print("Here is your madlib story 🤣😂")
    story = f"""Once upon a time in the magical land of {place}, there lived a {funny_adjective} explorer named {name}.
    One day, {name} found a mysterious {random_object} lying under a dancing tree.
    As {name} picked it up, a talking {animal} jumped out and shouted, "{funny_exclamation}!"
    Shocked but excited, {name} decided to {action_verb} with the {animal} all around {place}.
    From that day on, the two became best friends and were known as the weirdest duo in all of {place}!
    
    The End 🤪"""
     
    print(story)

if __name__ == "__main__":
    madlibs()




