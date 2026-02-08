from db import get_connection

def count_by_status():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT status, COUNT(*)
        FROM api_results
        GROUP BY status
    """)

    results = cursor.fetchall()
    conn.close()
    return results
