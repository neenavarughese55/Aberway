#! /bin/python

from aberway_background_code import create, update, main_loop


ColourFlip = True

    
screen, bg, lineList, nodeList = create(ColourFlip)
update(None, screen, bg, lineList, nodeList, None, None, None, None)


# --- SET THESE VALUES TO AN EXAMPLE ---
startPos = 0
listOfNodesToPass = [10,11,14]
length = 676.75
error = 0.06

def path_update():
    ListOfNodeId = [] #set the value of this to the nodes that your path takes
    # ---------- ---------- YOUR CODE GOES HERE ---------- ----------




    # ---------- ---------- ---------- ---------- ---------- ---------- ----------
    update(ListOfNodeId, screen, bg, lineList, nodeList, startPos, listOfNodesToPass, length, error)

path_update()
main_loop()
