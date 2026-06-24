from database.db_connect import get_connection


def add_attendance(intern_id, date, status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO attendance(intern_id,date,status)
        VALUES(?,?,?)
    """, (intern_id, date, status))

    conn.commit()
    conn.close()


def get_attendance():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            attendance.id,
            attendance.intern_id,
            interns.name AS intern_name,
            attendance.date,
            attendance.status
        FROM attendance
        LEFT JOIN interns ON attendance.intern_id = interns.id
        ORDER BY attendance.date DESC, attendance.id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def count_attendance():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) AS total FROM attendance")

    total = cursor.fetchone()["total"]

    conn.close()

    return total
