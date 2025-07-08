import subprocess
import time

def run_adb_command(command, message):
    try:
        subprocess.run(command, shell=True, check=True)
        print(message)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")


def repeat_command(command, message,repeat,dealy):
    for _ in range(repeat):
        run_adb_command(command, message)
        time.sleep(dealy)


#Sequesnce Start from here

run_adb_command("adb shell input keyevent 3", "Home")
time.sleep(5)
#8 times right move
repeat_command("adb shell input keyevent 22", "Right Move", 8,0.3)

#Press ok on setting
run_adb_command("adb shell input keyevent 23", "press ok")
time.sleep(3)

#3 Times down
repeat_command("adb shell input keyevent 20", "Down Move",3,0.3)

#3  Times Right Move
repeat_command("adb shell input keyevent 22", "Right Move",3,0.3)

#Press ok on setting
run_adb_command("adb shell input keyevent 23", "press ok")
time.sleep(2)

#2 Times down
repeat_command("adb shell input keyevent 20", "Down Move",2,0.3)

#Press ok on setting
run_adb_command("adb shell input keyevent 23", "press ok")
time.sleep(2)

#1 Times down
repeat_command("adb shell input keyevent 20", "Down Move",1,0.3)

#Press ok on setting
run_adb_command("adb shell input keyevent 23", "press ok")
time.sleep(1)

#Press ok on setting
run_adb_command("adb shell input keyevent 23", "press ok")
time.sleep(6)

run_adb_command("adb shell input keyevent 3", "Home")


