import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# ── Palette ──────────────────────────────────────────────────────────────────
BG        = "#0D0D0D"
CARD      = "#1A1A1A"
ACCENT    = "#FF2D55"   # hot-pink / Gen-Z energy
GOLD      = "#FFD60A"
CYAN      = "#00C2FF"
GREEN     = "#30D158"
MUTED     = "#3A3A3C"
TEXT      = "#F5F5F7"
SUBTEXT   = "#8E8E93"

plt.rcParams.update({
    "figure.facecolor":  BG,
    "axes.facecolor":    CARD,
    "axes.edgecolor":    MUTED,
    "axes.labelcolor":   TEXT,
    "xtick.color":       SUBTEXT,
    "ytick.color":       SUBTEXT,
    "text.color":        TEXT,
    "grid.color":        MUTED,
    "grid.linestyle":    "--",
    "grid.alpha":        0.4,
    "font.family":       "DejaVu Sans",
})

rupee = lambda x, _: f"₹{int(x):,}"

# ── Realistic Data ────────────────────────────────────────────────────────────
profiles = ["Rahul\n(Call-centre)", "Priya\n(Part-time job)", "Aryan\n(Freelancer)",
            "Sneha\n(Intern)", "Kabir\n(Delivery boy)"]

monthly_income   = np.array([22000, 15000, 28000, 12000, 18000])
bank_balance     = np.array([1800,   600,  3200,   300,  1100])   # actual savings after all spending

# EMI breakdown (monthly)
iphone_emi       = np.array([4500, 3200, 5500, 2800, 4000])
shoe_spend       = np.array([2000, 1500, 2500, 1200, 1800])
restaurant_spend = np.array([3500, 2800, 4000, 2200, 3000])
clothing_spend   = np.array([2500, 2000, 3000, 1500, 2200])
concert_reel     = np.array([1500, 1200, 2000,  800, 1200])

total_showoff = iphone_emi + shoe_spend + restaurant_spend + clothing_spend + concert_reel

# What parents actually earn (for the household reality panel)
parent_income = np.array([18000, 12000, 20000, 10000, 15000])

# DataFrame
df = pd.DataFrame({
    "Profile":          profiles,
    "Income":           monthly_income,
    "Bank Balance":     bank_balance,
    "iPhone EMI":       iphone_emi,
    "Shoes":            shoe_spend,
    "Restaurant":       restaurant_spend,
    "Clothing":         clothing_spend,
    "Concert/Reels":    concert_reel,
    "Total Show-off":   total_showoff,
    "Parent Income":    parent_income,
})

spend_cols  = ["iPhone EMI", "Shoes", "Restaurant", "Clothing", "Concert/Reels"]
spend_clrs  = [ACCENT, GOLD, CYAN, GREEN, "#BF5AF2"]

# ── Figure Layout ─────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(20, 24), facecolor=BG)
fig.suptitle("Gen-Z Show-off Culture  ·  Financial Reality Check",
             fontsize=26, fontweight="bold", color=TEXT, y=0.98)
fig.text(0.5, 0.965, "Monthly Income  vs  Actual Bank Balance  vs  What They Spend to Look Rich",
         ha="center", fontsize=13, color=SUBTEXT)

gs = gridspec.GridSpec(4, 2, figure=fig, hspace=0.52, wspace=0.38,
                        top=0.945, bottom=0.04, left=0.06, right=0.97)

# ── 1. Income vs Show-off Spend (grouped bar) ────────────────────────────────
ax1 = fig.add_subplot(gs[0, :])
x   = np.arange(len(profiles))
w   = 0.28
bars_inc  = ax1.bar(x - w, monthly_income,    w, label="Monthly Income",    color=GREEN,  alpha=0.9, zorder=3)
bars_show = ax1.bar(x,     total_showoff,     w, label="Total Show-off Spend", color=ACCENT, alpha=0.9, zorder=3)
bars_bal  = ax1.bar(x + w, bank_balance,      w, label="Bank Balance Left",  color=GOLD,   alpha=0.9, zorder=3)

ax1.set_xticks(x); ax1.set_xticklabels(profiles, fontsize=11)
ax1.yaxis.set_major_formatter(FuncFormatter(rupee))
ax1.set_title("Income  ·  Show-off Spending  ·  What Remains in Bank", fontsize=14,
               color=TEXT, pad=10)
ax1.legend(facecolor=CARD, edgecolor=MUTED, labelcolor=TEXT, fontsize=10)
ax1.grid(axis="y", zorder=0)
ax1.set_facecolor(CARD)

# Annotate bank balance bars (the sad truth)
for bar in bars_bal:
    h = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, h + 200, f"₹{int(h):,}",
             ha="center", va="bottom", fontsize=9, color=GOLD, fontweight="bold")

# ── 2. Stacked Show-off Spend Breakdown ──────────────────────────────────────
ax2 = fig.add_subplot(gs[1, :])
bottoms = np.zeros(len(profiles))
for col, clr in zip(spend_cols, spend_clrs):
    vals = df[col].values
    ax2.bar(x, vals, 0.5, bottom=bottoms, label=col, color=clr, alpha=0.88, zorder=3)
    # label inside each segment if big enough
    for i, (v, b) in enumerate(zip(vals, bottoms)):
        if v > 400:
            ax2.text(i, b + v/2, f"₹{v:,}", ha="center", va="center",
                     fontsize=8.5, color="white", fontweight="bold")
    bottoms += vals

