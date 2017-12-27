# Pins-and-Noodles
## Intro

Inspired by [this project](pins%20and%20noodles.jpg), this repository brute forces the different combinations of `Noodles` on the various `pins` of a `Board` to produce a list of the working combinations.

In order for a combination to work, all of the following conditions must be met:
 - No noodle can be sticking "out of bounds" 
   (bounds being determined by the edge of the (square) board and user-defined "holes")
 - No noodle can be overlapping another noodle
 - No noodle can fall on a pin other than the one on which it rests
 - Every non-hole square of the board must be covered by a noodle
 
 ## Use
 
 ### Imports
 
 To define your own `Board` and `Noodles`, create a file in the `Pins-and-Noodles` repository and import the following:
 ```
 from Noodles import *
 from Board import *
 import numpy as np
 ```
 ### Noodles
 
 Next, define a `Noodle`:
 ```
 n1 = Noodle(<name>, <np.matrix()>, <isSym>)
 ```
  - `<name>` is `n1`'s name.
 
  - `<np.matrix()>` is, for example, `np.matrix([(x1,y1), ... , (xn,yn)])`. It represents the coordinates of each square relative to the location of the pin hole. In other words, the pin hole represents the origin and every other square's coordinate corresponds to the (x,y) positions of the square relative to the hole. It is important to note that **the positive x-axis points to the right** and **the positive y-axis points down**. For example, the `Noodle` below (where `<>` represents the `Noodle`'s hole)  would be initialized like this: `n = Noodle("n", np.matrix([(0,0),(0,-1),(1,-1),(2,-1),(2,-2),(3,-1)]), False)`
 ```
        __
  _____|  |__
 |   ________|
 |<>|
 ```
 
  - `<isSym>` is `True` if the piece is "symmetrical" in the sense that it can be rotated into the exact same position after flipping it upside-down. If this is not the case, `<isSym>` should be `False`.
  ### Boards
  To define a `Board`:
  ```
  b1 = Board(<pin list>, <size>, <noodle list>, <hole list>)
  ```
   - `<pin list>` is a list of tuples (or lists) which represents the pins on the board. 
   - `<size>` is the size of the board (assumed to be a square)
   - `<noodle list>` is a list of noodles, as described above
   - `<hole list>` is a list of holes which appear inside the board
   
   For example, the board pictured below (where ` _ ` represents a blank square, ` o ` represents pins, and `   ` represents a hole) would be defined like this: 
   ```
   b1 = Board([(6,0),(7,0),(2,1),(0,2),(2,3),(7,3),(0,4),(5,4),(7,4),(3,5),(0,7),(5,7)], \
              8, [n1, n2, ... n12], [(3,3),(3,4),(4,3),(4,4)])
   ```
   ```
_	_	_	_	_	_	o	o	
_	_	o	_	_	_	_	_	
o	_	_	_	_	_	_	_	
_	_	o	 	 	_	_	o	
o	_	_	 	 	o	_	o	
_	_	_	o	_	_	_	_	
_	_	_	_	_	_	_	_	
o	_	_	_	_	o	_	_
```
### Checking for solutions
 Once a `Board` is defined with its corresponding `Noodles`, call the function `checkAll()` on the board and print the results.
 ```
 b1.checkAll()
 ```
 
 ## Example File
  Run `puzzleModel.py` to see the results of the original model.
