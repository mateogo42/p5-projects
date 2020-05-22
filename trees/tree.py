from p5 import *
import math
from PIL import ImageFont
from random import choice, random
from itertools import repeat

tree_size = 20
tree = []
node_height = 50
node_width = 150
radius = 30
f = None

def setup():
    global tree
    size(1000,1000)
    f = create_font("Roboto-Regular.ttf", 15)
    text_font(f, 100)
    text_align("CENTER", "CENTER")
    tree = [(i + 1, 2 * i + 1 if 2 * i + 1 < tree_size else -1, 2 * i + 2 if 2 * i + 2 < tree_size else -1) for i in range(tree_size) ]
    print(tree)

def draw():
    global tree
    background(255)
    translate(width * 0.5, height * 0.1)
    draw_tree(tree[0], Vector(0, 0))

def draw_tree(node, coord):
    stroke(0)
    if node[1] != -1:
        new_y = coord.y + node_height
        new_x = coord.x - node_width * node_height / new_y
        new_coord = Vector(new_x, new_y) 
        draw_tree(tree[node[1]], new_coord)
        draw_line(coord, new_coord, -1)
    fill(255)
    circle(coord, radius, mode="CENTER")
    fill(0)
    text(str(node[0]), (coord.x, coord.y))
    if node[2] != -1:
        new_y = coord.y + node_height
        new_x = coord.x + node_width * node_height / new_y
        new_coord = Vector(new_x, new_y) 
        draw_tree(tree[node[2]], new_coord)
        draw_line(coord, new_coord, 1)

def draw_line(center1, center2, dir):
    theta = math.atan(abs(center2.y - center1.y) / abs(center2.x - center1.x))
    #phi: angle of the line wrt a vertical line from the parent

    coord1 = center1 + Vector(dir * radius * math.cos(theta), radius * math.sin(theta)) * 0.5
    
    coord2 = center2 - Vector(dir * radius * math.cos(theta), radius * math.sin(theta)) * 0.5

    line(coord1, coord2)
        

if __name__ == "__main__":
    run()