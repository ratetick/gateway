import numpy as np

from pylatex import (
    Document,
    Section,
    Subsection,
    Tabular,
    Math,
    TikZ,
    Axis,
    Plot,
    Figure,
    Matrix,
    Alignat,
    NoEscape,
    Command,
    MultiColumn,
    MultiRow,
    Math,
)


# region functions
def get_header():
    doc.append(NoEscape(r"\vspace*{.5cm} "))

    doc.append(Command("centering"))

    doc.append(Command("begin", "tikzpicture"))


def print_latex(doc, V, H, stx, sty):
    zipset = zip(H, V)
    stx = round(stx, 3)
    sty = round(sty, 3)
    str = f"\draw[very thick] {stx,sty}"
    for x, y in zipset:
        sty += y
        sty = round(sty, 3)
        str += f"--{stx,sty}"
        stx += x
        stx = round(stx, 3)
        str += f"--{stx,sty}"

    str += ";\n"
    doc.append(NoEscape(str))

 
def draw_perimeter():
    cur_vector = draw_vector_vector(
        doc, 0, 0, 0, -(S[9] + S[1] + S[13] - S[4] + 2 * w[1] + w[4])
    )
    cur_vector = draw_vector_vector(doc, *cur_vector, w[4], 0)
    cur_vector = draw_vector_vector(doc, *cur_vector, 0, S[13] - S[4] - w[3] + w[4])
    cur_vector = draw_vector_vector(
        doc, *cur_vector, S[3] + w[1] - w[3] + w[3] - w[4], 0
    )
    cur_vector = draw_vector_vector(doc, *cur_vector, 0, -(S[13] - S[4] - w[3] + w[4]))
    cur_vector = draw_vector_vector(doc, *cur_vector, w[3] + S[14] + w[4], 0)
    cur_vector = draw_vector_vector(
        doc, *cur_vector, 0, S[9] + S[1] + S[13] - S[4] + 2 * w[1] + w[4]
    )
    cur_vector = draw_vector_vector(
        doc,
        *cur_vector,
        -(S[3] + w[1] - w[3] + w[2] - w[4] + w[5] + w[3] + S[14] + w[4]),
        0,
    )


def draw_balcony():
        cur_vector= draw_vector_vector(doc,w[4] + S[8] + w[1] + w[3] + S[11] + w[4] + S[20],0,0,-S[21] * 8 / 9)
        cur_vector= draw_vector_vector(doc, *cur_vector,S[3]+ w[1]+ w[2]+ w[5]+ S[14]
                - (w[4] + S[8] + w[1] + w[3] + S[11] + w[4] + S[20]),0)



def draw_hallway_stay(lcolor='black'):
    cur_vector= draw_vector_vector(doc, w[4],-S[9]-2*w[1],0,-S[1] + S[2],lcolor)
    cur_vector= draw_vector_vector(doc, *cur_vector,-w[1],0,lcolor)
    cur_vector= draw_vector_vector(doc, *cur_vector,0,-S[2],lcolor)
    cur_vector= draw_vector_vector(doc, *cur_vector,S[3],0,lcolor)
    cur_vector= draw_vector_vector(doc, *cur_vector,0,S[4],lcolor)
    
    return cur_vector
def draw_hallway_go(cur_vector,lcolor='black'):
    cur_vector= draw_vector_vector(doc, *cur_vector,-S[16]+S[15],0,lcolor)
    cur_vector= draw_vector_vector(doc, *cur_vector,0,S[5]+2*w[1],lcolor)
    return cur_vector
def draw_hallway_stay1(cur_vector,lcolor='black'):
    cur_vector= draw_vector_vector(doc, *cur_vector,S[6],0,lcolor)
    return cur_vector
def draw_hallway_go1(cur_vector,lcolor='black'):
    cur_vector= draw_vector_vector(doc, *cur_vector,0,S[12],lcolor)
    cur_vector= draw_vector_vector(doc, *cur_vector,-S[7],0,lcolor)
    return cur_vector
def draw_hallway():
    cur_vector=draw_hallway_stay()
    cur_vector=draw_hallway_go(cur_vector)
    cur_vector=draw_hallway_stay1(cur_vector)
    cur_vector=draw_hallway_go1(cur_vector)

def draw_hallway_removed():
    cur_vector=draw_hallway_stay()
    cur_vector=draw_hallway_go(cur_vector,'red')
    cur_vector=draw_hallway_stay1(cur_vector)
    cur_vector=draw_hallway_go1(cur_vector,'red')

def draw_hallway_new():
    cur_vector=draw_hallway_stay()
    cur_vector=draw_hallway_go(cur_vector,'white')
    cur_vector=draw_hallway_stay1(cur_vector)
    



def draw_bathroom_stay(lcolor='black'):
    cur_vector= draw_vector_vector(doc, w[4],-w[1], 0,-S[9],lcolor)
    cur_vector= draw_vector_vector(doc,w[4],-w[1], S[8],0,lcolor)
    return cur_vector

def draw_bathroom_go(lcolor='black'):
    cur_vector= draw_vector_vector(doc, w[4],-w[1]-S[9], S[8],0,lcolor)
    cur_vector= draw_vector_vector(doc, *cur_vector, 0,S[9],lcolor)

def draw_bathroom():
    draw_bathroom_stay()
    draw_bathroom_go()
def draw_bathroom_removed():
    draw_bathroom_stay()
    draw_bathroom_go('red')

def draw_toiletroom_stay(cur_vector,lcolor='black'):
    cur_vector= draw_vector_vector(doc, *cur_vector, 0,S[10],lcolor)
    cur_vector= draw_vector_vector(doc, *cur_vector, -S[11],0,lcolor)
    
