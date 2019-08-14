# -*- coding: utf-8 -*-
# Author: Jiajun Ren <jiajunren0522@gmail.com>

import os
import pickle

import numpy as np
import pytest

from ephMPS.mps import Mps
from ephMPS.mps.solver import construct_mps_mpo_2, optimize_mps
from ephMPS.mps.tests import cur_dir
from ephMPS.tests.parameter import mol_list

nexciton = 1
procedure = [[20, 0.4], [20, 0.2], [20, 0.1], [20, 0], [20, 0]]


def test_csvd(switch_to_64backend):
    # the pickle file is in 64bit backend
    np.random.seed(0)
    mps1, mpo = construct_mps_mpo_2(mol_list, procedure[0][0], nexciton)
    mps1.threshold = 1e-6
    mps1.optimize_config.procedure = procedure
    optimize_mps(mps1, mpo)
    mps1.compress()
    mps2 = Mps.load(mol_list, os.path.join(cur_dir, "test_svd_qn.npz"))
    assert mps1.distance(mps2) == pytest.approx(0, abs=1e-5)
