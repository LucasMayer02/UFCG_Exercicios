import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global devedores
        undertest = __import__(module)
        devedores = getattr(undertest, 'devedores', None)

    def test_1_vazio(self):
        contas = { 'Ana':1000, 'Antonio':-500, 'William':0, 'Carlos':2500, 'Kate':-1300 }
        assert devedores(contas) == 2

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
