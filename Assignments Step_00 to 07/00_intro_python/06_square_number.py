# Ask the user for a number and prints its square ( the products of the number times itself ).


def main():
    user_input = int(input("\033[1;3mEnter the number which its square? \033[0m"))

    print(f"The square of your given number is {user_input*user_input}")

if __name__ == '__main__':
    main()