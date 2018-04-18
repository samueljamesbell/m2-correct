import unittest

import correct


class CorrectSentenceTest(unittest.TestCase):

    def test_no_corrections(self):
        sentence = 'There are two points supporting this argument .'
        corrections = []
        expected = sentence
        actual = correct.apply_corrections(sentence, corrections)
        self.assertEqual(expected, actual)

    def test_single_insertion(self):
        sentence = 'In modern digital world .'
        corrections = [(1, 1, '', ['the'])]
        expected = 'In the modern digital world .'
        actual = correct.apply_corrections(sentence, corrections)
        self.assertEqual(expected, actual)
