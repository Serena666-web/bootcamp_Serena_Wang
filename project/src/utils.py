import pandas as pd
def get_summary_stats(data):
    """
    Returns numeric summary statistics and category aggregations.
    """
    summary = data.describe()
    category_stats = data.groupby("category")["value"].agg(["mean", "sum", "count"])
    return {"summary": summary, "category_stats": category_stats}
    