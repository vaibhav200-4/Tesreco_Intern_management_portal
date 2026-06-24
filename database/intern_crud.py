from database.db_connect import get_connection


def insert_intern(name, email, domain, duration):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO interns(name,email,domain,duration)
        VALUES(?,?,?,?)
        """,
        (name, email, domain, duration)
    )

    conn.commit()
    conn.close()


def get_all_interns():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM interns ORDER BY id DESC")

    interns = cursor.fetchall()

    conn.close()

    return interns


def get_intern_by_id(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM interns WHERE id=?", (id,))

    intern = cursor.fetchone()

    conn.close()

    return intern


def update_intern(id, name, email, domain, duration):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE interns
        SET name=?, email=?, domain=?, duration=?
        WHERE id=?
        """,
        (name, email, domain, duration, id)
    )

    conn.commit()
    conn.close()


def delete_intern(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM interns WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()


def count_interns():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) AS total FROM interns")

    total = cursor.fetchone()["total"]

    conn.close()

    return total
