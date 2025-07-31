import pandas as pd
from ydata_profiling import ProfileReport
import pathlib, datetime

df = pd.read_csv('data/raw/SeoulBikeData.csv', encoding='ISO-8859-1')
report = ProfileReport(df, title='Bike Demand EDA', minimal=True)
pathlib.Path("reports").mkdir(exist_ok=True)
report.to_file(f"reports/profile_{datetime.date.today().isoformat()}.html")