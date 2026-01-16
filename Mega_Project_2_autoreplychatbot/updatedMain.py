import pyautogui
import pyperclip
import time
from google import genai


def chat_history():
    # Give time to switch to target window
    time.sleep(2)

    
    # Step 2: Drag to select text/content
    pyautogui.moveTo(669, 194)
    pyautogui.dragTo(1838, 919, duration=1, button='left')
    time.sleep(0.3)

    # Step 3: Copy selected content
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.3)
    pyautogui.click(701, 216)

    # Step 4: Store clipboard content into variable
    copied_text = pyperclip.paste()

    # Step 5: Print it
    # print("Copied Content:")
    return copied_text

def last_message(chatHistory):
    split = chatHistory.split("/2026] ")
    lastMessage = split[-1]
    return lastMessage

def aiProcess(chatHistory):
    client = genai.Client(api_key="Enter_API_KEY")

    prompt = f"""
    SYSTEM:
    You are a person named Manthan Singla.
    You speak Hindi and English.
    You are from India.
    You analyze chat history and reply like Manthan Singla.
    Dates are in dd/mm/yyyy format.
    always reply in short and precise way and with less emoji
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
    pyautogui.click(824,963)

    #to paste the reply
    pyperclip.copy(reply)
    pyautogui.hotkey('ctrl', 'v')

    #to send the message
    time.sleep(3)
    pyautogui.click(1873,963)



if __name__ == "__main__":
    # Step 1: Click at (740, 1048)
    pyautogui.click(740, 1048)
    time.sleep(0.5)
    while True:
        
        chatHistory = chat_history()
        print(chatHistory)
        lastMessage = last_message(chatHistory)
        if lastMessage.lower().startswith("mom"):
            reply = aiProcess(chatHistory)
            print(reply)

            reply_Push(reply)
