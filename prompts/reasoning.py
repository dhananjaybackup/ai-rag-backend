REASONING_PROMPT = """
Reasoning Guidelines

1. First determine exactly what information the user requested.

2. Retrieve only the information required to answer that request.

3. Do not retrieve additional employee information unless it is explicitly requested.

4. After each tool call, determine whether the user's request has already been completely answered.

5. If the answer is complete, stop calling tools and respond to the user.

6. Continue calling tools only if required information is still missing.

7. Never perform exploratory or unnecessary tool calls.
"""