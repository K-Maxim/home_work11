import json

with open('candidates.json', 'r', encoding='utf-8') as file:
    candidates_list = json.load(file)


def load_candidates_from_json():
    """
    функция вытаскивает имена всех кандидатов и помещает их в список
    :return: возвращает список всех кандидатов
    """
    candidates = []
    for i in range(len(candidates_list)):
        candidates.append(candidates_list[i]["name"])
    return candidates


def get_candidate(candidate_id):
    """
    функция, в зависимости от числа, сравнивает его с id кандидата и помещает все его данные в список
    :param candidate_id: в качестве аргумента выступает число
    :return: возвращает одного кандидата по его id
    """
    person_profile = []

    for i in range(len(candidates_list)):
        if candidate_id == candidates_list[i]["id"]:
            person_profile.append(candidates_list[i]["name"])
            person_profile.append(candidates_list[i]["position"])
            person_profile.append(candidates_list[i]["picture"])
            person_profile.append(candidates_list[i]["skills"])

    return person_profile


def get_candidates_by_name(candidate_name):
    """
    функция переберает все имена и нужные помещает в список
    :param candidate_name: в качестве аргумента выступает строка (Имя кандидата)
    :return: возвращает кандидатов по имени
    """
    person_name = []
    for i in range(len(candidates_list)):
        if candidate_name in candidates_list[i]["name"]:
            person_name.append(candidates_list[i]["name"])

    return person_name


def get_candidates_by_skill(skill_name):
    """
    функция переберает все навыки кандидатов
    :param skill_name: в качестве аргумента выступает строка (Навыки кандидата)
    :return: возвращает кандидатов по навыку и полный список всех навыков (я жто сделал,
    чтобы можно было по индексу указать ссылку)
    """
    person_skills = []
    full_person_skills = []
    for i in range(len(candidates_list)):
        candidate_skills = candidates_list[i]["skills"].lower().split(', ')
        full_person_skills.append(candidate_skills)
        if skill_name in candidate_skills:
            person_skills.append(candidate_skills)

    return person_skills, full_person_skills



