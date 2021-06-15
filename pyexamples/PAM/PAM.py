import sys

sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head('..'),
    to_cor(),
    to_begin(),
    to_xFeature(name="x", offset="(0,0,0)", to="(0,0,0)", height=15, width=4, depth=15, caption="search region feature"),
    to_Conv(name='convB', offset="(1,0,0)", to="(x-east)", height=5, width=2, depth=5, caption="conv 1$\\times$1"),
    to_connection("x", "convB"),

    to_xf(name="B", offset="(1,0,0)", to="(convB-east)", height=10, width=8, depth=0, caption="B[H$\\times$W,C]"),
    to_connection('convB', 'B'),

    to_zFeature(name="z", offset="(0,5,0)", to="(x-north)",  height=10, width=4, depth=10, caption="template feature"),
    to_Conv(name='convC', offset="(1,-3,0)", to="(z-east)", height=5, width=2, depth=5, caption="conv 1$\\times$1"),
    to_connection("z", "convC"),

    to_zf(name="C", offset="(1,0,0)", to="(convC-east)", height=5, width=10, depth=0, caption="C[C,h$\\times$w]"),
    to_connection('convC', 'C'),

    to_Conv(name='convD', offset="(1,0,0)", to="(z-east)", height=5, width=2, depth=5, caption="conv 1$\\times$1"),
    to_connection("z", "convD"),

    to_zf(name="D", offset="(1,0,0)", to="(convD-east)", height=5, width=10, depth=0, caption="D[C,h$\\times$w]"),
    to_connection('convD', 'D'),

    to_Plus("plus1", offset="(1,-2,0)", to="(C-east)", radius=2, opacity=0.6),
    to_connection('B', 'plus1'),
    to_connection('C', 'plus1'),

    to_SoftMax("softmax", 10, "(1,0,0)", "(plus-east)", caption="SoftMax"),
    to_connection('plus1', 'softmax'),

    to_ff(name="S", offset="(1,0,0)", to="(softmax-east)",  height=5, width=8, depth=0, caption="S[H$\\times$W,h$\\times$w]"),
    to_connection('softmax', 'S'),

    to_Plus("plus2", offset="(1.5,0,0)", to="(S-east)", radius=2, opacity=0.6),
    to_connection('D', 'plus2'),
    to_connection('S', 'plus2'),

    to_ff(name="out", offset="(1.5,0,0)", to="(plus2-east)", height=8, width=10, depth=0, caption="out[C,H$\\times$W]"),
    to_connection('plus2', 'out'),

    to_Sum("add", offset="(1.5,0,0)", to="(out-east)", radius=2, opacity=0.6),
    to_connection('out', 'add'),
    to_connection('x', 'add'),

    to_ff(name="f", offset="(2,0,0)", to="(add-east)", height=15, width=4, depth=15, caption="$f$[C,H,W]"),
    to_connection('add', 'f'),
    to_end()
]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()
