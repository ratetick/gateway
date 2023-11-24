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
)
from pylatex.utils import italic
import os


### functions
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


def north_south_door(doc, x, y, wall, size):
    v = 0.7 * size / 2
    h = wall / 2
    s = size / 2
    doc.append(
        NoEscape(
            f"\draw[very thick] {round(x,3),round(y-v,3)}--{round(x,3),round(y+v,3)};"
        )
    )
    doc.append(
        NoEscape(
            f"\draw[very thick] {round(x-s,3),round(y-h,3)}--{round(x-s,3),round(y+h,3)};"
        )
    )
    doc.append(
        NoEscape(
            f"\draw[very thick] {round(x+s,3),round(y-h,3)}--{round(x+s,3),round(y+h,3)};"
        )
    )


def west_east_door(doc, x, y, wall, size):
    v = 0.7 * size / 2
    h = wall / 2
    s = size / 2
    doc.append(
        NoEscape(
            f"\draw[very thick] {round(x-v,3),round(y,3)}--{round(x+v,3),round(y,3)};"
        )
    )
    doc.append(
        NoEscape(
            f"\draw[very thick] {round(x-h,3),round(y-s,3)}--{round(x+h,3),round(y-s,3)};"
        )
    )
    doc.append(
        NoEscape(
            f"\draw[very thick] {round(x+h,3),round(y+s,3)}--{round(x-h,3),round(y+s,3)};"
        )
    )


def bathtab(doc, x, y, width, length):
    doc.append(
        NoEscape(
            f"\draw[very thick]{round(x,3),round(y-length,3)}--{round(x,3),round(y,3)}--{round(x+width,3),round(y,3)}--{round(x+width,3),round(y-length,3)};"
        )
    )

    doc.append(
        NoEscape(
            f"\draw[very thick] {round(x,3),round(y-length,3)} arc ({round(180,3)}:{round(360,3)}:{round(width/2,3)});"
        )
    )

    doc.append(
        NoEscape(
            f"\draw[very thick,fill=black] {round(x+width/2,3),round(y-length/4,3)} circle (0.05);"
        )
    )


S = [
    0,
    6.33,
    1.28,
    1.57,
    1.53,
    3.48,
    2.07,
    3.18,
    1.92,
    1.81,
    1.58,
    0.89,
    1.03,
    3.16,
    4.78,
    #  0   1    2    3    4    5   6     7    8    9     10   11   12   13   14
    4.78,
    5.06,
    4.27,
    3.01,
    2.13,
    2.13,
    3.01,
    3.36,
    3.16,
    1.16,
    #   15    16   17   18   19   20   21   22   23   24
]
S = [i * 1.3 for i in S]

w = [0, 0.145, 0.3, 0.4, 0.5, 0.6, 1.5]
#    0     1    2     3    4   5    6
w = [i * 1.3 for i in w]


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


