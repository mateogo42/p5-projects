from p5 import *
from random import randint
import time

arr = []
aux_arr = []
bins = 50
i = 1
j = 0
start_sorting = False
key = None
finished = False

def setup():
    global arr, key, aux_arr
    size(800,400)
    for _ in range(bins):
        elem = randint(50, 300)
        arr.append(elem)
    aux_arr = arr[:]
    key = arr[i]

def draw():
    background(0)
    translate(0, height)
    bins_width = width / len(arr)
    stroke(0)
    if start_sorting:
        insertion_sort()
    for k in range(len(arr)):
        if k == j:
            fill(255, 0, 0)
        elif k == i:
            fill(0, 0, 255)
        else:
            fill(255)
        if finished:
            fill(0, 255, 0)
        rect((bins_width * k, 0),bins_width, -arr[k])

def insertion_sort():
    global arr, i, j, key, aux_arr, finished
    if i < len(arr):
        if j >= 0 and aux_arr[j] > key:
            aux_arr[j + 1] = aux_arr[j]
            j = j - 1
        else:
            aux_arr[j + 1] = key
            i += 1
            j = i - 1
            arr = aux_arr[:]
            if i >= len(arr):
                no_loop()
            else:
                key = arr[i]
                arr = aux_arr[:]
    else:
        no_loop()
        finished = True
        
def mouse_pressed():
    global start_sorting
    start_sorting = not start_sorting


if __name__ == "__main__":
    run()
