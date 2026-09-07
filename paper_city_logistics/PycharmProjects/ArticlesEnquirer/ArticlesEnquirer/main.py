from config import EXCEL_FILE_PATH, SEARCH_COLUMNS, CONDITIONS
from search.loader import load_excel_file
from search.query_engine import execute_combined_query


def save_results(ids: list, file_path: str):
    with open(file_path, "w") as f:
        f.write(", ".join(ids))


def main():
    df = load_excel_file(EXCEL_FILE_PATH)

    or_keywords = CONDITIONS.get("or_conditions", {}).get("keywords", [])
    and_keywords = CONDITIONS.get("and_conditions", {}).get("keywords", [])

    or_keywords = [kw.lower() for kw in or_keywords]
    and_keywords = [kw.lower() for kw in and_keywords]

    ids, counts = execute_combined_query(df, or_keywords, and_keywords, SEARCH_COLUMNS)

    print(f"\nMatching IDs: {ids}")
    print(f"Total Matches: {len(ids)}")
    for kw, occ in counts.items():
        print(f'Occurrences of "{kw}": {occ}')

    save_results(ids, "results/output.txt")


if __name__ == "__main__":
    main()
