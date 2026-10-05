"""Spezifikation für flock.py. Anfangs schlagen diese Tests fehl – das ist Absicht."""

import pytest

from flock import Flock, quiz


def test_quiz_ergibt_die_formel():
    # (4 + 0) * 2 + 4 * 2
    assert quiz() == 16


def test_conjoin_laesst_beide_schwaerme_unveraendert():
    a, c = Flock(4), Flock(3)
    a.conjoin(c)
    assert (a.seagulls, c.seagulls) == (4, 3)


def test_breed_laesst_beide_schwaerme_unveraendert():
    a, b = Flock(4), Flock(2)
    a.breed(b)
    assert (a.seagulls, b.seagulls) == (4, 2)


def test_ergebnis_ist_ein_neuer_schwarm():
    a, b = Flock(4), Flock(2)
    r = a.conjoin(b)
    assert r is not a and r is not b
    assert r.seagulls == 6


@pytest.mark.parametrize("a, b, c", [(4, 2, 0), (4, 2, 3), (1, 5, 7)])
def test_ausdruck_ist_die_formel_die_er_zu_sein_scheint(a, b, c):
    fa, fb, fc = Flock(a), Flock(b), Flock(c)
    result = (fa.conjoin(fc)
                .breed(fb)
                .conjoin(fa.breed(fb))
                .seagulls)
    assert result == (a + c) * b + a * b
