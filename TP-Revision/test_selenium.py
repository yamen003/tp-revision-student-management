import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

URL = "http://127.0.0.1:5000"


class TestWebInterface(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        # Retirez la ligne suivante pour voir le navigateur pendant l'exécution
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        cls.driver = webdriver.Chrome(options=options)  # Selenium Manager gère le driver

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def submit(self, grades):
        self.driver.get(URL)
        field = self.driver.find_element(By.ID, "grades")
        button = self.driver.find_element(By.ID, "calculate")
        field.clear()
        field.send_keys(grades)
        button.click()

    def text_of(self, element_id):
        return self.driver.find_element(By.ID, element_id).text

    def test_1_average_15(self):
        self.submit("12,15,18")
        self.assertEqual(self.text_of("average"), "15")

    def test_2_average_10(self):
        self.submit("10,10,10")
        self.assertEqual(self.text_of("average"), "10")

    def test_3_mention_echec(self):
        self.submit("8,8,8")
        self.assertEqual(self.text_of("mention"), "Échec")

    def test_4_mention_excellent(self):
        self.submit("18,18,18")
        self.assertEqual(self.text_of("mention"), "Excellent")

    def test_5_error_grade_above_20(self):
        self.submit("12,25,18")
        self.assertIn("Erreur", self.text_of("error"))

    def test_6_error_empty_input(self):
        self.submit("")
        self.assertIn("Erreur", self.text_of("error"))


if __name__ == "__main__":
    unittest.main()
