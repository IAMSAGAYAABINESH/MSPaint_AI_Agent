PROMPT_TEMPLATE = ('''
You are an expert Python programmer. Your task is to generate the Python code for a file named drawShape.py. This file will contain a single function, draw_shape, which uses a predefined library of functions to draw a picture in MS Paint.
Instructions and Constraints:
File Name: The code you generate will be saved as drawShape.py.
Single Function: The file must contain only one function named draw_shape.
Function Signature: The function signature must be exactly: def draw_shape(win, start_pt, end_pt):.
win: The pywinauto window handle for MS Paint.
start_pt: A tuple (x1, y1) representing the top-left corner of the available drawing area.
end_pt: A tuple (x2, y2) representing the bottom-right corner of the available drawing area.
Use Provided Functions: You must only use the drawing functions provided in the shapes.py context below. Do not use pyautogui directly or define your own drawing logic. Import the necessary functions from shapes. You have shapes such as Line, Rectangle, Hexagon, Star, Polygon, Triangle and Square given in the functions. Think which ones can be used to draw creatively.
Coordinate System: All coordinates for the shapes you draw must be calculated relative to the start_pt and end_pt to ensure the drawing fits within the designated canvas area.
No Extra Code: Do not include any code to run the function (e.g., if **name** == "__main__":). The output should only be the import statements and the draw_shape function definition. Do not include comments in the code or markdown or use fenced code blocks with the language identifier. Give only the code no other texts.
Code Context:
Here are the other files in the project that you need to be aware of.
main.py (This file calls your function):
import time
import warnings
import pyautogui
from pywinauto import Application
from drawShape import draw_shape
warnings.filterwarnings("ignore", category=SyntaxWarning)
pyautogui.PAUSE = 0.05          
pyautogui.FAILSAFE = True
def main():
    app = Application(backend="uia").start(r"mspaint.exe")
    win = app.window(title_re=r".*Paint.*")
    win.wait('visible ready', timeout=10)
    win.set_focus()
    win.maximize()
    time.sleep(1)
    start_pt = (386, 265)
    end_pt   = (1531, 902)
    draw_shape(win, start_pt, end_pt)
    print("Completed")
    time.sleep(8)
if **name** == "__main__":
    main()
shapes.py (This is your library of available drawing functions):
import time
import math
import pyautogui
TOOL_MAP = {
    "pencil": "PencilTool",
}
def select_tool(win, tool_name: str):
    """Click the Paint toolbar button for the requested tool (pywinauto)."""
    auto_id = TOOL_MAP[tool_name.lower()]
    btn = win.child_window(auto_id=auto_id, control_type="Button")
    btn.wait('visible enabled', timeout=5)
    btn.click_input()
    time.sleep(0.6)  
def draw_line(start: tuple[int, int], end: tuple[int, int], duration: float = 0.25):
    """Draw a line using the pencil tool."""
    pyautogui.moveTo(*start)
    pyautogui.mouseDown(button='left')
    pyautogui.dragTo(*end, duration=duration, button='left')
    pyautogui.mouseUp(button='left')
    time.sleep(0.1)
# ── RECTANGLE ────────────────────────────────────────────────────────
def draw_rectangle_shape(win, start: tuple[int, int], end: tuple[int, int]):
    """Draw a rectangle using the pencil tool by drawing 4 lines."""
    select_tool(win, 'pencil')
    x1, y1 = start
    x2, y2 = end
    draw_line((x1, y1), (x2, y1))  
    draw_line((x2, y1), (x2, y2))
    draw_line((x2, y2), (x1, y2))  
    draw_line((x1, y2), (x1, y1))
# ── HEXAGON ────────────────────────────────────────────────────────
def draw_hexagon(win, center: tuple[int, int], radius: int):
    """Draw a hexagon using the pencil tool."""
    select_tool(win, 'pencil')
    cx, cy = center
    points = []
    for i in range(6):
        angle = 2 _math.pi_ i / 6          # ← fixed
        x = cx + int(radius * math.cos(angle))
        y = cy + int(radius * math.sin(angle))
        points.append((x, y))
    draw_polygon(win, points)
# ── STAR ────────────────────────────────────────────────────────────
def draw_star(win, center: tuple[int, int], size: int):
    """Draw a 5‑pointed star using lines."""
    select_tool(win, 'pencil')
    cx, cy = center
    points = []
    for i in range(10):
        angle = math.pi / 2 + 2 _math.pi_ i / 10
        if i % 2 == 0:  
            x = cx + int(size * math.cos(angle))
            y = cy + int(size * math.sin(angle))
        else:           
            x = cx + int(size _0.4_ math.cos(angle))  
            y = cy + int(size _0.4_ math.sin(angle))  
        points.append((x, y))
    for i in range(5):
        draw_line(points[2*i], points[(2*i + 4) % 10])
        draw_line(points[(2*i + 4) % 10], points[(2*i + 6) % 10])
# ── POLYGON, TRIANGLE, SQUARE, etc. (unchanged) ───────────────────────
def draw_polygon(win, points: list[tuple[int, int]]):
    """Draw a polygon by connecting consecutive points."""
    select_tool(win, 'pencil')
    if len(points) < 2:
        return
    for i in range(len(points) - 1):
        draw_line(points[i], points[i + 1])
    draw_line(points[-1], points[0])
def draw_triangle(win, points: list[tuple[int, int]]):
    """Draw a triangle (3 points)."""
    select_tool(win, 'pencil')
    if len(points) != 3:
        return
    draw_line(points[0], points[1])
    draw_line(points[1], points[2])
    draw_line(points[2], points[0])
def draw_square(win, center: tuple[int, int], size: int):
    """Draw a square (center + side length)."""
    select_tool(win, 'pencil')
    half = size // 2
    x, y = center
    tl = (x - half, y - half)
    tr = (x + half, y - half)
    br = (x + half, y + half)
    bl = (x - half, y + half)
    draw_line(tl, tr)
    draw_line(tr, br)
    draw_line(br, bl)
    draw_line(bl, tl)
Drawing Request:
Based on all the context and rules above, create the draw_shape function to draw the following:
{input_query}
''')