# AntiMaths

The AntiMaths paradigm explores the idea of negative dimensions. \
It is a metaphysical concept whereby every bit of maths has equal and opposite antimaths.

Everything you do in the mathematical realm is mirrored in the xy plane instead of the x plane. \
It explores the idea of -0 x -0 being -0 instead of 0.

![image](https://github.com/TheMindVirus/macropad/blob/archive/sketches/AntiMaths/image.png)

Normal Parabolic (and also Hyperbolic) Curves choose positive results for the negative dimension. \
Anti-Mathematical Shading and Controllerism prefers the use of tension curves instead.

This is done so that the transition between the negative side of x^2 and x^3 graphs \
doesn't have to flip up and down - the default interpolation of which is undefined for x^2.5.

It is suggested that the coefficient of -cos(2n) be used as the default interpolation. \
Otherwise, it forms a mirrored curve to make the value of n a real number instead of an integer.

With n being the number of dimensions, x is the input value and y is the output value. \
This also has implications for 3D because x and y (with z swapped and flipped) \
forms the same graph if not more complex with z and -z being factored in.

![screenshot](https://github.com/TheMindVirus/macropad/blob/archive/sketches/AntiMaths/screenshot.png)

AntiMaths seeks to find a usable pattern within a suitably defined context.

The example used to generate the custom code was that of programmable shading \
and also 2D->3D Proto-board PCB design, whereby you have a number of pads in a grid \
of variable dimensions (sometimes the dimensions are the same and squares can be simplified).

The number of pads is given by abc. When a=b=c, it's x^3. \
each set of pads in 2D could be connected in straight lines. \
when it is in a 3D lattice, there are more straight lines interconnecting the layers.

There are as many interconnect lines as there are pads, multiplied by the dimensions. \
A small but not insignificant optimisation to the number of interconnects can be made. \
The interconnects across the edge of each plane can be removed from the total. \
This only highlights the interconnects which are on the inside of the lattice.

The way that AntiMaths is applied to this problem allows for a standard formula to be written \
that makes use of what would otherwise be invalid dimensions in the negative space. \
Certain aspects of the calculation are considered edge-case and not suitable for general maths.
