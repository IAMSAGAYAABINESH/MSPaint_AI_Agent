import time
import math
import pyautogui

TOOL_MAP = {
    "pencil": "PencilTool",
}

def select_tool(win, tool_name: str):
    auto_id = TOOL_MAP[tool_name.lower()]
    btn = win.child_window(auto_id=auto_id, control_type="Button")
    btn.wait('visible enabled', timeout=5)
    btn.click_input()
    time.sleep(0.6)  

def draw_line(start: tuple[int, int], end: tuple[int, int], duration: float = 0.25):
    pyautogui.moveTo(*start)
    pyautogui.mouseDown(button='left')
    pyautogui.dragTo(*end, duration=duration, button='left')
    pyautogui.mouseUp(button='left')
    time.sleep(0.1)

# RECTANGLE
def draw_rectangle_shape(win, start: tuple[int, int], end: tuple[int, int]):
    select_tool(win, 'pencil')
    x1, y1 = start
    x2, y2 = end
    draw_line((x1, y1), (x2, y1))  
    draw_line((x2, y1), (x2, y2)) 
    draw_line((x2, y2), (x1, y2))  
    draw_line((x1, y2), (x1, y1)) 

# HEXAGON
def draw_hexagon(win, center: tuple[int, int], radius: int):
    select_tool(win, 'pencil')
    cx, cy = center
    points = []
    for i in range(6):
        angle = 2 * math.pi * i / 6          # ← fixed
        x = cx + int(radius * math.cos(angle))
        y = cy + int(radius * math.sin(angle))
        points.append((x, y))
    draw_polygon(win, points)

# STAR
def draw_star(win, center: tuple[int, int], size: int):
    select_tool(win, 'pencil')
    cx, cy = center
    points = []
    for i in range(10):
        angle = math.pi / 2 + 2 * math.pi * i / 10 
        if i % 2 == 0:  
            x = cx + int(size * math.cos(angle))
            y = cy + int(size * math.sin(angle))
        else:           
            x = cx + int(size * 0.4 * math.cos(angle))  
            y = cy + int(size * 0.4 * math.sin(angle))  
        points.append((x, y))
    for i in range(5):
        draw_line(points[2*i], points[(2*i + 4) % 10])
        draw_line(points[(2*i + 4) % 10], points[(2*i + 6) % 10])

# POLYGON
def draw_polygon(win, points: list[tuple[int, int]]):
    select_tool(win, 'pencil')
    if len(points) < 2:
        return
    for i in range(len(points) - 1):
        draw_line(points[i], points[i + 1])
    draw_line(points[-1], points[0])

# TRIANGLE
def draw_triangle(win, points: list[tuple[int, int]]):
    select_tool(win, 'pencil')
    if len(points) != 3:
        return
    draw_line(points[0], points[1])
    draw_line(points[1], points[2])
    draw_line(points[2], points[0])

# SQUARE
def draw_square(win, center: tuple[int, int], size: int):
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