import os
import time
import re

Sequence = []
parsedChar = []
incrs = []

OrderOfEvents = []


# Looks for sequences
def numerate(output):
    global parsedChar
    global incrs
    parsedChar = []
    incrs = []
    # Loop through the characters in the input string
    for i in range(len(output)):
        # If it's the first character or the sequence continues, append the character to parsedChar
        if i == 0 or output[i] == output[i - 1]:
            parsedChar.append(output[i])
        # If the sequence breaks, count occurrences and reset parsedChar
        else:
            iters = len(parsedChar)
            if iters > 1:
                incrs.append(iters)
            else:
                incrs.append(1)  # Add the individual character
            parsedChar = [output[i]]  # Start a new sequence
            Seq = [output[i - 1]]

    # Append the length of the last sequence
    if parsedChar:
        iters = len(parsedChar)
        if iters > 1:
            incrs.append(iters)
        else:
            incrs.append(1)
        global Sequence

    Sequence = []
    for i in range(len(output)):
        if output[i] != output[i - 1]:
            Sequence.append(output[i])
    return formatMacro(Sequence)


# Code format UwU:
def formatMacro(Sequence):
    formatted_commands = []
    for x in range(len(Sequence)):
            cmdLoop = f'''
for i in range({incrs[x]}):
    pyautogui.keyDown('{Sequence[x]}')
pyautogui.keyUp('{Sequence[x]}')
'''
    formatted_commands.append(cmdLoop)
    return formatted_commands


# Parses macro into text
def parseAutomator(automator_script):
    lines = automator_script.split('\n')
    pyautogui_commands = []

    for line in lines:
        if line.startswith('-- Type'):
            # Extract typed text from the line
            match = re.search(r"'([^']*)'", line)
            if match:
                typed_text = match.group(1)
                pyautogui_commands.append(f"{typed_text}")
        elif line.startswith('-- Press'):
            # Extract special character from the line
            match = re.search(r"Press (.+)", line)
            if match:
                special_char = match.group(1)
                pyautogui_commands.append(f"pyautogui.hotkey('{special_char}')")
        elif line.startswith('delay'):
            try:
                delay = float(line.split()[-1])
                pyautogui_commands.append(f"time.sleep({delay})")
            except ValueError:
                print("Invalid delay value:", line)

    return pyautogui_commands


automator_script_file = 'src/inputs.txt'

with open(automator_script_file, 'r') as file:
    automator_script = file.read()

pyautogui_commands = parseAutomator(automator_script)
formatted_commands_list = []

if pyautogui_commands:
    # Print the translated PyAutoGUI commands
    for command in pyautogui_commands:
        if len(command.split('⌃')) > 1:
            output = f"pyautogui.hotkey('ctrl','{command.split('⌃')[1]}"
            formatted_commands_list.append(output)
        else:
            if command.startswith('time.sleep'):
                formatted_commands_list.append(command)
            else:
                formatted_commands_list.extend(numerate(command))
        OrderOfEvents.append(command)

def sort(formatted_commands_list):
    for k in range(len(formatted_commands_list)):
        if formatted_commands_list[k].startswith('time'):
            formatted_commands_list[k], formatted_commands_list[k-1] = formatted_commands_list[k - 1], formatted_commands_list[k]
    for l in range(len(formatted_commands_list)):
        print(formatted_commands_list[l])
sort(formatted_commands_list)



