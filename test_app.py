def add_question(questions):
    """Добавляет новый вопрос в список вопросов."""
    question = input("Введите вопрос: ")
    answers = input("Введите варианты ответа (через запятую): ").split(",")
    correct_answer = int(input("Введите номер правильного ответа: ")) - 1

    if len(answers) >= correct_answer:
        questions.append({
            "question": question,
            "answers": answers,
            "correct_answer": correct_answer
        })
        print("Вопрос добавлен.")
    else:
        print("Ошибка: Неверный номер правильного ответа.")

def edit_question(questions):
    """Редактирует существующий вопрос."""
    print("Текущие вопросы:")
    for i, question_data in enumerate(questions):
        print(f"{i+1}. {question_data['question']}")
    
    question_number = int(input("Введите номер вопроса для редактирования: ")) - 1

    if 0 <= question_number < len(questions):
        question_data = questions[question_number]
        question_data["question"] = input(f"Введите новый вопрос (текущий: {question_data['question']}): ")
        question_data["answers"] = input(f"Введите новые варианты ответа (через запятую, текущие: {', '.join(question_data['answers'])}): ").split(",")
        while True:
            try:
                correct_answer = int(input(f"Введите новый номер правильного ответа (текущий: {question_data['correct_answer'] + 1}): ")) - 1
                if 0 <= correct_answer < len(question_data["answers"]):
                    question_data["correct_answer"] = correct_answer
                    break
                else:
                    print("Ошибка: Неверный номер правильного ответа.")
            except ValueError:
                print("Ошибка: Введите число.")
        print("Вопрос отредактирован.")
    else:
        print("Ошибка: Неверный номер вопроса.")

def delete_question(questions):
    """Удаляет вопрос из списка."""
    print("Текущие вопросы:")
    for i, question_data in enumerate(questions):
        print(f"{i+1}. {question_data['question']}")

    question_number = int(input("Введите номер вопроса для удаления: ")) - 1

    if 0 <= question_number < len(questions):
        del questions[question_number]
        print("Вопрос удален.")
    else:
        print("Ошибка: Неверный номер вопроса.")

def save_test(questions):
    """Сохраняет тест в текстовый файл."""
    filename = input("Введите имя файла для сохранения теста: ")
    with open(filename, "w", encoding='utf-8') as f:
        for i, question_data in enumerate(questions):
            f.write(f"{i+1}. {question_data['question']}\n")
            for j, answer in enumerate(question_data["answers"]):
                f.write(f"\t{j+1}. {answer}\n")
            f.write(f"\tПравильный ответ: {question_data['correct_answer'] + 1}\n")
    print(f"Тест сохранен в файл {filename}.")

def load_test(questions):
    """Загружает тест из текстового файла."""
    filename = input("Введите имя файла для загрузки теста: ")
    try:
        with open(filename, "r", encoding='utf-8') as f:
            questions.clear()
            current_question = {}
            for line in f:
                line = line.strip()
                if line.startswith("."):
                    if current_question:
                        questions.append(current_question)
                    current_question = {}
                    current_question["question"] = line[2:].strip()
                elif line.startswith("\t"):
                    if line.startswith("\tПравильный"):
                        current_question["correct_answer"] = int(line.split()[-1]) - 1
                    else:
                        current_question["answers"].append(line[1:].strip())
                else:
                    current_question = {"question": line, "answers": [], "correct_answer": 0}

            if current_question:
                questions.append(current_question)
            print(f"Тест загружен из файла {filename}.")
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")

def main():
    """Основная функция программы."""
    questions = []
    while True:
        print("\nВыберите действие:")
        print("1. Добавить вопрос")
        print("2. Редактировать вопрос")
        print("3. Удалить вопрос")
        print("4. Сохранить тест")
        print("5. Загрузить тест")
        print("6. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            add_question(questions)
        elif choice == "2":
            edit_question(questions)
        elif choice == "3":
            delete_question(questions)
        elif choice == "4":
            save_test(questions)
        elif choice == "5":
           load_test(questions)
        elif choice == "6":
            break
        else:
            print("Ошибка: Неверный выбор.")

if __name__ == "__main__":
    main()