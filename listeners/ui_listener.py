import asyncio
from tpspeek.core import TPspeekRealtime
from listeners import web_listener, db_listener
import threading

tp = TPspeekRealtime()

# Web listener example
async def web_task():
    audio_file = await web_listener.stream_audio("https://example.com/audio.mp3")
    tp.speech_to_speech(audio_file, "output.wav")
    print("✅ Web audio processed!")

# DB listener example
def db_callback(text):
    tp.speech_to_speech(text, "db_output.wav")
    print("✅ DB processed!")

threading.Thread(target=db_listener.db_poll_loop, args=("mydb.sqlite", db_callback), daemon=True).start()

asyncio.run(web_task())
