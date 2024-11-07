import subprocess
import re

def run(command):
    return subprocess.run(command, capture_output=True).stdout.decode("utf-8")

print(run(["xinput", "list"]))
tablet_id = input("Device ID of the tablet: ")
match = re.search(r"(\d+)x(\d+).+\*", run(["xrandr"]))
screen_width, screen_height = map(int, match.groups())

screen_ratio = screen_width / screen_height

tablet_ratio = eval(input('Enter the tablet screen ratio ("x/y"): '))

y_factor = screen_ratio/tablet_ratio

run(["xinput", "set-prop", tablet_id, "Coordinate Transformation Matrix", "1", "0", "0", "0", str(y_factor), "0", "0", "0", "1"])
