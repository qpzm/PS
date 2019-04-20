import sys

INF = 3000001


def main():
    NUM_STEPS = int(input())
    max_scores, scores = [[None, None] for _ in range(NUM_STEPS)], []

    for _ in range(NUM_STEPS):
        scores.append(int(sys.stdin.readline()))

    print(calc_max_score(max_scores, scores, NUM_STEPS - 1, 0))


def calc_max_score(max_scores, scores, idx, streak):
    if idx == -1:
        return 0
    elif idx == 0:
        max_scores[idx][streak] = scores[idx]
        return max_scores[idx][streak]
    else:
        if max_scores[idx][streak] is None:
            if streak == 1:
                max_lower_steps = calc_max_score(max_scores, scores, idx - 2, 0)
            else:
                max_lower_steps = max([
                    calc_max_score(max_scores, scores, idx - 1, (streak + 1) % 2),
                    calc_max_score(max_scores, scores, idx - 2, 0)
                ])
            max_scores[idx][streak] = scores[idx] + max_lower_steps
        return max_scores[idx][streak]


if __name__ == "__main__":
    main()
