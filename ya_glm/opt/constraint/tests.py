import numpy as np
from unittest import TestCase
from ya_glm.opt.constraint import convex

class TestProjectionsOnConstraints(TestCase):
    def setUp(self):
        pass

    def assert_arrays_close(self, test_array, ref_array):
        "Custom assertion for arrays being almost equal"
        try:
            np.testing.assert_allclose(test_array, ref_array)
        except AssertionError:
            self.fail()

    def test_Positive(self):
        cons = convex.Positive()
        v = np.array([-1, 0, 2, 3, -2])
        self.assert_arrays_close(cons.prox(v), [0, 0, 2, 3, 0])
        self.assertEqual(cons.prox(-2), 0)


    def test_L2Ball(self):
        cons1 = convex.L2Ball(1)
        self.assert_arrays_close(cons1.prox([0,0,0]), [0,0,0])
        self.assert_arrays_close(cons1.prox([1,0,0]), [1,0,0])
        self.assert_arrays_close(cons1.prox([0.5,0,0]), [0.5,0,0])
        self.assert_arrays_close(cons1.prox([1,1,1]), np.array([1,1,1])/np.sqrt(3))
        self.assert_arrays_close(cons1.prox([1,-1,1]), np.array([1,-1,1])/np.sqrt(3))

        cons4 = convex.L2Ball(4)
        self.assert_arrays_close(cons4.prox([0,0,0]), [0,0,0])
        self.assert_arrays_close(cons4.prox([1,0,0]), [1,0,0])
        self.assert_arrays_close(cons4.prox([0.5,0,0]), [0.5,0,0])
        self.assert_arrays_close(cons4.prox([-4,3,0]), np.array([-4,3,0])/(5/4))