def draw_toiletroom_go(lcolor='black'):
    cur_vector= draw_vector_vector(doc, w[4] + S[8] + w[1],-w[1] - S[9] + S[10],0,-S[10],lcolor)
    cur_vector= draw_vector_vector(doc, *cur_vector, S[11],0,lcolor)
    return cur_vector
def draw_toiletroom():
    cur_vector=draw_toiletroom_go()
    draw_toiletroom_stay(cur_vector)
     
def draw_toiletroom_removed():
    cur_vector=draw_toiletroom_go('red')
    draw_toiletroom_stay(cur_vector)
    
def draw_kitchen_stay1(lcolor='black'):
    cur_vector= draw_vector_vector(doc,w[4] + S[8] + w[1] + w[3] + S[11],-w[1],0,-S[18]/3,lcolor)
    cur_vector= draw_vector_vector(doc,*cur_vector,-w[2],0,lcolor)
    cur_vector= draw_vector_vector(doc,*cur_vector,0,-S[18]/6,lcolor)
    cur_vector= draw_vector_vector(doc,*cur_vector,w[2],0,lcolor)
    cur_vector= draw_vector_vector(doc,*cur_vector,0,A[1][1]+S[18]/2+w[1],lcolor)
    return cur_vector
    
def draw_kitchen_go(cur_vector,lcolor='black'):
    cur_vector= draw_vector_vector(doc,*cur_vector,0,-A[1][1]-S[18]-w[1],lcolor)
    return cur_vector

def draw_kitchen_stay2(cur_vector,lcolor='black'):
    cur_vector= draw_vector_vector(doc,*cur_vector,S[19],0,lcolor)
    cur_vector= draw_vector_vector(doc,*cur_vector,0,S[18],lcolor)
    cur_vector= draw_vector_vector(doc,*cur_vector,-S[19],0,lcolor)

def draw_kitchen_buildwall(cur_vector,lcolor='black'):

    cur_vector= draw_vector_vector(doc,*cur_vector,-w[2],0,lcolor)
    cur_vector= draw_vector_vector(doc,*cur_vector,0,-S[12]-w[1],lcolor)
    cur_vector= draw_vector_vector(doc,*cur_vector,w[2],0,lcolor)
    return cur_vector

def draw_kitchen():
    cur_vector=draw_kitchen_stay1()
    cur_vector=draw_kitchen_go(cur_vector)
    draw_kitchen_stay2(cur_vector)

def draw_kitchen_removed():
    cur_vector=draw_kitchen_stay1()
    cur_vector=draw_kitchen_go(cur_vector,'red')
    draw_kitchen_stay2(cur_vector)

def draw_kitchen_new(lcolor='black'):
    cur_vector=draw_kitchen_stay1()
    cur_vector=draw_kitchen_buildwall(cur_vector,lcolor)
    draw_kitchen_stay2(cur_vector)

def draw_livingroom_go(lcolor='black'):
    cur_vector= draw_vector_vector(doc,w[4]+S[24]+w[1],-3*w[1]-S[12]-S[9],0,-S[5],lcolor)
    return cur_vector

def draw_livingroom_stay(cur_vector,lcolor='black'):
    cur_vector= draw_vector_vector(doc,*cur_vector,S[16],0,lcolor)
    cur_vector= draw_vector_vector(doc,*cur_vector,0,S[22],lcolor)
    cur_vector= draw_vector_vector(doc,*cur_vector,-(S[16]-S[17]),0,lcolor)
    cur_vector= draw_vector_vector(doc,*cur_vector,0,S[5]-S[22],lcolor)
    cur_vector= draw_vector_vector(doc,*cur_vector,-S[17],0,lcolor)
    
def draw_livingroom():
    cur_vector=draw_livingroom_go()
    draw_livingroom_stay(cur_vector)

def draw_livingroom_removed():
    cur_vector=draw_livingroom_go('red')
    draw_livingroom_stay(cur_vector)

def draw_bedroom():
    cur_vector= draw_vector_vector(doc,w[3] + S[3] + w[1],-4 * w[1] - S[5] - S[12] - S[9],0,-S[13])
    cur_vector= draw_vector_vector(doc,*cur_vector,S[14],0)
    cur_vector= draw_vector_vector(doc,*cur_vector,0,S[23])
    cur_vector= draw_vector_vector(doc,*cur_vector,-S[15],0)
    

def draw_hallway_new(lcolor='black'):
        cur_vector= draw_vector_vector(doc,w[4],-3*w[1]-S[12]-S[9],S[24]+w[1],0,lcolor)
        cur_vector= draw_vector_vector(doc,w[4],-3*w[1]-S[12]-S[9],0,-S[1]+S[12]+S[2]+w[1])
        cur_vector= draw_vector_vector(doc,*cur_vector,-w[1],0)
        cur_vector= draw_vector_vector(doc,*cur_vector,0,-S[2])
        cur_vector= draw_vector_vector(doc,*cur_vector,S[3],0)
        cur_vector= draw_vector_vector(doc,*cur_vector,0,S[4]+w[1])

     
def draw_bathroom_new(lcolor='black'):
        cur_vector=draw_bathroom_stay()
        cur_vector= draw_vector_vector(doc,*cur_vector,0,-S[9] + S[10])
        cur_vector= draw_vector_vector(doc,*cur_vector,S[11]+w[1],0)
        cur_vector= draw_vector_vector(doc,*cur_vector,0,-S[10])
        cur_vector= draw_vector_vector(doc,*cur_vector,0,-S[12]-w[1],lcolor)
        cur_vector= draw_vector_vector(doc,*cur_vector,-S[6]+w[2],0)
        cur_vector= draw_vector_vector(doc,*cur_vector,-S[24],0,lcolor)
        cur_vector= draw_vector_vector(doc,*cur_vector,0,S[12]+w[1])

    
