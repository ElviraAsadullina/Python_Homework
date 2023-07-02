def is_harmless_pair_1(cur_rank):
    for i in range(len(cur_rank)):
        for j in range(i + 1, len(cur_rank)):
            if cur_rank[i][0] == cur_rank[j][0] or cur_rank[i][1] == cur_rank[j][1] \
                    or abs(cur_rank[i][0] - cur_rank[j][0]) == abs(cur_rank[i][1] - cur_rank[j][1]):
                return False
    return True


def is_harmless_pair_2(row, col, cur_ranking):
    if row == 0:
        return True
    for r in range(0, row):
        if col == cur_ranking[r] or abs(row - r) == abs(col - cur_ranking[r]):
            return False
    return True


def generate_ranking(row, queens_count_, cur_ranking):
    for col in range(queens_count_):
        if not is_harmless_pair_2(row, col, cur_ranking):
            continue
        else:
            cur_ranking[row] = col
            if row == (queens_count_ - 1):
                rankings_.append(list(zip(range(len(cur_ranking)), cur_ranking.copy())))
            else:
                generate_ranking(row + 1, queens_count_, cur_ranking)
    return rankings_


rankings_ = []

# if __name__ == '__main__':
#     generate_ranking(0, queens_count_, cur_ranking)
#     print(f'{len(rankings_)} rankings found: ', *rankings_, sep='\n')
