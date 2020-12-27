import os
import time
import pyttsx3


def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    engine = pyttsx3.init()
    engine.say("Happy New Year! Have fun breaking your resolutions.")
    engine.runAndWait()

    print("Happy New Year!")


if __name__ == "__main__":
    countdown(3)