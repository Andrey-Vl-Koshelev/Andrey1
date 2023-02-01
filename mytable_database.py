from faker import Faker

from mytables.my_database import create_db, Session
from mytables.name import Name
from mytables.number import Number
from mytables.lesson import Lesson


def mytable_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    lessons_names = ['Тактика', 'История', 'Стрельба', 'Эксплуатация вооружения',
                     'Высшая математика', 'Сопротивление материалов']

    group1 = Number(group_name='WELL-221')
    group2 = Number(group_name='WELL-222')
    session.add(group1)
    session.add(group2)

    for key, it in enumerate(lessons_names):
        lesson = Lesson(lesson_title=it)
        lesson.groups.append(group1)
        if key % 2 == 0:
            lesson.groups.append(group2)
        session.add(lesson)

    faker = Faker('ru_RU')
    group_list = [group1, group2]
    session.commit()

    for _ in range(40):
        full_name = faker.name().split()
        age = faker.random.randint(17, 27)
        group = faker.random.choice(group_list)
        cadet = Name(full_name, age, group.id)
        session.add(cadet)

    session.commit()
    session.close()
