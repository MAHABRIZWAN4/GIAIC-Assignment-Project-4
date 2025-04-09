# Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

# Around the world, different countries have different voting ages. In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different:

# the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)

# the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)

# the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)

# Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua.


print("Step03_IF_STATEMENT ==> 02_international_voting_age")


def voting_age():
    Age = int(input("Enter your age: "))
    if Age >= 48:
        print("You can vote in Mayengua.")
    elif Age >= 25:
        print("You can vote in Stanlau.")
    elif Age >= 16:
        print("You can vote in Peturksbouipo.")
    else:
        print("You cannot vote in any of the countries.")


if __name__ == "__main__":
    voting_age()

