# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

def meme_ending_mad_libs():
    print("Step01_expressions => 08_tiny_mad_lib")
    print("😂 Welcome to League Mad Libs! 🎭")

    adjective = input("Please type an adjective (e.g: masaledar, gol, tez): ")
    noun = input("Please type an noun (e.g: bhindi, uncle, remote): ")
    verb = input("Please type an verb(e.g: nachna, urhna, sohna): ")

    print("\n🤣 Yeh lo aapki funny kahani:")
    print(f"Kal raat ek {adjective} {noun} ne achanak {verb} shuru kar diya, aur background mein awaaz aayi: 'oye hoye oye hoye, mujhe gol gappay do re baba!' 🌮🤣💃")

if __name__ == '__main__':
    meme_ending_mad_libs()



