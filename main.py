import pygame
import game
import random

game.init()
pygame.init()

size = (800, 600)

gameDisplay = pygame.display.set_mode(size)
pygame.display.set_caption('A bit Racey')


clock = pygame.time.Clock()

terrain = [[game.blocks[0] if random.randint(0, 5) == 0 else game.blocks[1] for _ in range(20)] for _ in range(20)]
player = game.Player(int(len(terrain)/2),int(len(terrain[0])/2), game.Texture([game.Colored_chr(chr(9476), (255, 205, 148)), game.Colored_chr(chr(9532), (255, 205, 148)), game.Colored_chr(chr(9600), (255, 205, 148))]))
game_font = pygame.font.SysFont("Arial", 20)


def render_texture(texture, x, y):
    if type(texture.colored_chr) == list:
        for i in texture.colored_chr:
            gameDisplay.blit(game_font.render(i.character, 0, i.color), (x, y))
    else:
        gameDisplay.blit(game_font.render(texture.colored_chr.character, 0, texture.colored_chr.color), (x, y))


def render():
    gameDisplay.blit(game_font.render("TEST", 0, (255, 255, 255)), (0, 0))
    size = game_font.size(chr(219))
    x_text = 0
    y_text = size[1]

    for y in range(len(terrain)):
        for x in range(len(terrain[0])):

            render_texture(terrain[y][x].texture, x_text, y_text)

            if y == player.y and x == player.x:
                render_texture(player.texture, x_text, y_text)

            x_text += size[0]*2

        x_text = 0
        y_text += size[1]


crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.x += 1
            if event.key == pygame.K_LEFT:
                player.x -= 1
            if event.key == pygame.K_UP:
                player.y -= 1
            if event.key == pygame.K_DOWN:
                player.y += 1

        print(event)

    gameDisplay.fill((0, 0, 0))

    render()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()