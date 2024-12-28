from django.db import connection
from contextlib import closing


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_faculties():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from adminapp_faculty""")
        faculties = dictfetchall(cursor)
        return faculties


def get_kafedra():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from adminapp_kafedra""")
        kafedra = dictfetchall(cursor)
        return kafedra

def get_subject():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from adminapp_subject""")
        subject = dictfetchall(cursor)
        return subject


def get_teacher():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT 
                            adminapp_teacher.*, 
                            adminapp_kafedra.id AS kafedra_id, 
                            adminapp_subject.id AS subject_id
                          FROM 
                            adminapp_teacher 
                          LEFT JOIN 
                            adminapp_kafedra ON adminapp_teacher.kafedra_id = adminapp_kafedra.id 
                          LEFT JOIN 
                            adminapp_subject ON adminapp_teacher.subject_id = adminapp_subject.id
                        """)
        teacher = dictfetchall(cursor)
        return teacher

def get_group():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT 
                            adminapp_group.*, 
                            adminapp_faculty.name AS faculty_name
                        FROM 
                            adminapp_group 
                        LEFT JOIN 
                            adminapp_faculty ON adminapp_group.faculty_id = adminapp_faculty.id 
                        """)
        group = dictfetchall(cursor)
        return group

def get_student():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT 
                            adminapp_student.id, 
                            adminapp_student.first_name, 
                            adminapp_student.last_name, 
                            adminapp_student.age, 
                            adminapp_group.id AS group_id 
                        FROM 
                            adminapp_student 
                        LEFT JOIN 
                            adminapp_group ON adminapp_student.group_id = adminapp_group.id 
                         """)
        student = dictfetchall(cursor)
        return student
