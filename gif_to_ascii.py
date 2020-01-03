import os
import argparse
from PIL import Image, ImageSequence
import numpy as np
import time

def extractFrames(inGif):
    im = Image.open(inGif)
    frames = [frame.copy() for frame in ImageSequence.Iterator(im)]
    return frames

def img2ascii(img):
    w, h = img.size
    ratio = 60/w
    res_img = img.resize((round(w*ratio), round(h*ratio))).convert('L')
    im = np.array(res_img)
    w, h = im.shape
    avg = np.average(im)

    os.system('cls' if os.name=='nt' else 'clear')
    for i in range(w):
        for j in range(h):
            if im[i][j] < 100:
                print('x', end='')
            elif im[i][j] < 200:
                print('.', end='')
            else:
                print(' ', end='')
        print('')

if __name__=='__main__':

    parser = argparse.ArgumentParser(description='Gif turned to ascii art animation (you might need to resize your terminal window!)')
    parser.add_argument('gif', type=str, help='gif chosen for conversion (returns error if none existant path)')
    args = parser.parse_args()

    frames = extractFrames(args.gif)
    while True:
        for frame in frames:
            im = frame
            img2ascii(im)
            time.sleep(0.033)