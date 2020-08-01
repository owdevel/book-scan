# Book Scanning Utils
A set of scripts designed to be used in conjunction with the [DIY Cardboard Book Scanner](https://www.instructables.com/id/Bargain-Price-Book-Scanner-From-A-Cardboard-Box/) and the ScanTailor program.

## Scanning Process
1) Scan left pages of book, save to folder 'left'
2) Scan right pages of book by flipping the book and starting from the back, save to folder 'right'
3) Scan front and back pages to front.jpg and back.jpg respectively
4) Run `rename.py`
5) Import into scantailor or scantailor advanced and edit
6) Run `merge.sh` on the output folder

## Scripts

### Rename.py
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

### Merge.sh
Calls ImageMagickk convert function to combine scantailor output into one pdf file
