import pyautogui
import pyperclip
import time
from google import genai


def chat_history():
    # Give time to switch to target window
    time.sleep(3)

    # Step 1: Click at (740, 1048)
    pyautogui.click(740, 1048)
    time.sleep(0.5)

    # Step 2: Drag to select text/content
    pyautogui.moveTo(701, 216)
    pyautogui.dragTo(1838, 925, duration=1, button='left')
    time.sleep(0.3)

    # Step 3: Copy selected content
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.3)
    pyautogui.click(701, 216)
    # pyautogui.click(740, 1048)

    # Step 4: Store clipboard content into variable
    copied_text = pyperclip.paste()

    # Step 5: Print it
    # print("Copied Content:")
    return copied_text

def aiProcess(chatHistory):
    client = genai.Client(api_key="AIzaSyB0HPQhibfsEejVjUU4LBuGRc296ingPls")

    prompt = f"""
    SYSTEM:
    You are a person named Manthan Singla.
    You speak Hindi and English.
    You are from India and a coder.
    You analyze chat history and reply like Manthan Singla.
    Dates are in dd/mm/yyyy format.
    check through name of the sender to identify gender to reply

    CHAT:
    {chatHistory}

    Reply as Manthan Singla:
    """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    return response.text

def reply_Push(reply):
    # to click on the text box
    pyautogui.click(807,968)

    #to paste the reply
    pyperclip.copy(reply)
    pyautogui.hotkey('ctrl', 'v')

    #to send the message
    pyautogui.click(1807,965)



if __name__ == "__main__":
    chatHistory = chat_history()
    print(chatHistory)
    reply = aiProcess(chatHistory)
    print(reply)
    # reply_Push(reply)