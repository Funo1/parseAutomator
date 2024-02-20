# Application:
In the app automator you can macros also known as workflows. With this Python project, you can convert these commands to code so they are more flexible to work with.
This allows different macros to be triggered depending on different conditions; for example, you could have an AI that examines the screen in a video game for when it turns night
and you could have it automatically run a macro using Python code. This could be used for endless things, namely being farms in numerous games.

# Current features:
- Translates hotkeys/multiple input lines
- Translates held-down keys
- Includes delays between actions

# Planned to be added:
- Type/writing specifier (Specify which lines are typed rather than actions. For many apps you might have to open chat/search typically with "/" or whatever key bind or mouseclick action in pyautogui the coordinates of the text field)


# How to use:
- Record a workflow in Automator app preinstalled on every mac
- Click on a command
- Copy it and past it into the src/inputs.txt (you might want to delete example text)
- Run the Python file (in vs code next to the play button there's a down arrow, run Python file)
- In the console, it will have formatted the code, which you can paste into any Python project (make sure you import "pyautogui" for it to work)
