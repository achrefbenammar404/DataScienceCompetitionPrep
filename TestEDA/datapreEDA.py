from dataprep.eda import plot , create_report , create_diff_report , plot_correlation , plot_diff , plot_missing
import pandas as pd 

df = pd.read_csv("TestEDA\Microsoft_Stock.csv") 

create_report(df , title = "Full Report").show_browser()