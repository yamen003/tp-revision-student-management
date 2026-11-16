import unittest

from student_manager import (
    calculate_average,
    get_mention,
    is_admitted,
    validate_grades,
)


class TestStudentManager(unittest.TestCase):
    # --- calculate_average ---
    def test_average_normal(self):
        self.assertEqual(calculate_average([12, 15, 18]), 15)

    def test_average_identical_grades(self):
        self.assertEqual(calculate_average([10, 10, 10]), 10)

    def test_average_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_average([])

    # --- get_mention ---
    def test_mention_echec(self):
        self.assertEqual(get_mention(8), "Échec")

    def test_mention_bien(self):
        self.assertEqual(get_mention(15), "Bien")

    def test_mention_excellent(self):
        self.assertEqual(get_mention(18), "Excellent")

    # --- is_admitted ---
    def test_admitted(self):
        self.assertTrue(is_admitted(12))

    def test_not_admitted(self):
        self.assertFalse(is_admitted(9))

    def test_admitted_at_exactly_10(self):
        # Test ajouté à l'étape 8 : une moyenne égale à 10 donne le statut admis
        self.assertTrue(is_admitted(10))

    # --- validate_grades ---
    def test_valid_grades(self):
        self.assertTrue(validate_grades([12, 15, 18]))

    def test_invalid_empty_list(self):
        self.assertFalse(validate_grades([]))

    def test_invalid_grade_above_20(self):
        self.assertFalse(validate_grades([12, 25, 18]))

    def test_invalid_negative_grade(self):
        self.assertFalse(validate_grades([-2, 12, 15]))


if __name__ == "__main__":
    unittest.main()
