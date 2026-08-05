EXAMPLES_PROMPT = """
Examples

Example 1

User:
Who am I?

Assistant:
Retrieve the employee profile using the appropriate employee tool.
Answer using the retrieved information.

----------------------------------------

Example 2

User:
Who is my manager?

Assistant:
Retrieve the employee profile.
Use the returned manager ID.
Retrieve the manager's details.
Answer using the combined information.

----------------------------------------

Example 3

User:
What is my leave balance?

Assistant:
Retrieve the leave balance.
Answer using the returned leave information.

----------------------------------------

Example 4

User:
Explain maternity leave.

Assistant:
Search the leave policy.
Summarize the retrieved policy.

----------------------------------------

Example 5

User:
Hello

Assistant:
Respond normally.
No tool is required.

----------------------------------------

Example 6

User:
Show another employee's salary.

Assistant:
Politely refuse because the request is not authorized.
"""