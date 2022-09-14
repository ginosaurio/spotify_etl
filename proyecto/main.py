from etl_extract import extract
from transformer import transform
from loader import load
from datetime import datetime, timedelta
from create_table import create_tables
import click

@click.command()
@click.option('--day',type=int, help='Cantidad de días de info a obtener, default 10', default=10)

def etl(day: int):
    """_summary_

    Args:
        day (int): Cantidad de días de info a obtener, default 10

    """
    if day <= 0:
        raise Exception("El int en --day no puede ser 0 o un número menor")

    elif day == 10:

        date = datetime.today() - timedelta(days=10)
        create_tables()
        
        # Extract
        data_raw = extract(date)
        print(f"Extracted {len(data_raw['items'])} registers")

        # Transform
        clean_df = transform(data_raw, date)
        print(f"{clean_df.shape[0]} registers after transform")
        
        # Load
        load(clean_df)
        print("Done")
        
    else:
        
        date = datetime.today() - timedelta(days=day)
        print(date)
        create_tables()

        # Extract
        data_raw = extract(date)
        print(f"Extracted {len(data_raw['items'])} registers")

        # Transform
        clean_df = transform(data_raw, date)
        print(f"{clean_df.shape[0]} registers after transform")
        print(clean_df)
        
        # Load
        load(clean_df)
        print("Done")

if __name__ == "__main__":
    etl()