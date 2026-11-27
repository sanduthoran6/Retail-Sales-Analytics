
import streamlit as st
import pandas as pd
import plotly.express as px
import hashlib
import hmac
from pathlib import Path

# =====================================================
# CONFIGURATION
# =====================================================
st.set_page_config(
    page_title="Retail Analytics | Premium",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

EMAIL = "admin@retail.com"
PASSWORD_HASH = hashlib.sha256("Retail@123".encode()).hexdigest()

if "auth" not in st.session_state:
    st.session_state.auth = False

if "page" not in st.session_state:
    st.session_state.page = "Overview"

# =====================================================
# PREMIUM LUXURY DESIGN
# =====================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap');

:root {
    --rose: #B94F7C;
    --dark: #61334D;
    --muted: #987287;
    --pink: #E8A9C2;
}

* {font-family:'DM Sans',sans-serif;}

.stApp {
    background:
      radial-gradient(ellipse at 8% 8%, rgba(236,165,194,.48), transparent 35%),
      radial-gradient(ellipse at 92% 18%, rgba(255,255,255,.95), transparent 38%),
      radial-gradient(ellipse at 75% 90%, rgba(231,173,198,.40), transparent 38%),
      linear-gradient(135deg,#F9E8EF,#FFF9FB 48%,#F4DDE7);
    background-attachment: fixed;
    color: var(--dark);
}

[data-testid="stHeader"] {background:transparent;}
.block-container {padding-top:2rem;padding-bottom:3rem;max-width:1500px;}

h1,h2,h3,h4 {color:#71364F !important;font-weight:700 !important;}
p,label {color:#76536A;}

[data-testid="stSidebar"] {
    background:rgba(255,250,253,.78);
    backdrop-filter:blur(25px);
    border-right:1px solid rgba(255,255,255,.9);
}

[data-testid="stSidebar"] * {color:#71364F;}

.brand {
    font-family:'Playfair Display',serif;
    font-size:27px;
    font-weight:700;
    color:#A83D70;
    letter-spacing:-.5px;
    padding:12px 0 2px;
}

.brand-sub {
    font-size:10px;
    letter-spacing:3px;
    color:#B77A96;
    margin-bottom:25px;
}

.hero {
    background:
      radial-gradient(circle at 90% 10%,rgba(255,255,255,.32),transparent 35%),
      linear-gradient(115deg,#A83E70,#C65D8C 55%,#E5A0BA);
    border:1px solid rgba(255,255,255,.65);
    border-radius:26px;
    padding:30px 34px;
    box-shadow:0 18px 45px rgba(153,64,104,.19);
    margin-bottom:25px;
}

.hero h1 {
    color:white !important;
    font-size:30px;
    margin:0;
    font-family:'Playfair Display',serif;
}

.hero p {color:#FFF0F6 !important;margin:7px 0 0;font-size:13px;}

.eyebrow {
    color:#FFE4EF;
    font-size:10px;
    letter-spacing:3px;
    font-weight:700;
    margin-bottom:8px;
}

div[data-testid="stMetric"] {
    background:linear-gradient(145deg,rgba(255,255,255,.90),rgba(255,245,250,.65));
    backdrop-filter:blur(22px);
    border:1px solid rgba(255,255,255,.95);
    border-radius:21px;
    padding:19px 20px;
    box-shadow:0 10px 30px rgba(151,67,106,.09),inset 0 1px 0 white;
    transition:all .3s ease;
}

div[data-testid="stMetric"]:hover {
    transform:translateY(-5px);
    box-shadow:0 18px 35px rgba(151,67,106,.16);
}

[data-testid="stMetricLabel"] {
    color:#997087 !important;
    font-size:12px;
    font-weight:600;
}

[data-testid="stMetricValue"] {
    color:#A83E70 !important;
    font-size:27px;
    font-weight:800;
}

[data-testid="stMetricDelta"] {font-size:11px;}

.stPlotlyChart {
    background:rgba(255,255,255,.64);
    backdrop-filter:blur(18px);
    border:1px solid rgba(255,255,255,.95);
    border-radius:21px;
    padding:10px;
    box-shadow:0 10px 28px rgba(151,67,106,.08);
}

[data-testid="stDataFrame"] {
    background:rgba(255,255,255,.75);
    border:1px solid white;
    border-radius:16px;
}

.stButton button,.stDownloadButton button,
.stFormSubmitButton button {
    background:linear-gradient(120deg,#A83E70,#D4779D);
    color:white !important;
    border:0;
    border-radius:12px;
    font-weight:600;
    transition:.25s;
    box-shadow:0 5px 15px rgba(168,62,112,.16);
}

.stButton button:hover,.stDownloadButton button:hover {
    transform:translateY(-3px);
    box-shadow:0 10px 22px rgba(168,62,112,.25);
}

.stTextInput input {
    background:rgba(255,255,255,.85);
    border:1px solid #E9C4D4;
    border-radius:12px;
    color:#71364F;
}

.stSelectbox div[data-baseweb="select"],
.stMultiSelect div[data-baseweb="select"] {
    background:rgba(255,255,255,.8);
    border-radius:10px;
}

[data-testid="stRadio"] label {font-weight:500;}

.glass-note {
    background:rgba(255,255,255,.65);
    border:1px solid rgba(255,255,255,.9);
    border-radius:16px;
    padding:17px;
    color:#81516A;
    box-shadow:0 7px 22px rgba(151,67,106,.07);
}

.login-box {
    background:rgba(255,255,255,.73);
    backdrop-filter:blur(25px);
    border:1px solid white;
    border-radius:28px;
    padding:35px;
    box-shadow:0 20px 55px rgba(151,67,106,.16);
    text-align:center;
}

.footer {
    text-align:center;
    color:#A47A90;
    font-size:11px;
    padding:25px;
    margin-top:30px;
    border-top:1px solid rgba(255,255,255,.8);
}

@media(prefers-reduced-motion:reduce) {
    *,*::before,*::after {animation:none !important;transition:none !important;}
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# LOGIN
# =====================================================
if not st.session_state.auth:

    st.markdown("<br><br>", unsafe_allow_html=True)
    left, center, right = st.columns([1,1.1,1])

    with center:
        st.markdown("""
        <div class="login-box">
          <div style="font-size:48px;">◈</div>
          <h1 style="font-family:'Playfair Display',serif;color:#A83E70!important;">
          Retail Analytics
          </h1>
          <p>PREMIUM BUSINESS INTELLIGENCE</p>
          <hr style="border-color:#F0D7E2;">
          <h3>Welcome Back</h3>
          <p>Sign in to access your analytics workspace</p>
        </div>
        """, unsafe_allow_html=True)

        with st.form("login"):
            email = st.text_input("Email Address",placeholder="admin@retail.com")
            password = st.text_input("Password",type="password",placeholder="Enter password")
            submit = st.form_submit_button("Sign In →",use_container_width=True)

            if submit:
                entered_hash = hashlib.sha256(password.encode()).hexdigest()
                if (hmac.compare_digest(email.strip().lower(),EMAIL) and
                    hmac.compare_digest(entered_hash,PASSWORD_HASH)):
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("Incorrect email or password.")

        st.caption("Demo access | Secure session-based login")

    st.stop()

# =====================================================
# DATA
# =====================================================
path = Path(__file__).parent / "retail_sales_data.csv"

try:
    df = pd.read_csv(path,parse_dates=["Order_Date"])
except Exception as e:
    st.error(f"Dataset loading error: {e}")
    st.stop()

required = ["Order_Date","Region","Category","Product",
            "Payment_Method","Total_Sales","Quantity"]

if any(c not in df.columns for c in required):
    st.error("Please verify your dataset column names.")
    st.stop()

if df.empty or df["Order_Date"].dropna().empty:
    st.error("No valid sales records found.")
    st.stop()

# =====================================================
# SIDEBAR NAVIGATION
# =====================================================
with st.sidebar:
    st.markdown('<div class="brand">Retail Élité</div>',unsafe_allow_html=True)
    st.markdown('<div class="brand-sub">ANALYTICS STUDIO</div>',unsafe_allow_html=True)

    st.markdown("### WORKSPACE")
    page = st.radio(
        "Navigation",
        ["Overview","Product Analysis","Transactions","Reports"],
        label_visibility="collapsed"
    )
    st.session_state.page = page

    st.divider()
    st.markdown("### FILTERS")

    regions = st.multiselect(
        "Region",sorted(df["Region"].dropna().unique()),
        default=sorted(df["Region"].dropna().unique())
    )
    categories = st.multiselect(
        "Category",sorted(df["Category"].dropna().unique()),
        default=sorted(df["Category"].dropna().unique())
    )
    products = st.multiselect(
        "Product",sorted(df["Product"].dropna().unique()),
        default=sorted(df["Product"].dropna().unique())
    )
    payments = st.multiselect(
        "Payment Method",sorted(df["Payment_Method"].dropna().unique()),
        default=sorted(df["Payment_Method"].dropna().unique())
    )

    dates = st.date_input(
        "Date Range",
        value=(df["Order_Date"].min().date(),
               df["Order_Date"].max().date())
    )

    st.divider()
    st.markdown("**● Administrator**")
    st.caption("Active session")

    if st.button("↪ Logout",use_container_width=True):
        st.session_state.auth = False
        st.rerun()

# =====================================================
# FILTERED DATA
# =====================================================
filtered = df[
    df["Region"].isin(regions) &
    df["Category"].isin(categories) &
    df["Product"].isin(products) &
    df["Payment_Method"].isin(payments)
].copy()

if isinstance(dates,(tuple,list)) and len(dates)==2:
    filtered = filtered[
        (filtered["Order_Date"].dt.date>=dates[0]) &
        (filtered["Order_Date"].dt.date<=dates[1])
    ]

if filtered.empty:
    st.warning("No matching transactions. Adjust your filters.")
    st.stop()

# =====================================================
# CHART THEME
# =====================================================
pink = ["#AD4675","#CF6F98","#E69BB8","#F0BCD0","#B98BA7"]

layout = dict(
    paper_bgcolor="rgba(255,255,255,0)",
    plot_bgcolor="rgba(255,255,255,0)",
    font=dict(family="DM Sans",color="#70445D",size=12),
    title_font=dict(size=17,color="#85425F"),
    margin=dict(l=25,r=25,t=60,b=35),
    hoverlabel=dict(bgcolor="white",font_color="#70445D")
)

# =====================================================
# HERO
# =====================================================
st.markdown("""
<div class="hero">
 <div class="eyebrow">BUSINESS INTELLIGENCE PLATFORM</div>
 <h1>Retail Performance Overview</h1>
 <p>Discover insights. Understand performance. Make smarter decisions.</p>
</div>
""",unsafe_allow_html=True)

# =====================================================
# COMMON KPIs
# =====================================================
revenue = filtered["Total_Sales"].sum()
transactions = len(filtered)
quantity = filtered["Quantity"].sum()
average = filtered["Total_Sales"].mean()

def show_kpis():
    a,b,c,d = st.columns(4)
    a.metric("Total Revenue",f"₹{revenue:,.0f}")
    b.metric("Transactions",f"{transactions:,}")
    c.metric("Products Sold",f"{quantity:,}")
    d.metric("Average Sales",f"₹{average:,.2f}")

# =====================================================
# OVERVIEW PAGE
# =====================================================
if page == "Overview":

    st.subheader("Performance Snapshot")
    show_kpis()

    st.markdown("### Business Insights")

    top_product = filtered.groupby("Product")["Quantity"].sum().idxmax()
    best_region = filtered.groupby("Region")["Total_Sales"].sum().idxmax()
    month_sales = filtered.groupby(filtered["Order_Date"].dt.month)["Total_Sales"].sum()
    best_month = pd.Timestamp(
        year=2000,month=int(month_sales.idxmax()),day=1
    ).strftime("%B")

    a,b,c = st.columns(3)
    a.metric("Top Selling Product",top_product)
    b.metric("Best Performing Region",best_region)
    c.metric("Highest Sales Month",best_month)

    st.markdown("### Revenue & Category Intelligence")

    monthly = filtered.groupby(
        filtered["Order_Date"].dt.to_period("M")
    )["Total_Sales"].sum().reset_index()
    monthly["Month"] = monthly["Order_Date"].astype(str)

    categories_sales = filtered.groupby("Category")["Total_Sales"].sum().reset_index()

    left,right = st.columns([1.7,1])

    with left:
        fig = px.area(
            monthly,x="Month",y="Total_Sales",
            title="Revenue Growth Trend",
            markers=True
        )
        fig.update_traces(
            line_color="#B94F7C",
            fillcolor="rgba(217,121,159,.20)"
        )
        fig.update_layout(**layout)
        st.plotly_chart(fig,use_container_width=True)

    with right:
        fig = px.pie(
            categories_sales,names="Category",values="Total_Sales",
            hole=.62,title="Revenue by Category",
            color_discrete_sequence=pink
        )
        fig.update_layout(**layout)
        fig.update_traces(
            textposition="inside",
            textinfo="percent+label"
        )
        st.plotly_chart(fig,use_container_width=True)

    st.markdown("### Regional Performance")
    region = filtered.groupby("Region")["Total_Sales"].sum().reset_index()
    fig = px.bar(
        region,x="Region",y="Total_Sales",
        color="Region",color_discrete_sequence=pink,
        title="Revenue Across Regions"
    )
    fig.update_layout(**layout,showlegend=False)
    st.plotly_chart(fig,use_container_width=True)

# =====================================================
# PRODUCT ANALYSIS
# =====================================================
elif page == "Product Analysis":

    st.subheader("Product Intelligence")
    show_kpis()

    product = filtered.groupby("Product").agg(
        Quantity=("Quantity","sum"),
        Revenue=("Total_Sales","sum")
    ).reset_index().sort_values("Revenue",ascending=False)

    left,right = st.columns(2)

    with left:
        fig = px.bar(
            product,x="Product",y="Quantity",
            color="Product",color_discrete_sequence=pink,
            title="Product-wise Quantity Sold"
        )
        fig.update_layout(**layout,showlegend=False)
        st.plotly_chart(fig,use_container_width=True)

    with right:
        fig = px.bar(
            product,x="Product",y="Revenue",
            color="Product",color_discrete_sequence=pink,
            title="Product-wise Revenue"
        )
        fig.update_layout(**layout,showlegend=False)
        st.plotly_chart(fig,use_container_width=True)

    st.markdown("### Product Performance Table")
    st.dataframe(product,use_container_width=True,hide_index=True)

# =====================================================
# TRANSACTIONS
# =====================================================
elif page == "Transactions":

    st.subheader("Transaction Management")
    show_kpis()

    search = st.text_input("Search transactions or products")

    result = filtered.copy()

    if search:
        mask = result.astype(str).apply(
            lambda col: col.str.contains(search,case=False,na=False)
        ).any(axis=1)
        result = result[mask]

    st.caption(f"{len(result):,} matching records")
    st.dataframe(result,use_container_width=True,hide_index=True)

# =====================================================
# REPORTS
# =====================================================
elif page == "Reports":

    st.subheader("Sales Reports & Export")
    show_kpis()

    st.markdown("""
    <div class="glass-note">
    <b>Your business report is ready.</b><br>
    Download the filtered transaction records for further analysis.
    </div>
    """,unsafe_allow_html=True)

    st.markdown("### Report Summary")

    summary = filtered.groupby("Region").agg(
        Transactions=("Total_Sales","count"),
        Revenue=("Total_Sales","sum"),
        Products_Sold=("Quantity","sum")
    ).reset_index()

    st.dataframe(summary,use_container_width=True,hide_index=True)

    st.download_button(
        "↓ Download Full Sales Report",
        data=filtered.to_csv(index=False).encode("utf-8"),
        file_name="retail_sales_report.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.download_button(
        "↓ Download Regional Summary",
        data=summary.to_csv(index=False).encode("utf-8"),
        file_name="regional_sales_summary.csv",
        mime="text/csv",
        use_container_width=True
    )

# =====================================================
# FOOTER
# =====================================================
st.markdown("""
<div class="footer">
RETAIL ÉLITÉ · PREMIUM ANALYTICS STUDIO<br>
Business Intelligence | Retail Performance | Data Insights
</div>
""",unsafe_allow_html=True)
