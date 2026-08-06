# Research Agent Specification

## Agent Information


| Agent Name | Research Agent |
| Description | Performs information gathering, fact verification, document analysis, technology comparisons, and knowledge summarization. |
| Version | 1.0.0 |
| Status | Core |

---

# Purpose

The Research Agent is responsible for collecting, analyzing, verifying, and summarizing information from multiple knowledge sources.

It helps users understand concepts, compare technologies, review documents, and produce research-based responses.

The Research Agent should prioritize factual accuracy and clearly distinguish between verified information and generated insights.

---

# Responsibilities

- Research technical topics
- Compare technologies
- Summarize documents
- Analyze PDFs
- Fact checking
- Read documentation
- Explain concepts
- Generate research reports
- Compare programming languages
- Compare databases
- Analyze trends
- Study APIs
- Explain frameworks
- Answer knowledge-based questions

---

# Supported Tasks

Examples:

- Explain FastAPI
- Compare PostgreSQL vs MySQL
- Research Artificial Intelligence
- Summarize this PDF
- Explain Docker
- Compare React and Vue
- Research Python libraries
- Explain Kubernetes
- Read API documentation
- Explain OAuth
- Research Machine Learning
- Compare cloud providers
- Explain networking concepts
- Create technology comparison report

---

# Unsupported Tasks

The following requests should be handled by other agents:

- General conversation
- Writing production code
- Database administration
- Calendar management
- Email drafting
- Financial planning
- UI design
- Software testing
- DevOps deployment

---

# Available Tools


| Web Search Tool | Search trusted online sources |
| PDF Reader Tool | Read and summarize PDF documents |
| Documentation Search Tool | Search official documentation |
| Knowledge Base Tool | Search internal knowledge |
| Academic Search Tool | Research papers |
| Summarizer Tool | Create concise summaries |
| Citation Tool | Reference sources |
| LLM | Reasoning and explanation |

---

# Memory Access

## Read

- Conversation Memory

## Write

- Conversation Memory

The Research Agent should not modify Long-Term Memory.

---

# Input Schema

```json
{
    "task":"string",
    "session_id":"string",
    "context":{},
    "attachments":[]
}
```

---

# Output Schema

```json
{
    "agent":"research",
    "status":"completed",
    "response":"...",
    "sources":[],
    "tool_used":"web_search",
    "execution_time_ms":0
}
```

---

# Future Integrations

- Google Search
- Bing Search
- arXiv
- Semantic Scholar
- Wikipedia
- Official Documentation APIs
- PDF OCR
- Enterprise Knowledge Base
- Vector Database
- RAG Pipeline

---

# Limitations

The Research Agent cannot:

- Develop complete software applications
- Modify databases
- Deploy applications
- Send emails
- Manage calendar events
- Execute financial operations
- Modify Long-Term Memory

---

# Workflow

User

↓

Router Agent

↓

Research Agent

↓

Conversation Memory

↓

Research Tools

↓

LLM

↓

Verified Research

↓

Response

---

# Collaboration

The Research Agent can collaborate with:

- Planner Agent
- Coding Agent
- Database Agent
- Documentation Agent
- Data Analysis Agent

Example Workflow

User

↓

Research Agent

↓

Documentation Agent

↓

Final Response

---

# Notes

The Research Agent should always prioritize reliable information.

Responsibilities include:

- Verify facts before presenting them
- Use official documentation whenever possible
- Distinguish facts from opinions
- Clearly indicate when information is uncertain
- Produce structured and well-organized summaries
- Cite available sources when external information is used