def draw_vector(doc, x_start, y_start, x_end, y_end, lcolor="black"):
    x_start = round(x_start, 3)
    y_start = round(y_start, 3)
    x_end = round(x_end, 3)
    y_end = round(y_end, 3)

    vector_to_draw = (
        f"\draw[very thick][color={lcolor}]"
        + f"({x_start},{y_start})--({x_end},{y_end});"
    )
    doc.append(NoEscape(vector_to_draw))
    return [x_end, y_end]

def draw_windows():
    print_window(
        doc, w[4] + S[8] + w[1] + w[3] + S[11] + S[20], -w[1] - S[21] / 2 + w[6] / 2
    )  # kitchen

    print_window(
        doc, w[4] + S[16] + w[1] + S[24], -2 * w[1] - S[21] - S[5] / 2 + w[6] / 2
    )  # living

    print_window(
        doc,
        w[4] + S[16] + w[1] + S[24],
        -3 * w[1] - S[21] - S[5] - S[23] / 2 + w[6] / 2,
    )  # bed


def draw_vector_vector(doc, x_start, y_start, x, y, lcolor="black"):
    x_start = round(x_start, 3)
    y_start = round(y_start, 3)
    x = round(x, 3)
    y = round(y, 3)

    vector_to_draw = (
        f"\draw[very thick][color={lcolor}]"
        + f"({x_start},{y_start})--({x_start+x},{y_start+y});"
    )
    doc.append(NoEscape(vector_to_draw))
    return [x_start + x, y_start + y]


def draw_line(x_start, y_start, length):
    return (
        r"\draw[very thick] " + f"({x_start},{y_start})--({x_start+length},{y_start});"
    )


def draw_tar(x_start, y_start, length, width):
    return (
        r"\filldraw "
        + f"({x_start},{y_start}) rectangle({x_start+length},{y_start-width});"
    )


def draw_tile(x_start, y_start, length, width, density):
    ret = draw_line(x_start, y_start, length)
    # ret = r"\draw " + f"({x_start},{y_start})--({x_start+length},{y_start});"
    rt = length / (density)
    for i in range(density + 1):
        ret += (
            r"\draw " + f"({x_start+i*rt},{y_start})--({x_start+i*rt},{y_start-width});"
        )
    return ret


def draw_cement(x_start, y_start, length, width, density_width, density_length):
    ret = r"\draw " + f"({x_start},{y_start})--({x_start+length},{y_start});"
    rt_len = length / density_length
    rt_width = width / (density_width + 1)
    for j in range(density_width):
        for i in range(density_length):
            ret += (
                r"\filldraw "
                + f"({x_start+i*rt_len+((j+1)%2)*rt_len/2},{y_start-(j+1)*rt_width}) circle(1pt);"
            )
    return ret


def draw_concrete(x_start, y_start, length, density):
    ret = r"\draw " + f"({x_start},{y_start})--({x_start+length},{y_start});"
    rt = length / density
    for i in range(density):
        ret += (
            r"\draw "
            + f"({x_start+(i+1)*rt},{y_start})--({x_start+i*rt},{y_start-rt});"
        )
    return ret


def draw_shumanet(x_start, y_start, length, width, density):
    ret = r"\draw " + f"({x_start},{y_start})--({x_start+length},{y_start});"
    rt = width / (density + 1)
    for i in range(density):
        ret += (
            r"\draw[thick] "
            + f"({x_start},{y_start-rt*(i+1)})--({x_start+length},{y_start-rt*(i+1)});"
        )
    return ret


def print_list(doc, plist, stx, sty, lcolor="black"):
    stx = round(stx, 3)
    sty = round(sty, 3)
    str = f"\draw[very thick][color={lcolor}] {stx,sty}"
    for r in plist:
        sty += r[0]
        sty = round(sty, 3)
        str += f"--{stx,sty}"
        stx += r[1]
        stx = round(stx, 3)
        str += f"--{stx,sty}"

    str += ";\n"
    doc.append(NoEscape(str))

    #     |



def north_south_door(doc, x, y, wall, size, lcolor="black"):  #  |  |   |
    #     |
    v = 0.7 * size / 2
    h = wall / 2
    s = size / 2
    #    (x,y) is the center
    #
    doc.append(
        NoEscape(
            f"\draw[very thick][color={lcolor}] {round(x,3),round(y-v,3)}--{round(x,3),round(y+v,3)};"
        )
    )
    doc.append(
        NoEscape(
            f"\draw[very thick][color={lcolor}] {round(x-s,3),round(y-h,3)}--{round(x-s,3),round(y+h,3)};"
        )
    )
    doc.append(
        NoEscape(
            f"\draw[very thick][color={lcolor}] {round(x+s,3),round(y-h,3)}--{round(x+s,3),round(y+h,3)};"
        )
    )


def west_east_door(doc, x, y, wall, size, lcolor="black"):
    v = 0.7 * size / 2
    h = wall / 2
    s = size / 2
    doc.append(
        NoEscape(
            f"\draw[very thick][color={lcolor}] {round(x-v,3),round(y,3)}--{round(x+v,3),round(y,3)};"
        )
    )
    doc.append(
        NoEscape(
            f"\draw[very thick][color={lcolor}] {round(x-h,3),round(y-s,3)}--{round(x+h,3),round(y-s,3)};"
        )
    )
    doc.append(
        NoEscape(
            f"\draw[very thick][color={lcolor}] {round(x+h,3),round(y+s,3)}--{round(x-h,3),round(y+s,3)};"
        )
    )


