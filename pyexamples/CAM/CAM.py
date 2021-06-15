import sys

sys.path.append('../')
from pycore.tikzeng import *

arch = [
    to_head('..'),
    to_cor(),
    to_begin(),
    to_xFeature("f", offset="(0,0,0)", to="(0,0,0)", height=15, width=4, depth=15, caption="$f$[C,H,W]"),

    to_xf("B", offset="(1,4,0)", to="(f-east)", height=8, width=10, depth=0, caption="B[C,H$\\times$W]"),
    to_connection("f", "B"),

    to_xf("C", offset="(1,0,0)", to="(f-east)", height=8, width=10, depth=0, caption="C[H$\\times$W,C]"),
    to_connection("f", "C"),

    to_xf("D", offset="(1,-4,0)", to="(f-east)", height=8, width=10, depth=0, caption="D[C,H$\\times$W]"),
    to_connection("f", "D"),

    to_Plus("plus1", offset="(1.5,-2,0)", to="(B-east)", radius=2, opacity=0.6),
    to_connection("B", "plus1"),
    to_connection("C", "plus1"),

    to_ff("S", offset="(1,0,0)", to="(plus1-east)", height=10, width=10, depth=0, caption="S[C,C]"),
    to_connection("plus1", "S"),

    to_Plus("plus2", offset="(6.5,0,0)", to="(D-east)", radius=2, opacity=0.6),
    to_connection("S", "plus2"),
    to_connection("D", "plus2"),

    to_ff("out", offset="(3,0,0)", to="(plus2-east)", height=15, width=4, depth=15, caption="out[C,H,W]"),
    to_connection("plus2", "out"),

    to_end()
]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()
