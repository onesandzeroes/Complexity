#! /usr/bin/env python3


class CircleBuffer:
    def __init__(self, length, data=None):
        if not data:
            self.data = [None] * length
        else:
            # Convert to a list, allows any sequence as the
            # data argument
            self.data = [d for d in data]
            spots_left = length - len(self.data)
            self.data.extend([None * spots_left])
        self.length = length
        self.fill_count = len([d for d in self.data if not d is None])
        self.start = 0
        self.end = 0
        for index, dat in enumerate(self.data):
            if dat:
                if index > self.end:
                    self.end = index

    def append(self, value):
        if self.fill_count == 0:
            self.data[0] = value
            self.fill_count += 1
        elif self.fill_count < self.length:
            pos = self.end + 1
            # Wrap around if at the end
            if pos == self.length:
                pos = 0
            self.data[pos] = value
            self.end = pos
            self.fill_count += 1
        # If the buffer is full, overwrite the start position, i.e.
        # the oldest data
        # Don't need to increment fill_count as data is being overwritten
        else:
            pos = self.start
            self.data[pos] = value
            self.start = pos + 1
            if self.start == self.length:
                self.start = 0
            self.end = pos

    def pop(self):
        # Get value
        val = self.data[self.start]
        # Remove it from the list
        self.data[self.start] = None
        self.fill_count -= 1
        new_start = self.start + 1
        # Wraparound if the end of the list is reached
        if new_start == self.length:
            new_start = 0
        self.start = new_start
        return val

    def __str__(self):
        return str(self.data)

if __name__ == '__main__':
    buf = CircleBuffer(length=4)
    for i in range(10):
        buf.append(i)
        print(buf)
        print("Start: ", buf.start, "End: ", buf.end)
