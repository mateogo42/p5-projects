from p5 import *
from random import randint

arr = []
bins = 30
i = 0
j = 0
start_sorting = False
key = 0
finished = False

def setup():
    global arr
    size(800, 400)
    for _ in range(bins):
        elem = randint(50, 300)
        arr.append(elem)

def draw():
    #fill(255)
    #text("SELECTION", 0, 0, 100, 40)
    background(0)
    translate(0, height)
    bins_width = width / len(arr)
    stroke(0)
    if start_sorting:
        selection_sort()
    for k in range(len(arr)):
        if k == key:
            fill(0, 0, 255)
        elif k == i:
            fill(255, 0, 0)
        else:
            fill(255)
        if finished:
            fill(0, 255, 0)
        rect((bins_width * k, 0), bins_width, -arr[k])

def selection_sort():
    global arr, finished, i, j, key
    if j < len(arr):
        if i >= len(arr):
            arr[key], arr[j] = arr[j], arr[key]
            j += 1
            i = j
            key = j
        elif arr[key] > arr[i]:
            key = i
        i += 1

    else:
        no_loop()
        finished = True
    
def mouse_pressed():
    global start_sorting
    start_sorting = not start_sorting

if __name__ == "__main__":
    run()
