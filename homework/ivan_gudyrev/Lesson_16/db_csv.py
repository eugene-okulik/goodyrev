import mysql.connector as mysql
import csv
import os
import dotenv


dotenv.load_dotenv(override=True)

db = mysql.connect(
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
)
cursor = db.cursor(dictionary=True)

query_all = """
SELECT s.name, s.second_name, g.title as 'group', b.title as 'books', s2.title as 'subjects',
l.title as 'lessons', m.value as 'values'
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON b.taken_by_student_id = s.id
JOIN marks m  ON m.student_id = s.id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjets s2 ON s2.id = l.subject_id
WHERE s.name = %s AND s.second_name = %s AND g.title = %s AND b.title = %s AND s2.title = %s
AND l.title = %s AND  m.value = %s
"""

absent = []

with open(r"homework\eugene_okulik\Lesson_16\hw_data\data.csv", encoding="utf-8") as csv_file:
    file_data = csv.DictReader(csv_file, delimiter=",")
    for row in file_data:
        data = [v for v in row.values()]
        cursor.execute(query_all, tuple(data))
        if not cursor.fetchall():
            absent.append(row)

print("В базе не хватает данных:", *absent, sep="\n" if absent else 'Все данные в базе')
db.close()
