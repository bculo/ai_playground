import re


def clean_string(input_string: str) -> str:
    input_string = re.sub(r'•', '', input_string)
    input_string = re.sub(r'\s+', ' ', input_string)
    input_string = re.sub(r'[.]+', '.', input_string)
    return input_string
