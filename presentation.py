# save the frequency list to excel
import pandas as pd
import openpyxl
from translation import *

excel_file_name = "finnish word frequency"

# create DataFrame using data
df = pd.DataFrame(top_100_frequency_list_with_translation, columns=["Frequency", "Finnish", "English"])
df.to_excel(f"data/{excel_file_name}.xlsx", index=False)
