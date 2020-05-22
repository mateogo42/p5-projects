from p5 import *
from random import randint

arr = []
bins = 30

def setup():
    global arr
    size(800, 400)
    for _ in range(bins):
        elem = randint(50, 300)
        arr.append(elem)

def draw():
    background(0)
    translate(0, height)
    bins_width = width / len(arr)
    stroke(0)
    for k in range(len(arr)):
        fill(255)
        rect((bins_width * k, 0), bins_width, -arr[k])

def merge_sort():
    pass

def merge(arr1, arr2):
    j = 0
    k = 0
    res = []

    while j < len(arr1) and k < len(arr2):
        if j < len(arr1) and arr1[j] <= arr2[k]:
            res.append(arr1[j])
            j += 1
        elif k < len(arr2) and arr2[k] <= arr1[j]:
            res.append(arr2[k])
            k += 1

    return res

    

def mouse_pressed():
    pass  

if __name__ == "__main__":
    run()