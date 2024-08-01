import unittest
from distincoes.services import split_producers

class TestSplitProducers(unittest.TestCase):

    def test_split_producers(self):
        # Teste com diferentes casos de entrada
        self.assertEqual(split_producers("Producer 1, Producer 2 and Producer 3"), 
                         ["Producer 1", "Producer 2", "Producer 3"])
        self.assertEqual(split_producers("Producer 1, Producer 2, and Producer 3"), 
                         ["Producer 1", "Producer 2", "Producer 3"])
        self.assertEqual(split_producers("Producer 1 and Producer 2"), 
                         ["Producer 1", "Producer 2"])
        self.assertEqual(split_producers("Producer 1"), 
                         ["Producer 1"])
        self.assertEqual(split_producers("Producer 1, Producer 2, and Producer 3"), 
                         ["Producer 1", "Producer 2", "Producer 3"])

if __name__ == '__main__':
    unittest.main()

