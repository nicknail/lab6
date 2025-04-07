def sort_students(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and (
            (data[j][1] > key[1])
            or (data[j][1] == key[1] and data[j][2] < key[2])
            or (data[j][1] == key[1] and data[j][2] == key[2] and data[j][0] > key[0])
        ):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


def search_students(data, subject, grade):
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid][1] == subject and data[mid][2] == grade:
            return data[mid]
        elif data[mid][1] < subject or (
            data[mid][1] == subject and data[mid][2] < grade
        ):
            low = mid + 1
        else:
            high = mid - 1
    return None


def calculate_average_grade(data):
    average_grades = {}
    for student in data:
        subject = student[1]
        grade = student[2]
        if subject not in average_grades:
            average_grades[subject] = [grade]
        else:
            average_grades[subject].append(grade)
    for subject, grades in average_grades.items():
        total = 0
        count = 0
        for grade in grades:
            total += grade
            count += 1
        average_grades[subject] = total / count
    return average_grades


def top_students(data):
    average_grades = {}
    for student in data:
        surname = student[0]
        subject = student[1]
        grade = student[2]
        if surname not in average_grades:
            average_grades[surname] = {}
        if subject not in average_grades[surname]:
            average_grades[surname][subject] = []
        average_grades[surname][subject].append(grade)

    for surname, subjects in average_grades.items():
        for subject, grades in subjects.items():
            total = 0
            count = 0
            for grade in grades:
                total += grade
                count += 1
            average_grades[surname][subject] = total / count

    rating = []
    for surname, subjects in average_grades.items():
        total = 0
        count = 0
        for subject, grade in subjects.items():
            total += grade
            count += 1
        average_grade = total / count
        rating.append((surname, average_grade))

    for i in range(len(rating)):
        for j in range(i + 1, len(rating)):
            if rating[i][1] < rating[j][1]:
                rating[i], rating[j] = rating[j], rating[i]

    return "\n".join(
        "%s. %s: %.2f" % (i + 1, rating[i][0], rating[i][1]) for i in range(3)
    )


def main():
    data = [
        ("Иванов", "Математика", 85),
        ("Петров", "Физика", 92),
        ("Сидоров", "Математика", 78),
        ("Иванов", "Физика", 90),
        ("Петров", "Математика", 88),
        ("Сидоров", "Информатика", 95),
        ("Иванов", "Информатика", 82),
        ("Петров", "Информатика", 97),
        ("Сидоров", "Физика", 85),
    ]
    _filter = "Математика", 85

    print("Входные данные: [")
    for item in data:
        print("\t" + str(item))
    print("]")
    print(str(_filter))

    print("\nРезультат:")
    sorted_data = sort_students(data)

    print("Отсортированные данные: [")
    for item in sorted_data:
        print("\t" + str(item))
    print("]")

    print("\nСтуденты с оценкой %s по предмету %s:" % _filter[::-1])
    print(search_students(sorted_data, *_filter))

    print("\nСредние оценки по предметам:")

    average_grades = calculate_average_grade(sorted_data)
    for item in average_grades.items():
        print("%s: %.2f" % item)

    print("\nЛучшие студенты:")
    print(top_students(sorted_data))


if __name__ == "__main__":
    main()
