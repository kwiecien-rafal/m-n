#2 Write a function which takes sets of parameters of two figures and compares their fields. (4p)
# The exemplary input is [[Circle, 4], [Rhombus, 2, 4]]
# Expected output would be 'The first figure (Circle) has larger field'

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

def compareFields(figures):

    flds=[]
    for fig in figures:
        if len(fig) == 2:
            flds.append(countField(fig[0],fig[1]))
        else:
            flds.append(countField(fig[0],fig[1],fig[2]))

    if flds[0] == 0 or flds[1] == 0:
        print('The input is invalid.')
    elif flds[0] > flds [1]:
        print('The first figure (', figures[0][0], ') has a larger field.')
    elif flds[0] < flds [1]:
        print('The second figure (', figures[1][0], ') has a larger field.')
    else:
        print('The fields are equal.')


figury1 = [['Circle', 4], ['Rhombus', 2, 4]]
compareFields(figury1)
figury2 = [['triangle', 4, 2], ['Rhombus', 2, 4]]
compareFields(figury2)
figury3 = [['Circle', -5], ['rectangle', 2, 4]]
compareFields(figury3)
figury4 = [['RECTANGLE', 4, 4], ['Triangle', 22, 4]]
compareFields(figury4)