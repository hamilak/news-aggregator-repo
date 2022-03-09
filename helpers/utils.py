import re


def text_formatter(text):
    paras = re.findall(r"""
                       [IVXLCDM]+\n\n   # Line of Roman numeral characters
                       [^a-z]+\n\n      # Line without lower case characters
                       (.*?)\n          # First paragraph line
                       """, text, re.VERBOSE)
    return "\n\n".join(paras)
