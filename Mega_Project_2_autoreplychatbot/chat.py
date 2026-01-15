import pyautogui
import pyperclip
import time

# Give time to switch to target window
time.sleep(3)

# Step 1: Click at (740, 1048)
pyautogui.click(740, 1048)
time.sleep(0.5)

# Step 2: Drag to select text/content
pyautogui.moveTo(650, 185)
pyautogui.dragTo(1838, 919, duration=1, button='left')
time.sleep(0.3)

# Step 3: Copy selected content
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.3)

#to deselect the text
pyautogui.click(701, 216)

#return to vs code
pyautogui.click(740, 1048)

# Step 4: Store clipboard content into variable
copied_text = pyperclip.paste()

# Step 5: Print it
print(copied_text)