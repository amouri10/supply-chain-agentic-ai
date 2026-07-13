import os
import asyncio
import streamlit as st
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process

# Load environment configurations
load_dotenv()

# Configure an ultra-clean, modern wider page layout
st.set_page_config(page_title="Autonomous Procurement Engine", page_icon="🛒", layout="wide")

# Theme styling override for an executive dark-mode presentation aesthetic
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stTextArea textarea { background-color: #161b22; color: #c9d1d9; border: 1px solid #30363d; }
    .stNumberInput input { background-color: #161b22; color: #c9d1d9; border: 1px solid #30363d; }
    div[data-testid="stMetricValue"] { color: #58a6ff; font-family: monospace; }
    .report-box { background-color: #161b22; padding: 24px; border-radius: 8px; border: 1px solid #30363d; color: #ffffff; }
    </style>
""", unsafe_allow_html=True)

st.title("🛒 Enterprise Supply Chain & Procurement Engine")
st.markdown("An autonomous multi-agent fleet mitigating inventory stock deficits and negotiating B2B contracts.")
st.markdown("---")

# Layout Splitting: Parameters on the left, data on the right
col1, col2 = st.columns(2)

with col1:
    st.subheader("⚙️ Customizable Parameters")
    target_supplier = st.text_input("Target Wholesale Vendor:", value="AlphaManufacturing Co.")
    retail_price = st.number_input("Retail Price per Unit ($):", value=149.99, step=10.0)
    max_wholesale_margin = st.slider("Max Wholesale Cost Ceiling (% of Retail):", min_value=10, max_value=80, value=40)
    
    st.markdown("---")
    st.subheader("📦 Live Real-Time Inventory Alert Data")
    sample_system_alert = (
        "CRITICAL STOCK ALERT | Warehouse: WH-MIDWEST | "
        "Item: EcoSmart Pro Noise-Cancelling Headphones (SKU: ECO-HEAD-092) | "
        "Current Stock: 4 units | Safety Re-order Buffer: 100 units | "
        "Pending Customer Unfulfilled Backlog: 245 units due to viral marketing surge."
    )
    inventory_log = st.text_area("System Log Feed:", value=sample_system_alert, height=140)

# OPTIMIZATION: Cache the agent network creation so the UI boots up instantly
@st.cache_resource
def setup_procurement_fleet():
    # Agent 1: The Logistics Strategist
    logistics_strategist = Agent(
        role="Senior E-Commerce Logistics Analyst",
        goal="Parse inventory stock notifications and calculate mathematically optimal restocking targets.",
        backstory=(
            "You are a master of supply chain metrics. You analyze system inventory alert files, "
            "compute required backlog additions, and determine exact restock numbers."
        ),
        verbose=True,
        allow_delegation=False
    )

    # Agent 2: The B2B Wholesale Negotiator
    procurement_negotiator = Agent(
        role="Lead Global B2B Procurement Specialist",
        goal="Construct persuasive, professional wholesale acquisition contracts and formal purchase orders.",
        backstory=(
            "You are a sharp corporate buyer. You take supply chain requirements profiles "
            "and craft formal supplier negotiation emails maintaining absolute corporate presence."
        ),
        verbose=True,
        allow_delegation=False
    )
    return logistics_strategist, procurement_negotiator

def run_procurement_suite(inventory_alert_log: str, vendor: str, retail: float, margin_ceiling: float):
    # Fetch cached agents instantly
    logistics_strategist, procurement_negotiator = setup_procurement_fleet()

    # Task 1: Deficit Evaluation
    task_logistics = Task(
        description=(
            f"Process this automated alert data:\n\n{inventory_alert_log}\n\n"
            f"Calculate the absolute minimum restock quantity to cover the safety buffer and backlogs. "
            f"Note that standard retail is ${retail} and wholesale target cost must stay under {margin_ceiling}% of retail."
        ),
        expected_output="A structured supply chain brief mapping out calculated restock metrics and exact financial thresholds.",
        agent=logistics_strategist
    )

    # Task 2: Supplier Contract Negotiation Draft
    task_negotiate = Task(
        description=(
            f"Review the supply brief. Draft a professional, formal B2B wholesale purchase order email "
            f"addressed directly to {vendor}. Outline the target bulk pricing based on the math rules, "
            f"assert a volume discount based on the massive deficit, and request concrete delivery timelines."
        ),
        expected_output="A ready-to-send corporate B2B vendor contract proposal email containing exact inventory numbers and delivery milestones.",
        agent=procurement_negotiator
    )

    ecommerce_crew = Crew(
        agents=[logistics_strategist, procurement_negotiator],
        tasks=[task_logistics, task_negotiate],
        process=Process.sequential
    )

    # Windows safe Async loop handler
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    return ecommerce_crew.kickoff()

with col2:
    st.subheader("📊 Output & Agent Collaboration Traces")
    
    # Live KPI previews based on UI inputs
    kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
    kpi_col1.metric("Retail Anchor", f"${retail_price:.2f}")
    kpi_col2.metric("Wholesale Ceiling", f"${(retail_price * (max_wholesale_margin/100)):.2f}")
    kpi_col3.metric("Target Margin", f"{100 - max_wholesale_margin}%")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("🚀 Trigger Fleet Procurement Outflow", type="primary", use_container_width=True):
        with st.spinner("🤖 E-Commerce agents are processing logistics data and drafting B2B bids..."):
            try:
                # Fire the connected backend logic pipeline passing user configurations
                result = run_procurement_suite(inventory_log, target_supplier, retail_price, max_wholesale_margin)
                
                st.success("✅ Supply Chain Remediation Strategy Formulated!")
                st.subheader("✉️ Generated B2B Vendor Procurement Proposal")
                st.markdown(f"<div class='report-box'>{result}</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Execution Error: {str(e)}")
