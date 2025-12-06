import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models_student import Base, Student  # Импортируйте свои модели и Base

DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/mydatabase"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

@pytest.fixture(scope='function')
def session():
    """Fixture для создания сессии и очистки данных после теста"""
    Base.metadata.create_all(engine)
    session = Session()
    yield session
    session.rollback()  # Откатить все изменения после теста
    session.close()

def test_add_student(session):
    student = Student(name="Иван Иванов")
    session.add(student)
    session.commit()

    assert student.id is not None
    # Проверяем, что студент появился в базе
    saved_student = session.query(Student).filter_by(name="Иван Иванов").first()
    assert saved_student is not None

def test_update_student(session):
    student = Student(name="Пётр Петров")
    session.add(student)
    session.commit()

    student.name = "Пётр Петровский"
    session.commit()

    updated_student = session.query(Student).filter_by(id=student.id).first()
    assert updated_student.name == "Пётр Петровский"

def test_delete_student(session):
    student = Student(name="Светлана Светлова")
    session.add(student)
    session.commit()
    student_id = student.id

    session.delete(student)
    session.commit()

    deleted_student = session.query(Student).filter_by(id=student_id).first()
    assert deleted_student is None