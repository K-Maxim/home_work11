from flask import Flask, render_template

# template_rendered подключает HTML-шаблоны
import utils

app = Flask(__name__)


@app.route('/')
def list_html():
    """
    выводит главную страницу
    :return: выводит html документ (names - список имен кандидатов, quantity - количество кандидатов)
    """
    candidate_list = utils.load_candidates_from_json()
    quantity = len(candidate_list)
    return render_template("list.html", names=candidate_list, quantity=quantity)


@app.route('/candidate/<int:candidate_id>')
def candidate(candidate_id):
    """
    выводит страницу кандидата в зависимости от id
    :param candidate_id: в качестве аргумента выступает число
    :return: выводит html документ (data - данные кандидата в виде списка)
    """
    data = utils.get_candidate(candidate_id)
    return render_template('single.html', data=data)


@app.route('/search/<candidate_name>')
def name(candidate_name):
    """
    выводит страницу кандидата в зависимости от имени кандидата
    :param candidate_name: в качестве аргумента выступает строка (Имя кандидата)
    :return: выводит html документ (names - список кандидатов, quantity - количество кандидатов,
    candidate_list - полный список кандидатов)
    """
    person_name = utils.get_candidates_by_name(candidate_name)
    candidate_list = utils.load_candidates_from_json()
    quantity = len(person_name)
    return render_template('search.html', names=person_name, quantity=quantity, candidate_list=candidate_list)


@app.route('/skills/<skills>')
def skills(skills):
    """
    страницу кандидата в зависимости навыков кандида
    :param skills: в качестве аргумента выступает строка (навык кандидата)
    :return: выводит html документ (quantity - количество кандидатов, person_skills - индивидульные навыки
    full_person_skills - список навыков кандидатов (индивидульные навыки вложены в это список в виде списка)
    candidate_list - полный список кандидатов)
    """
    person_skills, full_person_skills = utils.get_candidates_by_skill(skills)
    quantity = len(person_skills)
    candidate_list = utils.load_candidates_from_json()
    return render_template('skills.html', quantity=quantity, person_skills=person_skills,
                           full_person_skills=full_person_skills, candidate_list=candidate_list)


app.run()
