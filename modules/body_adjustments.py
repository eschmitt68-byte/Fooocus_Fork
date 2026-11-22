import math


BODY_RATIO_FEATURES = {
    'overall_build': ('overall build', 'fuller', 'slimmer'),
    'bust_chest': ('bust/chest', 'fuller', 'smaller'),
    'breast_form': ('breast form', 'rounder and more projected', 'flatter and less projected'),
    'waist': ('waist', 'wider', 'narrower'),
    'hips': ('hips', 'wider', 'narrower'),
    'thighs': ('thighs', 'fuller', 'slimmer'),
    'butt': ('butt/glutes', 'fuller and more projected', 'smaller and less projected'),
    'lips': ('lip fullness', 'fuller', 'thinner'),
    'hair_length': ('hair length', 'longer', 'shorter')
}


def _validate_slider_value(value, name, minimum, maximum):
    try:
        numeric_value = float(value)
    except (TypeError, ValueError) as error:
        raise ValueError(f'{name} must be a number between {minimum} and {maximum}.') from error

    if not math.isfinite(numeric_value) or not minimum <= numeric_value <= maximum:
        raise ValueError(f'{name} must be a number between {minimum} and {maximum}.')

    if not numeric_value.is_integer():
        raise ValueError(f'{name} must be a whole number.')

    return int(numeric_value)


def _strength_description(strength):
    if strength <= 3:
        return 'subtle'
    if strength <= 6:
        return 'moderate'
    return 'strong'


def build_body_adjustment_prompt(
        prompt,
        ratios,
        hair_color,
        hair_color_strength,
        eye_color,
        eye_color_strength,
        ear_shape,
        ear_shape_strength):
    if set(ratios) != set(BODY_RATIO_FEATURES):
        raise ValueError('Body ratio values must include exactly the configured body features.')

    instructions = []
    for key, (label, positive_change, negative_change) in BODY_RATIO_FEATURES.items():
        value = _validate_slider_value(ratios[key], key, -200, 200)
        if value == 0:
            continue

        change = positive_change if value > 0 else negative_change
        percentage = abs(value)
        instructions.append(
            f'{label} approximately {percentage}% {change} than in the original image'
        )

    target_changes = [
        ('hair color', hair_color, hair_color_strength),
        ('eye color', eye_color, eye_color_strength),
        ('ear shape', ear_shape, ear_shape_strength)
    ]
    for label, target, strength in target_changes:
        strength = _validate_slider_value(strength, f'{label} strength', 0, 10)
        target = target.strip()
        if target and strength > 0:
            instructions.append(
                f'change {label} to {target} with {_strength_description(strength)} strength ({strength}/10)'
            )

    if not instructions:
        return prompt

    adjustment_prompt = '; '.join(instructions)
    if prompt.strip():
        return f'{prompt.rstrip(" ,;")}, {adjustment_prompt}'
    return adjustment_prompt
