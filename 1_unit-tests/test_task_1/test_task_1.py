import pytest
from task_1 import generate_courses

@pytest.mark.parametrize("courses,mentors,durations,expected", [
    (["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"],
     [["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
      ["Евгений Шмаргунов"],
      ["Евгений Шмаргунов"],
      ["Владимир Чебукин"]],
     [14, 20, 12, 20],
     (["Python-разработчик с нуля"], 12, ["Fullstack-разработчик на Python","Frontend-разработчик с нуля"], 20))
])
def test_generate_courses(courses, mentors, durations, expected):
    assert generate_courses(courses, mentors, durations) == expected
