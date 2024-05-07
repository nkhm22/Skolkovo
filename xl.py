import pandas as pd
import sqlite3


def xl():
    conn = sqlite3.connect("my_database.db")
    df = pd.read_sql('SELECT * FROM weather ORDER BY date DESC LIMIT 10', conn)
    df.to_excel(r'result.xlsx', index=False)


xl()
