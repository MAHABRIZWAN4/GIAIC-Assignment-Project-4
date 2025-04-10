import time

def countdown_timer(seconds):
    min = seconds // 60
    seconds = seconds % 60
    print(f'{min:02d}:{seconds:02d}', end="\r")
    time.sleep(1)
    seconds -= 1

    if seconds >= 0:
        countdown_timer(seconds)
    else:
        print("Time's Up!!")


if __name__ == "__main__":
    countdown_timer(10)


    