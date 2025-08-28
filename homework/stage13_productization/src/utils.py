def add_feature_and_plot(df, price_col, date_col, window=20):
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df = df.dropna(subset=[date_col]).sort_values(date_col)
    df['change_in_price'] = df[price_col].diff().fillna(0)
    df['rolling_price'] = df[price_col].rolling(window, min_periods=1).mean()
    display(df.head())
    plt.figure(figsize=(12,6))
    plt.plot(df[date_col], df[price_col], label='Price', linewidth=1.5)
    plt.plot(df[date_col], df['rolling_price'], label=f'{window}-day SMA', linewidth=2)
    plt.title("Price with 20-Day Rolling Average", fontsize=14)
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.legend()
    plt.grid(True, alpha=0.25)
    plt.tight_layout()
    plt.show()
    return df
    