class TicTacToe:
    def __init__(self, game_size=3):
        self.game_size = game_size
        self.header_len = '-' * (game_size * 3)
        self.game_progress = [x for x in input('Enter cells:')]
        self.ends_of_game = ['Impossible', 'X wins', 'O wins', 'Draw', 'Game not finished']
        self.winnerX = ''.join('X' for x in range(self.game_size))
        self.winnerO = ''.join('O' for x in range(self.game_size))
    
    def index_by_coords(self, row, col):
        if row == 2:
            return row + col 
        return row**2 - (row - col + 1)
    
    def get_board(self):
        print(self.header_len)
        for i in range(0, pow(self.game_size, 2), self.game_size):
            print('|', *self.game_progress[i: i + self.game_size], '|')
        print(self.header_len)

    def get_rules(self):
        self.rules = [self.game_progress[:self.game_size],
                      self.game_progress[self.game_size: self.game_size * 2],
                      self.game_progress[self.game_size * 2: self.game_size * 3],

                      self.game_progress[::self.game_size],
                      self.game_progress[1::self.game_size],
                      self.game_progress[2::self.game_size],

                      self.game_progress[::self.game_size + 1],
                      self.game_progress[self.game_size - 1: pow(self.game_size, 2) - self.game_size + 1:
                                         self.game_size - 1]
                      ]

    def check_state(self):
        if self.winnerX in self.rules and self.winnerO in self.rules and \
                abs(self.game_progress.count('X') - self.game_progress.count('O')) > 0 or \
                abs(self.game_progress.count('X') - self.game_progress.count('O')) > 1:
            print(self.ends_of_game[0])
        elif self.winnerX in self.rules:
            print(self.ends_of_game[1])
        elif self.winnerO in self.rules:
            print(self.ends_of_game[2])
        elif '_' not in self.game_progress:
            print(self.ends_of_game[3])
        elif '_' in self.game_progress:
            print(self.ends_of_game[4])

    def entry_check_OK_user(self):
        while 555 < 666:
            coords = input('Enter the coordinates:').split(' ')
            self.row, self.col = coords
            if not self.col.isnumeric() or not self.row.isnumeric():
                print('You should enter numbers!')
            elif not all([x in [str(x) for x in range(1, self.game_size + 1)] for x in [self.col, self.row]]):
                print(f'Coordinates should be from 1 to {self.game_size}!')
            elif self.game_progress[self.index_by_coords(int(self.row), int(self.col))] != '_':
                print('This cell is occupied! Choose another one!')
            else:
                return True
                break

    def make_move(self, who, mark):
        if who == 'user':
            if self.entry_check_OK_user():
                move_cell = self.index_by_coords(int(self.row), int(self.col))
                self.game_progress[move_cell] = mark

    def main(self):
        self.get_board()
        self.make_move('user', 'X')
        self.get_board()


BWS_game = TicTacToe()
BWS_game.main()
