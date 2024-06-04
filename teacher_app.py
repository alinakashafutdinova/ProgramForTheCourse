import tkinter as tk
from tkinter import messagebox, simpledialog
import json
#tkinter: Стандартная библиотека Python для создания графических пользовательских интерфейсов.
#messagebox: Предоставляет функции для отображения всплывающих окон с сообщениями.
#simpledialog: Предоставляет функции для отображения диалоговых окон с вводом.
#json: Библиотека для работы с данными в формате JSON.

class TeacherApp:
    def __init__(self, master):
        self.master = master
        master.title("Генератор тестов для Учителя")

        self.questions = []

        # Фрейм для создания вопросов
        self.create_question_frame = tk.LabelFrame(master, text="Создать вопрос")
        self.create_question_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.question_label = tk.Label(self.create_question_frame, text="Вопрос:")
        self.question_label.grid(row=0, column=0, padx=5, pady=5)
        self.question_entry = tk.Entry(self.create_question_frame, width=50)
        self.question_entry.grid(row=0, column=1, padx=5, pady=5)

        self.answer_label = tk.Label(self.create_question_frame, text="Варианты ответа (через запятую):")
        self.answer_label.grid(row=1, column=0, padx=5, pady=5)
        self.answer_entry = tk.Entry(self.create_question_frame, width=50)
        self.answer_entry.grid(row=1, column=1, padx=5, pady=5)

        self.correct_answer_label = tk.Label(self.create_question_frame, text="Номер правильного ответа:")
        self.correct_answer_label.grid(row=2, column=0, padx=5, pady=5)
        self.correct_answer_entry = tk.Entry(self.create_question_frame, width=10)
        self.correct_answer_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_question_button = tk.Button(self.create_question_frame, text="Добавить вопрос", command=self.add_question)
        self.add_question_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        # Фрейм для просмотра и редактирования вопросов
        self.questions_frame = tk.LabelFrame(master, text="Вопросы")
        self.questions_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.questions_listbox = tk.Listbox(self.questions_frame, width=50)
        self.questions_listbox.grid(row=0, column=0, padx=5, pady=5)

        self.edit_question_button = tk.Button(self.questions_frame, text="Редактировать", command=self.edit_question)
        self.edit_question_button.grid(row=1, column=0, padx=5, pady=5)

        self.delete_question_button = tk.Button(self.questions_frame, text="Удалить", command=self.delete_question)
        self.delete_question_button.grid(row=2, column=0, padx=5, pady=5)

        # Фрейм для сохранения и загрузки тестов
        self.save_load_frame = tk.LabelFrame(master, text="Сохранить/Загрузить")
        self.save_load_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.save_button = tk.Button(self.save_load_frame, text="Сохранить тест", command=self.save_test)
        self.save_button.grid(row=0, column=0, padx=5, pady=5)

        self.load_button = tk.Button(self.save_load_frame, text="Загрузить тест", command=self.load_test)
        self.load_button.grid(row=1, column=0, padx=5, pady=5)

        # Фрейм для журнала оценок
        self.grades_frame = tk.LabelFrame(master, text="Журнал оценок")
        self.grades_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        self.view_grades_button = tk.Button(self.grades_frame, text="Просмотреть журнал", command=self.view_grades)
        self.view_grades_button.grid(row=0, column=0, padx=5, pady=5)

        self.grades_listbox = tk.Listbox(self.grades_frame, width=50)
        self.grades_listbox.grid(row=1, column=0, padx=5, pady=5)

    def add_question(self):
        question = self.question_entry.get()
        answers = self.answer_entry.get().split(",")
        correct_answer = int(self.correct_answer_entry.get())

        if question and answers and correct_answer:
            self.questions.append({
                "question": question,
                "answers": answers,
                "correct_answer": correct_answer - 1
            })
            self.update_questions_listbox()
            self.clear_entry_fields()

    def edit_question(self):
        selection = self.questions_listbox.curselection()
        if selection:
            index = selection[0]
            question_data = self.questions[index]

            self.question_entry.delete(0, tk.END)
            self.question_entry.insert(0, question_data["question"])
            self.answer_entry.delete(0, tk.END)
            self.answer_entry.insert(0, ",".join(question_data["answers"]))
            self.correct_answer_entry.delete(0, tk.END)
            self.correct_answer_entry.insert(0, question_data["correct_answer"] + 1)

            self.questions.pop(index)
            self.update_questions_listbox()

    def delete_question(self):
        selection = self.questions_listbox.curselection()
        if selection:
            index = selection[0]
            self.questions.pop(index)
            self.update_questions_listbox()

    def update_questions_listbox(self):
        self.questions_listbox.delete(0, tk.END)
        for i, question_data in enumerate(self.questions):
            self.questions_listbox.insert(tk.END, f"{i+1}. {question_data['question']}")

    def clear_entry_fields(self):
        self.question_entry.delete(0, tk.END)
        self.answer_entry.delete(0, tk.END)
        self.correct_answer_entry.delete(0, tk.END)

    def save_test(self):
        try:
            with open("test.json", "w", encoding='utf-8') as f:
                json.dump(self.questions, f, ensure_ascii=False, indent=4)
            messagebox.showinfo("Успешно!", "Тест сохранен в файл test.json")
        except Exception as e:
            messagebox.showerror("Ошибка!", f"Ошибка при сохранении теста: {e}")

    def load_test(self):
        try:
            with open("test.json", "r", encoding='utf-8') as f:
                self.questions = json.load(f)
            self.update_questions_listbox()
            messagebox.showinfo("Успешно!", "Тест загружен из файла test.json")
        except FileNotFoundError:
            messagebox.showerror("Ошибка!", "Файл test.json не найден!")
        except Exception as e:
            messagebox.showerror("Ошибка!", f"Ошибка при загрузке теста: {e}")

    def view_grades(self):
        self.grades_listbox.delete(0, tk.END)
        try:
            with open("grades.json", "r", encoding='utf-8') as f:
                grades = json.load(f)
            for record in grades:
                self.grades_listbox.insert(tk.END, f"{record['name']}: {record['grade']:.2f}%")
        except FileNotFoundError:
            messagebox.showerror("Ошибка!", "Файл grades.json не найден!")
        except Exception as e:
            messagebox.showerror("Ошибка!", f"Ошибка при загрузке журнала оценок: {e}")

root = tk.Tk()
app = TeacherApp(root)
root.mainloop()