def shower(doc, x, y, width, length,lcolor='black'):
    doc.append(
        NoEscape(
            f"\draw[very thick][color={lcolor}]({round(x,3)},{round(y,3)}) rectangle ({round(x+length,3)},{round(y-width,3)}) ;"
        )
    )
    doc.append(
        NoEscape(
            f"\draw[very thick][color={lcolor}]({round(x+.2*length,3)},{round(y-.2*width,3)}) circle (2pt);"
        )
    )


def faucet(doc, x, y, width, length):
    doc.append(
        NoEscape(
            f"\draw[very thick]{round(x,3),round(y-length,3)}--{round(x,3),round(y,3)}--{round(x+width,3),round(y,3)}--{round(x+width,3),round(y-length,3)}--{round(x,3),round(y-length,3)};"
        )
    )
    doc.append(
        NoEscape(
            f"\draw[very thick]{round(x+width/2,3),round(y,3)}--{round(x+width/2,3),round(y-length/2,3)}--{round(x+width/3,3),round(y-length/2,3)};"
        )
    )


def cooktop(doc, x, y, width, length):
    doc.append(
        NoEscape(
            f"\draw[very thick]{round(x,3),round(y-length,3)}--{round(x,3),round(y,3)}--{round(x+width,3),round(y,3)}--{round(x+width,3),round(y-length,3)}--{round(x,3),round(y-length,3)};"
        )
    )


def toilet(doc, x, y, width, length):
    doc.append(
        NoEscape(
            f"\draw[very thick]{round(x,3),round(y-length,3)}--{round(x,3),round(y,3)}--{round(x+width,3),round(y,3)}--{round(x+width,3),round(y-length,3)};"
        )
    )
    doc.append(
        NoEscape(
            f"\draw[very thick]{round(x,3),round(y-length/3,3)}--{round(x+width,3),round(y-length/3,3)};"
        )
    )
    doc.append(
        NoEscape(
            f"\draw[very thick] {round(x,3),round(y-length,3)} arc ({round(180,3)}:{round(360,3)}:{round(width/2,3)});"
        )
    )
    doc.append(
        NoEscape(
            f"\draw[very thick] {round(x+width/2,3),round(y-length,3)} circle (0.05);"
        )
    )


def bathtab(doc, x, y, width, length,lcolor):
    doc.append(
        NoEscape(
            f"\draw[very thick][color={lcolor}]{round(x,3),round(y-length,3)}--{round(x,3),round(y,3)}--{round(x+width,3),round(y,3)}--{round(x+width,3),round(y-length,3)};"
        )
    )

    doc.append(
        NoEscape(
            f"\draw[very thick][color={lcolor}] {round(x,3),round(y-length,3)} arc ({round(180,3)}:{round(360,3)}:{round(width/2,3)});"
        )
    )

    doc.append(
        NoEscape(
            f"\draw[very thick,fill=black][color={lcolor}] {round(x+width/2,3),round(y-length/4,3)} circle (0.05);"
        )
    )


def fixtures_stay():
    faucet(doc, S[8]*2/3 + w[4], -1.5 * w[1], 0.6, 0.6)
    faucet(doc, S[13] + S[20] / 4 + w[4], -1.5 * w[1], 0.6, 0.6)
    toilet(doc, S[8] + S[11] / 3 + w[4] + w[1], -w[1] - S[9] + S[10], 0.55, 0.65)
    cooktop(doc, S[13] + S[20] * 2 / 3 + w[4], -1.5 * w[1], 0.6, 0.6)

def fixtures_go(lcolor='black'):
    bathtab(doc, w[4] + w[1], -2 * w[1], 0.9, 1.5,lcolor)
def fixtures_new(lcolor='black'):
    bathtab(doc, w[4] + w[1], -2 * w[1]-S[12], 0.9, 1.5,lcolor)
    shower(doc,w[4] + w[1],-2*w[1], 1.1,1.1,lcolor)

def doors_new(lcolor='black'):
    north_south_door(
        doc,
        w[4] + S[8] + w[1] + w[3] + S[11] + S[20] / 3,
        -w[1] - 0.5 * w[1] - S[21],
        w[1],
        0.7,
        lcolor,
    )  # kitchen door

    north_south_door(
        doc,
        w[4] + 3/4*S[8] ,
        -w[1] - 0.5 * w[1] - S[21],
        w[1],
        0.7,
        lcolor,
    ) #bathroom door    

def doors_stay():
    north_south_door(
        doc, w[4] + S[24] + S[14] / 3 + w[1], -5 * w[1] / 2 - S[5] - S[21], w[1], 0.7
    )  # bedroom door

    north_south_door(
        doc, w[4] + S[24] / 2, -2 * w[1] - S[1] - S[9] - w[3] / 2, w[3], 0.8
    )  # entrance door

def doors_removed(lcolor='black'):

    north_south_door(
        doc, w[4] + 2 * S[8] / 3, -3 * w[1] / 2 - S[9], w[1], 0.5,lcolor
    )  # bathroom door
    north_south_door(
        doc, w[4] + S[8] + w[1] + S[11] / 2, -3 * w[1] / 2 - S[9], w[1], 0.5,lcolor
    )  # toilet door
    west_east_door(
        doc, w[4] + S[24] + w[1] / 2, -3 * w[1] - S[9] - S[12] - S[5] / 2, w[1], 0.7,lcolor
    )  # living room door
    west_east_door(
        doc, w[4] + S[7] + w[1] / 2, -2 * w[1] - S[9] - S[12] / 2, w[1], 0.7,lcolor
    )  # kitchen door
    ##################################################



def draw_end_line(doc, x, y, len):
    doc.append(
        NoEscape(
            f"\draw[line width=.1pt]{round(x-2*len,3),round(y-2*len,3)}--{round(x+2*len,3),round(y+2*len,3)};"
        )
    )


