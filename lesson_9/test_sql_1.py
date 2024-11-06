from sqlalchemy import create_engine 
from sqlalchemy.sql import text

db_connection_string = "postgresql://postgres:835@localhost:5432/postgres?client_encoding=utf8"
db = create_engine(db_connection_string)


def test_insert():
    db = create_engine(db_connection_string)
    sql = text("insert into subject(subject_id, subject_title) values (17, 'Art')")
    rows = db.execute(sql, new_title = 'Art')
    sql = text("select subject_title from subject where subject_id=17")
    result = db.execute(sql)
    assert result.rowcount == 1


def test_update():
    db = create_engine(db_connection_string)
    sql = text("update subject set subject_title = 'Astronomy' where subject_id = 17")
    rows = db.execute(sql)
    sql = text("select subject_title from subject where subject_id=17")
    result = db.execute(sql)
    assert result.fetchone()[0] == 'Astronomy'
    


def test_delete():
    db = create_engine(db_connection_string)
    sql = text("delete from subject where subject_id = :id")
    rows = db.execute(sql, id = 17)
    sql = text("select subject_title from subject where subject_id=17")
    result = db.execute(sql)
    assert result.rowcount == 0