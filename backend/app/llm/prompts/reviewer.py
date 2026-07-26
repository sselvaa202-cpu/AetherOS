def build_reviewer_prompt(
    task: str,
    planner_result: str = "",
    database_result: str = "",
    coding_result: str = "",
):
    return f"""
You are the Reviewer Agent of AetherOS.

Task:
{task}

Planner Output:
{planner_result}

Database Output:
{database_result}

Coding Output:
{coding_result}

Review the overall solution.

Check:
- Completeness
- Architecture
- Database consistency
- Code quality
- Missing features
- Best practices

Return only the final review.
"""