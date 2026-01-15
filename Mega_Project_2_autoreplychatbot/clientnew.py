from google import genai

client = genai.Client(api_key="AIzaSyC_qz4yNvthROLBXw1Ih_HRH6xJ2CXjCbw")

prompt = """
SYSTEM:
You are a person named Manthan Singla.
You speak Hindi and English.
You are from India and a coder.
You analyze chat history and reply like Manthan Singla.
Dates are in dd/mm/yyyy format.

CHAT:
[12:01 pm, 8/1/2026] Mayank Sharma New: Manthan bruh
[12:02 pm, 8/1/2026] Mayank Sharma New: Was ❌were ✅my classmates 😁
[12:02 pm, 8/1/2026] Manthan Singla: Ok
[12:02 pm, 8/1/2026] Mayank Sharma New: Piyush ne kaha h mereko kehne ko 😂
[12:03 pm, 8/1/2026] Manthan Singla: Kar diya thik
[12:03 pm, 8/1/2026] Mayank Sharma New: Gud boi

Reply as Manthan Singla:
"""

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt
)

print(response.text)
