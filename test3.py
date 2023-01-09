import pygame


def chess(screen, a, n):
    if n % 2 == 0:
        even = True
    else:
        even = False
    x = 0
    while x < a:
        if even:
            y = a / n
        else:
            y = 0
        while y < a:
            pygame.draw.rect(screen, (0, 0, 0), (x, y, a / n, a / n))
            y += a / n * 2
        x += a / n
        if even:
            even = False
        else:
            even = True


if __name__ == '__main__':
    a, n = input().split()
    if int(a) != float(a) or int(n) != float(n) or int(a) % int(n) != 0:
        print('Неправильный формат ввода')
    else:
        a, n = int(a), int(n)
        pygame.init()
        size = width, height = a, a
        screen = pygame.display.set_mode(size)
        screen.fill((255, 255, 255))
        chess(screen, a, n)
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
