from typing import Optional, Callable
from p5 import circle, Vector, text, text_align, fill, line
import math

RADIUS = 50
ANGLE = math.pi * 0.9

class Node:
    def __init__(self, value: int, dist: float, angle: float) -> None:
        self.value: int = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.coord: Optional[Vector] = None
        self.distance_to_childs = dist
        self.angle = angle

    def draw(self) -> None:
        fill(255)
        circle(self.coord, RADIUS, mode="CENTER")
        fill(0)
        text_align("CENTER", "CENTER")
        text(str(self.value), (self.coord.x, self.coord.y))

    def connect(self, node: 'Node') -> None:
        line(self.coord, node.coord)

    def traverse_and_draw(self) -> None:
        if self.left:
            self.left.traverse_and_draw()
            self.connect(self.left)
        self.draw()
        if self.right:
            self.right.traverse_and_draw()
            self.connect(self.right)
