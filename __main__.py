# MAIN FILE FOR LOADING THE GAME

import pygame
from Resources import constants
from Classes import square_methods, debug_methods, bot_gameplay

pygame.init()
pygame.display.set_caption('TIC TAC TOE !!!')
screen = pygame.display.set_mode((constants.SCREEN_X, constants.SCREEN_Y))

grid = square_methods.make_empty_grid()
bot_grid = [-1 for _ in range(9)]

bot = bot_gameplay.bot()

QUIT = False
player_turn = True
debug_pressed = False
game_complete = False
game_outcome = None

while not QUIT:

    game_outcome = square_methods.game_outcome(grid)

    if game_complete or game_outcome == 'x' or game_outcome == 'o':
        QUIT = True
        continue

    modified_now = False
    for i in grid:
        pygame.draw.rect(screen, constants.GRID_COLOR, i.return_empty_rectangle())
        pygame.draw.line(screen, constants.LINE_COLOR, i.border[0][0], i.border[0][1])
        pygame.draw.line(screen, constants.LINE_COLOR, i.border[1][0], i.border[1][1])
        pygame.draw.line(screen, constants.LINE_COLOR, i.border[2][0], i.border[2][1])
        pygame.draw.line(screen, constants.LINE_COLOR, i.border[3][0], i.border[3][1])
        if i.symbol_value == 'x':
            screen.blit(constants.X_ICON, (i.x, i.y))
        if i.symbol_value == 'o':
            screen.blit(constants.O_ICON, (i.x, i.y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            QUIT = True
            break
        if event.type == pygame.MOUSEBUTTONUP and player_turn:
            if len(square_methods.find_available(bot_grid)) <= 0:
                # END THE GAME
                game_complete = True
                break
            pos = pygame.mouse.get_pos()
            square_value = square_methods.find_block(grid, pos[0], pos[1])
            current_symbol = square_value.symbol_value
            if current_symbol is None:
                square_value.symbol_value = 'x'
            original_values = (square_methods.range_finder(pos[0]), square_methods.range_finder(pos[1]))
            bot_grid[constants.INDICES[original_values]] = 'x'

            # DEBUG STATEMENTS
            print("original values are ", original_values)
            print("co-ordinates are ", pos)
            print("Bot grid index is ", constants.INDICES[original_values])
            square_methods.find_block(grid, pos[0], pos[1])

            player_turn = False
            modified_now = True

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        debug_pressed = True

    if not modified_now and not player_turn:
        # handle computer turn
        options = square_methods.find_available(bot_grid)
        if len(options) <= 0:
            game_complete = True
            break
        else:
            temp = [j for j in bot_grid]
            o_wins = False
            index = -1
            for j in options:
                temp[j] = 'o'
                sample_outcome = bot.return_prediction(temp)
                # DEBUG
                print("main - sample outcome for ", temp, " is ", sample_outcome)
                if sample_outcome == 'o':
                    o_wins = True
                    index = j
                    break
                else:
                    temp = [j for j in bot_grid]
            if o_wins:
                print("Index selected by computer is ", index)
                required_block = grid[index]
                required_block.symbol_value = 'o'
            else:
                print("NO INDEX FOUND ", options[0])
                required_block = grid[options[0]]
                required_block.symbol_value = 'o'
                temp[options[0]] = 'o'
            bot_grid = temp
        player_turn = True

    if debug_pressed and constants.DEBUG_ENABLED:

        print("bot grid values are ")
        print(bot_grid)
        print("squares values are ")
        for j in grid:
            print(j.symbol_value, end=' ')
        print()

        debug_pressed = not debug_pressed
        print("FINAL GAME OUTCOME : ", game_outcome)

    pygame.display.flip()

print("GAME COMPLETE ")
print("OUTCOME : ", game_outcome)

QUIT = False
text_surface = ''
if game_outcome == 'x':
    text_surface = constants.text_surface_creator('Congratulations Player : X ')
elif game_outcome == 'o':
    text_surface = constants.text_surface_creator('Congratulations Player : O ')
else:
    text_surface = constants.text_surface_creator('Game ended in a Draw')
while not QUIT:
    screen.fill((0, 0, 0))
    screen.blit(text_surface, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            QUIT = True
    pygame.display.flip()
