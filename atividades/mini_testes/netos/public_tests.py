import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        global netos
        undertest = __import__(module)
        netos = getattr(undertest, 'netos', None)   
    
    def test_exemplo(self):
        pais = {
            "homer": ("abraham", "mona"),
            "herb": ("abraham", None),
            "marge": ("clancy", "jackie"),
            "bart": ("homer", "marge"), 
            "lisa": ("homer", "marge"),
            "maggie": ("homer", "marge"),
        }

        assert netos("homer", pais) == []
        assert netos("abraham", pais) == ["bart", "lisa", "maggie"]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
