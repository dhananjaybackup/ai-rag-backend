import sqlite3

from sympy import content

class MemoryService:
    def get_history(self, session_id):
        # Connect to the SQLite database
        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()
        # Retrieve the chat history for the given session_id
        cursor.execute("""
        SELECT Role, Content
        FROM (
            SELECT Role, Content
            FROM Conversation
            WHERE SessionId = ?
            ORDER BY Id DESC
            LIMIT 10
        )
       
    """, (session_id,))
        rows = cursor.fetchall()

        # Close the database connection
        conn.close()
        messages = []
        for row in rows:
            messages.append(
                {
                    "role": row[0],
                    "content": row[1]
                }
            )

        return messages
    
    def save_message( self,session_id,role,content):
        conn = sqlite3.connect("employee.db")
        cursor = conn.cursor()

        cursor.execute(""" INSERT INTO Conversation( SessionId, Role,Content) VALUES ( ?,?,?) """,
                       ( session_id, role, content) )

        conn.commit()
        conn.close()
