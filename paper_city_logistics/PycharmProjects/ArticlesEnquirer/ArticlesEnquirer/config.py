# Path to the input file
EXCEL_FILE_PATH = "data/input.xlsx"

# Columns the user wants to search in (must match Excel headers)
SEARCH_COLUMNS = ["title", "abstract", "keywords"]

# These conditions will be used to filter the search results
# The or conditions will have priority over the and conditions
# Example: (A OR B) AND C
CONDITIONS = {
    "or_conditions" : {
        "type": "OR",
        "keywords": ["electric","zero-emission","e-vehicle","e-truck","e-van","e-cargo","green vehicle"
]

    },
    "and_conditions": {
        "type": "AND",
        "keywords": ["battery","charging"



]

    }
}
