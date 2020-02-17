import unittest

from models.glasses import Glasses
from models.prescription import Prescription


class TestGlasses(unittest.TestCase):
    def test_createGlasses(self):
        right_eye_prescription = Prescription(-3.50, -1.00, 90, None)
        left_eye_prescription = Prescription(-3.50, -1.00, 90, None)

        glasses = Glasses("A1 - LionsClub1", right_eye_prescription, left_eye_prescription)
        self.assertEqual(glasses.code, "A1 - LionsClub1")
