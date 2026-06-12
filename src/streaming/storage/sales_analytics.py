"""Sales Analytics Dashboard.

Phase 5 - Apply the Skills to a New Problem

Reads consumed sales data and generates
business analytics reports and charts.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT_DIR = Path()
DATA_DIR = ROOT_DIR / "data"
OUTPUT_DIR = DATA_DIR / "output"

CSV_FILE = OUTPUT_DIR / "consumed_sales.csv"


def main():
    """Run analytics."""
    df = pd.read_csv(CSV_FILE)

    total_revenue = df["total"].sum()
    total_orders = len(df)
    average_order = df["total"].mean()
    highest_order = df["total"].max()

    best_product = df.groupby("product_id")["total"].sum().sort_values(ascending=False)

    best_region = df.groupby("region_id")["total"].sum().sort_values(ascending=False)

    summary_df = pd.DataFrame(
        {
            "Metric": [
                "Total Revenue",
                "Total Orders",
                "Average Order Value",
                "Highest Order Total",
            ],
            "Value": [
                round(total_revenue, 2),
                total_orders,
                round(average_order, 2),
                round(highest_order, 2),
            ],
        }
    )

    summary_df.to_csv(
        OUTPUT_DIR / "sales_summary.csv",
        index=False,
    )

    plt.figure(figsize=(8, 5))
    best_product.plot(kind="bar")
    plt.title("Revenue by Product")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "revenue_by_product.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    best_region.plot(kind="bar")
    plt.title("Revenue by Region")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "revenue_by_region.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    df["total"].cumsum().plot()
    plt.title("Cumulative Revenue")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "orders_over_time.png")
    plt.close()

    print("\nSALES ANALYTICS SUMMARY")
    print("=" * 40)
    print(f"Total Revenue: ${total_revenue:.2f}")
    print(f"Total Orders: {total_orders}")
    print(f"Average Order: ${average_order:.2f}")
    print(f"Highest Order: ${highest_order:.2f}")
    print("=" * 40)


if __name__ == "__main__":
    main()
