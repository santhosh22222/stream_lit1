import streamlit as st
from pymongo import MongoClient
from datetime import datetime

# ─── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="Streamlit Complete App", layout="wide")

# ─── Sidebar ───────────────────────────────────────────────────────────────────
st.sidebar.title("Navigation")
st.sidebar.text("Choose a section below:")
st.sidebar.markdown("---")
page = st.sidebar.radio("Go to", ["Home", "Task Form"])
st.sidebar.markdown("---")
st.sidebar.subheader("About")
st.sidebar.info("This app demonstrates Streamlit components + MongoDB integration.")
st.sidebar.markdown("**Built with** `Streamlit` & `pymongo`")
st.sidebar.caption("v1.0 — 2026")

# ─── MongoDB Connection ─────────────────────────────────────────────────────────
# Replace with your Atlas URI if using cloud MongoDB:
# "mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/"
MONGO_URI = "mongodb://localhost:27017/"

@st.cache_resource
def get_db():
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
    client.admin.command("ping")   # raises immediately if not reachable
    return client["streamlit_demo"]["tasks"]

def mongo_available():
    try:
        get_db()
        return True, None
    except Exception as e:
        return False, str(e)

# ─── HOME PAGE ─────────────────────────────────────────────────────────────────
if page == "Home":

    st.title("Streamlit Complete App")
    st.header("Explore Streamlit Elements")
    st.subheader("Every common component in one place")

    st.markdown("""
Welcome to the **Streamlit Complete App**!
This page showcases all major *text display* elements.

> Use the **sidebar** to navigate between sections.
""")

    st.write("### st.write — prints anything")
    st.write("Plain text", 42, 3.14, True, {"key": "value"}, [1, 2, 3])

    st.text("st.text — monospace, no markdown, exact whitespace:  hello   world")

    st.markdown("---")
    st.markdown("""
| Element | Purpose |
|---|---|
| `st.title` | Page title |
| `st.header` | Section header |
| `st.subheader` | Sub-section header |
| `st.markdown` | Rich markdown text |
| `st.write` | Print anything |
| `st.text` | Raw monospace text |
| `st.caption` | Small helper text |
| `st.code` | Syntax-highlighted code |
| `st.metric` | KPI cards |
""")

    st.caption("Caption: small helper text shown above")

    st.code("""
# Example Python snippet
def greet(name: str) -> str:
    return f"Hello, {name}!"
""", language="python")

    st.markdown("---")
    st.subheader("Metric Cards")
    col1, col2, col3 = st.columns(3)
    col1.metric("Users", "1,234", "+12%")
    col2.metric("Revenue", "$5,678", "-3%")
    col3.metric("Tasks Done", "89", "+5")

    st.markdown("---")
    st.subheader("Media & Display")
    st.info("st.info — informational message")
    st.success("st.success — success message")
    st.warning("st.warning — warning message")
    st.error("st.error — error message")

    with st.expander("Click to expand hidden content"):
        st.write("This content was hidden inside `st.expander`.")
        st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=100)

# ─── TASK FORM PAGE ────────────────────────────────────────────────────────────
elif page == "Task Form":

    st.title("Task Manager")
    st.header("Single Tab — Multiple Inputs")
    st.subheader("Fill the form below and save to MongoDB")
    st.markdown("---")

    db_ok, db_err = mongo_available()
    if not db_ok:
        st.error(f"MongoDB not connected: {db_err}")
        st.info("""
**To fix this, choose one option:**

**Option A — Local MongoDB**
1. Download & install: https://www.mongodb.com/try/download/community
2. Start it: open PowerShell as Admin → `net start MongoDB`

**Option B — MongoDB Atlas (free cloud)**
1. Sign up at https://cloud.mongodb.com
2. Create a free cluster → get your connection string
3. Open `app.py` and replace `MONGO_URI` at the top with your Atlas URI
        """)
        st.stop()

    with st.form("task_form", clear_on_submit=True):
        col1, col2 = st.columns(2)

        with col1:
            task_name   = st.text_input("Task Name", placeholder="e.g. Fix login bug")
            assigned_to = st.text_input("Assigned To", placeholder="e.g. Alice")
            priority    = st.selectbox("Priority", ["Low", "Medium", "High", "Critical"])
            due_date    = st.date_input("Due Date", value=datetime.today())

        with col2:
            status      = st.radio("Status", ["Pending", "In Progress", "Completed"])
            tags        = st.multiselect("Tags", ["Bug", "Feature", "Docs", "Refactor", "Testing"])
            progress    = st.slider("Progress (%)", 0, 100, 0, step=5)
            notify      = st.checkbox("Send email notification")

        description = st.text_area("Description", placeholder="Describe the task in detail…", height=120)
        notes       = st.text_area("Additional Notes", placeholder="Any extra context…", height=80)

        submitted = st.form_submit_button("Save Task to MongoDB", use_container_width=True)

    if submitted:
        if not task_name.strip():
            st.error("Task Name is required.")
        else:
            doc = {
                "task_name":   task_name,
                "assigned_to": assigned_to,
                "priority":    priority,
                "due_date":    str(due_date),
                "status":      status,
                "tags":        tags,
                "progress":    progress,
                "notify":      notify,
                "description": description,
                "notes":       notes,
                "created_at":  datetime.utcnow(),
            }
            collection = get_db()
            result = collection.insert_one(doc)
            st.success(f"Task saved! MongoDB ID: `{result.inserted_id}`")
            st.balloons()

    st.markdown("---")
    st.subheader("Saved Tasks")

    collection = get_db()
    tasks = list(collection.find({}, {"_id": 0}).sort("created_at", -1).limit(10))
    if tasks:
        st.dataframe(tasks, use_container_width=True)
    else:
        st.info("No tasks saved yet. Submit the form above to create one.")
