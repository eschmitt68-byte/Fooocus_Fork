import unittest

from modules.body_adjustments import BODY_RATIO_FEATURES, build_body_adjustment_prompt


class TestBodyAdjustments(unittest.TestCase):
    def setUp(self):
        self.ratios = {key: 0 for key in BODY_RATIO_FEATURES}

    def test_zero_values_preserve_the_prompt(self):
        prompt = 'adult woman, photorealistic'
        result = build_body_adjustment_prompt(prompt, self.ratios, '', 0, '', 0, '', 0)
        self.assertEqual(prompt, result)

    def test_signed_ratios_add_approximate_changes(self):
        self.ratios['bust_chest'] = 70
        self.ratios['waist'] = -40
        result = build_body_adjustment_prompt('', self.ratios, '', 0, '', 0, '', 0)
        self.assertIn('bust/chest approximately 70% fuller', result)
        self.assertIn('waist approximately 40% narrower', result)

    def test_bust_ratio_uses_direct_percentage(self):
        self.ratios['bust_chest'] = 40
        result = build_body_adjustment_prompt('', self.ratios, '', 0, '', 0, '', 0)
        self.assertIn('bust/chest approximately 40% fuller', result)

    def test_breast_form_uses_independent_negative_to_positive_scale(self):
        self.ratios['breast_form'] = 120
        result = build_body_adjustment_prompt('', self.ratios, '', 0, '', 0, '', 0)
        self.assertIn('breast form approximately 120% rounder and more projected', result)

    def test_categorical_targets_require_a_nonzero_strength(self):
        result = build_body_adjustment_prompt(
            'adult woman', self.ratios, 'auburn', 5, 'green', 0, 'rounded', 8
        )
        self.assertIn('change hair color to auburn with moderate strength (5/10)', result)
        self.assertIn('change ear shape to rounded with strong strength (8/10)', result)
        self.assertNotIn('change eye color', result)

    def test_ratio_out_of_range_is_rejected(self):
        self.ratios['thighs'] = 201
        with self.assertRaises(ValueError):
            build_body_adjustment_prompt('', self.ratios, '', 0, '', 0, '', 0)
