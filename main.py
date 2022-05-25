from pynput import mouse
import pyautogui


def on_click(x, y, button, pressed):
    if pressed is True:
        r,g,b = pyautogui.pixel(x, y)
        rgb = (f'{r}, {g}, {b}')
        rgbhex = '#%02x%02x%02x' % (r,g,b)

        print(rgb)
        print(rgbhex,'\n')

with mouse.Listener(on_click=on_click) as listener:
    listener.join()
    
