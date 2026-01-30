import math
import svgwrite
from generator import generate_question


def draw_triangle(dwg, center_x, center_y, size, rotation):
    points = [
        (0, -size),
        (size, size),
        (-size, size),
    ]

    rad = math.radians(rotation)
    rotated_points = []

    for x, y in points:
        rx = x * math.cos(rad) - y * math.sin(rad)
        ry = x * math.sin(rad) + y * math.cos(rad)
        rotated_points.append((center_x + rx, center_y + ry))

    dwg.add(
        dwg.polygon(
            rotated_points,
            fill="none",
            stroke="black",
            stroke_width=4
        )
    )


def save_svg(filename, rotation):
    dwg = svgwrite.Drawing(filename, size=("200px", "200px"))
    draw_triangle(dwg, 100, 100, 40, rotation)
    dwg.save()


def render_question(question):
    """
    Draw images based on question type
    """

    # Sequence question → has stem
    if question["type"] == "sequence":
        save_svg("stem.svg", question["sequence"][-1])

    # Draw options (common)
    letters =
