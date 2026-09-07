# Article Enquirer - Excel Keyword Search Tool
This Python project allows you to perform powerful and customizable keyword searches on an Excel file (`.xlsx`) containing bibliographic or textual data. It supports both OR and AND conditions and counts both matching rows and total keyword occurrences across selected fields.

## Project Structure
```
keyword_search_project/
├── config.py               # Configuration file for input file, fields, and query logic
├── main.py                 # Entry point – runs the search
├── requirements.txt        # Required Python libraries
├── /data/
│   └── input.xlsx          # Your Excel input file (not included in repo)
├── /results/
│   └── combined_query_ids.txt  # Output file with matching IDs
└── /search/
    ├── __init__.py
    ├── loader.py           # Loads the Excel file
    ├── query_engine.py     # Executes keyword queries (OR + AND logic)
    └── utils.py            # Helper functions for text normalization and counting

```

## Input File Format
The input Excel file must be located at `data/input.xlsx` and must contain at least the following columns:
- `id` (used as a unique identifier)
- Other text columns like `title`, `abstract`, `keywords`, etc.

You can select which of these columns will be searched in `config.py`.

## Configuration
Edit the `config.py` file to customize:
```python
# Path to the input Excel file
EXCEL_FILE_PATH = "data/input.xlsx"

# Columns to search (must match column names in the Excel file)
SEARCH_COLUMNS = ["title", "abstract", "keywords"]

# Query conditions:
# (city logistics OR city-logistics) AND routing
CONDITIONS = {
    "or_conditions": {
        "type": "OR",
        "keywords": ["city logistics", "city-logistics"]
    },
    "and_conditions": {
        "type": "AND",
        "keywords": ["routing"]
    }
}
```
Notes:
- You can use only OR, only AND, or a combination of both.
- If both are defined, the logic is: (**OR condition**) **AND** (**AND condition**)

## How to Run
1. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
2. Ensure your inputExcel file is correctly formatted and located at `data/input.xlsx`.
3. Run the script:
   ```bash
   python main.py
   ```
4. The results will be saved in `results/output.txt`, containing the IDs of matching rows.

### Example Output
```text
Matching IDs: ['374682', '374701', '374651', '374644', '374691', '374761']
Total Matches: 6
Occurrences of "city logistics": 25
Occurrences of "city-logistics": 0
Occurrences of "routing": 18
```

### Requirements
- Python 3.6+
- Libraries: `pandas`, `openpyxl`, `re`
- Ensure you have the `input.xlsx` file in the correct format as described above.
- The script assumes the input file is well-formed and does not handle missing columns or malformed data.

# Detailed Explanation - `query_engine.py`
The file query_engine.py is the core logic engine that performs keyword searches on the Excel data.
It contains two main components:
### `build_searchable_field(row, columns)`
```python
def build_searchable_field(row: pd.Series, columns: List[str]) -> str:
return " ".join(normalize_text(str(row.get(col, ""))) for col in columns)
```
**What it does:**
- Takes a row from the Excel file and a list of column names (e.g. `["title", "abstract", "keywords"]`)
- Concatenates the text content of these columns into a single lowercase string
- This combined string is used for keyword searching

**Why it's needed:**
- Keywords can appear in any of the selected fields — this function simplifies the row into one searchable text block.

### `execute_combined_query(...)`
```python
def execute_combined_query(
    df: pd.DataFrame,
    or_keywords: List[str],
    and_keywords: List[str],
    search_columns: List[str]
) -> Tuple[List[str], Dict[str, int]]:
```
**Parameters:**
- `df`: the loaded DataFrame from the Excel file
- `or_keywords`: list of keywords to be matched with OR logic (at least one must be present)
- `and_keywords`: list of keywords to be matched with AND logic (all must be present)
- `search_columns`: the user-defined list of columns to search through

**Returns:**
- A tuple containing:
  - `matching_ids`: a list of id values from rows that matched the conditions
  - `keyword_counts`: a dictionary counting how many times each keyword appears in the file

**Logic:**
1. For each row in the Excel file:
   - The text of the selected columns is combined using `build_searchable_field`.
   - Then:
      - If at least one OR keyword is found in the text (or `or_keywords` is empty),
      - And all AND keywords are found in the text (or `and_keywords` is empty),
      - → The row is considered a match and its `id` is added to the result.

2. Regardless of whether the row matches:
   - The function counts how many times each keyword (both OR and AND) appears in the row.
   - This is done using regex for exact, case-insensitive match (`re.findall`).

## Summary of the Logic Flow
```sql
for each row:
    content = merge selected columns into lowercase string
    if OR conditions match AND AND conditions match:
        save the ID
    for each keyword:
        count occurrences in content

```