ax2.set_xticks(x); ax2.set_xticklabels(profiles, fontsize=11)
ax2.yaxis.set_major_formatter(FuncFormatter(rupee))
ax2.set_title("How Show-off Budget is Split Every Month", fontsize=14, color=TEXT, pad=10)
ax2.legend(facecolor=CARD, edgecolor=MUTED, labelcolor=TEXT, fontsize=10,
           loc="upper right", ncol=5)
ax2.grid(axis="y", zorder=0); ax2.set_facecolor(CARD)

# ── 3. % of Income Blown on Show-off (donut-style horizontal bar) ─────────────
ax3 = fig.add_subplot(gs[2, 0])
pct = (df["Total Show-off"] / df["Income"] * 100).values
colors_pct = [ACCENT if p > 70 else GOLD if p > 50 else GREEN for p in pct]
hbars = ax3.barh(profiles, pct, color=colors_pct, alpha=0.9, height=0.55, zorder=3)
ax3.axvline(50, color=CYAN, lw=1.5, linestyle="--", alpha=0.7, label="50% line")
ax3.axvline(70, color=ACCENT, lw=1.5, linestyle="--", alpha=0.7, label="Danger zone")
for bar, p in zip(hbars, pct):
    ax3.text(p + 0.8, bar.get_y() + bar.get_height()/2,
             f"{p:.1f}%", va="center", fontsize=10, color=TEXT, fontweight="bold")
ax3.set_xlim(0, 110)
ax3.set_xlabel("% of Monthly Income", fontsize=10)
ax3.set_title("Show-off Spend as % of Income\n🔴 >70% = Danger Zone", fontsize=12, color=TEXT)
ax3.legend(facecolor=CARD, edgecolor=MUTED, labelcolor=TEXT, fontsize=9)
ax3.grid(axis="x", zorder=0); ax3.set_facecolor(CARD)

# ── 4. Their spend vs Parent's full income ────────────────────────────────────
ax4 = fig.add_subplot(gs[2, 1])
bar_w = 0.35
b1 = ax4.bar(x - bar_w/2, df["Parent Income"], bar_w, label="Parent Monthly Income",
             color="#636366", alpha=0.9, zorder=3)
b2 = ax4.bar(x + bar_w/2, df["Total Show-off"], bar_w, label="Child Show-off Spend",
             color=ACCENT, alpha=0.9, zorder=3)
ax4.set_xticks(x)
ax4.set_xticklabels([p.split("\n")[0] for p in profiles], fontsize=10)
ax4.yaxis.set_major_formatter(FuncFormatter(rupee))
ax4.set_title("Child's Show-off vs Parent's Total Income\n(Reality check for the family)", fontsize=12, color=TEXT)
ax4.legend(facecolor=CARD, edgecolor=MUTED, labelcolor=TEXT, fontsize=9)
ax4.grid(axis="y", zorder=0); ax4.set_facecolor(CARD)

# ── 5. Heatmap – spend intensity per category per person ─────────────────────
ax5 = fig.add_subplot(gs[3, 0])
heat_data = df[spend_cols].set_index(df["Profile"].str.split("\n").str[0])
sns.heatmap(heat_data, ax=ax5, cmap="RdYlGn_r", annot=True, fmt=",d",
            linewidths=0.5, linecolor=BG, cbar_kws={"format": "₹%d"},
            annot_kws={"size": 9, "color": "white"})
ax5.set_title("Spending Heat Map (₹ per month)\nRedder = More Money Wasted", fontsize=12, color=TEXT)
ax5.set_xlabel(""); ax5.set_ylabel("")
ax5.tick_params(colors=SUBTEXT, labelsize=9)

# ── 6. Scatter – Bank Balance vs Total Show-off ───────────────────────────────
ax6 = fig.add_subplot(gs[3, 1])
for i, row in df.iterrows():
    ax6.scatter(row["Total Show-off"], row["Bank Balance"],
                s=220, color=spend_clrs[i], zorder=5, edgecolors="white", linewidths=0.8)
    ax6.annotate(row["Profile"].split("\n")[0],
                 (row["Total Show-off"], row["Bank Balance"]),
                 textcoords="offset points", xytext=(8, 4),
                 fontsize=9, color=TEXT)

ax6.set_xlabel("Total Show-off Spend / Month (₹)", fontsize=10)
ax6.set_ylabel("Bank Balance Left (₹)", fontsize=10)
ax6.set_title("More You Show Off → Less You Actually Have\n(Each dot is a person)", fontsize=12, color=TEXT)
ax6.xaxis.set_major_formatter(FuncFormatter(rupee))
ax6.yaxis.set_major_formatter(FuncFormatter(rupee))

# trend line
z = np.polyfit(df["Total Show-off"], df["Bank Balance"], 1)
xline = np.linspace(df["Total Show-off"].min(), df["Total Show-off"].max(), 100)
ax6.plot(xline, np.poly1d(z)(xline), color=ACCENT, lw=1.5, linestyle="--", alpha=0.7)
ax6.grid(zorder=0); ax6.set_facecolor(CARD)

# ── Footer ────────────────────────────────────────────────────────────────────
fig.text(0.5, 0.012,
         "Data is illustrative / realistic — based on typical Gen-Z spending patterns in Tier-2 Indian cities  •  All values in Indian Rupees (₹)",
         ha="center", fontsize=9, color=SUBTEXT)

plt.savefig("/mnt/user-data/outputs/genz_showoff_culture.png",
            dpi=160, bbox_inches="tight", facecolor=BG)
print("Saved → genz_showoff_culture.png")
plt.show()