groupmates = [
    {
        "name": "Екатерина",
        "sername": "Газетова",
        "exams": ["Информатика","Математика","История"],
        "marks": [3,3,3]
    },
    {
        "name": "Анна",
        "sername": "Иванова",
        "exams": ["Философия","Информатика","Математика"],
        "marks": [4,3,4]
    },
    {
        "name": "Виктория",
        "sername": "Маркелова",
        "exams": ["АиГ","История","Философия"],
        "marks": [5,5,5]
    },
    {
        "name": "Яна",
        "sername": "Смирнова",
        "exams": ["Математика","Философия","Информатика"],
        "marks": [5,4,5]
    },
    {
        "name": "Ольга",
        "sername": "Позднякова",
        "exams": ["Информатика","История","АиГ"],
        "marks": [3,4,3]
    }
]

def print_students(students):
    print (u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print (student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))
        print_students(groupmates)
