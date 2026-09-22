from scripts.clean_data import clean_data
from scripts.load_to_postgres import load_to_postgres
from build_workbook import build_workbook

def main():
    clean_data()
    load_to_postgres()
    build_workbook()
    print("\nPipeline Complete")

if __name__ == "__main__":
    main()