
from pathlib import Path

def load_sql(path):

    with open(path, "r") as file:
        return file.read()



# Basic Formatting for Reports

def format_worksheet(
    worksheet,
    df
):

    worksheet.freeze_panes(1, 0)

    worksheet.autofilter(
        0,
        0,
        len(df),
        len(df.columns)-1
    )

    worksheet.set_column(
        0,
        len(df.columns),
        18
    )


# To protect database password

from dotenv import load_dotenv
from sqlalchemy import create_engine
import os

def get_engine():

    load_dotenv()

    connection_string = (
        f"postgresql://"
        f"{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}:"
        f"{os.getenv('DB_PORT')}/"
        f"{os.getenv('DB_NAME')}"
    )

    return create_engine(
        connection_string
    )