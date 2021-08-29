from typing import List


class Solver:

    def __init__(self, ranked_scores: List[int], player_score: int) -> None:
        self.index = 0
        self.ranked_scores = ranked_scores.copy()
        self.ranked_scores_backup = self.ranked_scores.copy()
        self.player_score = player_score

    @staticmethod
    def is_between(_list: List[int], number: int) -> bool:
        return False if not _list else _list[0] >= number >= _list[-1]

    def find_index(self) -> int:
        first_half = self.ranked_scores[:len(self.ranked_scores) // 2]
        second_half = self.ranked_scores[len(self.ranked_scores) // 2:]

        if len(first_half) == 1 and len(second_half) == 1 and first_half[0] >= self.player_score >= second_half[0]:
            return self.index

        if Solver.is_between(first_half, self.player_score):
            self.index += len(first_half) // 2
            self.ranked_scores = first_half
            return self.find_index()
        elif Solver.is_between(second_half, self.player_score):
            self.index += len(first_half) + len(second_half) // 2
            self.ranked_scores = second_half
            return self.find_index()
        elif first_half:
            return self.index + len(first_half)  # TODO

        return self.index

    def check_if_first_or_last(self) -> int:
        first_half = self.ranked_scores[:len(self.ranked_scores) // 2]
        second_half = self.ranked_scores[len(self.ranked_scores) // 2:]
        if first_half and first_half[0] <= self.player_score:
            return 1
        if second_half and second_half[-1] >= self.player_score:
            return len(self.ranked_scores) + 1

    def find_rank(self) -> int:
        position = self.check_if_first_or_last()
        if not position:
            position = self.find_index()
        part = self.ranked_scores_backup[:position]
        position = position - (len(part) - len(set(part)))
        return position


def climbing_leaderboard(ranked, player):
    ranks = []
    for score in player:
        rank = Solver(ranked, score).find_rank()
        ranks.append(rank)
    return ranks


if __name__ == '__main__':
    result = climbing_leaderboard(
        ranked=[100, 90, 90, 80, 75, 60],
        player=[50, 65, 77, 90, 102]
    )
    print(result)