def measurements(
    doc,
    orientation: bool,
    x: float,
    y: float,
    dist: float,
    offset: float,
    dist_number: float,
):
    M = 0.15
    if orientation == "hor_top":
        doc.append(
            NoEscape(
                f"\draw[line width=.1pt]{round(x,3),round(y-offset,3)}--{round(x,3),round(y,3)};"
            )
        )
        doc.append(
            NoEscape(
                f"\draw[line width=.1pt]{round(x+dist,3),round(y-offset,3)}--{round(x+dist,3),round(y,3)};"
            )
        )
        doc.append(
            NoEscape(
                f"\draw[line width=.1pt]{round(x,3),round(y-offset-M,3)}--{round(x+dist,3),round(y-offset-M,3)};"
            )
        )

        doc.append(
            NoEscape(
                rf"\node[anchor=center,font=\large] at ({x+dist/2},{y-offset+2*M})"
                + "{"
                + f"{dist_number}"
                + "};"
            )
        )
        draw_end_line(doc, x, y - offset - M, M)
        draw_end_line(doc, x + dist, y - offset - M, M)
        # doc.append(
        #    NoEscape(
        #        f"\draw[line width=.1pt]{round(x-2*M,3),round(y-offset-M-2*M,3)}--{round(x+2*M,3),round(y-offset-M+2*M,3)};"
        #    )
        # )
        # doc.append(
        #    NoEscape(
        #        f"\draw[line width=.1pt]{round(x+dist-2*M,3),round(y-offset-M-2*M,3)}--{round(x+dist+2*M,3),round(y-offset-M+2*M,3)};"
        #    )
        # )
    elif orientation == "vert_right":
        doc.append(
            NoEscape(
                f"\draw[line width=.1pt]{round(x,3),round(y,3)}--{round(x+offset,3),round(y,3)};"
            )
        )
        doc.append(
            NoEscape(
                f"\draw[line width=.1pt]{round(x,3),round(y-dist,3)}--{round(x+offset,3),round(y-dist,3)};"
            )
        )
        doc.append(
            NoEscape(
                f"\draw{round(x+offset-M,3),round(y,3)}--{round(x+offset-M,3),round(y-dist,3)};"
            )
        )
        doc.append(
            NoEscape(
                rf"\node[anchor=center,font=\large,rotate=90] at ({x+offset-4*M},{y-dist/2})"
                + "{"
                + f"{dist_number}"
                + "};"
            )
        )
        draw_end_line(doc, x - M + offset, y, M)
        draw_end_line(doc, x - M + offset, y - dist, M)
    elif orientation == "vert_left":
        doc.append(
            NoEscape(
                f"\draw[line width=.1pt]{round(x,3),round(y,3)}--{round(x-offset,3),round(y,3)};"
            )
        )
        doc.append(
            NoEscape(
                f"\draw[line width=.1pt]{round(x,3),round(y-dist,3)}--{round(x-offset,3),round(y-dist,3)};"
            )
        )
        doc.append(
            NoEscape(
                f"\draw{round(x-offset+M,3),round(y,3)}--{round(x-offset+M,3),round(y-dist,3)};"
            )
        )
        doc.append(
            NoEscape(
                rf"\node[anchor=center,font=\large,rotate=90] at ({x-offset-4*M},{y-dist/2})"
                + "{"
                + f"{dist_number}"
                + "};"
            )
        )
        draw_end_line(doc, x + M - offset, y, M)
        draw_end_line(doc, x + M - offset, y - dist, M)
        # doc.append(
        #    NoEscape(
        #        f"\draw[line width=.1pt]{round(x-2*M-M+offset,3),round(y-2*M,3)}--{round(x+offset-M+2*M,3),round(y+2*M,3)};"
        #    )
        # )
        # doc.append(
        #    NoEscape(
        #        f"\draw[line width=.1pt]{round(x+offset-2*M-M,3),round(y-dist-2*M,3)}--{round(x+offset-M+2*M,3),round(y-dist+2*M,3)};"
        #    )
        # )


def print_window(doc, stx, sty):
    stx = round(stx, 3)
    sty = round(sty, 3)
    doc.append(NoEscape(f"\draw[very thick] {stx,sty}"))
    stx1 = stx + w[4]
    stx1 = round(stx1, 3)
    doc.append(NoEscape(f"--{stx1,sty};"))
    sty1 = sty - w[6]
    sty1 = round(sty1, 3)
    doc.append(NoEscape(f"\draw[very thick] {stx,sty1}"))
    doc.append(NoEscape(f"--{stx1,sty1};"))
    stx2 = stx + w[4] / 2 - w[1] / 2
    stx3 = stx + w[4] / 2 + w[1] / 2
    stx2 = round(stx2, 3)
    stx3 = round(stx3, 3)
    doc.append(NoEscape(f"\draw[very thick] {stx2,sty}--{stx2,sty1};"))
    doc.append(NoEscape(f"\draw[very thick] {stx3,sty}--{stx3,sty1};"))


# endregion

# region values
scale = 1.3

