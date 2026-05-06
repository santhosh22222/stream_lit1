# Streamlit Complete App

A reference Streamlit application that demonstrates all major UI components alongside a MongoDB-connected task manager — everything in a single file.
# screenshots
<img width="1868" height="905" alt="image" src="https://github.com/user-attachments/assets/0520b313-ca96-4739-a3ad-79ec14788a61" />
<img width="1646" height="880" alt="image" src="https://github.com/user-attachments/assets/fd82d5cc-ccec-4729-8c38-e0702894f17e" />
<img width="1891" height="940" alt="image" src="https://github.com/user-attachments/assets/11f86f24-a75e-485c-b308-c13ef4934d37" />
<img width="1874" height="898" alt="image" src="https://github.com/user-attachments/assets/66cc7434-9987-4901-8f24-5221f0488b22" />



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
