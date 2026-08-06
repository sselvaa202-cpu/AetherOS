# General Agent Specification

## Agent Information

Agent Name  :  General Agent 
Description :  Handles general conversations and acts as the default AI assistant. 
Version     :  1.0.0 
Status      :  Core 

---

# Purpose

The General Agent is responsible for handling everyday conversations with the user.

It serves as the default agent whenever no specialized agent is required.

It is also responsible for maintaining conversational context and interacting with the memory system.

---

# Responsibilities

- Greeting users
- General conversation
- Answering general questions
- Remembering user preferences
- Retrieving previous conversation
- Maintaining conversation context
- Asking follow-up questions when needed
- Redirecting complex requests through the Router Agent

---

# Supported Tasks

Examples:

- Hello
- Hi
- Good Morning
- My name is Selva
- Remember my favorite language
- What is my name?
- Tell me a joke
- Explain Artificial Intelligence
- Thank you
- How are you?

---

# Unsupported Tasks

The following requests should be routed to specialized agents:

- Programming
- SQL Queries
- Database Design
- Financial Planning
- Email Management
- Calendar Scheduling
- UI Design
- DevOps
- Data Analysis
- Testing
- Documentation

---

# Available Tools

Tool   : Purpose 
LLM    : Generate responses 
Conversation Memory : Store current conversation 
Long-Term Memory : Store persistent user information 
Prompt Builder : Build context-aware prompts 

---

# Memory Access

## Read

- Conversation Memory
- Long-Term Memory

## Write

- Conversation Memory
- Long-Term Memory

---

# Input Schema

```json
{
    "task":"string",
    "session_id":"string",
    "context":{}
}
```

---

# Output Schema

```json
{
    "agent":"general",
    "status":"completed",
    "response":"...",
    "tool_used":"llm"
}
```

---

# Future Integrations

- Voice Agent
- Emotion Detection
- Translation
- Personal Assistant
- Reminder System

---

# Limitations

The General Agent cannot:

- Execute SQL
- Write production code
- Deploy applications
- Manage Docker
- Access GitHub directly
- Send emails
- Manage Calendar
- Analyze datasets

---

# Workflow

User

↓

Router Agent

↓

General Agent

↓

Conversation Memory

↓

Long-Term Memory

↓

LLM

↓

Response

---

# Notes

The General Agent acts as the default fallback agent.

If the Router Agent cannot confidently classify a request, it should always route it here.