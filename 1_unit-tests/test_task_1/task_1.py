# Задание № 1

"""Рекордсмены: находим самый продолжительный и самый короткий курс по программированию"""

courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
mentors = [
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко"],
	["Евгений Шмаргунов"],
	["Владимир Чебукин"]
]
durations = [14, 20, 12, 20]

def generate_courses(courses, mentors, durations):
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)

    min_duration = min(durations)
    max_duration = max(durations)

    minis = [index for index, duration in enumerate(durations) if duration == min_duration]
    maxes = [index for index, duration in enumerate(durations) if duration == max_duration]

    courses_min = [courses_list[id]["title"] for id in minis]
    courses_max = [courses_list[id]["title"] for id in maxes]

    return courses_min, min_duration, courses_max, max_duration

courses_min, min_duration, courses_max, max_duration = generate_courses(courses, mentors, durations)
print(f'Самый короткий курс(ы): {", ".join(courses_min)} - {min_duration} месяца(ев)')
print(f'Самый длинный курс(ы): {", ".join(courses_max)} - {max_duration} месяца(ев)')