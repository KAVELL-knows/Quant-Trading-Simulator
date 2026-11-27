# TEST STRIKE PRICES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

strikes = np.arange(85, 116, 2.5)

expiration_days = [7, 14, 30, 60, 90, 180, 365]
synthetic_data = []

rng = np.random.default_rng(42)
for days in expiration_days:
    for strike in strikes:
        spread = 8 - (strike - 100) * 0.75
        spread = spread * (1 + days / 365 * 0.15) + rng.normal(0, 1.2)
        synthetic_data.append({"Days to Expiration": days, "Strike": strike, "IV Spread (%)": spread})

iv_spread_data = pd.DataFrame(synthetic_data)
print(iv_spread_data.head(20))
print("Total rows:", len(iv_spread_data))

# CREATE HEATMAP DATA
iv_heatmap_data = iv_spread_data.pivot_table(index="Days to Expiration", columns="Strike", values="IV Spread (%)")
print("\nHEATMAP MATRIX")
print(iv_heatmap_data)

spread_limit = iv_heatmap_data.abs().max().max()
fig, ax = plt.subplots(figsize=(15, 9))

fig.patch.set_facecolor("#0b0f17")
ax.set_facecolor("#151a24")

heatmap = ax.imshow(iv_heatmap_data, aspect="auto", origin="lower", cmap="RdYlGn", interpolation="nearest", vmin=-spread_limit, vmax=spread_limit)

ax.contour(np.arange(len(iv_heatmap_data.columns)), np.arange(len(iv_heatmap_data.index)), iv_heatmap_data.values, levels=[0], colors="white", linewidths= 3)

# DISPLAY VALUES INSIDE EACH CELL
for row in range(len(iv_heatmap_data.index)):
    for column in range(len(iv_heatmap_data.columns)):

        value = iv_heatmap_data.iloc[row, column]

        text_color = "white" if abs(value) > spread_limit * 0.55 else "black"

        ax.text(
            column,
            row,
            f"{value:.1f}",
            ha="center",
            va="center",
            fontsize=8,
            color=text_color,
            fontweight="bold"
        )

# COLORBAR
colorbar = fig.colorbar(heatmap, ax=ax, pad=0.03)

colorbar.set_label(
    "PUT - CALL IV Spread (Percentage Points)",
    color="white",
    fontsize=11
)

colorbar.ax.yaxis.set_tick_params(color="white")
plt.setp(colorbar.ax.get_yticklabels(), color="white")

# AXIS LABELS
ax.set_xlabel("Strike Price ($)", color="white", fontsize=12, labelpad=15)
ax.set_ylabel("Days to Expiration", color="white", fontsize=12, labelpad=15)

# TITLE
ax.set_title(
    "CALL-PUT IMPLIED VOLATILITY SPREAD",
    color="white",
    fontsize=16,
    fontweight="bold",
    pad=20
)

# X-AXIS
ax.set_xticks(range(len(iv_heatmap_data.columns)))
ax.set_xticklabels(
    iv_heatmap_data.columns,
    rotation=45,
    ha="right",
    color="white"
)

# Y-AXIS
ax.set_yticks(range(len(iv_heatmap_data.index)))
ax.set_yticklabels(
    iv_heatmap_data.index,
    color="white"
)

# TICKS & BORDERS
ax.tick_params(colors="white")

for spine in ax.spines.values():
    spine.set_color("#3a4252")

# LAYOUT FIX
fig.subplots_adjust(
    left=0.12,
    right=0.85,
    bottom=0.24,
    top=0.88
)

plt.show()