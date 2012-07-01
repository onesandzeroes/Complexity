#! /usr/bin/env python3
import random, pygame

class City:
    def __init__(self, num_blocks, block_size):
        self.num_blocks = num_blocks
        self.block_size = block_size
        block = ['.'] * block_size
        self.layout = []
        self.empties = []
        for i in range(num_blocks):
            # append copies of block to prevent every block being a copy
            # of the same mutable object
            self.layout.append(block[:])
        self.view = CityViewer(block_size, num_blocks)
        self.view.draw(self.layout)
    def __str__(self):
        out = '\n'.join([str(block) for block in self.layout]) + '\n\n'
        return out
    def get(self, x, y):
        return self.layout[y][x]
    def set(self, location, value):
        self.layout[location[1]][location[0]] = value
    def populate(self, red_weight=45, blue_weight=45, empty_weight=10):
        self.popweights = (['R'] * red_weight + ['B'] * blue_weight +
                          ['.'] * empty_weight)
        for bnum, block in enumerate(self.layout):
            for hnum, house in enumerate(block):
                new_owner = random.choice(self.popweights)
                self.layout[bnum][hnum] = new_owner
                if new_owner == '.':
                    # Store all locations as (x, y), I forgot to do this
                    # and it meant the population disappeared when you
                    # ran the happiness check a large number of times
                    # because people were moving into occupied locations
                    self.empties.append((hnum, bnum))
    def happy_check(self):
        found_person = False
        while not found_person:
            xpos = random.randint(0, self.block_size - 1)
            ypos = random.randint(0, self.num_blocks - 1)
            happy_loc = (xpos, ypos)
            happy_person = self.get(*happy_loc)
            if not happy_person == '.':
                found_person = True
        neighbour_locs = [(xpos + 1, ypos), (xpos - 1, ypos),
                      (xpos, ypos + 1), (xpos, ypos -1)
                      ]
        num_like_neighbours = 0
        for n in neighbour_locs:
            try:
                current_n = self.get(*n)
            except IndexError:
                num_like_neighbours += 1
                continue
            if current_n == happy_person:
                num_like_neighbours += 1
        if num_like_neighbours < 2:
            self.move(happy_loc, happy_person)
    def move(self, location, person):
        new_house = random.choice(self.empties)
        #print(person, 'moving from ', location, 'to ', new_house)
        self.set(new_house, person)
        self.set(location, '.')
        self.empties.remove(new_house)
        self.empties.append(location)
        #self.view.draw(self.layout)
        self.view.update(new_house, person)
        self.view.update(location, '.')

class CityViewer:
    colours = {'R': (255, 0, 0), 'B': (0, 0, 255), '.': (255, 255, 255)}
    def __init__(self, xsize, ysize, scale=15):
        self.scale = scale
        pygame.init()
        self.xsize = xsize
        self.ysize = ysize
        self.screen = pygame.display.set_mode((xsize * scale, ysize * scale))
        #background = pygame.Surface(self.screen.get_size())
        #background = background.convert()
        #background.fill((0, 0, 0))
        #self.screen.blit(background, (0, 0))
        pygame.display.update()
    def draw(self, layout):
        for bpos, block in enumerate(layout):
            for hpos, house in enumerate(block):
                h_colour = self.colours[house]
                new_rect = pygame.Rect(hpos * self.scale, bpos * self.scale, self.scale, self.scale)
                pygame.draw.rect(self.screen, h_colour, new_rect)
                pygame.display.update()
    def update(self, loc, value):
        h_colour = self.colours[value]
        #print(h_colour)
        #new_loc = (loc[0] * self.scale, loc[1] * self.scale)
        new_rect = pygame.Rect(loc[0] * self.scale, loc[1] * self.scale, self.scale, self.scale)
        pygame.draw.rect(self.screen, h_colour, new_rect)
        #print(new_loc)
        #self.screen.blit(new_rect, new_loc)
        pygame.display.update()

redtown = City(20, 20)
redtown.populate()
print(redtown)
for i in range(1000):
    redtown.happy_check()
print(redtown)
import sys
sys.exit()
