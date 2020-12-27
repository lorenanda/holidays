import time
import datetime
import pyttsx3


def countdown(target_datetime):
    while True:
        difference = target_datetime - datetime.datetime.now()
        count_hours, rem = divmod(difference.seconds, 3600)
        count_minutes, count_seconds = divmod(rem, 60)

        if (
            difference.days == 0
            and count_hours == 0
            and count_minutes == 0
            and count_seconds == 0
        ):
            engine = pyttsx3.init()
            engine.say("Happy New Year! Have fun breaking your resolutions.")
            engine.runAndWait()

            print("Happy New Year!")
            break

        else:
            print(
                "Countdown to New Year: "
                + str(difference.days)
                + " day(s) "
                + str(count_hours)
                + " hour(s) "
                + str(count_minutes)
                + " minute(s) "
                + str(count_seconds)
                + " second(s) "
            )

        time.sleep(1)


if __name__ == "__main__":
    end_time = datetime.datetime(2021, 1, 1, 00, 00)
    countdown(end_time)
