from ydata_profiling import ProfileReport


import pandas as pd 

df = pd.read_csv("TestEDA\Microsoft_Stock.csv") 

profile = ProfileReport(
        df, title="Profile Report of the UCI Bank Marketing Dataset", explorative=True
    )
profile.to_file("sequential_data_analysis_report.html")
