from pathlib import Path

import pandas as pd
import streamlit as st


DATA_FILE = Path(__file__).with_name("Indian_Economy.csv")
REQUIRED_COLUMNS = {
    "Year",
    "Quarter",
    "Sector",
    "GDP_Lakh_Crore",
    "Growth_%",
    "Employment_Million",
    "Exports_Crore",
    "Imports_Crore",
    "FDI_Crore",
    "Inflation_%",
    "CPI",
    "IIP",
    "Tax_Revenue_Crore",
}
QUARTERS = ["Q1", "Q2", "Q3", "Q4"]

st.set_page_config(
    page_title="India Economic Monitor",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    :root {
        --ink: #292738;
        --muted: #706b67;
        --panel: #fffaf0;
        --line: rgba(94, 75, 54, 0.17);
        --saffron: #b95e25;
        --green: #287454;
        --blue: #3b7185;
        --gold: #b08a45;
        --font-body: 'Nirmala UI', 'Noto Sans Devanagari', 'Segoe UI', sans-serif;
        --font-display: 'Noto Serif Devanagari', 'Nirmala UI', Georgia, serif;
    }
    html, body, [class*="css"] {
        font-family: var(--font-body);
    }
    .stApp {
        background:
            radial-gradient(circle at 91% 10%, rgba(185, 94, 37, 0.055) 0 2px, transparent 2.5px) 0 0 / 22px 22px,
            radial-gradient(ellipse at 87% 0%, rgba(176, 138, 69, 0.12), transparent 34%),
            #f7f2e8;
        color: var(--ink);
    }
    [data-testid="stHeader"] { background: rgba(247, 242, 232, 0.92); }
    [data-testid="stSidebar"] {
        background:
            radial-gradient(circle at 15px 15px, rgba(233, 213, 170, 0.08) 1.2px, transparent 1.6px) 0 0 / 24px 24px,
            #292b40;
        border-right: 1px solid rgba(176, 138, 69, 0.42);
    }
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h3,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] strong { color: #f7edda; }
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
        color: #d1c5ae;
    }
    h1, h2, h3 {
        font-family: var(--font-display) !important;
        letter-spacing: -0.025em;
        color: var(--ink);
    }
    .hero {
        position: relative;
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 24px;
        padding: 14px 0 23px;
        border-bottom: 3px solid transparent;
        border-image: linear-gradient(90deg, #c96f32 0 33%, #f6f0e4 33% 66%, #347653 66% 100%) 1;
        margin-bottom: 22px;
    }
    .hero::after {
        content: '✺';
        position: absolute;
        right: 17%;
        top: -26px;
        color: rgba(176, 138, 69, 0.13);
        font-size: 8rem;
        line-height: 1;
        pointer-events: none;
    }
    .eyebrow {
        color: var(--saffron);
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        margin-bottom: 9px;
    }
    .hero h1 {
        position: relative;
        z-index: 1;
        font-size: clamp(2rem, 4vw, 3.15rem);
        line-height: 1.08;
        margin: 0;
        color: #292b40;
    }
    .hero p {
        position: relative;
        z-index: 1;
        color: var(--muted);
        margin: 10px 0 0;
        max-width: 660px;
        line-height: 1.6;
    }
    .hero-tag {
        position: relative;
        z-index: 1;
        white-space: nowrap;
        border: 1px solid rgba(176, 138, 69, 0.5);
        color: #72552a;
        border-radius: 4px;
        padding: 8px 12px;
        font-size: 0.75rem;
        background: rgba(255, 250, 240, 0.88);
        margin-top: 8px;
        box-shadow: 3px 3px 0 rgba(176, 138, 69, 0.13);
    }
    .heritage-seal {
        position: relative;
        z-index: 1;
        display: flex;
        align-items: center;
        gap: 11px;
        align-self: flex-start;
        margin-top: 4px;
        padding: 9px 12px 9px 9px;
        border: 1px solid rgba(176, 138, 69, 0.56);
        border-radius: 5px;
        background: rgba(255, 250, 240, 0.94);
        box-shadow: 3px 3px 0 rgba(176, 138, 69, 0.14);
        color: #72552a;
    }
    .emblem-mark {
        display: block;
        width: auto;
        height: 52px;
        max-width: 42px;
        flex: 0 0 auto;
        object-fit: contain;
    }
    .motto-devanagari {
        font-family: var(--font-display);
        font-size: 0.93rem;
        font-weight: 700;
        line-height: 1.4;
        white-space: nowrap;
    }
    .motto-translation {
        color: var(--muted);
        font-size: 0.65rem;
        letter-spacing: 0.045em;
        white-space: nowrap;
    }
    @media (max-width: 900px) {
        .hero { flex-wrap: wrap; }
        .heritage-seal { margin-top: 0; }
    }
    [data-testid="stMetric"] {
        background: linear-gradient(145deg, #fffdf7, #f1e8d8);
        border: 1px solid var(--line);
        border-radius: 5px;
        padding: 17px 18px;
        min-height: 122px;
        box-shadow: 0 4px 14px rgba(73, 55, 35, 0.055);
    }
    [data-testid="stMetricLabel"] {
        color: var(--muted);
        font-size: 0.78rem;
    }
    [data-testid="stMetricValue"] {
        color: var(--ink);
        font-family: var(--font-display);
        font-size: 1.65rem;
    }
    [data-testid="stMetricDelta"] { font-size: 0.76rem; }
    [data-testid="stVerticalBlock"] > [data-testid="stHorizontalBlock"] {
        gap: 1rem;
    }
    .section-kicker {
        color: var(--muted);
        font-size: 0.76rem;
        letter-spacing: 0.10em;
        text-transform: uppercase;
        margin: 5px 0 8px;
    }
    .insight-card {
        height: 100%;
        background: var(--panel);
        border: 1px solid var(--line);
        border-radius: 5px;
        padding: 17px 18px;
        box-shadow: 0 4px 14px rgba(73, 55, 35, 0.045);
    }
    .insight-label {
        color: var(--muted);
        text-transform: uppercase;
        letter-spacing: 0.1em;
        font-size: 0.68rem;
        margin-bottom: 10px;
    }
    .insight-value {
        color: var(--ink);
        font-family: var(--font-display);
        font-size: 1.18rem;
        font-weight: 700;
        margin-bottom: 5px;
    }
    .insight-detail {
        color: var(--muted);
        font-size: 0.8rem;
        line-height: 1.5;
    }
    .note {
        border-left: 3px solid var(--saffron);
        background: #efe6d5;
        padding: 12px 15px;
        border-radius: 0 4px 4px 0;
        color: #514b43;
        font-size: 0.82rem;
        line-height: 1.55;
    }
    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] p,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
        color: #e2d7c1 !important;
    }
    [data-testid="stSidebar"] [data-baseweb="select"] > div,
    [data-testid="stSidebar"] [data-baseweb="input"] > div {
        background-color: #f8f2e6;
        border-color: rgba(222, 202, 164, 0.45);
    }
    [data-testid="stSidebar"] [data-testid="stSlider"] [role="slider"] {
        background-color: #d98b42;
        border-color: #d98b42;
    }
    [data-testid="stDownloadButton"] button {
        color: #fffaf0;
        background: #2c7255;
        border: 1px solid #2c7255;
        border-radius: 4px;
    }
    [data-testid="stDownloadButton"] button:hover {
        color: #fffaf0;
        background: #225a42;
        border-color: #225a42;
    }
    footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    data = pd.read_csv(path)
    missing = REQUIRED_COLUMNS.difference(data.columns)
    if missing:
        raise ValueError(f"CSV is missing required columns: {', '.join(sorted(missing))}")

    data["Year"] = pd.to_numeric(data["Year"], errors="raise").astype(int)
    for column in REQUIRED_COLUMNS - {"Year", "Quarter", "Sector"}:
        data[column] = pd.to_numeric(data[column], errors="raise")
    data["Quarter"] = pd.Categorical(data["Quarter"], categories=QUARTERS, ordered=True)
    return data


