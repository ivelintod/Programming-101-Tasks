class IvanCount:

    def __init__(self, word, table, rows, columns):
        self.word = word
        self.table = table
        self.rows = rows
        self.columns = columns
        self.occurances = 0

    def combine_ind_changers(self):
        changers = [[(i, i), (-i, -i), (i, -i), (-i, i),
        (i, 0), (-i, 0), (0, i), (0, -i)] for i in range(1, len(self.word))]

        zipped_changers = zip(*[changers[i] for i in range(len(self.word) - 1)])

        return zipped_changers


    def manage_indices(self, i, j, map):
        letters = [x for x in self.word[1:]]
        ind_changers = self.combine_ind_changers()
        addition = True
        ind_changers = list(ind_changers)
        for ind_changer in ind_changers:
            for ind, letter in zip(ind_changer, letters):
                try:
                    if map[i + ind[0]][j + ind[1]] != letter or i + ind[0] < 0 or j + ind[1] < 0:
                        addition = False
                        break
                except IndexError:
                    addition = False
                    break

            if addition:
                self.occurances += 1
                print(i, j)

            addition = True



    def get_occurances(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.table[i][j] == self.word[0]:
                    self.manage_indices(i, j, self.table)

        return self.occurances


def main():

    table = list()
    word = input('Enter word: ')
    num_rows = int(input('Enter num of rows: '))
    num_cols = int(input('Enter num of columns: '))
    for i in range(num_rows):
        table.append([x for x in input()])

    w = IvanCount(word, table, num_rows, num_cols)
    print(w.get_occurances())

if __name__ == '__main__':
    main()
