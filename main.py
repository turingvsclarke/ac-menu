import pygame

pygame.init()

def main():
  screen = pygame.display.set_mode((320, 240))

  keepGoing = True
  while keepGoing:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        keepGoing = False

    screen.fill((255, 255, 255))
    pygame.display.update()

  pygame.quit()


if __name__ == "__main__":
  main()
