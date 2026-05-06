# Streamlit Complete App

A reference Streamlit application that demonstrates all major UI components alongside a MongoDB-connected task manager — everything in a single file.

## Features

### Home Page — Streamlit Elements
| Element | Description |
|---|---|
| `st.title` | Page title |
| `st.header` | Section header |
| `st.subheader` | Sub-section header |
| `st.markdown` | Rich text, tables, bold/italic |
| `st.write` | Print text, numbers, dicts, lists |
| `st.text` | Raw monospace text |
| `st.caption` | Small helper text |
| `st.code` | Syntax-highlighted code block |
| `st.metric` | KPI cards with delta |
| `st.info / success / warning / error` | Colored alert boxes |
| `st.expander` | Collapsible content section |

### Sidebar
- `st.sidebar.title`, `st.sidebar.text`, `st.sidebar.radio`
- `st.sidebar.subheader`, `st.sidebar.info`, `st.sidebar.markdown`, `st.sidebar.caption`

### Task Form Page — MongoDB Integration
- Single tab with multiple input types:
  - `st.text_input`, `st.selectbox`, `st.date_input`
  - `st.radio`, `st.multiselect`, `st.slider`, `st.checkbox`
  - `st.text_area` (×2)
- Saves form data to MongoDB on submit
- Displays the last 10 saved tasks in a dataframe

## Requirements

- Python 3.9+
- MongoDB running locally on `localhost:27017` (or MongoDB Atlas)

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python -m streamlit run app.py
```

App opens at **http://localhost:8501**

## MongoDB Setup

**Local (MongoDB Compass):** Make sure the MongoDB service is running.
```powershell
net start MongoDB
```

**Atlas (cloud):** Replace `MONGO_URI` in `app.py` with your Atlas connection string:
```python
MONGO_URI = "mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/"
```

Data is stored in:
- Database: `streamlit_demo`
- Collection: `tasks`
