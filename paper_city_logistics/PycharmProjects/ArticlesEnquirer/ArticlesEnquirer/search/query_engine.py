from typing import List, Dict, Tuple

import pandas as pd

from .utils import normalize_text, count_keyword_occurrences


def build_searchable_field(row: pd.Series, columns: List[str]) -> str:
    return " ".join(normalize_text(str(row.get(col, ""))) for col in columns)


def execute_combined_query(
        df: pd.DataFrame,
        or_keywords: List[str],
        and_keywords: List[str],
        search_columns: List[str]
) -> Tuple[List[str], Dict[str, int]]:
    matching_ids = set()
    all_keywords = list(set(or_keywords + and_keywords))
    keyword_counts = {kw: 0 for kw in all_keywords}

    for _, row in df.iterrows():
        content = build_searchable_field(row, search_columns)

        or_match = any(kw in content for kw in or_keywords) if or_keywords else True
        and_match = any(kw in content for kw in and_keywords) if and_keywords else True
    #   or_match = any(kw in content.split() for kw in or_keywords) if or_keywords else True
    #   and_match = any(kw in content.split() for kw in and_keywords) if and_keywords else True

        if or_match and and_match:
            matching_ids.add(str(row["id"]))

        for kw in all_keywords:
            keyword_counts[kw] += count_keyword_occurrences(content, kw)

    return list(matching_ids), keyword_counts
