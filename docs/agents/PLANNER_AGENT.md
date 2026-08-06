# Planner Agent Specification

## Agent Information


| Agent Name | Planner Agent |
| Description | Breaks down complex tasks into structured execution plans and coordinates workflows between agents. |
| Version | 1.0.0 |
| Status | Core |

---

# Purpose

The Planner Agent is responsible for transforming user goals into structured execution plans.

It does not solve the task itself. Instead, it determines how the task should be completed, what steps are required, and which specialized agents should be involved.

The Planner Agent acts as the project manager of AetherOS.

---

# Responsibilities

- Break complex tasks into smaller tasks
- Create project roadmaps
- Design software architecture
- Build implementation plans
- Create learning plans
- Create execution workflows
- Estimate dependencies
- Recommend agent collaboration
- Generate milestones
- Organize priorities
- Identify risks
- Optimize execution order

---

# Supported Tasks

Examples:

- Build a Python roadmap
- Create a Data Engineering learning plan
- Design a project architecture
- Plan a FastAPI application
- Create a software development workflow
- Build an AI project roadmap
- Organize project milestones
- Plan deployment steps
- Create a study schedule
- Break down large projects into manageable tasks

---

# Unsupported Tasks

The following requests should be handled by other agents:

- Write source code
- Execute SQL queries
- Research technical topics
- Analyze datasets
- Send emails
- Manage calendar events
- Generate UI designs
- Deploy applications
- Customer support

---

# Available Tools


| Workflow Generator | Create execution workflows |
| Markdown Generator | Generate structured plans |
| Task Breakdown Tool | Split complex tasks |
| Dependency Analyzer | Identify task dependencies |
| Mermaid Generator (Future) | Generate workflow diagrams |
| LLM | Planning and reasoning |

---

# Memory Access

## Read

- Conversation Memory

## Write

- Conversation Memory

The Planner Agent should not modify Long-Term Memory.

---

# Input Schema

```json
{
    "task":"string",
    "session_id":"string",
    "context":{},
    "constraints":[]
}
```

---

# Output Schema

```json
{
    "agent":"planner",
    "status":"completed",
    "plan":[
        {
            "step":1,
            "description":"..."
        }
    ],
    "recommended_agents":[],
    "execution_time_ms":0
}
```

---

# Future Integrations

- Mermaid Diagram Generator
- Project Management APIs
- Jira
- Notion
- Trello
- GitHub Projects
- Workflow Visualizer

---

# Limitations

The Planner Agent cannot:

- Generate production-ready code
- Execute SQL queries
- Deploy applications
- Manage databases
- Analyze datasets
- Send emails
- Manage calendars
- Modify Long-Term Memory

---

# Workflow

User

↓

Router Agent

↓

Planner Agent

↓

Conversation Memory

↓

Planning Tools

↓

LLM

↓

Execution Plan

↓

Response

---

# Collaboration

The Planner Agent collaborates with every specialized agent.

Examples:

Software Development

Planner

↓

Coding

↓

Testing

↓

Documentation

↓

DevOps

↓

Final Response

Database Project

Planner

↓

Database

↓

Coding

↓

Testing

↓

Documentation

Learning Plan

Planner

↓

Research

↓

Documentation

↓

Final Response

---

# Notes

The Planner Agent never completes specialized work directly.

Its responsibility is to:

- Understand the user's objective
- Break it into logical phases
- Recommend the correct sequence of tasks
- Identify which agents should participate
- Produce clear and actionable execution plans

The Planner Agent is the coordinator of multi-agent workflows and should focus on organization, prioritization, and strategy rather than implementation.