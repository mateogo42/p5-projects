from p5 import *
from random import randint

arr = []
bins = 30
i = 0
j = 0
start_sorting = False
key = None
finished = False

def setup():
    global arr, key
    size(800, 400)
    for _ in range(bins):
        elem = randint(50, 300)
        arr.append(elem)
    key = arr[i]

def draw():
    background(0)
    translate(0, height)
    bins_width = width / len(arr)
    stroke(0)
    if start_sorting:
        bubble_sort()
    for k in range(len(arr)):
        if k == j:
            fill(255, 0, 0)
        else:
            fill(255)
        if finished:
            fill(0, 255, 0)
        rect((bins_width * k, 0), bins_width, -arr[k])

def bubble_sort():
    global arr, finished, i, j
    if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    if i < len(arr):
        j += 1
        if j >= len(arr) - 1 - i:
            j = 0
            i += 1
    else:
        no_loop()
        finished = True


def mouse_pressed():
    global start_sorting
    start_sorting = True


if __name__ == "__main__":
    run()