if __name__ == "__main__":
    # image_filename = os.path.join(os.path.dirname(__file__), 'kitten.jpg')

    geometry_options = {"tmargin": "4cm", "lmargin": "1cm", "bmargin": "1.2cm"}

    doc = Document(geometry_options=geometry_options, page_numbers=False)
    doc.preamble.append(Command("usepackage", "tikz"))
    doc.preamble.append(Command("usepackage", "background"))
    doc.preamble.append(Command("usetikzlibrary", "calc"))  # \usetikzlibrary{calc}

    background_setup = r"angle = 0,scale = 1,vshift = -2ex,contents = {\tikz[overlay, remember picture]\draw [line width = .8pt,color = black, double = blue!10]($(current page.north west)+(1cm,-1cm)$)rectangle ($(current page.south east)+(-1,1)$);}"
    background_noescape = f"\\backgroundsetup{{{background_setup}}}"
    doc.preamble.append(NoEscape(background_noescape))
    doc.append(Command("begin", "tikzpicture"))
    doc.append(Command("centering"))

    #####################################################################
    # perimeter
    VERT = []
    HOR = []
    VERT.append(-(S[9] + S[1] + S[13] - S[4] + 2 * w[1] + w[4]))
    HOR.append(w[4])
    VERT.append(S[13] - S[4] - w[3] + w[4])
    HOR.append(S[3] + w[1] - w[3] + w[3] - w[4])
    VERT.append(-(S[13] - S[4] - w[3] + w[4]))
    HOR.append(w[3] + S[14] + w[4])
    VERT.append(S[9] + S[1] + S[13] - S[4] + 2 * w[1] + w[4])
    HOR.append(-(S[3] + w[1] - w[3] + w[2] - w[4] + w[5] + w[3] + S[14] + w[4]))
    stx = 0
    sty = 0
    print_latex(doc, VERT, HOR, stx, sty)

    # doc.append(italic("italic text. "))
    # with doc.create(Subsection("Table of something")):
    #    with doc.create(Tabular("rc|cl")) as table:
    #        table.add_hline()
    #        table.add_row((1, 2, 3, 4))
    #        table.add_hline(1, 2)
    #        table.add_empty_row()
    #        table.add_row((4, 5, 6, 7))
    VERT = []
    HOR = []
    VERT.append(-S[1] + S[2])
    HOR.append(-w[1])
    VERT.append(-S[2])
    HOR.append(S[3])
    VERT.append(S[4])
    HOR.append(-S[16] + S[15])
    VERT.append(S[5] + 2 * w[1])
    HOR.append(S[6])
    VERT.append(S[12])
    HOR.append(-S[7])
    stx = w[4]
    sty = -S[9] - 2 * w[1]
    print_latex(doc, VERT, HOR, stx, sty)

    #####################################################
    VERT = []
    HOR = []
    VERT.append(-S[9])
    HOR.append(S[8])
    VERT.append(S[9])
    HOR.append(-S[8])
    stx = w[4]
    sty = -w[1]
    print_latex(doc, VERT, HOR, stx, sty)
    #########################################################
    VERT = []
    HOR = []
    VERT.append(-S[10])
    HOR.append(S[11])
    VERT.append(S[10])
    HOR.append(-S[11])

    stx = w[4] + S[8] + w[1]
    sty = -w[1] - S[9] + S[10]
    print_latex(doc, VERT, HOR, stx, sty)
    ###########################################################
    # kitchen
    VERT = []
    HOR = []
    VERT.append(-S[18] / 3)
    HOR.append(-w[2])
    VERT.append(-S[18] / 6)
    HOR.append(w[2])
    VERT.append(-S[18] / 2)
    HOR.append(S[19])
    VERT.append(S[18])
    HOR.append(-S[19])

    stx = w[4] + S[8] + w[1] + w[3] + S[11]
    sty = -w[1]
    print_latex(doc, VERT, HOR, stx, sty)
    #################################################
    # living room
    VERT = []
    HOR = []
    VERT.append(-S[5])
    HOR.append(S[16])
    VERT.append(S[22])
    HOR.append(-(S[16] - S[17]))
    VERT.append(S[5] - S[22])
    HOR.append(-S[17])

    stx = w[4] + S[24] + w[1]
    sty = -3 * w[1] - S[12] - S[9]
    print_latex(doc, VERT, HOR, stx, sty)
    ########################################################
    # bedroom
    VERT = []
    HOR = []
    VERT.append(-S[13])
    HOR.append(S[14])
    VERT.append(S[23])
    HOR.append(-S[15])

    stx = w[3] + S[3] + w[1]
    sty = -4 * w[1] - S[5] - S[12] - S[9]
    print_latex(doc, VERT, HOR, stx, sty)
    ########################################################
    # balcony
    VERT = []
    HOR = []
    VERT.append(-S[21] * 8 / 9)
    HOR.append(
        S[3]
        + w[1]
        + w[2]
        + w[5]
        + S[14]
        - (w[4] + S[8] + w[1] + w[3] + S[11] + w[4] + S[20])
    )

    stx = w[4] + S[8] + w[1] + w[3] + S[11] + w[4] + S[20]
    sty = 0
    print_latex(doc, VERT, HOR, stx, sty)
    ########################################################
    # windows
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

    ###########################################################
    # doors
    north_south_door(
        doc, w[4] + S[24] + S[14] / 3 + w[1], -5 * w[1] / 2 - S[5] - S[21], w[1], 0.7
    )  # bedroom door
    north_south_door(
        doc, w[4] + 2 * S[8] / 3, -3 * w[1] / 2 - S[9], w[1], 0.5
    )  # bathroom door
    north_south_door(
        doc, w[4] + S[8] + w[1] + S[11] / 2, -3 * w[1] / 2 - S[9], w[1], 0.5
    )  # toilet door
    north_south_door(
        doc, w[4] + S[24] / 2, -2 * w[1] - S[1] - S[9] - w[3] / 2, w[3], 0.8
    )  # entrance door
    west_east_door(
        doc, w[4] + S[24] + w[1] / 2, -3 * w[1] - S[9] - S[12] - S[5] / 2, w[1], 0.7
    )  # living room door
    west_east_door(
        doc, w[4] + S[7] + w[1] / 2, -2 * w[1] - S[9] - S[12] / 2, w[1], 0.7
    )  # kitchen door
    ##################################################
    bathtab(doc, w[4] + w[1], -2 * w[1], 0.75, 1.1)  # bathtab

    doc.append(Command("end", "tikzpicture"))

    # with doc.create(Tabular("rc|cl")) as table:
    #    table.add_hline()
    #    table.add_row((1, 2, 3, 4))
    #    table.add_hline(1, 2)
    #    table.add_empty_row()
    #    table.add_row((4, 5, 6, 7))
    doc.append(NoEscape(r"\vfill"))

    with doc.create(Tabular("|c|c|c|c|c|", row_height=3)) as table:
        table.add_hline()
        table.add_row(("Column 1", "", ",", "Column 2", ""))
        table.add_hline(1, 2)
        table.add_row(("Value 1", "Value 2", "", "", ""))
        table.add_hline(2, 3)
        table.add_row(("Value 1", "Value 2", "", "", ""))
        table.add_hline()
        table.add_row(
            (
                MultiColumn(size=2, align="|c|", data="MultiColumn"),
                "",
                MultiColumn(size=2, align="|c|", data="MultiColumn2"),
            ),
            strict=True,
        )
        table.add_hline()

    doc.generate_pdf("ml", clean_tex=False)


# Add the background setup using TikZ
