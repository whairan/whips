import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color, speed, controls):
        super().__init__()
        self.pos = pygame.Vector2(x, y)
        self.radius = radius
        self.color = pygame.Color(color)
        self.speed = speed
        self.controls = controls
        self.direction = pygame.Vector2(0, 0)

        # Create image and rect for sprite
        size = radius * 2 + 4
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self._draw_base()

    def _draw_base(self):
        # Draw circle
        self.image.fill((0, 0, 0, 0))
        pygame.draw.circle(self.image, self.color,
                           (self.radius + 2, self.radius + 2), self.radius)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        dir = pygame.Vector2(0, 0)
        if keys[self.controls['up']]: dir.y = -1
        if keys[self.controls['down']]: dir.y = 1
        if keys[self.controls['left']]: dir.x = -1
        if keys[self.controls['right']]: dir.x = 1

        if dir.length_squared() > 0:
            self.direction = dir.normalize()
            self.pos += self.direction * self.speed
            self.rect.center = self.pos

    def update(self, *args):
        self.handle_input()
        self._draw_base()
        self._draw_triangles()

    def _draw_triangles(self):
        # draw 4 small triangles at cardinal points, pointing outward
        center = pygame.Vector2(self.radius + 2, self.radius + 2)
        for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            base = center + pygame.Vector2(dx, dy) * (self.radius * 0.6)
            perp = pygame.Vector2(-dy, dx) * (self.radius * 0.2)
            tip = center + pygame.Vector2(dx, dy) * self.radius
            pts = [base - perp, base + perp, tip]
            pygame.draw.polygon(self.image, pygame.Color('white'), pts)
