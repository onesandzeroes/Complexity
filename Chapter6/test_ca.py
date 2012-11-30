from CA import CA, CircularCA
from CADrawer import PyplotDrawer, EPSDrawer


def first_ca_test():
    ca = CA(147, 20)
    ca.start_single()
    ca.loop(19)

    drawer = PyplotDrawer()
    drawer.draw(ca)
    drawer.show()


def circular_ca_test(n, random_pos=False):
    ca = CircularCA(50, n)
    if random_pos:
        ca.start_random()
    else:
        ca.start_single()
    ca.loop(n - 1)

    drawer = PyplotDrawer()
    drawer.draw(ca)
    drawer.show()


def test_eps_drawer():
    ca = CA(50, 20)
    ca.start_single()
    ca.loop(19)

    drawer = EPSDrawer()
    drawer.draw(ca)
    drawer.save(filename='eps_draw_test.eps')


def sierpinski(n):
    """
    Rules 18 and 90 should approximate a Sierpinski triangle,
    testing that here.
    """
    ca1 = CA(18, n)
    ca1.start_single()
    ca1.loop(n - 1)

    drawer = PyplotDrawer()
    drawer.draw(ca1)
    drawer.show()

    ca2 = CA(90, n)
    ca2.start_single()
    ca2.loop(n - 1)

    drawer = PyplotDrawer()
    drawer.draw(ca2)
    drawer.show()


if __name__ == '__main__':
    sierpinski(65)
    # circular_ca_test(40, random_pos=True)
    # test_eps_drawer()
