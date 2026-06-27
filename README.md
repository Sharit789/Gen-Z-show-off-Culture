# 📊 Gen-Z Show-off Culture — Financial Reality Check

A data visualization project that exposes the financial gap between how Gen-Z **looks** on social media and how they **actually live** — built with Python, Pandas, Matplotlib, and Seaborn.

---

## 🔍 What This Project Is About

Gen-Z is buying iPhones on EMI, wearing first-copy Nike shoes, eating at expensive restaurants, and attending concerts just to make reels — all while their bank balance sits near zero and their parents struggle at home.

This project visualizes that **hard truth** using realistic data for 5 common Gen-Z profiles from Tier-2 Indian cities.

---

## 📸 Dashboard Preview

> Run the script to generate a full dark-themed 6-panel dashboard saved as `genz_showoff_culture.png`

The dashboard includes:
- **Grouped Bar Chart** — Monthly Income vs Show-off Spend vs Bank Balance
- **Stacked Bar Chart** — Breakdown of show-off spending by category
- **Horizontal Bar Chart** — Show-off spend as % of income (danger zones highlighted)
- **Reality Check Chart** — Child's show-off spend vs Parent's total income
- **Heatmap** — Spending intensity per category per person
- **Scatter Plot** — More you show off → less you actually have (with trend line)

---

## 👤 Profiles Used (Realistic Data)

| Name | Profession | Monthly Income | Bank Balance Left |
|------|-----------|---------------|------------------|
| Rahul | Call Centre | ₹22,000 | ₹1,800 |
| Priya | Part-time Job | ₹15,000 | ₹600 |
| Aryan | Freelancer | ₹28,000 | ₹3,200 |
| Sneha | Intern | ₹12,000 | ₹300 |
| Kabir | Delivery Boy | ₹18,000 | ₹1,100 |

---

## 💸 Show-off Spending Categories Tracked

| Category | Examples |
|----------|---------|
| iPhone EMI | Buying iPhone 13/14 on EMI just for the Apple logo |
| Shoes | First-copy Nike, Adidas, Jordan for clout |
| Restaurant | Expensive cafés and restaurants for Instagram |
| Clothing | Branded or fake-branded clothes |
| Concert / Reels | Spending on events just to make content |

---

## 🛠️ Tech Stack

| Library | Purpose |
|---------|---------|
| `pandas` | Data creation and DataFrame management |
| `numpy` | Numerical calculations and trend lines |
| `matplotlib` | Core charting, layout, and custom theming |
| `seaborn` | Heatmap visualization |

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone (https://github.com/Sharit789/Gen-Z-show-off-Culture)
cd genz-showoff-culture
```

### 2. Install dependencies

```bash
pip install pandas numpy matplotlib seaborn
```

Or install from requirements file:

```bash
pip install -r requirements.txt
```

### 3. Run the script

```bash
python genz_showoff.py
```

The chart will be saved as `genz_showoff_culture.png` in the same directory.

---

## 📁 Project Structure

```
genz-showoff-culture/
│
├── genz_showoff.py            # Main Python script
├── genz_showoff_culture.png   # Output dashboard (generated on run)
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

---

## 📄 requirements.txt

```
pandas
numpy
matplotlib
seaborn
```

---

## 🎨 Design Choices

- **Dark theme** (`#0D0D0D` background) — mirrors the aesthetic world Gen-Z lives in
- **Hot pink accent** (`#FF2D55`) — highlights danger zones and overspending
- **Gold color** (`#FFD60A`) — used for bank balance (ironically, the least visible bar)
- **Color-coded danger zones** — red when spend > 70% of income, yellow > 50%, green otherwise

---

## 💡 Key Insights from the Data

- Sneha (intern, ₹12,000/month) spends ₹8,500 on show-off while her parents earn ₹10,000 total
- All 5 profiles spend more than **60% of their income** on non-essential show-off items
- The average bank balance across all profiles is under ₹1,500
- iPhone EMI alone eats up **20–25% of monthly income** for most profiles
- The scatter plot confirms: the more you spend to look rich, the less money you actually have

---

## 🤔 Why This Matters

This is not just a data project — it's a mirror. Social media creates pressure to look wealthy, and Gen-Z is bearing the financial cost of that pressure silently. The goal of this visualization is to make those numbers impossible to ignore.

---

## 🙌 Contributing

Pull requests are welcome. If you want to add:
- More realistic profiles
- City-wise comparisons (Metro vs Tier-2 vs Tier-3)
- Time-series data showing EMI debt accumulation
- Interactive Plotly version

Feel free to fork and open a PR.

---

## 📜 License

MIT License — free to use, share, and modify with credit.

---

## ✍️ Author

Made with data, Python, and a little bit of frustration about the culture.

> *"They have ₹300 in their bank but ₹3,000 Nike shoes on their feet."*
