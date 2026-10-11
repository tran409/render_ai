import time

def chat(message, history):
    # Thử gửi tối đa 3 lần nếu gặp lỗi nghẽn mạng từ Google
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=message,
            )
            return response.text
        except Exception as e:
            if attempt < 2:  # Nếu chưa đủ 3 lần thì chờ 2 giây rồi thử lại
                time.sleep(2)
            else:
                return f"Máy chủ Google đang quá tải tạm thời, anh vui lòng bấm gửi lại sau vài giây nhé! (Lỗi: {e})"