try:
    economy = load_data(str(DATA_FILE))
except FileNotFoundError:
    st.error(f"Could not find the dataset: {DATA_FILE.name}. Place it beside app.py.")
    st.stop()
except (ValueError, pd.errors.ParserError) as error:
    st.error(f"Could not load the dataset: {error}")
    st.stop()

years = sorted(economy["Year"].unique().tolist())
sectors = sorted(economy["Sector"].dropna().unique().tolist())

with st.sidebar:
    st.markdown("### INDIA / DATA DESK")
    st.caption("Economic intelligence dashboard")
    st.markdown("---")
    st.markdown("#### Refine the view")
    year_range = st.slider(
        "Year range",
        min_value=min(years),
        max_value=max(years),
        value=(min(years), max(years)),
        step=1,
    )
    selected_sectors = st.multiselect("Sectors", sectors, default=sectors)
    selected_quarters = st.multiselect("Quarters", QUARTERS, default=QUARTERS)
    st.markdown("---")
    st.markdown("#### Number slider")
    number = st.slider("Pick a number:", min_value=1, max_value=10)
    st.text("Your number is " + str(number))
    st.markdown("---")
    st.caption("Source: Indian_Economy.csv")
    st.caption(f"{len(economy):,} records · {min(years)}–{max(years)}")

