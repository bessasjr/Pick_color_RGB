from pynput import mouse
import pyautogui


def on_click(x, y, button, pressed):
    if button == mouse.Button.left and pressed:
        r,g,b = pyautogui.pixel(x, y)
        rgb = (f'{r}, {g}, {b}')
        rgbperc = f'{r/ 255:.3f},{g/ 255:.3f},{b/ 255:.3f}'
        rgbhex = '#%02x%02x%02x' % (r,g,b)

        print(f'RGB: {rgb}')
        print(f'Percentual: {rgbperc}')
        print(f'Hexadecimal: {rgbhex}\n')

    
    if button == mouse.Button.right and pressed:
        listener.stop()
        
        
with mouse.Listener(on_click=on_click) as listener:
    listener.join() 



    
