import pygame


def chess(screen, n):
    screen.fill((255, 255, 255))
    if n % 2 == 0:
        flag = 1
    else:
        flag = 0
    x = 0
    while x < a:
        if flag:
            y = a // n
        else:
            y = 0
        while y < a:
            pygame.draw.rect(screen, (0, 0, 0), (x, y, a // n, a // n), width=0)
            y += a // n * 2
        x += a // n
        flag = 1 - flag
 
 
if __name__ == '__main__':
    pygame.init()
    try:
        a, n = input().split()
        if int(a) != float(a) or int(n) != float(n) or int(a) % int(n) != 0:
            print('Неправильный формат ввода')
        else:
            a = int(a)
            n = int(n)
            size = width, height = a, a
            screen = pygame.display.set_mode(size)
            chess(screen, n)
            pygame.display.flip()
            while pygame.event.wait().type != pygame.QUIT:
                pass
            pygame.quit()
    except Exception:
        print('Неправильный формат ввода')
 