"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Veronica Gawarecki.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
size=100
bill=rg.SimpleTurtle()
bill.speed=35
for k in range(100):
    bill.pen=rg.Pen('green',5)
    bill.forward(size)
    bill.right(60)
    bill.forward(size)
    bill.right(60)
    bill.forward(size)
    bill.right(60)
    size=size-1
distance=500
jane=rg.SimpleTurtle()
jane.speed=35
for k in range(100):
    jane.pen = rg.Pen('red', 5)
    jane.forward(distance)
    jane.right(120)
    jane.forward(distance)
    jane.right(120)
    jane.forward(distance)
    jane.right(120)
    distance = distance - 5