import time
import warnings
import pyautogui
import importlib
from pywinauto import Application
from textToShape import generate_and_save_drawing

warnings.filterwarnings("ignore", category=SyntaxWarning)
pyautogui.PAUSE = 0.05          
pyautogui.FAILSAFE = True

def main(): 
    while True:
        input_query = str(input("Input Query: "))
        generate_and_save_drawing(input_query)
        
        app = Application(backend="uia").start(r"mspaint.exe")
        win = app.window(title_re=r".*Paint.*")
        win.wait('visible ready', timeout=10)
        win.set_focus()
        win.maximize()
        time.sleep(1)
        start_pt = (386, 265)
        end_pt = (1531, 902)
        
        try:
            import drawShape
            importlib.reload(drawShape)
            print("Drawing in MS Paint...")
            drawShape.draw_shape(win, start_pt, end_pt)
            print("Completed!")
        except Exception as e:
            print(f"Error drawing shape: {e}")
        
        time.sleep(2)
        
        changes = input("Do you want to make any changes? (yes/no): ").strip().lower()
        if changes not in ['yes', 'y']:
            print("Program stopping...")
            break
        else:
            print("Current chat history will be used for context in next query.")
            
if __name__ == "__main__":
    main()