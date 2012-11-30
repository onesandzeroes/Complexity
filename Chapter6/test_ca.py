from CA import CA, CircularCA
from CADrawer import PyplotDrawer


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

if __name__ == '__main__':
    circular_ca_test(40, random_pos=True)
