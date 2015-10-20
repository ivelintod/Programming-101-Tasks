# pass x and y as keyword arguments to the calc_position function
def calc_position(directions, **current):
    curr_x = current['x']
    curr_y = current['y']
    def_dirs = {
                '>': 1,
                '<': -1,
                '^': -1,
                'v': 1
    }

    for d in directions:
        if d == '>':
            curr_x += def_dirs['>']
        elif d == '<':
            curr_x += def_dirs['<']
        elif d == '^':
            curr_y += def_dirs['^']
        elif d == 'v':
            curr_y += def_dirs['v']
        elif d == '~':
            for k, v in def_dirs.items():
                def_dirs[k] = -v

    return (curr_x, curr_y)

print(calc_position('>>><<<~>>>~^^^', x=0, y=0))
