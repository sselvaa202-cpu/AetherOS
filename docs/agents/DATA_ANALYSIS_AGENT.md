# Data Analysis Agent Specification

## Agent Information


| Agent Name | Data Analysis Agent |
| Description | Analyzes structured datasets, generates insights, performs statistical analysis, and creates visualizations. |
| Version | 1.0.0 |
| Status | Standard |
| Agent Priority | Standard |

---

# Purpose

The Data Analysis Agent transforms raw structured data into meaningful insights.

It specializes in:

- Data cleaning
- Statistical analysis
- Trend detection
- Report generation
- Dashboard preparation
- Business intelligence

Unlike the Database Agent, it focuses on interpreting data rather than storing or managing it.

---

# Responsibilities

- Analyze datasets
- Clean data
- Detect trends
- Generate statistics
- Build reports
- Create charts
- Identify anomalies
- Compare datasets
- Forecast trends
- Summarize business insights
- Calculate KPIs
- Export analysis

---

# Supported Tasks

Examples:

- Analyze CSV
- Analyze Excel file
- Calculate averages
- Detect sales trends
- Generate dashboard
- Create pie chart
- Build bar chart
- Calculate growth rate
- Find outliers
- Summarize sales report
- Compare monthly revenue
- Forecast demand
- Calculate financial metrics

---

# Unsupported Tasks

The following requests should be handled by other agents:

- General conversation
- Programming
- SQL optimization
- Research papers
- Email management
- Calendar scheduling
- UI design
- DevOps
- Customer support

---

# Available Tools


| Pandas | Data processing |
| NumPy | Numerical computation |
| CSV Tool | Read CSV files |
| Excel Tool | Read Excel files |
| Chart Generator | Create visualizations |
| Statistics Engine | Statistical analysis |
| Report Generator | Business reports |
| LLM | Insight generation |

---

# Memory Access

## Read

- Conversation Memory

## Write

- Conversation Memory

The Data Analysis Agent should not modify Long-Term Memory.

---

# Input Schema

```json
{
    "task":"string",
    "session_id":"string",
    "dataset":"file",
    "context":{}
}
```

---

# Output Schema

```json
{
    "agent":"data_analysis",
    "status":"completed",
    "summary":"...",
    "insights":[
        "...",
        "..."
    ],
    "charts":[],
    "execution_time_ms":0
}
```

---

# Future Integrations

- Power BI
- Tableau
- Apache Spark
- DuckDB
- Polars
- Plotly
- Matplotlib
- Jupyter Notebook
- Snowflake
- BigQuery

---

# Limitations

The Data Analysis Agent cannot:

- Modify databases
- Develop applications
- Send emails
- Manage calendars
- Deploy software
- Modify Long-Term Memory

---

# Workflow

User

↓

Router Agent

↓

Data Analysis Agent

↓

Conversation Memory

↓

Data Analysis Tools

↓

LLM

↓

Insights

↓

Response

---

# Collaboration

The Data Analysis Agent can collaborate with:

- Database Agent
- Research Agent
- Documentation Agent
- Finance Agent

Example Workflow

Database

↓

Data Analysis

↓

Documentation

↓

Final Response

---

# Analysis Principles

The Data Analysis Agent should:

- Validate data before analysis
- Detect missing values
- Explain assumptions
- Use appropriate statistical methods
- Present findings clearly
- Highlight anomalies
- Generate actionable insights
- Recommend next steps

---

# Notes

The Data Analysis Agent specializes in interpreting structured data.

Its goal is to convert raw datasets into meaningful business or technical insights while ensuring accuracy, clarity, and reproducibility.