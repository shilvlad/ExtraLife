
def Egraphics():
    # здесь происходит инициация, создание объектов и др.
    pygame.init()
    sc = pygame.display.set_mode((600, 400))
    clock = pygame.time.Clock()

    # если надо до цикла отобразить объекты на экране
    pygame.display.update()

    # главный цикл
    while True:

        # задержка
        clock.tick(FPS)

        # цикл обработки событий
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()

        pygame.draw.rect(sc, PREDATOR_COLOR, (20, 20, DISCRETENESS, DISCRETENESS))

        pygame.draw.rect(sc, HERBIVORES_COLOR, (40, 40, DISCRETENESS, DISCRETENESS))

        pygame.draw.rect(sc, HERBIVORES_COLOR, (60, 60, DISCRETENESS, DISCRETENESS))

        # обновление экрана
        pygame.display.update()


