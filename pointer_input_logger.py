# pointer_input_logger.py
from datetime import datetime
from pynput import keyboard, mouse

def ts():
    return datetime.now().strftime("%H:%M:%S.%f")[:-3]

def safe_attr(obj, name, default=None):
    try:
        return getattr(obj, name, default)
    except Exception:
        return default

def on_key_press(key):
    vk = safe_attr(key, "vk", None)
    sc = safe_attr(key, "scan", None)
    print(f"[{ts()}] KEYDOWN key={key!r} vk={vk} scan={sc}")

def on_key_release(key):
    vk = safe_attr(key, "vk", None)
    sc = safe_attr(key, "scan", None)
    print(f"[{ts()}] KEYUP   key={key!r} vk={vk} scan={sc}")

def on_click(x, y, button, pressed):
    state = "DOWN" if pressed else "UP"
    print(f"[{ts()}] MOUSE{state} button={button} x={x} y={y}")

if __name__ == "__main__":
    print("Listening for pointer input. Press pointer buttons now. Ctrl+C to stop.")
    k = keyboard.Listener(on_press=on_key_press, on_release=on_key_release)
    m = mouse.Listener(on_click=on_click)
    k.start()
    m.start()
    k.join()
    m.join()