from tkinter import *


def searcher(target: str, array: list):
    findings = []

    length = len(target)
    if length >= 3:
        for item in array:
            if item[:length] == target:
                findings.append(item)

        return findings
    else:
        return None


names = ["raghav", "ragnav", "ragrav", "ragarga", "nikita", "niktin", "nintik", "nik"]

found = searcher("ragh", names)
if type(found) is list:
    if len(found) != 0:
        print(found)
    else:
        print("Not Found")
else:
    print("Nope")

