import pandas as pd
from src.processing import DataProcessor

processor = DataProcessor("data/raw_data.csv", "data/final_tickets_tenge_df.csv")

df = (processor
    .load_data()
    .preprocess("revenue_rub", "revenue_rub", 99)
    .create_profile()
    .filter_outliers_by_percentile("count_orders_per_user",99)
    .profile_statistic()
    .retention(["first_order_event", "first_order_device", "first_order_region"])
    .day_of_week_retention()
    .correlation_analys() 
    )          


