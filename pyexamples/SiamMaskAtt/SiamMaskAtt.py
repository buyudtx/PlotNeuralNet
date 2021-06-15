import sys

sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head('..'),
    to_cor(),
    to_begin(),
    to_Conv(name='x', offset="(0,0,0)", to="(0,0,0)", height=15, width=1, depth=15,
            caption="search region 287$\\times$287$\\times$3"),
    to_Conv(name='z', offset="(0,4,0)", to="(x-north)", height=10, width=1, depth=10,
            caption="template 127$\\times$127$\\times$3"),

    to_Conv(name='googlenet_z', offset="(2,0,0)", to="(z-east)", height=10, width=10, depth=0, caption="GoogleNet"),
    to_Conv(name='googlenet_x', offset="(2,0,0)", to="(x-east)", height=10, width=10, depth=0, caption="GoogleNet"),

    to_zFeature(name="zf", offset="(2,0,0)", to="(googlenet_z-east)", height=10, width=4, depth=10,
                caption="zf[256,25,25]"),
    to_xFeature(name="xf", offset="(2,0,0)", to="(googlenet_x-east)", height=15, width=4, depth=15,
                caption="xf[256,31,31]"),

    to_connection("z", "googlenet_z"),
    to_connection("x", "googlenet_x"),
    to_connection("googlenet_z", "zf"),
    to_connection("googlenet_x", "xf"),

    to_Conv(name='attention', offset="(2,2,0)", to="(xf-east)", height=15, width=15, depth=0,
            caption="Attention Similarity Module"),
    to_ff(name="f", offset="(2,0,0)", to="(attention-east)", height=15, width=4, depth=15,
          caption="response feature map [256,31,31]"),
    to_connection("zf", "attention"),
    to_connection("xf", "attention"),
    to_connection("attention", "f"),

    to_Conv(name='cls', offset="(3,2,0)", to="(f-east)", height=15, width=15, depth=0, caption="CNN"),
    to_Conv(name='reg', offset="(3,-2,0)", to="(f-east)", height=15, width=15, depth=0, caption="CNN"),
    to_connection("f", "cls"),
    to_connection("f", "reg"),

    to_ff(name="fc", offset="(2,0,0)", to="(cls-east)", height=15, width=2, depth=0, caption="cls"),
    to_ff(name="fr", offset="(2,0,0)", to="(reg-east)", height=15, width=4, depth=0, caption="reg"),
    to_connection("cls", "fc"),
    to_connection("reg", "fr"),
    to_end()
]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()
