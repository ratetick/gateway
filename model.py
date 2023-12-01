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
]
S = [i * scale for i in S]

w = [0, 0.145, 0.3, 0.4, 0.5, 0.6, 1.5]
#    0     1    2     3    4   5    6
w = [i * scale for i in w]


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

    geometry_options = {
        "tmargin": "1.5cm",
        "lmargin": ".5cm",
        "bmargin": "1.2cm",
        "rmargin": ".6cm",
    }

    doc = Document(
        geometry_options=geometry_options,
        page_numbers=False,
        # document_options=["utf8"],
    )
    doc.preamble.append(Command("usepackage", "tikz"))
    doc.preamble.append(Command("usepackage", "background"))
    doc.preamble.append(Command("usetikzlibrary", "calc"))  # \usetikzlibrary{calc}
    doc.preamble.append(Command("usepackage", options="russian", arguments="babel"))

    background_setup = r"angle = 0,scale = 1,vshift = -2ex,contents = {\tikz[overlay, remember picture]\draw [line width = .8pt,color = black, double = blue!10]($(current page.north west)+(1cm,-1cm)$)rectangle ($(current page.south east)+(-1,1)$);}"
    background_noescape = f"\\backgroundsetup{{{background_setup}}}"
    doc.preamble.append(NoEscape(background_noescape))
    doc.append(Command("centering"))
    doc.append(Command("begin", "tikzpicture"))

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
    measurements(doc, "hor_top", 0, 0, -HOR[3], -1.2, -round(HOR[3] / scale, 2))
    measurements(doc, "vert_right", -HOR[3], 0, VERT[3], 1.2, round(VERT[3] / scale, 2))
    ###########################################################

    # hallway
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
    # bathroom
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
    # toilet
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
    faucet(doc, S[8] / 2 + w[4], -1.5 * w[1], 0.6, 0.6)
    faucet(doc, S[13] + S[20] / 4 + w[4], -1.5 * w[1], 0.6, 0.6)
    toilet(doc, S[8] + S[11] / 3 + w[4] + w[1], -w[1] - S[9] + S[10], 0.55, 0.65)
    cooktop(doc, S[13] + S[20] * 2 / 3 + w[4], -1.5 * w[1], 0.6, 0.6)

    doc.append(Command("end", "tikzpicture"))

    doc.append(NoEscape(r"\vfill"))
    # "Подпись"

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
                "",
                "",
                "",
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
                MultiRow(size=3, data="Ведомость рабочих чертежей"),
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
        strict = (True,)

    doc.generate_pdf("ml", clean_tex=False)


# Add the background setup using TikZ
