# ProgramForTheCourse
Инструментальные средства разработки ПО
Импортируемые библиотеки: 
• #tkinter: Стандартная библиотека Python для создания графических пользовательских интерфейсов. 
• #messagebox: Предоставляет функции для отображения всплывающих окон с сообщениями. 
• #simpledialog: Предоставляет функции для отображения диалоговых окон с вводом. 
• #json: Библиотека для работы с данными в формате JSON. 
Класс TeacherApp: 
Класс TeacherApp представляет собой графический пользовательский интерфейс (GUI) для учителя, позволяющий создавать, редактировать, сохранять и загружать тесты. Он состоит из следующих основных компонентов: 
Фрейм для создания вопросов (create_question_frame): 
• Позволяет учителю создавать новые вопросы для теста, предоставляя поля для ввода вопроса, вариантов ответа и номера правильного ответа. 
Фрейм для просмотра и редактирования вопросов (questions_frame): 
• Отображает список созданных вопросов и предоставляет кнопки для редактирования и удаления вопросов. 
Фрейм для сохранения и загрузки тестов (save_load_frame): 
• Позволяет учителю сохранять текущий тест в файл JSON и загружать тесты из файла JSON. 
Фрейм для журнала оценок (grades_frame): 
• Отображает журнал оценок учащихся, загружая данные из файла JSON. 
Методы класса: 
• init: Конструктор, который создает все элементы GUI и сохраняет их в атрибуты объекта. 
• add_question: Обработчик событий для кнопки добавления вопроса, который создает новый вопрос и добавляет его в список вопросов. 
• edit_question: Обработчик событий для кнопки редактирования вопроса, который редактирует выбранный вопрос. 
• delete_question: Обработчик событий для кнопки удаления вопроса, который удаляет выбранный вопрос. 
• update_questions_listbox: Обновляет список вопросов для отображения списка вопросов. 
• clear_entry_fields: Очищает поля ввода после добавления или редактирования вопроса. 
• save_test: Сохраняет текущий тест в файл JSON. 
• load_test: Загружает тест из файла JSON. 
• view_grades: Отображает журнал оценок. 
Основная программа: 
• root = tk.Tk(): Создает главное окно приложения. 
• app = TeacherApp(root): Создает экземпляр класса TeacherApp. 
• root.mainloop(): Запускает основной цикл приложения
