from function import *

import random

window = pygame.display.set_mode(size_window)
pygame.display.set_caption("Space Shooter")



def run():
    game = True
    clock = pygame.time.Clock()
    start_time_bot = 0

    hero = Hero(15, 15, size_hero[0], size_hero[1], hero_image_list, 5, 5)

    background = Background(size_bg[0], size_bg[1], bg_image)
    
    
    font = pygame.font.Font(None, 35)

    while game:
        events = pygame.event.get()
        background.move(window)

        window.blit(hp_image, (5, 5))
        window.blit(font.render(f"x{hero.hp}", True, (250,100,50)), (27, 5))
        hero.move(window)

        hero.minus_heart(bullet_list_bot)

        end_time_bot = pygame.time.get_ticks()
        if end_time_bot - start_time_bot >= 2000:
            start_time_bot = end_time_bot
            Bot.bot_list.append(Bot(
                random.randint(0, size_window[0] - size_bot[0]),
                                - size_bot[1],
                                size_bot[0],
                                size_bot[0],
                                bot_image_list,
                                1,
                                1,
                                1
                                ))
        for bot in Bot.bot_list:
                bot.move(window)
                bot.remove(bullet_list_hero)
                bot.shoot(end_time_bot)
                bot.collide_hero(hero)


        for bullet in bullet_list_hero:
                bullet.move(window)
                if bullet.y < -10:
                     bullet_list_hero.remove(bullet)
        for bullet in bullet_list_bot:
                bullet.move(window)
        if hero.hp == 0:
             game = False

        for event in events:
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_w:
                    hero.move_check["up"] = True
                if event.key == pygame.K_s:
                    hero.move_check["down"] = True
                if event.key == pygame.K_a:
                    hero.move_check["left"] = True
                if event.key == pygame.K_d:
                    hero.move_check["right"] = True
                if event.key == pygame.K_SPACE:
                    bullet_list_hero.append(Bullet(
                                            hero.centerx, hero.y, 10, 20, None, colors["RED"], -5))
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    hero.move_check["up"] = False
                if event.key == pygame.K_s:
                    hero.move_check["down"] = False
                if event.key == pygame.K_a:
                    hero.move_check["left"] = False
                if event.key == pygame.K_d:
                    hero.move_check["right"] = False   




        clock.tick(FPS)
        pygame.display.flip()

run()