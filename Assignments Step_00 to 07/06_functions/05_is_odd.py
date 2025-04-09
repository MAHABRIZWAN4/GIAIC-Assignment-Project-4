# 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd


print("Step 06_FUNCTIONS ==> 05_is_odd")



def main():
    for i in range(10):  # 0 se 9 tak numbers check karenge
        if i % 2 == 0:  # Agar number 2 se divide ho jaata hai (even number)
            print(f'{i} is even')
        else:  # Agar number 2 se divide nahi hota (odd number)
            print(f'{i} is odd')

if __name__ == '__main__':
    main()






