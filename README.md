# Bootcamp Repository
## Folder Structure
- **homework/** → All homework contributions will be submitted here(most of the homework is in project/notebooks as requested).
- **project/** → All project contributions will be submitted here(Also the
- **class_materials/** → Local storage for class materials. Never pushed to
GitHub.

## Homework Folder Rules
- Each homework will be in its own subfolder (`homework0`, `homework1`, etc.)
- Include all required files for grading.
## Project Folder Rules
- Keep project files organized and clearly named.
## Data Storage
- data/raw/, data/processed/ are used by request. 
(For hw5, I use the demo data from the lecture notebook.)
-Csv file — human-readable tables (easiest to diff/inspect).
-Parquet (.parquet) — columnar, compressed, faster for big data (requires pyarrow or fastparquet).
-Using a configurable data directory (.env) to reads data