
---
# Starting the Drawing
April 23rd 2026

"Ribbon Menu"
Categories for *all* the tools.
But! The faster we learn the shortcuts for the tools rather than clicking on them, the faster we can work.

We are spending most of the time on the *HOME* tab.
From time to time, *INSERT*
And as well, we'll spend a lot of time on *ANNOTATE*

The rest isn't really relevant.

**What is AutoCAD for?**
- Not all that great for 3D modelling
- But it's helpful to know how to draw in 2D first then switch over to modelling
	- "Easier learning curve"

It appears to have Build tools. Kind of like Assets.

```
Basic AutoCAD command list (course tutorials may vary)

Main geometry generators
- Line ("L") ~
- Polyline ("PL") ~
- Arc ("A") ~
- Circle ~
- Advanced polyline ("PL" -> enter -> "A" -> enter -> "S" -> enter -> "L" ~
- Object snap ("F3") ~

Modifying geometry
- Move ("M")
- Copy ("CO")
- Rotate ("RO")
- Scale ("SC")
- Mirror ("MI")
- Trim ("TR")
- Extend ("EX")
- Fillet ("F")
- Zoom extents ("Z" -> enter "E" enter)
- Array ("ARRAY")
- Hatch ("H")

Annotation
- Text ("T")
- Linear dimension ("DIMLIN")
- Aligned dimension ("DIMALI")
- Measure distance ("DI")
- Block
- Object properties ("PR")
- Match properties ("MA")
- Plot ("P)
```

Navigation
- Scrolling (zoom)
- Panning (Hold M3, move moue

Selection
- Hold left click, drag --> Lasso selection
- So let's get rid of it!
	- Drag from left to right --> Blue       -     Only selects FULLY in
	- Drag from right to left --> Green    -      Selects everything that it crosses

Crosshair
- Can really max it out at 100
- Good for aligning things

On the command line --> Units --> Precision + Units  

**Let's create a line!**
How do you delete things? Press delete, or the erase command.
If we want to draw straight, flat lines, turn on "orthographic snapping" ---> **F8**
- Either horizontal or vertical

**Let's create a polyline!**
- It's very similar to a line, except everything is all sewn together
- BUT it has much more information stored inside of it
	- cmd line -> EXPLODE (lets us separate each line individually)
	- cmd line -> JOIN (lets us connect each line into one unit)

**Let's create ARC and CIRCLE**
- It's a circle and an arc
- Circles can be defined with one side of diameter/other side of the diameter (2P)
- OR three touching points (3P)

// At this point, the circle, line, arc, polyline is enough to describe any kind of geometry.
// We are complete.

(RECT)angle Tool
- cmd line -> RECT
- Select first point, cmd line -> d(imension) -> set length and width -> set the alignment of the rectangle

We digress to **OBJECT SNAPPING**
"O-Snap" - Bottom right corner menu
- Lots of different use-cases
	- End point
	- Mid point
	- Centre
	- Geometric Centre - Calculates all the average of all the corners of the polyline! Kinda cool
	- Quadrants - Divides into four, equal pieces
	- Intersection
	- Perpendicular 
	- Tangent Point
	- Nearest - On the hovered over line with a cursor, find the nearest point to where you're pointing

---

April 24th, 2026