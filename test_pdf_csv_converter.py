
import os
import pytest
import pandas as pd
from dataextraction import data_extraction
from headerdatatocsv import header_data_to_csv

pdf_path = "139447-0.pdf"

def test_pdf_csv_conversion(pdf_path, output_csv_path):
    output_csv_path = "output.csv"

    pdf_path = "139447-0.pdf"

    data_extraction(pdf_path)

    assert os.path.exists(output_csv_path)

    df = pd.read_csv(output_csv_path)

    assert not df.empty

    assert list(df.columns) == ["Line No", "Item ID"]
    assert df.iloc[0]["Line No"] == "1"
    assert df.iloc[1]["Item ID"] == "H5450T"


    