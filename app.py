import os
import time
import gradio as gr
from google import genai

# Khởi tạo client Gemini từ API Key
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def chat(message, history):
    # Thử gửi tối đa 3 lần nếu máy chủ bị nghẽn
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=message,
            )
            return response.text
        except Exception as e:
            if attempt < 2:
                time.sleep(2)
            else:
                return f"Máy chủ Google đang quá tải tạm thời, anh vui lòng bấm gửi lại sau ít phút nhé! (Lỗi: {e})"

# Tạo giao diện Chatbot bằng Gradio
demo = gr.ChatInterface(fn=chat, title="Gemini AI Chatbot")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    demo.launch(server_name="0.0.0.0", server_port=port)