filtered = economy[
    economy["Year"].between(year_range[0], year_range[1])
    & economy["Sector"].isin(selected_sectors)
    & economy["Quarter"].isin(selected_quarters)
].copy()

st.markdown(
    """
    <div class="hero">
      <div>
        <div class="eyebrow">भारत · India · Macroeconomic pulse</div>
        <h1>Economic Monitor</h1>
        <p>A clear read on output, growth, jobs and prices — built from the sector-by-quarter dataset.</p>
      </div>
      <div class="heritage-seal" aria-label="Emblem of India and motto, Satyameva Jayate">
        <img class="emblem-mark" src="/app/static/emblem-of-india.svg" alt="Emblem of India" title="Emblem of India">
        <div>
          <div class="motto-devanagari">सत्यमेव जयते</div>
          <div class="motto-translation">SATYAMEVA JAYATE · TRUTH ALONE TRIUMPHS</div>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

if filtered.empty:
    st.warning("No records match these filters. Select at least one sector and quarter.")
    st.stop()

annual = (
    filtered.groupby("Year", observed=True)
    .agg(
        GDP=("GDP_Lakh_Crore", "sum"),
        Growth=("Growth_%", "mean"),
        Inflation=("Inflation_%", "mean"),
        Employment=("Employment_Million", "sum"),
        Exports=("Exports_Crore", "sum"),
        Imports=("Imports_Crore", "sum"),
        FDI=("FDI_Crore", "sum"),
        Tax_Revenue=("Tax_Revenue_Crore", "sum"),
        CPI=("CPI", "mean"),
        IIP=("IIP", "mean"),
    )
    .sort_index()
)

latest_year = int(filtered["Year"].max())
latest_quarter = max(filtered["Quarter"].dropna().tolist(), key=QUARTERS.index)
latest = filtered[
    (filtered["Year"] == latest_year) & (filtered["Quarter"] == latest_quarter)
]
latest_growth = latest["Growth_%"].mean() if not latest.empty else float("nan")
latest_employment = latest["Employment_Million"].sum() if not latest.empty else float("nan")
latest_inflation = latest["Inflation_%"].mean() if not latest.empty else float("nan")

gdp_delta = None
if len(annual) > 1:
    first, last = annual["GDP"].iloc[0], annual["GDP"].iloc[-1]
    if first:
        gdp_delta = (last / first - 1) * 100

st.markdown('<div class="section-kicker">At a glance - selected window</div>', unsafe_allow_html=True)
kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)
kpi1.metric("GDP - selected period", f"INR {annual['GDP'].sum():,.1f} Lakh Cr")
kpi2.metric(
    "GDP change - first to last year",
    f"{gdp_delta:+.1f}%" if gdp_delta is not None else "N/A",
    help="Change between the first and last selected year using the same sector and quarter filters.",
)
kpi3.metric(
    f"Avg. growth - {latest_year} {latest_quarter}",
    f"{latest_growth:.2f}%" if pd.notna(latest_growth) else "N/A",
)
kpi4.metric(
    f"Employment - {latest_year} {latest_quarter}",
    f"{latest_employment:,.1f} M" if pd.notna(latest_employment) else "—",
)
kpi5.metric(
    f"Avg. inflation - {latest_year} {latest_quarter}",
    f"{latest_inflation:.2f}%" if pd.notna(latest_inflation) else "N/A",
)

st.markdown("")
left, right = st.columns([1.45, 1])
with left:
    st.markdown("### Output over time")
    st.caption("GDP is summed across the selected sectors and quarters.")
    st.bar_chart(annual[["GDP"]], color="#f4a340", height=300)
with right:
    st.markdown("### Growth & inflation")
    st.caption("Average reported rates for each year in the selected view.")
    st.line_chart(annual[["Growth", "Inflation"]], color=["#59c38b", "#75a9ef"], height=300)

st.markdown("")
left, right = st.columns([1, 1.45])
with left:
    st.markdown("### Sector contribution")
    st.caption(f"GDP by sector - {latest_year} {latest_quarter}")
    sector_gdp = (
        latest.groupby("Sector", observed=True)["GDP_Lakh_Crore"]
        .sum()
        .sort_values(ascending=False)
    )
    st.bar_chart(sector_gdp, horizontal=True, color="#75a9ef", height=360)
with right:
    st.markdown("### Trade flows")
    st.caption("Exports and imports, in crore rupees, summed across the selected view.")
    trade = annual[["Exports", "Imports"]].rename(
        columns={"Exports": "Exports · Cr", "Imports": "Imports · Cr"}
    )
    st.bar_chart(trade, color=["#59c38b", "#f4a340"], height=360)

st.markdown("")
st.markdown("### What stands out")
top_sector = sector_gdp.index[0] if not sector_gdp.empty else "—"
top_sector_gdp = sector_gdp.iloc[0] if not sector_gdp.empty else 0
growth_sector = latest.groupby("Sector", observed=True)["Growth_%"].mean().sort_values(ascending=False)
fastest_sector = growth_sector.index[0] if not growth_sector.empty else "—"
fastest_growth = growth_sector.iloc[0] if not growth_sector.empty else float("nan")
trade_balance = annual["Exports"].sum() - annual["Imports"].sum()

insight1, insight2, insight3 = st.columns(3)
with insight1:
    st.markdown(
        f'<div class="insight-card"><div class="insight-label">Largest GDP sector</div>'
        f'<div class="insight-value">{top_sector}</div>'
        f'<div class="insight-detail">INR {top_sector_gdp:,.2f} lakh crore in {latest_year} {latest_quarter}.</div></div>',
        unsafe_allow_html=True,
    )
with insight2:
    growth_text = f"{fastest_growth:.2f}%" if pd.notna(fastest_growth) else "—"
    st.markdown(
        f'<div class="insight-card"><div class="insight-label">Fastest reported growth</div>'
        f'<div class="insight-value">{fastest_sector}</div>'
        f'<div class="insight-detail">{growth_text} average growth in {latest_year} {latest_quarter}.</div></div>',
        unsafe_allow_html=True,
    )
with insight3:
    balance_label = "surplus" if trade_balance >= 0 else "deficit"
    st.markdown(
        f'<div class="insight-card"><div class="insight-label">Selected-window trade balance</div>'
        f'<div class="insight-value">INR {abs(trade_balance):,.0f} Cr {balance_label}</div>'
        f'<div class="insight-detail">Exports minus imports across the selected years, sectors and quarters.</div></div>',
        unsafe_allow_html=True,
    )

with st.expander("Explore additional indicators", expanded=False):
    st.caption("Annual totals for monetary flows; annual averages for CPI and IIP.")
    indicator1, indicator2, indicator3 = st.columns(3)
    with indicator1:
        st.markdown("**Foreign direct investment**")
        st.line_chart(annual[["FDI"]], color="#75a9ef", height=230)
    with indicator2:
        st.markdown("**Tax revenue**")
        st.line_chart(annual[["Tax_Revenue"]], color="#f4a340", height=230)
    with indicator3:
        st.markdown("**Employment**")
        st.line_chart(annual[["Employment"]], color="#59c38b", height=230)
    index1, index2 = st.columns(2)
    with index1:
        st.markdown("**Consumer price index (CPI)**")
        st.line_chart(annual[["CPI"]], color="#f4a340", height=230)
    with index2:
        st.markdown("**Industrial production index (IIP)**")
        st.line_chart(annual[["IIP"]], color="#75a9ef", height=230)

st.markdown("")
st.markdown(
    '<div class="note"><strong>Reading this dashboard:</strong> period totals sum the records that pass the filters; '
    'growth and inflation are simple averages. Employment is summed across sectors for the latest selected quarter. '
    'These figures reflect the supplied dataset and have not been independently validated against official sources.</div>',
    unsafe_allow_html=True,
)
st.download_button(
    "Download filtered data",
    data=filtered.drop(columns=["Quarter"]).assign(Quarter=filtered["Quarter"].astype(str)).to_csv(index=False),
    file_name="india_economy_filtered.csv",
    mime="text/csv",
)
