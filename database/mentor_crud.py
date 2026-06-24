from database.db_connect import get_connection


# Create Mentor
def insert_mentor(name, specialization):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO mentors(name, specialization)
        VALUES (?, ?)
        """,
        (name, specialization)
    )

    conn.commit()
    conn.close()


# Get All Mentors
def get_all_mentors():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM mentors ORDER BY mentor_id DESC
        """
    )

    mentors = cursor.fetchall()

    conn.close()

    return mentors


# Assign Mentor to Intern
def assign_mentor(intern_id, mentor_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO assignment(intern_id, mentor_id)
        VALUES (?, ?)
        """,
        (intern_id, mentor_id)
    )

    conn.commit()
    conn.close()


# View Assignments
def get_assignments():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            a.id,
            i.name AS intern_name,
            m.name AS mentor_name,
            m.specialization
        FROM assignment a
        JOIN interns i ON a.intern_id = i.id
        JOIN mentors m ON a.mentor_id = m.mentor_id
        ORDER BY a.id DESC
        """
    )

    assignments = cursor.fetchall()

    conn.close()

    return assignments


def count_mentors():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) AS total FROM mentors")

    total = cursor.fetchone()["total"]

    conn.close()

    return total


def count_assignments():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) AS total FROM assignment")

    total = cursor.fetchone()["total"]

    conn.close()

    return total
