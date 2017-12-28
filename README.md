# Pins-and-Noodles
## TL;DR

Run [the example file puzzleModel.py](puzzleModel.py), which simulates [the board pictured here](pins%20and%20noodles.jpg). Then read [this last section](#understanding-the-output) to interpret the output. Remember to install Numpy first.

## Intro

Inspired by [this project](pins%20and%20noodles.jpg), this repository brute forces the different combinations of `Noodles` on the various `pins` of a `Board` to produce a list of the working combinations.

In order for a combination to work, all of the following conditions must be met:
 - No noodle can be sticking "out of bounds" 
   (bounds being determined by the edge of the (square) board and user-defined "holes")
 - No noodle can be overlapping another noodle
 - No noodle can fall on a pin other than the one on which it rests
 - Every non-hole square of the board must be covered by a noodle
 
 NOTE: **Requires Numpy** (for matrix multiplication). Any version should do, tested with Numpy 1.13.0 and Python 3.5.
 
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
 
  - `<np.matrix()>` is, for example, `np.matrix([(x1,y1), ... , (xn,yn)])`. It represents the coordinates of each square relative to the location of the pin hole. In other words, the pin hole represents the origin and every other square's coordinate corresponds to the (x,y) positions of the square relative to the hole. 
  
  It is important to note that **the positive x-axis points to the right** and **the positive y-axis points down**. 
  
  ```
        (-y)
         ^
(-x) <-+-> (+x)
         v
        (+y)
  ```
  
  For example, the `Noodle` below (where `<>` represents the `Noodle`'s hole, which is also the `Noodle`'s origin)  would be initialized like this: `n = Noodle("n", np.matrix([(0,0),(0,-1),(1,-1),(2,-1),(2,-2),(3,-1)]), False)`
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
 
### Understanding the Output
  Running `puzzleModel.py` produces the following output:
  ```
[('n12', (0, 7), 0), ('n08', (3, 5), 0), ('n04', (6, 0), 0), ('n11', (7, 4), 0), ('n01', (0, 2), 0), ('n03', (2, 3), 0), ('n07', (0, 4), 0), ('n10', (5, 7), 0), ('n05', (7, 0), 0), ('n02', (2, 1), 0), ('n06', (7, 3), 0), ('n09', (5, 4), 0), None]
run time: 33
number of iterations: 972161
iterations/second: 29284
  ```
  There is only one set of answers in the list (each set of answers ends with `None`), so this means that the `Board` has only **one unique solution**.
  
  Each item in the list contains the following information: `(<noodle name>, <pin location>, <orientation>)`
  - `<noodle name>` is the name given to the noodle
  - `<pin location>` is the location of the pin on which the noodle sits
  - `<orientation>` is a number 0 through 7, where 0 is the original orientation of the piece as entered, 0-3 represent the original orientation rotated 90 degrees clockwise (0-3) times, and orientation 4 represents orientation 3 reflected about the y axis, and orientations 4-7 represent the orientation 4 rotated 90 degrees clockwise (0-3) times.
  
    Whew! That was a lot. See the following examples for visual representations of this.
  <details>
 <summary>Orientation Examples</summary>
 
  orientation 0:
 ```
        __
  _____|  |__
 |   ________|
 |<>|
 ```
 
  orientation 1:
 ```
  _____
 |<>   |__
    |   __|
    |__|
 ```
 
   orientation 2:
 ```
  ______|<>|
 |__    ___|
    |__|
 ```
 
   orientation 3:
 ```
     __
  __|  |
 |__   |__
    |___<>|
 ```
 
   orientation 4:
 ```
     __
    |  |__
  __|   __|
 |<> __|
 ```

   orientation 5:
 ```
 |<>|______
 |__    ___|
    |__|
 ```
  orientation 6:
 ```
     _____
  __|   <>|
 |__   |
    |__|
 ```
   orientation 7:
 ```
     __
  __|  |__
 |_____   |
       |<>|
 ```
</details>
  
