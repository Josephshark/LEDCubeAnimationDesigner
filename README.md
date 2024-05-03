Copyright <2024> <Joseph Bagheri>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


# LEDCubeAnimationDesigner
A high level design of a program to create an animation for 5x5x5 LED cube.

## Use the example droplet animation and random animation for tips
![image](https://github.com/Josephshark/LEDCubeAnimationDesigner/assets/39276421/635a97a8-9437-48b5-a2ad-30b1c8fe584a)


## Constructor
LedCube(n) - Returns an nxnxn LedCube object with the following attributes:
        
        n - integer representing the length width and height of the cube.
        brightness - array containing the brighntess of the leds.

        x - array for encoded x
        y - array for encoded y
        z - array for encoded z

## Methods
    .show() shows a map of what leds are on in the stationary cube
    .change_led([x,y,z], Brightness) changes the brightness of a specified led.

## Log
The last work session had animations figured out. This session the focus will be on creating a good animation to potentially demo. 


Ok so last time there was this chatgpt code that allowed me to create animations
So i found out that the items were updated based on what they were last time like a function.
But it would be cool to be able to create a new array every time. This looks like it would have to be an array that contains the cube arrays and iterate through them. So imma have to figure out how to create this animation array and how to iterate through it over time.


Blitting did not work for the 3d iteration. Trying the next thing.

Need a way to create animations using the current functionality of the system.

https://matplotlib.org/stable/users/explain/animations/animations.html#sphx-glr-users-explain-animations-animations-py
To animate the animation, each frame of the animation will be iterated through in the animation function from matplotlib.
To animate the animation attribute of the led the animation will first need to be created by some function.
The animation attribute will contain a list of brightness arrays.
It has been decided that the methode of making an animation will be to make a new cube attribute called an animation attribute.


Need to design a method for users to design animations. 
To create this functionality the library documentation will be looked into for isights on its usage.
An animation needs to be created. The strategy that is being considered is the method of blotting offered by matplotlib.


Created the function that alows an led to be edited.
More work needs to be done for animation.

For example: Z: [0, 1, 2, 3, 4, 0, ...] will be changed to Z: [0, 0, 0, 0, 0, 1, 2, ...] and the result will be anylyzed.
For example currently the z is being used as the color so a section of its repeating pattern will be changed.
To figure this out the color map will be played with and the result recorded.
The process to access the specific led needs to be figured out.
Some system needs to created to pick any desired pixel to choose a collor for it.

The current system can produce a cube, But the color still needs to be implemented. Currently, just to visualize the process the z values were used for color. This creates a pattern where the taler leds are lit up.
