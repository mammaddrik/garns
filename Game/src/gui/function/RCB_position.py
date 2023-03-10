#::::: Cell Selection ::::::
def get_RCB_pos(x,y) -> set:
    "Cell selection function."
    pos = set()
    for i in range(9):
        pos.add((x,i))
    for i in range(9):
        pos.add((i,y))
    box_x = x // 3
    box_y = y // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            pos.add((j,i))
    return pos