import unittest
from YOLO_WORLD_EfficientSAM import process_categories

class TestYOLOWorldEfficientSAM(unittest.TestCase):

    def test_process_categories(self):
        # Test with a single category
        self.assertEqual(process_categories("cat"), ["cat"])
        # Test with multiple categories
        self.assertEqual(process_categories("cat, dog, bird"), ["cat", "dog", "bird"])
        # Test with extra whitespace
        self.assertEqual(process_categories(" cat ,  dog  , bird "), ["cat", "dog", "bird"])
        # Test with empty string
        self.assertEqual(process_categories(""), [])

if __name__ == '__main__':
    unittest.main()
