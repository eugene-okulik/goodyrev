INSERT INTO students (name, second_name)
VALUES ('Guido', 'van Rossum')


INSERT INTO books (title, taken_by_student_id)
VALUES ('Grokking Algorithms', (select id FROM students WHERE name = 'Guido' AND second_name = 'van Rossum')),
	   ('Learning Python', (select id FROM students WHERE name = 'Guido' AND second_name = 'van Rossum')),
	   ('38 попугаев', (select id FROM students WHERE name = 'Guido' AND second_name = 'van Rossum'))


INSERT INTO `groups` (title, start_date, end_date)
VALUES ('BIM', 'may 2024', 'jul 2024')


UPDATE students 
SET group_id = (SELECT id FROM `groups` WHERE title = 'BIM')
WHERE name = 'Guido' AND second_name = 'van Rossum'


INSERT INTO subjets (title)
VALUES ('Python'),
       ('Paint')


INSERT INTO lessons (title, subject_id)
VALUES ('OOP in Python', (select id FROM subjets  WHERE title = 'Python')),
       ('Playwright in Python', (select id FROM subjets  WHERE title = 'Python')),
       ('Impressionism', (select id FROM subjets  WHERE title = 'Paint')),
       ('Рисуем солнышко', (select id FROM subjets  WHERE title = 'Paint'))


INSERT INTO marks (value, lesson_id, student_id)
VALUES ('3', (select id FROM lessons WHERE title = 'OOP in Python'), (select id FROM students WHERE name = 'Guido' AND second_name = 'van Rossum')),
       ('4', (select id FROM lessons WHERE title = 'Playwright in Python'), (select id FROM students WHERE name = 'Guido' AND second_name = 'van Rossum')),
       ('2', (select id FROM lessons WHERE title = 'Impressionism'), (select id FROM students WHERE name = 'Guido' AND second_name = 'van Rossum')),
       ('5', (select id FROM lessons WHERE title = 'Рисуем солнышко'), (select id FROM students WHERE name = 'Guido' AND second_name = 'van Rossum'))
	   
	   
SELECT value
FROM marks m 
WHERE student_id = (select id FROM students WHERE name = 'Guido' AND second_name = 'van Rossum')


SELECT title
FROM books
WHERE taken_by_student_id = (select id FROM students WHERE name = 'Guido' AND second_name = 'van Rossum')


SELECT s.name, s.second_name, g.title as 'group', b.title as 'books', s2.title as 'subjects', l.title as 'lessons', m.value as 'values'
FROM students s 
JOIN `groups` g ON s.group_id = g.id 
JOIN books b ON b.taken_by_student_id = s.id
JOIN marks m  ON m.student_id = s.id
JOIN lessons l ON l.id = m.lesson_id 
JOIN subjets s2 ON s2.id = l.subject_id 
WHERE s.name = 'Guido' AND s.second_name = 'van Rossum'
