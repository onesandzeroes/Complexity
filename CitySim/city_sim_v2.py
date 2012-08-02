#! /usr/bin/env python3
import random
import pygame


class City:
    def __init__(self, width, height, drawing=True):
        self.width = width
        self.height = height
        self.create_map()
        self.populate()
        self.drawing = drawing
        if self.drawing:
            self.view = CityView(self)
            self.view.draw()
    def create_map(self):
        self.map = []
        # Need to reference instance variables with self.var
        one_block = ['.'] * self.width
        for y in range(self.height):
            self.map.append(one_block[:])
    def random_occupied(self):
        found = False
        while not found:
            house_pos = self.random_house()
            pers = self[house_pos]
            if pers in ('R', 'B'):
                return {'person': pers, 'location': house_pos}
    def random_empty(self):
        found = False
        while not found:
            house_pos = self.random_house()
            pers = self[house_pos]
            if pers == '.':
                return {'person': pers, 'location': house_pos}
    def random_house(self):
        rand_x = random.randint(0, self.width -1)
        rand_y = random.randint(0, self.height - 1)
        return (rand_x, rand_y)
    def populate(self, red_weight=45, blue_weight = 45, empty_weight = 10):
        weight_list = (
            ['R'] * red_weight + ['B'] *
            blue_weight + 
            ['.'] * empty_weight
        )
        for x in range(self.width):
            for y in range(self.height):
                self[x, y] = random.choice(weight_list)
    def move_out(self, location):
        cur_x, cur_y = location
        cur_pers = self[location]
        new_house = self.random_empty()
        new_x, new_y = new_house['location']
        assert new_house['person'] == '.', 'Trying to move into non-empty house'
        self[cur_x, cur_y] = '.'
        self[new_x, new_y] = cur_pers
    def check_happy(self, location):
        x, y = location
        current_pers = self[location]
        matches = (current_pers, '.')
        like_neighbours = 0
        for adj in (-1, 1):
            # Check for same colour neighbour or empty house
            if self[x + adj, y] in matches:
                like_neighbours += 1
            if self[x, y + adj] in matches:
                like_neighbours += 1
        if like_neighbours < self.happy_threshold:
            self.move_out(location)
    def do_sim(self, iterations=10000, happy_threshold=2, draw_every=100):
        self.happy_threshold = happy_threshold
        for i in range(iterations):
            to_check = self.random_occupied()
            self.check_happy(to_check['location'])
            if self.drawing:
                if i % draw_every == 0:
                    self.view.draw()
    # Operator overloading to allow coordinate indexing
    def __getitem__(self, xy):
        try:
            x, y = xy
            return self.map[y][x]
        # Return an empty house when it's outside the map boundaries
        except IndexError:
            return '.'
    def __str__(self):
        # __str__ needs to return a string
        layout = '\n'.join([str(block) for block in self.map]) 
        return layout + '\n\n'
    def __setitem__(self, xy, value):
        x, y = xy
        self.map[y][x] = value


class CityView:
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    col_dict = {'R': RED, 'B': BLUE, '.': WHITE}
    scale = 5
    def __init__(self, city):
        pygame.init()
        self.city = city
        self.size = (self.city.width * self.scale, self.city.height * self.scale)
        self.screen = pygame.display.set_mode(self.size)
        self.draw()
    def draw(self):
        for x in range(self.city.width):
            for y in range(self.city.height):
                pers = self.city[x, y]
                screenpos = (x * self.scale, y * self.scale, self.scale, self.scale)
                pygame.draw.rect(self.screen, self.col_dict[pers], screenpos)
        pygame.display.update()
        #pygame.time.wait(100)

if __name__ == '__main__':
    bluetown = City(120, 120)
    bluetown.do_sim(100000, 3)
    print('Done!')
    import sys
    sys.exit()
