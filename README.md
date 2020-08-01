# Book Scanning Utils

## Rename.py
Makes a copy of sources files and places them in numerical order.

Assumes a folder structure of
- folder
	- front.jpg
	- back.jpg
	- left
		- left1.jpg
		- left2.jpg
	- right
		- right1.jpg
		- right2.jpg

Assumes right side is in reverse order (adjustable in config vars)

## Scantailor
Tool used to process the images ready for pdf

Can use normal or advanced

## Merge.sh
Calls ImageMagickk convert function to combine scantailor output into one pdf file
