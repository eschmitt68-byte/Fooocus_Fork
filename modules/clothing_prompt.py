def build_clothing_change_prompt(prompt, clothes, boots, additional):
    details = []
    for label, value in [
        ('clothing/outfit', clothes),
        ('boots/footwear', boots),
        ('additional details', additional)
    ]:
        value = value.strip()
        if value:
            details.append(f'{label}: {value}')

    if not details:
        return prompt

    if prompt.strip():
        return f'{prompt.rstrip(" ,;")}, {"; ".join(details)}'
    return '; '.join(details)
