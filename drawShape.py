from shapes import draw_rectangle_shape, draw_polygon, draw_hexagon, draw_triangle

def draw_shape(win, start_pt, end_pt):
    x1, y1 = start_pt
    x2, y2 = end_pt
    width = x2 - x1
    height = y2 - y1

    ground_level = y1 + int(height * 0.75)

    tree1_trunk_start = (x1 + int(width * 0.05), y1 + int(height * 0.45))
    tree1_trunk_end = (x1 + int(width * 0.1), ground_level)
    draw_rectangle_shape(win, tree1_trunk_start, tree1_trunk_end)
    
    tree1_leaves_points = [
        (x1 + int(width * 0.075), y1 + int(height * 0.2)),
        (x1, y1 + int(height * 0.5)),
        (x1 + int(width * 0.15), y1 + int(height * 0.5))
    ]
    draw_triangle(win, tree1_leaves_points)

    tree2_trunk_start = (x1 + int(width * 0.85), y1 + int(height * 0.4))
    tree2_trunk_end = (x1 + int(width * 0.9), ground_level)
    draw_rectangle_shape(win, tree2_trunk_start, tree2_trunk_end)
    
    tree2_leaves_points = [
        (x1 + int(width * 0.875), y1 + int(height * 0.15)),
        (x1 + int(width * 0.8), y1 + int(height * 0.45)),
        (x1 + int(width * 0.95), y1 + int(height * 0.45))
    ]
    draw_triangle(win, tree2_leaves_points)

    body_start_y = y1 + int(height * 0.5)
    body_start = (x1 + int(width * 0.2), body_start_y)
    body_end = (x1 + int(width * 0.8), ground_level)
    draw_rectangle_shape(win, body_start, body_end)

    roof_points = [
        (x1 + int(width * 0.3), body_start_y),
        (x1 + int(width * 0.7), body_start_y),
        (x1 + int(width * 0.6), y1 + int(height * 0.25)),
        (x1 + int(width * 0.4), y1 + int(height * 0.25))
    ]
    draw_polygon(win, roof_points)

    wheel_radius = int(height * 0.1)
    wheel_y_center = ground_level

    front_wheel_center = (x1 + int(width * 0.35), wheel_y_center)
    draw_hexagon(win, front_wheel_center, wheel_radius)

    back_wheel_center = (x1 + int(width * 0.65), wheel_y_center)
    draw_hexagon(win, back_wheel_center, wheel_radius)