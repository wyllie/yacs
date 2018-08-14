from __future__ import absolute_import, division, print_function

from Yacs.yacs import Yacs


def test_init():
    yac = Yacs()
    assert yac.eye_type == 'oo'
    assert yac.wrap_len == 30
    assert yac.yac_saying == 'Moooo!'
