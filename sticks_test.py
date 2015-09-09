import unittest


class TestStickGame(unittest.TestCase):

    def test_get_num_sticks(self):
        self.assertEqual(get_num_sticks(word_list), ["bird", "calf", "river", "stream", "brain"])
