from p5 import *
import math
from PIL import ImageFont
from random import choice, random, randint
from binary import Node, RADIUS, ANGLE

tree_size = 20
node_height = 50
node_width = 500
radius = 30
f = None
root = None

def setup():
    global tree
    size(800,800)
    f = create_font("Roboto-Regular.ttf", 15)
    text_font(f, 100)

def draw():
    global tree
    background(255)
    translate(width * 0.5, height * 0.1)
    if root:
        root.traverse_and_draw()

def mouse_pressed():
    value = randint(1, tree_size) 
    add_node_to_tree(root, value)

def add_node_to_tree(node: Node, value: int):
    global root
    if not root:
        root = Node(value, 3 * RADIUS, ANGLE)
        root.coord = Vector(0, RADIUS / 2)
    elif value < node.value:
        if not node.left:
            node.left = Node(value, node.distance_to_childs, node.angle * 0.8)
            node.left.coord = node.coord + Vector(node.distance_to_childs * math.cos(node.angle), node.distance_to_childs * math.sin(node.angle))
        else:
            add_node_to_tree(node.left, value)
    else:
        if not node.right:
            node.right = Node(value, node.distance_to_childs, node.angle * 0.8)
            node.right.coord = node.coord + Vector(- node.distance_to_childs * math.cos(node.angle), node.distance_to_childs * math.sin(node.angle))
        else:
            add_node_to_tree(node.right, value)

if __name__ == "__main__":
    run()