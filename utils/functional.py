from functools import reduce


def functional_demo():
    durations = [1, 2, 3, 6, 12]

    doubled = list(map(lambda month: month * 2, durations))
    long_terms = list(filter(lambda month: month >= 3, durations))
    total_duration = reduce(lambda total, month: total + month, durations)

    return {
        "doubled": doubled,
        "long_terms": long_terms,
        "total_duration": total_duration,
    }


if __name__ == "__main__":
    print(functional_demo())
