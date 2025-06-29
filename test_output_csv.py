
import pandas as pd
import os
from dataextraction import data_extraction

def test_pdf_conversion():
    pdf_file = "139447-1.pdf"  
    output_csv_file = "orderquoteline.csv"

    data_extraction(pdf_file)

    assert os.path.exists(pdf_file)

    df_output = pd.read_csv(output_csv_file)

    pd.testing.assert_frame_equal(df_output, check_dtype=False) 

    assert len(df_output) > 0, "Output CSV is empty."
    assert "Line No" in df_output.columns, "Column 'Line No' not found in output."

    os.remove(output_csv_file)