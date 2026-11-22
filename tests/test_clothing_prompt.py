import unittest

from modules.clothing_prompt import build_clothing_change_prompt


class TestClothingChangePrompt(unittest.TestCase):
    def test_details_are_combined_with_main_prompt(self):
        result = build_clothing_change_prompt(
            'adult woman', 'red dress', 'black boots', 'silver jewelry'
        )
        self.assertEqual(
            'adult woman, clothing/outfit: red dress; boots/footwear: black boots; '
            'additional details: silver jewelry',
            result
        )

    def test_blank_fields_preserve_main_prompt(self):
        self.assertEqual(
            'adult woman',
            build_clothing_change_prompt('adult woman', ' ', '', '')
        )

    def test_details_work_without_main_prompt(self):
        self.assertEqual(
            'boots/footwear: black boots',
            build_clothing_change_prompt('', '', 'black boots', '')
        )
