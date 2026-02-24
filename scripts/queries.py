from db import get_connection

def count_by_status():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT user_id 
        FROM api_results 
        WHERE status = 'invalid_data';
    """)

    results = cursor.fetchall()
    conn.close()
    return results