S = [
    0,  # 0
    6.33,  # 1
    1.28,  # 2
    1.57,  # 3
    1.53,  # 4
    3.48,  # 5
    2.07,  # 6
    3.18,  # 7
    1.92,  # 8
    1.81,  # 9
    1.58,  # 10
    0.89,  # 11
    1.03,  # 12
    3.18,  # 13
    4.78,  # 14
    4.78,  # 15
    5.06,  # 16
    4.27,  # 17
    3.01,  # 18
    2.13,  # 19
    2.13,  # 20
    3.01,  # 21
    3.36,  # 22
    3.16,  # 23
    1.16,  # 24
    0.8,  # 25 door size not on original plan
    1,  # 26 bathroom wall size
    0,  # 27 bathroom coordinate
    0,  # 28 bathroom angle wall
]
w = [0, 0.17, 0.253, 0.4, 0.5, 0.6, 1.5, 0.07]
# angle wall calculations
sin_alpha = S[25] / (S[24] - w[2] + S[6] - S[26])
cos_alpha = np.cos(np.arcsin(sin_alpha))
S[28] = (S[24] - w[2] + S[6] - S[26]) / cos_alpha
S[27] = S[25] / cos_alpha  # angle wall down distance

S = [i * scale for i in S]


#    0     1    2     3    4   5    6
w = [i * scale for i in w]
A = [
    [
        w[4] + S[24] + S[6],
        -w[1] - S[9] - w[1] - S[12],  # south east coner hollway
    ],
    [w[4] + S[8] + w[1] + S[11], -w[1] - S[9]],  # south east coner bathroom
]


TotalPages = 7
PageCount = 0

# endregion


# region stamp
def create_stamp(Title, PageNo, NumPages, Stage):
    with doc.create(
        Tabular(
            "|p{.8cm}|p{.8cm}|p{.8cm}|p{.8cm}|p{1.3cm}|p{.8cm}|p{6cm}|p{1.3cm}|p{1.3cm}|p{1.3cm}|",
            row_height=1.5,
        )
    ) as table:
        table.add_hline()
        table.add_row(
            (
                "",
                "",
                "",
                "",
                "",
                "",
                MultiColumn(
                    size=4,
                    align="|c|",
                    data=MultiRow(size=3, data="Заказчик: Собственник помещений"),
                ),
            )
        )
        table.add_hline(1, 6)
        table.add_row(
            (
                "",
                "",
                "",
                "",
                " ",
                "",
                MultiColumn(size=4, align="|c|", data=""),
            )
        )
        table.add_hline(1, 6)
        table.add_row(
            (
                "",
                "",
                "",
                "",
                "",
                "",
                MultiColumn(size=4, align="|c|", data=""),
            )
        )
        table.add_hline()

        table.add_row(
            (
                "",
                "",
                "",
                "",
                "",
                "",
                MultiColumn(
                    size=4,
                    align="|c|",
                    data=MultiRow(
                        size=3, data="Адрес: г. Москва пр-т. Мира д. 122 кв. 166"
                    ),
                ),
            )
        )
        table.add_hline(1, 6)

        table.add_row(
            ("", "", "", "", " ", "", MultiColumn(size=4, align="|c|", data=""))
        )
        table.add_hline(1, 6)
        table.add_row(
            (
                "Изм.",
                "Кол.",
                "Лист",
                "Nдок.",
                "Подпись",
                "Дата",
                MultiColumn(size=4, align="|c|", data=""),
            )
        )
        table.add_hline()
        table.add_row(
            (
                MultiColumn(size=2, align="|c|", data="Разраб."),
                MultiColumn(size=2, align="|c|", data=""),
                "",
                "",
                MultiRow(
                    size=3,
                    data=NoEscape(
                        r"\parbox{4.5cm}{Проект перепланировки и переустройства}"
                    ),
                ),
                "Стадия",
                "Лист",
                "Листов",
            )
        )

        table.add_hline(1, 6)
        table.add_hline(8, 10)
        table.add_row(
            (
                MultiColumn(size=2, align="|c|", data="Пров."),
                MultiColumn(size=2, align="|c|", data=""),
                "",
                "",
                "",
                MultiRow(
                    size=2,
                    data=NoEscape(r"\parbox{2cm}{Stage}"),
                ),
                MultiRow(
                    size=2,
                    data=NoEscape(r"\parbox{2cm}" + f"{PageNo}"),
                ),
                MultiRow(
                    size=2,
                    data=NoEscape(r"\parbox{2cm}" + f"{NumPages}"),
                ),
            )
        )
        table.add_hline(1, 6)
        table.add_row(
            (
                MultiColumn(size=2, align="|c|", data="ГАП"),
                MultiColumn(size=2, align="|c|", data=""),
                "",
                "",
                "",
                "",
                "",
                "",
            )
        )
        table.add_hline()
        table.add_row(
            (
                MultiColumn(size=2, align="|c|", data="ГИП"),
                MultiColumn(size=2, align="|c|", data=""),
                "",
                "",
                MultiRow(
                    size=3,
                    data=NoEscape(r"\parbox{5.5cm}{" + f"{Title}" + "}"),
                ),
                MultiColumn(size=3, align="|c|", data=""),
            ),
        )

        table.add_hline(1, 6)
        table.add_row(
            (
                MultiColumn(size=2, align="|c|", data=""),
                MultiColumn(size=2, align="|c|", data=""),
                "",
                "",
                "",
                MultiColumn(size=3, align="|c|", data=""),
            )
        )
        table.add_hline(1, 6)
        table.add_row(
            (
                MultiColumn(size=2, align="|c|", data=""),
                MultiColumn(size=2, align="|c|", data=""),
                "",
                "",
                "",
                MultiColumn(size=3, align="|c|", data=""),
            )
        )
        table.add_hline()


# endregion

