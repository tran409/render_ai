import os
from google import genai
import gradio as gr

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def chat(message, history):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=message,
    )
    return response.text

demo = gr.ChatInterface(fn=chat)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    demo.launch(server_name="0.0.0.0", server_port=port)