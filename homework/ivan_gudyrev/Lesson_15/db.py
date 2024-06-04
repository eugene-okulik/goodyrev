import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)
cursor = db.cursor(dictionary=True)


insert_query_students = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
NAME = 'Vincent'
SECOND_NAME = 'van Gogh'
cursor.execute(insert_query_students, (NAME, SECOND_NAME))
student_id = cursor.lastrowid


insert_query_books = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
BOOK1 = 'Учусь рисовать'
BOOK2 = 'Как рисовать подсолнухи?'
BOOK3 = 'Я люблю подсолнухи'
cursor.executemany(
    insert_query_books, [
        (BOOK1, student_id),
        (BOOK2, student_id),
        (BOOK3, student_id),
    ]
)


insert_query_groups = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
GROUP_NAME = 'Искусство для дошколят'
START_DATE = 'may 1995'
END_DATE = 'apr 2000'
cursor.execute(insert_query_groups, (GROUP_NAME, START_DATE, END_DATE))
group_id = cursor.lastrowid


update_query_students = f"UPDATE students SET group_id = {group_id} WHERE id = {student_id}"
cursor.execute(update_query_students)


insert_query_subjets = "INSERT INTO subjets (title) VALUES (%s)"
SUB1 = 'IZO'
SUB2 = 'Sculpture'
cursor.execute(insert_query_subjets, (SUB1,))
izo_id = cursor.lastrowid
cursor.execute(insert_query_subjets, (SUB2,))
sculpture_id = cursor.lastrowid


insert_query_lessons = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
LESSON1 = 'Landscape'
LESSON2 = 'Portreit'
LESSON3 = 'Clay'
LESSON4 = 'Gypsum'
cursor.execute(insert_query_lessons, (LESSON1, izo_id))
landscape_id = cursor.lastrowid
cursor.execute(insert_query_lessons, (LESSON2, izo_id))
portreit_id = cursor.lastrowid
cursor.execute(insert_query_lessons, (LESSON3, sculpture_id))
clay_id = cursor.lastrowid
cursor.execute(insert_query_lessons, (LESSON4, sculpture_id))
gypsum_id = cursor.lastrowid


insert_query_marks = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    insert_query_marks, [
        ('5', landscape_id, student_id),
        ('4', portreit_id, student_id),
        ('3', clay_id, student_id),
        ('2', gypsum_id, student_id)
    ]
)


query_marks = "SELECT value FROM marks WHERE student_id = %s"
cursor.execute(query_marks, (student_id,))
print(cursor.fetchall())


query_books = "SELECT title FROM books WHERE taken_by_student_id = %s"
cursor.execute(query_books, (student_id,))
print(cursor.fetchall())


query_all = '''
SELECT s.name, s.second_name, g.title as 'group', b.title as 'books', s2.title as 'subjects',
l.title as 'lessons', m.value as 'values'
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON b.taken_by_student_id = s.id
JOIN marks m  ON m.student_id = s.id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjets s2 ON s2.id = l.subject_id
WHERE s.id = %s
'''
cursor.execute(query_all, (student_id,))
print(cursor.fetchall())


db.commit()
db.close()
