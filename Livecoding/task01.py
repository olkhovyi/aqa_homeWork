# some_dict = [
#     {"name": "Azimova", "salary": 20000, "gender": "f"},
#     {"name": "Borenko", "salary": 9000, "gender": "m"},
#     {"name": "Vasilenko", "salary": 10000, "gender": "m"},
#     {"name": "Zabolotna", "salary": 25000, "gender": "f"},
#     {"name": "Koval", "salary": 35000, "gender": "m"}
# ]


import pytest


def get_salaries_information(some_dict):

    max_salary_name = some_dict[0]["name"]
    max_salary = some_dict[0]["salary"]

    for i in some_dict:
        if i["salary"] > max_salary:
            max_salary = i["salary"]
            max_salary_name = i["name"]
        elif i["salary"] == max_salary:
            if i["name"] < max_salary_name:
                max_salary_name = i["name"]

    male_salary_min = None
    for i in some_dict:
        if i["gender"] == "m":
            if male_salary_min is None or i["salary"] < male_salary_min:
                male_salary_min = i["salary"]

    female_salary_max = None
    for i in some_dict:
        if i["gender"] == "f":
            if female_salary_max is None or i["salary"] > female_salary_max:
                female_salary_max = i["salary"]

    return max_salary_name, male_salary_min, female_salary_max

# print(get_salaries_information(some_dict))


def test_salaries_information():
    some_dict = [
        {"name": "Azimova", "salary": 20000, "gender": "f"},
        {"name": "Borenko", "salary": 9000, "gender": "m"},
        {"name": "Vasilenko", "salary": 10000, "gender": "m"},
        {"name": "Zabolotna", "salary": 25000, "gender": "f"},
        {"name": "Koval", "salary": 35000, "gender": "m"}
    ]
    assert get_salaries_information(some_dict) == ("Koval", 9000, 25000)


def test_salaries_information1():
    some_dict = [
        {"name": "Azimova", "salary": 20000, "gender": "f"},
        {"name": "Borenko", "salary": 9000, "gender": "m"},
        {"name": "Vasilenko", "salary": 10000, "gender": "m"},
        {"name": "Zabolotna", "salary": None, "gender": "f"},
        {"name": "Koval", "salary": 35000, "gender": "m"}
    ]
    with pytest.raises(TypeError) as exc_info:
        get_salaries_information(some_dict)
    data = str(exc_info.value)
    assert data == "'>' not supported between instances of 'NoneType' and 'int'"