if __name__ == "__main__":
    geometry_options = {
        "tmargin": "1.5cm",
        "lmargin": ".5cm",
        "bmargin": "1.2cm",
        "rmargin": ".6cm",
    }

    doc = Document(
        geometry_options=geometry_options,
        page_numbers=False,
    )
    doc.preamble.append(Command("usepackage", "tikz"))
    doc.preamble.append(Command("usepackage", "background"))
    doc.preamble.append(Command("usetikzlibrary", "calc"))

    # doc.preamble.append(NoEscape("%Enable Source Line Numbers\n"))
    # doc.preamble.append(NoEscape("%\\usepackage{lineno}\n"))
    # doc.preamble.append(NoEscape("%\\linenumbers\n"))

    doc.preamble.append(Command("usepackage", options="russian", arguments="babel"))
    background_setup = r"angle = 0,scale = 1,vshift = -2ex,contents = {\tikz[overlay, remember picture]\draw [line width = .8pt,color = black, double = blue!10]($(current page.north west)+(1cm,-1cm)$)rectangle ($(current page.south east)+(-1,1)$);}"
    background_noescape = f"\\backgroundsetup{{{background_setup}}}"
    doc.preamble.append(NoEscape(background_noescape))

    # region page 0 content
    doc.append(NoEscape(r"\vspace*{1cm} "))
    doc.append(Command("centering "))

    with doc.create(Tabular("|p{3.1cm}|p{12.05cm}|p{3.1cm}|", row_height=3)) as table:
        table.add_hline()
        table.add_row(
            (MultiColumn(size=3, align="|c|", data="Ведомость рабочих чертежей"),)
        )
        table.add_hline()
        table.add_row("№", "Наименованние", "Прим.")
        table.add_hline()
        table.add_row("1", "Схема расположения объекта в г. Москва", "")
        table.add_hline()
        table.add_row("2", "План помещений квартиры до перепланировки", "")
        table.add_hline()
        table.add_row(
            "3",
            "План демонтажа оборудования и строительных конструкций в помещениях квартиры",
            "",
        )
        table.add_hline()
        table.add_row(
            "4",
            "План возводимого оборудования и строительных конструкций в помещениях квартиры",
            "",
        )
        table.add_hline()
        table.add_row("5", "План помещения квартиры после перепланировки", "")
        table.add_hline()
        table.add_row("6", "Экспикация полов в помещениях квартиры", "")
        table.add_hline()
        table.add_row("7", "", "")
        table.add_hline()
    doc.append(NoEscape(r"\vfill"))

    PageCount += 1
    create_stamp("Ведомость рабочих чертежей", PageCount, TotalPages, "")

    doc.append(NoEscape("\pagebreak"))

    # endregion
    # region page 1 content
    doc.append(NoEscape(r"\vspace*{.5cm} "))
    doc.append(Command("centering "))
    doc.append(NoEscape(r"\section*{\bf Схема расположения объекта в г. Москва}"))
    doc.append(NoEscape(r"\vspace*{.2cm} "))

    with doc.create(Figure(position="htbp")) as fig:
        fig.add_image("122166map.jpg", width=NoEscape(r".6\linewidth"))
        # fig.add_caption("Your Image Caption")
    doc.append(NoEscape(r"\vfill"))

    PageCount += 1
    create_stamp("Схема расположения объекта в г. Москва", PageCount, TotalPages, "")

    doc.append(NoEscape("\pagebreak"))

    # endregion
    # region page 2 original plan

    get_header()
    draw_perimeter()

    measurements(
        doc,
        "hor_top",
        0,
        0,
        S[3] + w[1] - w[3] + w[2] - w[4] + w[5] + w[3] + S[14] + w[4],
        -1.2,
        -round(
            -(S[3] + w[1] - w[3] + w[2] - w[4] + w[5] + w[3] + S[14] + w[4]) / scale,
            2,
        ),
    )

    #measurements(
    #    doc,
    #    "vert_right",
    #)
    measurements(
        doc,
        "vert_left",
        0,
        0,
        S[9] + S[1] + S[13] - S[4] + 2 * w[1] + w[4],
        1.2,
        round(S[9] + S[1] + S[13] - S[4] + 2 * w[1] + w[4] / scale, 2),
    )
    ###########################################################

    draw_hallway()
    draw_bathroom()
    draw_toiletroom()
    draw_kitchen()
    draw_livingroom()
    draw_bedroom()
    draw_balcony() 
    draw_windows()


    ###########################################################
    
    fixtures_stay()
    fixtures_go()
    doors_stay()
    doors_removed()

    doc.append(Command("end", "tikzpicture"))

    doc.append(NoEscape(r"\vfill"))

    PageCount += 1
    create_stamp("План помещений квартиры до перепланировки", PageCount, TotalPages, "")

    doc.append(NoEscape("\pagebreak"))
    # endregion
    # region page 3 removed walls

    get_header()
    draw_perimeter()
    draw_hallway_removed()
    draw_bathroom_removed()     
    draw_toiletroom_removed()
    draw_kitchen_removed()
    draw_livingroom_removed()
    draw_balcony()
    draw_bedroom()
    draw_windows() 
    doors_stay()
    doors_removed('red') 
    fixtures_stay()
    fixtures_go('red')
    
    doc.append(Command("end", "tikzpicture"))

    doc.append(NoEscape(r"\vfill"))
    PageCount += 1
    create_stamp(
        "План демонтажа оборудования и строительных конструкций в помещениях квартиры",
        PageCount,
        TotalPages,
        "",
    )

    doc.append(NoEscape("\pagebreak"))
    # endregion
    
    # region page 4 installed walls
    get_header()
    draw_perimeter()
    draw_hallway_new('green')
    draw_bathroom_new('green')

    draw_kitchen_new('green')    
     
    doors_new()

    lvec=[w[4]+S[24]+w[1],-3*w[1]-S[9]-S[12]-S[5]]
    draw_livingroom_stay(lvec)
    draw_bedroom()
    draw_balcony()
    draw_windows()  
    doors_stay()
    doors_new('green')
    fixtures_stay()
    fixtures_new('green')
    
    doc.append(Command("end", "tikzpicture"))

    doc.append(NoEscape(r"\vfill"))

    PageCount += 1
    create_stamp(
        "План возводимого оборудования и строительных конструкций в помещениях квартиры",
        PageCount,
        TotalPages,
        "",
    )
    doc.append(NoEscape("\pagebreak"))
    # endregion  
    # region page 5 final plan
     
    get_header()
    draw_perimeter()
    draw_hallway_new()
    draw_bathroom_new()
    draw_kitchen_new()
    
    lvec=[w[4]+S[24]+w[1],-3*w[1]-S[9]-S[12]-S[5]]
    draw_livingroom_stay(lvec)
    draw_bedroom()
    draw_balcony()
    draw_windows() 
    fixtures_stay()
    fixtures_new()
    doors_stay()
    doors_new()
    
    doc.append(Command("end", "tikzpicture"))

    doc.append(NoEscape(r"\vfill"))

    PageCount += 1
    create_stamp(
        "План помещения квартиры после перепланировки", PageCount, TotalPages, ""
    )
    doc.append(NoEscape("\pagebreak"))
    # endregion
    # region page 6 Floors structure

    doc.append(NoEscape(r"\vspace*{1cm} "))
    # with doc.create(Section("Экспикация полов в помеще", numbered=False)):
    #    doc.append("")
    doc.append(NoEscape(r"\section*{\bf Экспликация полов в помещении}"))
    doc.append(NoEscape(r"\vspace*{1cm} "))
    doc.append(NoEscape(r"\hyphenation{ар-ми-ро-ван-ная}"))
    with doc.create(
        Tabular("|p{2cm}|p{1.5cm}|p{4.8cm}|p{6.7cm}|p{2cm}|", row_height=2)
    ) as table:
        table.add_hline()
        table.add_row(
            "№ помещ.", "Тип", "Схема пола", "Данные элементов пола", "Площадь,м²"
        )
        table.add_hline()

        table.add_row(
            MultiRow(6, data=" "),
            MultiRow(6, data="I"),
            MultiRow(
                6,
                data=NoEscape(
                    r"\begin{tikzpicture}"
                    + draw_tile(0.2, 0.2, 4.5, 0.2, 5)
                    + draw_cement(0.2, 0, 4.5, 0.8, 3, 20)
                    + draw_tar(0.2, -0.8, 4.5, 0.1)
                    + draw_shumanet(0.2, -0.9, 4.5, 0.1, 2)
                    + draw_concrete(0.2, -1.0, 4.5, 20)
                    + r"\end{tikzpicture}"
                ),
            ),
            MultiRow(
                6,
                data=NoEscape(
                    r"\parbox{6.5cm}{"
                    + r"1. Керамическая плитка $\delta$=15мм"
                    + "\\newline"
                    + r"2. Ценентно-песчанная стяжка, армированная сеткой. $\delta$=50мм"
                    + "\\newline"
                    + r"3. Гидроизоляция - 2 слоя гидроизола на битумноЙ мастике. $\delta$=5мм"
                    + "\\newline"
                    + r"4. Звукоизоляция - Шуманет 100. $\delta$=5мм"
                    + "\\newline"
                    + r"5. Экструдированный пенополистирол. $\delta$=70мм"
                    + "\\newline"
                    + r"6. Существующее ж/б перекрытие."
                    + "}"
                ),
            ),
            MultiRow(6, data="7.0 "),
        )
        table.add_row("", "", "", "", "")
        table.add_row("", "", "", "", "")
        table.add_row("", "", "", "", "")
        table.add_row("", "", "", "", "")
        table.add_row("", "", "", "", "")

        table.add_hline()

        table.add_row(
            MultiRow(6, data=" "),
            MultiRow(6, data="II"),
            MultiRow(
                6,
                data=NoEscape(
                    r"\begin{tikzpicture}"
                    + draw_tile(0.2, 0.2, 4.5, 0.2, 5)
                    + draw_cement(0.2, 0, 4.5, 0.8, 3, 20)
                    + draw_tar(0.2, -0.8, 4.5, 0.1)
                    + draw_shumanet(0.2, -0.9, 4.5, 0.1, 2)
                    + draw_concrete(0.2, -1.0, 4.5, 20)
                    + r"\end{tikzpicture}"
                ),
            ),
            MultiRow(
                6,
                data=NoEscape(
                    r"\parbox{6.5cm}{"
                    + r"1. Керамическая плитка $\delta$=15мм"
                    + "\\newline"
                    + r"2. Ценентно-песчанная стяжка, армированная сеткой. $\delta$=50мм"
                    + "\\newline"
                    + r"3. Гидроизоляция - 2 слоя гидроизола на битумноЙ мастике. $\delta$=5мм"
                    + "\\newline"
                    + r"4. Звукоизоляция - Шуманет 100. $\delta$=5мм"
                    + "\\newline"
                    + r"5. Экструдированный пенополистирол. $\delta$=70мм"
                    + "\\newline"
                    + r"6. Существующее ж/б перекрытие."
                    + "}"
                ),
            ),
            MultiRow(6, data="7.0 "),
        )

        table.add_row("", "", "", "", "")
        table.add_row("", "", "", "", "")
        table.add_row("", "", "", "", "")
        table.add_row("", "", "", "", "")
        table.add_row("", "", "", "", "")
        table.add_hline()
    doc.append(NoEscape(r"\vfill"))
    PageCount += 1
    create_stamp("Экспикация полов в помещениях квартиры", PageCount, TotalPages, "")
    doc.append(NoEscape("\pagebreak"))
# endregion
doc.generate_pdf("app122-166", clean_tex=False)


# Add the background setup using TikZ
