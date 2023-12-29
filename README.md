# LEDCubeAnimationDesigner
A high level design of a program to create an animation for 5x5x5 LED cube.

## Functions

create_cube

populate_x
populate_y
populate_z


## Log
For example: Z: [0, 1, 2, 3, 4, 0, ...] will be changed to Z: [0, 0, 0, 0, 0, 1, 2, ...] and the result will be anylyzed.
For example currently the z is being used as the color so a section of its repeating pattern will be changed.
To figure this out the color map will be played with and the result recorded.
The process to access the specific led needs to be figured out.
Some system needs to created to pick any desired pixel to choose a collor for it.

The current system can produce a cube, But the color still needs to be implemented. Currently, just to visualize the process the z values were used for color. This creates a pattern where the taler leds are lit up.
