
import Yacs.yacs as y

def test_init():
    yac = y.Yacs()
    assert yac.eye_type == 'oo'
    assert yac.wrap_len == 30
    assert yac.yac_saying == 'Moooo!'
