game_size = 3
header = footer = '-' * (game_size * 3)
game_progress = input()

print(header)
for i in range(0, pow(game_size, 2), game_size):
    print('|', *game_progress[i: i + game_size], '|')
print(footer)
