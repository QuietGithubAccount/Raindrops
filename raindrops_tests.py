import unittest
from raindrops import raindrops

class RaindropsTest(unittest.TestCase):

#Pling tests
    def test_value_3(self):
        self.assertEqual(raindrops(3), "Pling")

    def test_value_9(self):
        self.assertEqual(raindrops(9), "Pling")

    def test_value_12(self):
        self.assertEqual(raindrops(12), "Pling")

#Plang tests
    def test_value_5(self):
        self.assertEqual(raindrops(5), "Plang")

    def test_value_10(self):
        self.assertEqual(raindrops(10), "Plang")

    def test_value_5000(self):
        self.assertEqual(raindrops(5000), "Plang")
#Plong tests

    def test_value_7(self):
        self.assertEqual(raindrops(7), "Plong")

    def test_value_14(self):
        self.assertEqual(raindrops(14), "Plong")

        #Example case
    def test_value_28(self):
        self.assertEqual(raindrops(28), "Plong")

#Return tests

    #Prime number testing for returns
    def test_value_2(self):
        self.assertEqual(raindrops(2), '2')

    def test_value_11(self):
        self.assertEqual(raindrops(11), '11')

    def test_value_13(self):
        self.assertEqual(raindrops(13), '13')

    def test_value_17(self):
        self.assertEqual(raindrops(17), '17')

    def test_value_19(self):
        self.assertEqual(raindrops(19), '19')

    def test_value_23(self):
        self.assertEqual(raindrops(23), '23')
    #Example case
    def test_value_34(self):
        self.assertEqual(raindrops(34), '34')

#Compound tests

    def test_value_21(self):
        self.assertEqual(raindrops(21), "PlingPlong")

    def test_value_15(self):
        self.assertEqual(raindrops(15), "PlingPlang")

    def test_value_63(self):
        self.assertEqual(raindrops(63), "PlingPlong")

    def test_value_105(self):
        self.assertEqual(raindrops(105), "PlingPlangPlong")

#Edge cases
    def test_value_1(self):
        self.assertEqual(raindrops(1), '1')

        #Exponent test
    def test_2_to_the_3(self):
        self.assertEqual(raindrops(8), '8')

if __name__ == "__main__":
    unittest.main()
