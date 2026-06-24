from database.mentor_crud import (
    insert_mentor,
    get_all_mentors,
    assign_mentor,
    get_assignments
)

insert_mentor(
    "Rahul Sharma",
    "Machine Learning"
)

mentors = get_all_mentors()

for mentor in mentors:
    print(dict(mentor))


assign_mentor(
    intern_id=1,
    mentor_id=1
)

assignments = get_assignments()

for assignment in assignments:
    print(dict(assignment))