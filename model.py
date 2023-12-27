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
]
S = [i * scale for i in S]

w = [0, 0.145, 0.3, 0.4, 0.5, 0.6, 1.5]
#    0     1    2     3    4   5    6
w = [i * scale for i in w]

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
                    data=NoEscape(r"\parbox{4.5cm}{" + f"{Title}" + "}"),
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

    # region page 1 content

    with doc.create(Tabular("|p{3.1cm}|p{12.05cm}|p{3.1cm}|", row_height=1.5)) as table:
        table.add_hline()
        table.add_row(
            (MultiColumn(size=3, align="|c|", data="Ведомость рабочих чертежей"),)
        )
        table.add_hline()
        table.add_row("N", "ЕЕЕЕЕЕЕЕ", "Note")
        table.add_hline()
    doc.append(NoEscape(r"\vfill"))

    PageCount += 1
    create_stamp("Ведомость рабочих чертежей", PageCount, TotalPages, "")

    doc.append(NoEscape("\pagebreak"))
    # endregion
    ###################################################################################
    # region page 2 original plan
    doc.append(NoEscape(r"\vspace*{1cm} "))
    doc.append(Command("centering "))
    doc.append(Command("begin", "tikzpicture"))

    #  region perimeter
    print_list(
        doc,
        [
            [-(S[9] + S[1] + S[13] - S[4] + 2 * w[1] + w[4]), w[4]],
            [S[13] - S[4] - w[3] + w[4], S[3] + w[1] - w[3] + w[3] - w[4]],
            [-(S[13] - S[4] - w[3] + w[4]), w[3] + S[14] + w[4]],
            [
                S[9] + S[1] + S[13] - S[4] + 2 * w[1] + w[4],
                -(S[3] + w[1] - w[3] + w[2] - w[4] + w[5] + w[3] + S[14] + w[4]),
            ],
        ],
        0,
        0,
    )
    # endregion
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

    # hallway
    print_list(
        doc,
        [
            [-S[1] + S[2], -w[1]],
            [-S[2], S[3]],
            [S[4], -S[16] + S[15]],
            [S[5] + 2 * w[1], S[6]],
            [S[12], -S[7]],
        ],
        w[4],
        -S[9] - 2 * w[1],
    )
    # print_list(doc, [[0, S[24] - w[1]]], w[4], -S[9] - 2 * w[1], "green")
    #####################################################
    # bathroom
    print_list(doc, [[-S[9], S[8]], [S[9], -S[8]]], w[4], -w[1])

    #########################################################
    # toilet
    print_list(
        doc,
        [[-S[10], S[11]], [S[10], -S[11]]],
        w[4] + S[8] + w[1],
        -w[1] - S[9] + S[10],
    )

    ###########################################################
    # kitchen
    print_list(
        doc,
        [[-S[18] / 3, -w[2]], [-S[18] / 6, w[2]], [-S[18] / 2, S[19]], [S[18], -S[19]]],
        w[4] + S[8] + w[1] + w[3] + S[11],
        -w[1],
    )

    #################################################
    # living room
    print_list(
        doc,
        [[-S[5], S[16]], [S[22], -(S[16] - S[17])], [S[5] - S[22], -S[17]]],
        w[4] + S[24] + w[1],
        -3 * w[1] - S[12] - S[9],
    )
    ########################################################
    # bedroom
    print_list(
        doc,
        [[-S[13], S[14]], [S[23], -S[15]]],
        w[3] + S[3] + w[1],
        -4 * w[1] - S[5] - S[12] - S[9],
    )

    ########################################################
    # balcony
    print_list(
        doc,
        [
            [
                -S[21] * 8 / 9,
                S[3]
                + w[1]
                + w[2]
                + w[5]
                + S[14]
                - (w[4] + S[8] + w[1] + w[3] + S[11] + w[4] + S[20]),
            ]
        ],
        w[4] + S[8] + w[1] + w[3] + S[11] + w[4] + S[20],
        0,
    )

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

    bathtab(doc, w[4] + w[1], -2 * w[1], 0.75, 1.1)
    faucet(doc, S[8] / 2 + w[4], -1.5 * w[1], 0.6, 0.6)
    faucet(doc, S[13] + S[20] / 4 + w[4], -1.5 * w[1], 0.6, 0.6)
    toilet(doc, S[8] + S[11] / 3 + w[4] + w[1], -w[1] - S[9] + S[10], 0.55, 0.65)
    cooktop(doc, S[13] + S[20] * 2 / 3 + w[4], -1.5 * w[1], 0.6, 0.6)

    doc.append(Command("end", "tikzpicture"))

    doc.append(NoEscape(r"\vfill"))

    PageCount += 1
    create_stamp("Ведомость рабочих чертежей", PageCount, TotalPages, "")

    doc.append(NoEscape("\pagebreak"))
    # endregion
    ####################################################################################
    # region page 3 removed walls

    doc.append(NoEscape(r"\vspace*{1cm} "))

    doc.append(Command("centering"))

    doc.append(Command("begin", "tikzpicture"))

    print_list(
        doc,
        [
            [-(S[9] + S[1] + S[13] - S[4] + 2 * w[1] + w[4]), w[4]],
            [S[13] - S[4] - w[3] + w[4], S[3] + w[1] - w[3] + w[3] - w[4]],
            [-(S[13] - S[4] - w[3] + w[4]), w[3] + S[14] + w[4]],
            [
                S[9] + S[1] + S[13] - S[4] + 2 * w[1] + w[4],
                -(S[3] + w[1] - w[3] + w[2] - w[4] + w[5] + w[3] + S[14] + w[4]),
            ],
        ],
        0,
        0,
    )

    ###########################################################

    # hallway with removed walls
    print_list(
        doc,
        [
            [-S[1] + S[2], -w[1]],
            [-S[2], S[3]],
            [S[4], -S[16] + S[15]],
        ],
        w[4],
        -S[9] - 2 * w[1],
    )
    print_list(
        doc,
        [[S[5] + 2 * w[1], 0]],
        w[4] - w[1] + S[3] - S[16] + S[15],
        -S[9] - 2 * w[1] - S[1] + S[2] - S[2] + S[4],
        "red",
    )
    print_list(
        doc,
        [
            [0, S[6]],
            [S[12], 0],
        ],
        w[4] - w[1] + S[3] - S[16] + S[15],
        -S[9] - 2 * w[1] - S[1] + S[2] - S[2] + S[4] + S[5] + 2 * w[1],
    )
    print_list(
        doc,
        [
            # [S[12], -S[7]],
            [0, -S[7]],
        ],
        w[4] - w[1] + S[3] - S[16] + S[15] + S[6],
        -S[9] - 2 * w[1] - S[1] + S[2] - S[2] + S[4] + S[5] + 2 * w[1] + S[12],
        "red",
    )

    #####################################################
    # bathroom with removed walls
    print_list(doc, [[-S[9], 0]], w[4], -w[1])
    print_list(doc, [[0, S[8]]], w[4], -w[1] - S[9], "red")
    print_list(doc, [[S[9], 0]], w[4] + S[8], -w[1] - S[9], "red")
    print_list(doc, [[0, -S[8]]], w[4] + S[8], -w[1] - S[9] + S[9])

    #########################################################
    # toilet
    print_list(doc, [[-S[10], S[11]]], w[4] + S[8] + w[1], -w[1] - S[9] + S[10], "red")
    print_list(
        doc,
        [[S[10], -S[11]]],
        w[4] + S[8] + w[1] + S[11],
        -w[1] - S[9] + S[10] - S[10],
    )

    ###########################################################
    # kitchen
    print_list(
        doc,
        [[-S[18] / 3, -w[2]], [-S[18] / 6, w[2]], [-S[18] / 2, S[19]], [S[18], -S[19]]],
        w[4] + S[8] + w[1] + w[3] + S[11],
        -w[1],
    )

    #################################################
    # living room
    print_list(doc, [[-S[5], 0]], w[4] + S[24] + w[1], -3 * w[1] - S[12] - S[9], "red")
    print_list(
        doc,
        [[0, S[16]], [S[22], -(S[16] - S[17])], [S[5] - S[22], -S[17]]],
        w[4] + S[24] + w[1],
        -3 * w[1] - S[12] - S[9] - S[5],
    )
    ########################################################
    # bedroom
    print_list(
        doc,
        [[-S[13], S[14]], [S[23], -S[15]]],
        w[3] + S[3] + w[1],
        -4 * w[1] - S[5] - S[12] - S[9],
    )

    ########################################################
    # balcony
    print_list(
        doc,
        [
            [
                -S[21] * 8 / 9,
                S[3]
                + w[1]
                + w[2]
                + w[5]
                + S[14]
                - (w[4] + S[8] + w[1] + w[3] + S[11] + w[4] + S[20]),
            ]
        ],
        w[4] + S[8] + w[1] + w[3] + S[11] + w[4] + S[20],
        0,
    )

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
        doc, w[4] + S[7] + w[1] / 2, -2 * w[1] - S[9] - S[12] / 2, w[1], 0.7, "red"
    )  # kitchen door
    ##################################################

    bathtab(doc, w[4] + w[1], -2 * w[1], 0.75, 1.1)
    faucet(doc, S[8] / 2 + w[4], -1.5 * w[1], 0.6, 0.6)
    faucet(doc, S[13] + S[20] / 4 + w[4], -1.5 * w[1], 0.6, 0.6)
    toilet(doc, S[8] + S[11] / 3 + w[4] + w[1], -w[1] - S[9] + S[10], 0.55, 0.65)
    cooktop(doc, S[13] + S[20] * 2 / 3 + w[4], -1.5 * w[1], 0.6, 0.6)

    doc.append(Command("end", "tikzpicture"))

    doc.append(NoEscape(r"\vfill"))
    PageCount += 1
    create_stamp("Удаляемые перегородки и двери", PageCount, TotalPages, "")

    doc.append(NoEscape("\pagebreak"))
    # endregion
    ####################################################################################
    # region page 4 installed walls
    doc.append(NoEscape(r"\vspace*{1cm} "))

    doc.append(Command("centering"))

    doc.append(Command("begin", "tikzpicture"))

    print_list(
        doc,
        [
            [-(S[9] + S[1] + S[13] - S[4] + 2 * w[1] + w[4]), w[4]],
            [S[13] - S[4] - w[3] + w[4], S[3] + w[1] - w[3] + w[3] - w[4]],
            [-(S[13] - S[4] - w[3] + w[4]), w[3] + S[14] + w[4]],
            [
                S[9] + S[1] + S[13] - S[4] + 2 * w[1] + w[4],
                -(S[3] + w[1] - w[3] + w[2] - w[4] + w[5] + w[3] + S[14] + w[4]),
            ],
        ],
        0,
        0,
    )

    ###########################################################

    # hallway with removed walls
    print_list(
        doc,
        [
            [-S[1] + S[2], -w[1]],
            [-S[2], S[3]],
            [S[4] + w[1], 0],  # S[15]-S[16]
        ],
        w[4],
        -S[9] - 2 * w[1],
    )

    print_list(
        doc,
        [
            [0, S[6] - w[2]],
        ],
        w[4] - w[1] + S[3] - S[16] + S[15],
        -S[9] - 2 * w[1] - S[1] + S[2] - S[2] + S[4] + S[5] + 2 * w[1],
    )
    print_list(
        doc,
        [[0, S[24] - w[1]], [-S[12] - w[1], 2 * w[1]]],
        w[4],
        -S[9] - 2 * w[1],
        "green",
    )

    #####################################################
    # bathroom new walls
    print_list(doc, [[-S[9], 0]], w[4], -w[1])
    print_list(
        doc,
        [[0, S[24]], [-S[12] - w[1], 0]],
        w[4],
        -S[9] - w[1],
        "green",
    )

    print_list(doc, [[0, -S[8] - w[1]]], w[4] + S[8] + w[1], -w[1] - S[9] + S[9])

    print_list(doc, [[-S[9] + S[10], 0]], w[4] + S[8] + w[1], -w[1])

    #########################################################
    # toilet new walls

    print_list(
        doc,
        [[S[10], -S[11]]],
        w[4] + S[8] + w[1] + S[11],
        -w[1] - S[9] + S[10] - S[10],
    )
    print_list(
        doc,
        [[-w[1] - S[12], 0]],
        w[4] + S[8] + w[1] + S[11],
        -w[1] - S[9] + S[10] - S[10],
        "green",
    )
    west_east_door(
        doc, w[4] + S[24] - w[1] / 2, -(2 * w[1] + S[9] + S[12] / 2), w[1], 0.7, "green"
    )
    ###########################################################
    # kitchen new walls
    print_list(
        doc,
        [[-S[18] / 3, -w[2]], [-S[18] / 6, w[2]], [-S[9] + S[18] / 2, 0]],
        w[4] + S[8] + w[1] + w[3] + S[11],
        -w[1],
    )
    print_list(
        doc,
        [[0, -w[2]], [-S[12] - w[1], w[2]]],
        w[4] + S[8] + w[1] + w[3] + S[11],
        -w[1] - S[9],
        "green",
    )
    print_list(
        doc,
        [[0, S[19]], [S[18], -S[19]]],
        w[4] + S[8] + w[1] + w[3] + S[11],
        -w[1] - S[18],
    )
    north_south_door(
        doc,
        w[4] + S[8] + w[1] + w[3] + S[11] + S[20] / 3,
        -w[1] - 0.5 * w[1] - S[21],
        w[1],
        0.7,
        "green",
    )  # kitchen door
    #################################################
    # living room

    print_list(
        doc,
        [[0, S[15] + w[1]], [S[22], -(S[16] - S[17])], [S[5] - S[22], -S[17]]],
        w[4] + S[24] + w[1] - S[15] + S[16] - w[1],
        -3 * w[1] - S[12] - S[9] - S[5],
    )
    ########################################################
    # bedroom
    print_list(
        doc,
        [[-S[13], S[14]], [S[23], -S[15]]],
        w[3] + S[3] + w[1],
        -4 * w[1] - S[5] - S[12] - S[9],
    )

    ########################################################
    # balcony
    print_list(
        doc,
        [
            [
                -S[21] * 8 / 9,
                S[3]
                + w[1]
                + w[2]
                + w[5]
                + S[14]
                - (w[4] + S[8] + w[1] + w[3] + S[11] + w[4] + S[20]),
            ]
        ],
        w[4] + S[8] + w[1] + w[3] + S[11] + w[4] + S[20],
        0,
    )

    ########################################################
    # windows
    print_window(
        doc, w[4] + S[8] + w[1] + w[3] + S[11] + S[20], -w[1] - S[21] / 2 + w[6] / 2
    )  # kitchen

    print_window(
        doc, w[4] + S[16] + w[1] + S[24], -2 * w[1] - S[21] - S[5] / 2 + w[6] / 2
    )  # living room

    print_window(
        doc,
        w[4] + S[16] + w[1] + S[24],
        -3 * w[1] - S[21] - S[5] - S[23] / 2 + w[6] / 2,
    )  # bedroom

    ###########################################################
    # doors
    north_south_door(
        doc, w[4] + S[24] + S[14] / 3 + w[1], -5 * w[1] / 2 - S[5] - S[21], w[1], 0.7
    )  # bedroom door

    north_south_door(
        doc, w[4] + S[24] / 2, -2 * w[1] - S[1] - S[9] - w[3] / 2, w[3], 0.8
    )  # entrance door

    ##################################################

    bathtab(doc, w[4] + w[1], -2 * w[1], 0.75, 1.1)
    faucet(doc, S[8] / 2 + w[4], -1.5 * w[1], 0.6, 0.6)
    faucet(doc, S[13] + S[20] / 4 + w[4], -1.5 * w[1], 0.6, 0.6)
    toilet(doc, S[8] + S[11] / 3 + w[4] + w[1], -w[1] - S[9] + S[10], 0.55, 0.65)
    cooktop(doc, S[13] + S[20] * 2 / 3 + w[4], -1.5 * w[1], 0.6, 0.6)

    doc.append(Command("end", "tikzpicture"))

    doc.append(NoEscape(r"\vfill"))

    PageCount += 1
    create_stamp("Возводимые перегородки и двери", PageCount, TotalPages, "")
    doc.append(NoEscape("\pagebreak"))
    # endregion
    ####################################################################################
    # region page 5 final plan
    doc.append(NoEscape(r"\vspace*{1cm} "))

    doc.append(Command("centering"))

    doc.append(Command("begin", "tikzpicture"))

    print_list(
        doc,
        [
            [-(S[9] + S[1] + S[13] - S[4] + 2 * w[1] + w[4]), w[4]],
            [S[13] - S[4] - w[3] + w[4], S[3] + w[1] - w[3] + w[3] - w[4]],
            [-(S[13] - S[4] - w[3] + w[4]), w[3] + S[14] + w[4]],
            [
                S[9] + S[1] + S[13] - S[4] + 2 * w[1] + w[4],
                -(S[3] + w[1] - w[3] + w[2] - w[4] + w[5] + w[3] + S[14] + w[4]),
            ],
        ],
        0,
        0,
    )

    ###########################################################

    # hallway with removed walls
    print_list(
        doc,
        [
            [-S[1] + S[2], -w[1]],
            [-S[2], S[3]],
            [S[4] + w[1], 0],  # S[15]-S[16]
        ],
        w[4],
        -S[9] - 2 * w[1],
    )

    print_list(
        doc,
        [
            [0, S[6] - w[2]],
        ],
        w[4] - w[1] + S[3] - S[16] + S[15],
        -S[9] - 2 * w[1] - S[1] + S[2] - S[2] + S[4] + S[5] + 2 * w[1],
    )
    print_list(
        doc,
        [[0, S[24] - w[1]], [-S[12] - w[1], 2 * w[1]]],
        w[4],
        -S[9] - 2 * w[1],
    )

    #####################################################
    # bathroom new walls
    print_list(doc, [[-S[9], 0]], w[4], -w[1])
    print_list(
        doc,
        [[0, S[24]], [-S[12] - w[1], 0]],
        w[4],
        -S[9] - w[1],
    )

    print_list(doc, [[0, -S[8] - w[1]]], w[4] + S[8] + w[1], -w[1] - S[9] + S[9])

    print_list(doc, [[-S[9] + S[10], 0]], w[4] + S[8] + w[1], -w[1])

    #########################################################
    # toilet new walls

    print_list(
        doc,
        [[S[10], -S[11]]],
        w[4] + S[8] + w[1] + S[11],
        -w[1] - S[9] + S[10] - S[10],
    )
    print_list(
        doc,
        [[-w[1] - S[12], 0]],
        w[4] + S[8] + w[1] + S[11],
        -w[1] - S[9] + S[10] - S[10],
    )
    west_east_door(
        doc,
        w[4] + S[24] - w[1] / 2,
        -(2 * w[1] + S[9] + S[12] / 2),
        w[1],
        0.7,
    )
    ###########################################################
    # kitchen new walls
    print_list(
        doc,
        [[-S[18] / 3, -w[2]], [-S[18] / 6, w[2]], [-S[9] + S[18] / 2, 0]],
        w[4] + S[8] + w[1] + w[3] + S[11],
        -w[1],
    )
    print_list(
        doc,
        [[0, -w[2]], [-S[12] - w[1], w[2]]],
        w[4] + S[8] + w[1] + w[3] + S[11],
        -w[1] - S[9],
    )
    print_list(
        doc,
        [[0, S[19]], [S[18], -S[19]]],
        w[4] + S[8] + w[1] + w[3] + S[11],
        -w[1] - S[18],
    )
    north_south_door(
        doc,
        w[4] + S[8] + w[1] + w[3] + S[11] + S[20] / 3,
        -w[1] - 0.5 * w[1] - S[21],
        w[1],
        0.7,
    )  # kitchen door
    #################################################
    # living room

    print_list(
        doc,
        [[0, S[15] + w[1]], [S[22], -(S[16] - S[17])], [S[5] - S[22], -S[17]]],
        w[4] + S[24] + w[1] - S[15] + S[16] - w[1],
        -3 * w[1] - S[12] - S[9] - S[5],
    )
    ########################################################
    # bedroom
    print_list(
        doc,
        [[-S[13], S[14]], [S[23], -S[15]]],
        w[3] + S[3] + w[1],
        -4 * w[1] - S[5] - S[12] - S[9],
    )

    ########################################################
    # balcony
    print_list(
        doc,
        [
            [
                -S[21] * 8 / 9,
                S[3]
                + w[1]
                + w[2]
                + w[5]
                + S[14]
                - (w[4] + S[8] + w[1] + w[3] + S[11] + w[4] + S[20]),
            ]
        ],
        w[4] + S[8] + w[1] + w[3] + S[11] + w[4] + S[20],
        0,
    )

    ########################################################
    # windows
    print_window(
        doc, w[4] + S[8] + w[1] + w[3] + S[11] + S[20], -w[1] - S[21] / 2 + w[6] / 2
    )  # kitchen

    print_window(
        doc, w[4] + S[16] + w[1] + S[24], -2 * w[1] - S[21] - S[5] / 2 + w[6] / 2
    )  # living room

    print_window(
        doc,
        w[4] + S[16] + w[1] + S[24],
        -3 * w[1] - S[21] - S[5] - S[23] / 2 + w[6] / 2,
    )  # bedroom

    ###########################################################
    # doors
    north_south_door(
        doc, w[4] + S[24] + S[14] / 3 + w[1], -5 * w[1] / 2 - S[5] - S[21], w[1], 0.7
    )  # bedroom door

    north_south_door(
        doc, w[4] + S[24] / 2, -2 * w[1] - S[1] - S[9] - w[3] / 2, w[3], 0.8
    )  # entrance door

    ##################################################

    bathtab(doc, w[4] + w[1], -2 * w[1], 0.75, 1.1)
    faucet(doc, S[8] / 2 + w[4], -1.5 * w[1], 0.6, 0.6)
    faucet(doc, S[13] + S[20] / 4 + w[4], -1.5 * w[1], 0.6, 0.6)
    toilet(doc, S[8] + S[11] / 3 + w[4] + w[1], -w[1] - S[9] + S[10], 0.55, 0.65)
    cooktop(doc, S[13] + S[20] * 2 / 3 + w[4], -1.5 * w[1], 0.6, 0.6)

    doc.append(Command("end", "tikzpicture"))

    doc.append(NoEscape(r"\vfill"))

    PageCount += 1
    create_stamp(
        "План помещения квартиры после перепланировки", PageCount, TotalPages, ""
    )
    doc.append(NoEscape("\pagebreak"))
    # endregion
    #####################################################################################
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
            "помещ", "Тип", "Схема пола", "Данные элементов пола", "Площадь,м²"
        )
        table.add_hline()
        table.add_row(
            MultiRow(6, data=" "),
            MultiRow(6, data=" "),
            MultiRow(
                6,
                data=NoEscape(
                    r"\begin{tikzpicture}"
                    + draw_cement(0.2, 0, 4.5, 0.8, 3, 20)
                    + draw_shumanet(0.2, -0.8, 4.5, 0.1, 2)
                    + draw_concrete(0.2, -0.9, 4.5, 20)
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
		    + r"3. Существующее ж/б перекрытие."
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
    create_stamp("Экспикация полов в помеще", PageCount, TotalPages, "")
    doc.append(NoEscape("\pagebreak"))
# endregion
doc.generate_pdf("ml", clean_tex=False)


# Add the background setup using TikZ
