#!/bin/bash

FOLDER='./out/*.tif'
OUTPUT='out.pdf'

convert -monitor $FOLDER $OUTPUT
