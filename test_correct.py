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

    def test_single_replace(self):
        sentence = ('In modern digital world , electronic products are '
                    'widely used in daily lives such as Smart phones , '
                    'computers and etc .')
        corrections = [(12, 13, 'lives', ['life'])]
        expected = ('In modern digital world , electronic products are '
                    'widely used in daily life such as Smart phones , '
                    'computers and etc .')
        actual = correct.apply_corrections(sentence, corrections)
        self.assertEqual(expected, actual)
                   
    def test_replace_and_insert(self):
        sentence = ('In modern digital world , electronic products are '
                    'widely used in daily lives such as Smart phones , '
                    'computers and etc .')
        corrections = [(1, 1, '', ['the']), (12, 13, 'lives', ['life'])]
        expected = ('In the modern digital world , electronic products are '
                    'widely used in daily life such as Smart phones , '
                    'computers and etc .')
        actual = correct.apply_corrections(sentence, corrections)
        self.assertEqual(expected, actual)

    def test_single_reduce(self):
        sentence = ('In work places , electronic devices '
                    'such as computers are also inevitable to '
                    'use to increase the productivity of the corporation .')
        corrections = [(1, 2, u'work', [u'the workplace'])]
        expected = ('In the workplace , electronic devices '
                    'such as computers are also inevitable to '
                    'use to increase the productivity of the corporation .')
        actual = correct.apply_corrections(sentence, corrections)
        self.assertEqual(expected, actual)

    def test_reduce_and_insert(self):
        sentence = ('In work places , electronic devices '
                    'such as computers are also inevitable to '
                    'use to increase the productivity of the corporation .')
        corrections = [(1, 2, u'work', [u'the workplace']), (6, 6, '', [u','])]
        expected = ('In the workplace , electronic devices , '
                    'such as computers are also inevitable to '
                    'use to increase the productivity of the corporation .')
        actual = correct.apply_corrections(sentence, corrections)
        self.assertEqual(expected, actual)
           
    def test_reduce_insert_insert_reduce(self):
        sentence = ('In work places , electronic devices '
                    'such as computers are also inevitable to '
                    'use to increase the productivity of the corporation .')
        corrections = [
                (1, 2, u'work', [u'the workplace']),
                (6, 6, '', [u',']),
                (9, 9, '', [u',']),
                (13, 15, u'use to', [u''])
        ]
        expected = ('In the workplace , electronic devices , '
                    'such as computers , are also inevitable to '
                    'increase the productivity of the corporation .')
        actual = correct.apply_corrections(sentence, corrections)
        self.assertEqual(expected, actual)
 
    def test_difficult_example(self):
        sentence = ('Surveillance technology such as RFID '
                    'can be operated twenty-four hours with the '
                    'absence of operators to track done every detail '
                    'about human activities .')
        corrections = [
            (2, 2, '', [u',']),
            (5, 5, '', [u',']),
            (10, 11, u'with', [u'without']),
            (11, 14, u'the absence of', [u'']),
            (17, 18, u'done', [u''])
        ]
        expected = ('Surveillance technology , such as RFID , '
                    'can be operated twenty-four hours without '
                    'operators to track every detail '
                    'about human activities .')
        actual = correct.apply_corrections(sentence, corrections)
        self.assertEqual(expected, actual)
