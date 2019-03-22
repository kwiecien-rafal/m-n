#1 Write a function countField which calculates the field of a given figure. It takes the following input parameters:
# - type: circle/rectangle/triangle/rhombus
# - x & optional y.
# For circle we get only x which stands for radius. For Rectangle x&y are the figure's sides, for triangle they are
# accordingly the base and the height and for rhombus - diagonals (4p)

import numpy as np

def countField(fig,x,y=1):

    if x <= 0 or y <= 0:
        fld = 0
    elif fig.lower() == 'circle':
        fld = np.pi * x ** 2
    elif fig.lower() == 'rectangle':
        fld = x * y
    elif fig.lower() == 'triangle' or fig.lower() == 'rhombus':
        fld = (x * y) / 2
    else:
        fld = 0

    return fld

print(countField('circle',6))
print(countField('RECTANGLE',6,8))
print(countField('octagon',6))
print(countField('rhombus',-4,5))
print(countField('TrianGle',3,9))