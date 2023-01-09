import pygame


def chess(screen, n):
    print('tipo sam pishu', n)


if __name__ == '__main__':
    a, n = input().split()
    if type(a) == float or type(n) == float or int(a) % int(n) != 0:
        print('Неправильный формат ввода')
    else:
        a, n = int(a), int(n)
        pygame.init()
        size = width, height = a, a
        screen = pygame.display.set_mode(size)
        chess(screen, n)
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
