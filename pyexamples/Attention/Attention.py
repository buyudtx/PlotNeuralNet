import sys

sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head('..'),
    to_cor(),
    to_begin(),
    to_xFeature(name="x", offset="(0,0,0)", to="(0,0,0)", height=15, width=4, depth=15, caption="search region feature"),
    to_zFeature(name="z", offset="(0,4,0)", to="(x-north)", height=10, width=4, depth=10, caption="template feature"),
    to_Conv(name='PAM', offset="(3,3,0)", to="(x-east)", height=15, width=15, depth=0,  caption="PAM"),
    to_connection("x", "PAM"),
    to_connection("z", "PAM"),
    to_Conv(name='CAM', offset="(2,0,0)", to="(PAM-east)", height=15, width=15, depth=0, caption="CAM"),
     to_connection("PAM", "CAM"),
    to_ff(name="f", offset="(2,0,0)", to="(CAM-east)", height=15, width=4, depth=15, caption="response feature map"),
    to_connection("CAM", "f"),
    to_end()
]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()
