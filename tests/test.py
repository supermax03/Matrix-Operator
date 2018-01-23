import unittest
from matrix import Matrix

class Test(unittest.TestCase):
    def test_add(self):
        m1 = Matrix([[1, 2, 3], [4, 5, 6]])
        m2 = Matrix([[1, 2, 3], [4, 5, 6]])
        self.assertTrue(m1.equal(m2), "Son diferentes")
    def test_ithasthesameorder(self):
        m1 = Matrix([[1, 2, 3], [4, 5, 6]])
        m2 = Matrix([[7, 8, 0], [7, 8, 9]])
        self.assertTrue(m1.hasthesameorder(m2), "Tienen diferente orden")
    def test_isidentitymatrix(self):
        m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertTrue(m1.isidentitymatrix(), "No es identidad")
    def test_isnotsquarematrix(self):
        m1=Matrix([[1,2,3],[1,2,3]])
        self.assertFalse(m1.issquarematrix(),"Es una matriz cuadrada")
    def test_issquarematrix(self):
         m1=Matrix([[1,2,3],[2,3,4],[5,6,7]])
         self.assertTrue(m1.issquarematrix(), "No es una matriz cuadrada")
    def test_getorder(self):
        m1=Matrix([[1,1,1]])
        self.assertTupleEqual(m1.getOrder(),(1,3),"El orden no es correcto")
if __name__ == '__main__':
    unittest.main(verbosity=2)
