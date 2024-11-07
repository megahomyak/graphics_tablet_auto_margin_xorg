import re
import subprocess

def execute(command):
    return subprocess.run(command, capture_output=True, shell=True).stdout.decode("utf-8")

match = re.search(r"(\d+)x(\d+)", "xrandr | grep '*'")
width = match.group(1)
height = match.group(2)

screen_ratio = width / height
