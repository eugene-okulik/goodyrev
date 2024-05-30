INSERT INTO students (name, second_name)
VALUES ('Guido', 'van Rossum')

SET @guido_id := (SELECT id FROM students WHERE name = 'Guido' AND second_name = 'van Rossum' ORDER BY id DESC LIMIT 1)


INSERT INTO books (title, taken_by_student_id)
VALUES ('Grokking Algorithms', @guido_id),
	   ('Learning Python', @guido_id),
	   ('38 попугаев', @guido_id)


INSERT INTO `groups` (title, start_date, end_date)
VALUES ('BIM', 'may 2024', 'jul 2024')

SET @guido_group_id := (SELECT id FROM `groups` WHERE title = 'BIM' AND start_date = 'may 2024' AND end_date = 'jul 2024' ORDER BY id DESC LIMIT 1)


UPDATE students 
SET group_id = @guido_group_id
WHERE id = @guido_id


INSERT INTO subjets (title)
VALUES ('Python'),
       ('Paint')
       
SET @python_subject_id := (SELECT id FROM subjets s  WHERE title = 'Python' ORDER BY id DESC LIMIT 1)
SET @paint_subject_id := (SELECT id FROM subjets s  WHERE title = 'Paint' ORDER BY id DESC LIMIT 1)


INSERT INTO lessons (title, subject_id)
VALUES ('OOP in Python', @python_subject_id),
       ('Playwright in Python', @python_subject_id),
       ('Impressionism', @paint_subject_id),
       ('Рисуем солнышко', @paint_subject_id)
           
SET @oop_in_python_lesson_id := (SELECT id FROM lessons l WHERE title = 'OOP in Python' AND subject_id = @python_subject_id ORDER BY id DESC LIMIT 1)
SET @playwright_in_python_lesson_id := (SELECT id FROM lessons l WHERE title = 'Playwright in Python' AND subject_id = @python_subject_id ORDER BY id DESC LIMIT 1)
SET @impressionizm_lesson_id := (SELECT id FROM lessons l WHERE title = 'Impressionism' AND subject_id = @paint_subject_id ORDER BY id DESC LIMIT 1)
SET @paint_sun_lesson_id := (SELECT id FROM lessons l WHERE title = 'Рисуем солнышко' AND subject_id = @paint_subject_id ORDER BY id DESC LIMIT 1)
       
             
INSERT INTO marks (value, lesson_id, student_id)
VALUES ('3', @oop_in_python_lesson_id, @guido_id),
       ('4', @playwright_in_python_lesson_id, @guido_id),
       ('2', @impressionizm_lesson_id, @guido_id),
       ('5', @paint_sun_lesson_id, @guido_id)
	   
	   
SELECT value
FROM marks m 
WHERE student_id = @guido_id


SELECT title
FROM books
WHERE taken_by_student_id = @guido_id


SELECT s.name, s.second_name, g.title as 'group', b.title as 'books', s2.title as 'subjects', l.title as 'lessons', m.value as 'values'
FROM students s 
JOIN `groups` g ON s.group_id = g.id 
JOIN books b ON b.taken_by_student_id = s.id
JOIN marks m  ON m.student_id = s.id
JOIN lessons l ON l.id = m.lesson_id 
JOIN subjets s2 ON s2.id = l.subject_id 
WHERE s.id = @guido_id
