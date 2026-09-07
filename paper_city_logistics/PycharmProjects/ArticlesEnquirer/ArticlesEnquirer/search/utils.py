import re


def normalize_text(text: str) -> str:
    """
    Normalize text by converting it to lowercase.
    :param text:
    :return:
    """
    return text.lower()


def count_keyword_occurrences(text: str, keyword: str) -> int:
    """
    Count occurrences of a keyword in a text.
    :param text:
    :param keyword:
    :return:
    """
    if not text or not keyword:
        return 0
    return len(re.findall(re.escape(keyword.lower()), text.lower()))
#   words = normalize_text(text).split()
#   keyword_norm = keyword.lower()
#   return sum(1 for word in words if word == keyword_norm)
