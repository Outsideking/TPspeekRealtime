def ui_audio_listener(callback):
    while True:
        audio_file = wait_for_audio()  # ใส่ logic สำหรับ Android/Windows UI
        callback(audio_file)
