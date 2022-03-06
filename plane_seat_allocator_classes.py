import pygame

class Passenger(pygame.sprite.Sprite):
    def __init__(self, entry_point, allocated_seat_object):
        super().__init__()
        self.entry_point = entry_point
        self.allocated_seat = allocated_seat_object
        self.size = 0.05
        self.move_speed = 1

        self.image_searching = pygame.image.load('art/pax_moving.png').convert_alpha()
        self.image_seated = pygame.image.load('art/pax_seated.png').convert_alpha()
        self.image = self.image_searching        # Change this to animate state of passenger
        self.resize_image()

        self.initial_position = self.get_initial_position()
        self.x = self.initial_position[0]
        self.y = self.initial_position[1]
        self.rect = self.image.get_rect(center = self.initial_position)

        self.row_found = False
        self.seat_found = False
        self.counter = 0
    
    def get_initial_position(self):
        screen_width, screen_height = pygame.display.get_surface().get_size()

        if self.entry_point == 'front':
            return (int(screen_width/2), 0)
        elif self.entry_point == 'back':
            return (int(screen_width/2), int(screen_height))

        self.image = pygame.transform.rotozoom(self.image, self.angle, self.size)
        self.rect = self.image.get_rect(center = self.rect.center)
    
    def move_to_seat(self):

        if not self.row_found:
            # print("seat position:", self.allocated_seat.y, "pax position:", self.y)
            if self.allocated_seat.y > self.y:
                self.y += self.move_speed
            elif self.allocated_seat.y < self.y:
                self.y -= self.move_speed

            if int(self.allocated_seat.y) == int(self.y):
                self.row_found = True

        elif self.row_found:

            if self.allocated_seat.x > self.x:
                self.x += self.move_speed
            elif self.allocated_seat.x < self.x:
                self.x -= self.move_speed

            if int(self.allocated_seat.x) == int(self.x):
                self.seat_found = True
                self.image = self.image_seated        # Change this to animate state of passenger
                self.resize_image()

        self.rect = self.image.get_rect(center = (self.x, self.y))

    def resize_image(self):
        screen_width, screen_height = pygame.display.get_surface().get_size()
        size = int(screen_width/8)
        self.image = pygame.transform.scale(self.image, (size, size))

    def update(self):
        self.move_to_seat()



class Seat(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y, seat_diameter, row, column):
        super().__init__()
        self.size = 0.05
        self.seat_id = {'row' : row, 'column' : column}

        self.image_seat_empty = pygame.image.load('art/seat_empty_2.png').convert_alpha()
        self.image_seat_taken = pygame.image.load('art/seat_taken.png').convert_alpha()
        self.image = self.image_seat_empty        # Change this to animate state of passenger
        self.resize_image()

        self.x = position_x
        self.y = position_y

        self.rect = self.image.get_rect(center = (self.x, self.y))
    
    def resize_image(self):
        screen_width, screen_height = pygame.display.get_surface().get_size()
        size = int(screen_width/8)
        self.image = pygame.transform.scale(self.image, (size, size))