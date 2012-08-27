import string


def gen_alphanum():
    while True:
        for n in string.digits:
            for c in string.lowercase:
                yield c + str(n)

if __name__ == '__main__':
    for an in gen_alphanum():
        print(an)
