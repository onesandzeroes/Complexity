#! /usr/bin/env python


def bisect_search(value, seq):
    start = 0
    end = len(seq)
    while end > start:
        print("Start: ", start)
        print("End: ", end)
        halfway = (start + end) // 2
        halfval = seq[halfway]
        if halfval == value:
            return halfway
        elif halfval < value:
            # You've already checked the value of halfway, so start from
            # the next item
            start = halfway + 1
        elif halfval > value:
            end = halfway
    return None

if __name__ == '__main__':
    print(bisect_search(3, [1, 2, 3, 4, 5]))
    print(bisect_search(4, [1, 2, 4, 6, 9, 10, 11]))
    print(bisect_search(5, [1, 2, 4, 6, 9, 10, 11]))
    print(bisect_search(10, [1, 2, 4, 6, 9, 10, 11]))
