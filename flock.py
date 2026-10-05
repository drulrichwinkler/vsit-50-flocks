"""Möwenschwärme – das Quiz aus der Vorlesung.

Nach Brian Lonsdorf, „Mostly Adequate Guide to Functional Programming“, Kapitel 1.

Starten:  python flock.py
Prüfen:   pytest tests/test_flock.py
"""


class Flock:
    def __init__(self, n):
        self.seagulls = n

    def conjoin(self, other):
        self.seagulls += other.seagulls
        return self

    def breed(self, other):
        self.seagulls *= other.seagulls
        return self


def quiz():
    flock_a, flock_b, flock_c = Flock(4), Flock(2), Flock(0)

    result = (flock_a.conjoin(flock_c)
                     .breed(flock_b)
                     .conjoin(flock_a.breed(flock_b))
                     .seagulls)
    return result


if __name__ == "__main__":
    print(quiz())   # ?
