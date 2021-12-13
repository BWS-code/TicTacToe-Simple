game_size = 3

winnerX = ''.join('X' for x in range(game_size))
winnerO = ''.join('O' for x in range(game_size))

header = footer = '-' * (game_size * 3)
game_progress = input()

ends_of_game = ['Impossible', 'X wins', 'O wins', 'Draw', 'Game not finished']

rules = [
    game_progress[:game_size],
    game_progress[game_size: game_size * 2],
    game_progress[game_size * 2: game_size * 3],

        game_progress[::game_size],
        game_progress[1::game_size],
        game_progress[2::game_size],

            game_progress[::game_size + 1],
            game_progress[game_size - 1: pow(game_size, 2) - game_size + 1:
            game_size - 1]
    ]
       
       
print(header)
for i in range(0, pow(game_size, 2), game_size):
    print('|', *game_progress[i: i + game_size], '|')
print(footer)
                                  
if winnerX in rules and winnerO in rules and abs(game_progress.count('X') - game_progress.count('O')) > 0 \
    or \
abs(game_progress.count('X') - game_progress.count('O')) > 1:
    print(ends_of_game[0])
elif winnerX in rules:
    print(ends_of_game[1])
elif winnerO in rules:
    print(ends_of_game[2])
elif '_' not in game_progress:
    print(ends_of_game[3])
elif '_' in game_progress:
    print(ends_of_game[4])


