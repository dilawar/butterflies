"""locate_butterfly.py: 

Locate butterfly in an image.

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2015, Dilawar Singh and NCBS Bangalore"
__credits__          = ["NCBS Bangalore"]
__license__          = "GNU GPL"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import cv2
import numpy as np
from image_analysis import edge_detector as ed
from image_analysis import contour_detector as cd

args_  = None

def main():
    global args_ 
    inputFile = args_['input']
    print('[INFO] Processing %s' % inputFile)
    img = cv2.imread( inputFile)
    surf = cv2.SURF( 1000 )
    kp, des = surf.detectAndCompute( img, None)
    img2 = cv2.drawKeypoints(img, kp, None, (255,0,0), 4)
    cv2.imshow('interesting', img2)
    cv2.waitKey( 0 )

if __name__ == '__main__':
    import argparse
    # Argument parser.
    description = '''Locate a butterfly'''
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--input', '-i'
        , required = True
        , help = 'Input image file'
        )
    parser.add_argument('--output', '-o'
        , required = False
        , help = 'Output file'
        )
    parser.add_argument( '--debug', '-d'
        , required = False
        , default = 0
        , type = int
        , help = 'Enable debug mode. Default 0, debug level'
        )
    class Args: pass 
    args = Args()
    parser.parse_args(namespace=args)
    args_ = vars( args )
    main()
