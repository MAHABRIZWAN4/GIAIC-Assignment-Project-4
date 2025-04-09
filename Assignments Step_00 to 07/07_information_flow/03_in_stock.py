# Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit as a parameter and returns how many of that fruit are in her inventory. Write code in main() which will:

print("Step 07_INFORMATION_FLOW ==> 03_in_stock")


def num_in_stock(fruit:str):
    # This function returns the number of fruit Sophia has in stock.
	if fruit == 'apple':
		return 2
	if fruit == 'durian':
		return 4
	if fruit == 'pear':
		return 1000
	else:
		# this fruit is not in stock.
		return 0
	

def main():
	fruit : str = input("\033[1;3mEnter a fruit: \033[0m")
	stock = num_in_stock(fruit)
	if stock == 0:
		print("This fruit is not in stock.")
	else:
		print("This fruit is in stock! Here is how many:")
		print(stock)
		


if __name__ == '__main__':
    main()