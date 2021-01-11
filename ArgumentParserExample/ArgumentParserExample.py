'''
    Statement : Counting shapes in any given input image while annotating an output image
    that gets written to disk. Basically, the number of shapes in a particular image.

    Use of Argument Parser : Using the command line arguments, specifying the input and output
    path, making it dynamic.


'''

# Packages to be used.

# Argument Parser for passing command line arguments.

import argparse
import matplotlib.pyplot as plt
import os

# OpenCV package.

import cv2

# Series of convenience functions to make basic image processing functions such as
# translation, rotation, resizing, skeletonization, displaying Matplotlib images, sorting
# contours, detecting edges, and much more easier with OpenCV.

import imutils

# Argument Parser Object for parsing command line arguments
ap = argparse.ArgumentParser()

#Input file path
ap.add_argument("-i","--input",required=True,help="path to input image")

# #Output file path
# ap.add_argument("-o","--output",required=True,help="path to output image")

# Loading the arguments,in the ArgumentParser objects to parse the
# command line arguments

'''
vars() function : The vars() function returns the __dic__ attribute of an object.

The __dict__ attribute is a dictionary containing the object's changeable attributes.
 calling the vars() function without parameters will return a dictionary containing the local symbol table.

'''
args = vars(ap.parse_args()) # Arguments in the form of a dictionary

# Reading the input image using OpenCV
'''
We need the image in grayscale, because it's easier to process 
the image in grayscale rather than RGB or BGR

OpenCV by default image input format follows the "BGR" color scheme

There are two way to change the image to grayscale :
1. Directly in the cv2.imread() function
2. Using cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) -> a complicated way to change it to GRAYSCALE

Hence, using the first one.
'''
image = cv2.imread(args["input"],0)

'''
Further Image Processing steps to detect the shapes (technically contours) :-

1. Change image to grayscale.
    Reason :- 
2.


'''








