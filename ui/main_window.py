# Импортируем tkinter для создания графического интерфейса.
import tkinter as tk
# Импортируем ttk для использования более аккуратных виджетов.
from tkinter import ttk
# Импортируем функции логики из папки logic.
from logic.palindrome import is_palindrome, normalize_text

# Создаем класс главного окна приложения.
class PalindromeApp(tk.Tk):
    # Создаем конструктор класса, который срабатывает при создании окна.
    def __init__(self):
        # Инициализируем родительский класс Tk.
        super().__init__()
        # Задаем заголовок окна программы.
        self.title("Проверка строки на палиндром")
        # Задаем стартовый размер окна.
        self.geometry("820x540")
        # Задаем минимальный размер окна, чтобы интерфейс не ломался при сильном уменьшении.
        self.minsize(720, 480)
        # Задаем цвет фона главного окна.
        self.configure(bg="#F4F7FB")
        # Разрешаем единственному столбцу окна растягиваться по ширине.
        self.columnconfigure(0, weight=1)
        # Разрешаем единственной строке окна растягиваться по высоте.
        self.rowconfigure(0, weight=1)
        # Создаем переменную для текста результата.
        self.result_var = tk.StringVar(value="Здесь появится результат проверки.")
        # Создаем переменную для отображения очищенной строки.
        self.normalized_var = tk.StringVar(value="Здесь появится очищенная строка.")
        # Настраиваем стили ttk-элементов.
        self._set_ttk_styles()
        # Создаем и размещаем все виджеты интерфейса.
        self._create_widgets()
        # Подписываемся на изменение размера окна, чтобы текст красиво переносился.
        self.bind("<Configure>", self._handle_resize)

    # Создаем метод для настройки визуальных стилей.
    def _set_ttk_styles(self):
        # Создаем объект стилей ttk.
        style = ttk.Style()
        # Переключаемся на тему clam, потому что она выглядит аккуратнее стандартной.
        style.theme_use("clam")
        # Настраиваем стиль основного контейнера приложения.
        style.configure("App.TFrame", background="#F4F7FB")
        # Настраиваем стиль карточек внутри приложения.
        style.configure("Card.TFrame", background="#FFFFFF")
        # Настраиваем стиль большого заголовка.
        style.configure("Title.TLabel", background="#F4F7FB", font=("Segoe UI", 20, "bold"))
        # Настраиваем стиль подзаголовка.
        style.configure("Subtitle.TLabel", background="#F4F7FB", font=("Segoe UI", 11))
        # Настраиваем стиль заголовков карточек.
        style.configure("CardTitle.TLabel", background="#FFFFFF", font=("Segoe UI", 12, "bold"))
        # Настраиваем стиль обычного текста внутри карточек.
        style.configure("CardText.TLabel", background="#FFFFFF", font=("Segoe UI", 11))
        # Настраиваем стиль основной кнопки.
        style.configure("Primary.TButton", font=("Segoe UI", 11, "bold"), padding=(14, 10))
        # Настраиваем стиль дополнительной кнопки.
        style.configure("Secondary.TButton", font=("Segoe UI", 10), padding=(12, 10))

    # Создаем метод для построения интерфейса.
    def _create_widgets(self):
        # Создаем главный контейнер для всех элементов интерфейса.
        main_frame = ttk.Frame(self, style="App.TFrame", padding=20)
        # Размещаем главный контейнер внутри окна и разрешаем ему растягиваться.
        main_frame.grid(row=0, column=0, sticky="nsew")
        # Разрешаем единственному столбцу главного контейнера растягиваться по ширине.
        main_frame.columnconfigure(0, weight=1)
        # Создаем заголовок приложения.
        title_label = ttk.Label(main_frame, text="🔁 Проверка строки на палиндром", style="Title.TLabel")
        # Размещаем заголовок в верхней части окна.
        title_label.grid(row=0, column=0, sticky="w")
        # Создаем поясняющий текст под заголовком.
        subtitle_label = ttk.Label(main_frame, text="Введите слово, фразу или предложение. Программа сама очистит строку и определит результат.", style="Subtitle.TLabel")
        # Размещаем поясняющий текст под заголовком.
        subtitle_label.grid(row=1, column=0, sticky="w", pady=(6, 18))
        # Создаем карточку для ввода текста.
        input_card = ttk.Frame(main_frame, style="Card.TFrame", padding=18)
        # Размещаем карточку ввода на форме.
        input_card.grid(row=2, column=0, sticky="nsew")
        # Разрешаем столбцу карточки ввода растягиваться по ширине.
        input_card.columnconfigure(0, weight=1)
        # Создаем заголовок секции ввода.
        input_title_label = ttk.Label(input_card, text="📝 Введите строку для проверки", style="CardTitle.TLabel")
        # Размещаем заголовок секции ввода.
        input_title_label.grid(row=0, column=0, sticky="w")
        # Создаем поясняющий текст для поля ввода.
        input_hint_label = ttk.Label(input_card, text="Можно писать с пробелами, запятыми и разными регистрами, например: А роза упала на лапу Азора", style="CardText.TLabel")
        # Размещаем поясняющий текст для поля ввода.
        input_hint_label.grid(row=1, column=0, sticky="w", pady=(6, 12))
        # Создаем многострочное поле ввода текста.
        self.input_text = tk.Text(input_card, height=5, wrap="word", font=("Segoe UI", 12), relief="solid", bd=1)
        # Размещаем поле ввода на карточке.
        self.input_text.grid(row=2, column=0, sticky="nsew")
        # Разрешаем строке с полем ввода растягиваться по высоте.
        input_card.rowconfigure(2, weight=1)
        # Создаем контейнер для кнопок.
        button_frame = ttk.Frame(input_card, style="Card.TFrame")
        # Размещаем контейнер для кнопок под полем ввода.
        button_frame.grid(row=3, column=0, sticky="w", pady=(14, 0))
        # Создаем кнопку для запуска проверки.
        check_button = ttk.Button(button_frame, text="✅ Проверить", style="Primary.TButton", command=self.check_palindrome)
        # Размещаем кнопку запуска проверки.
        check_button.grid(row=0, column=0, padx=(0, 10))
        # Создаем кнопку для очистки поля и результата.
        clear_button = ttk.Button(button_frame, text="🧹 Очистить", style="Secondary.TButton", command=self.clear_fields)
        # Размещаем кнопку очистки.
        clear_button.grid(row=0, column=1)
        # Создаем карточку результата.
        result_card = ttk.Frame(main_frame, style="Card.TFrame", padding=18)
        # Размещаем карточку результата под карточкой ввода.
        result_card.grid(row=3, column=0, sticky="nsew", pady=(18, 0))
        # Разрешаем столбцу карточки результата растягиваться по ширине.
        result_card.columnconfigure(0, weight=1)
        # Создаем заголовок секции результата.
        result_title_label = ttk.Label(result_card, text="📌 Результат проверки", style="CardTitle.TLabel")
        # Размещаем заголовок секции результата.
        result_title_label.grid(row=0, column=0, sticky="w")
        # Создаем текстовую метку для основного результата.
        self.result_label = tk.Label(result_card, textvariable=self.result_var, font=("Segoe UI", 14, "bold"), bg="#FFFFFF", anchor="w", justify="left")
        # Размещаем текстовую метку результата.
        self.result_label.grid(row=1, column=0, sticky="ew", pady=(10, 14))
        # Создаем заголовок для очищенной строки.
        normalized_title_label = ttk.Label(result_card, text="🧼 Очищенная строка", style="CardTitle.TLabel")
        # Размещаем заголовок очищенной строки.
        normalized_title_label.grid(row=2, column=0, sticky="w")
        # Создаем текстовую метку для отображения очищенной строки.
        self.normalized_label = tk.Label(result_card, textvariable=self.normalized_var, font=("Consolas", 12), bg="#FFFFFF", anchor="w", justify="left")
        # Размещаем текстовую метку очищенной строки.
        self.normalized_label.grid(row=3, column=0, sticky="ew", pady=(10, 14))
        # Создаем дополнительную подсказку снизу.
        footer_label = ttk.Label(result_card, text="Подсказка: программа сравнивает символы слева и справа после очистки строки.", style="CardText.TLabel")
        # Размещаем дополнительную подсказку снизу.
        footer_label.grid(row=4, column=0, sticky="w")
        # Устанавливаем курсор в поле ввода, чтобы можно было сразу печатать текст.
        self.input_text.focus()

    # Создаем метод, который будет вызываться при нажатии на кнопку проверки.
    def check_palindrome(self):
        # Получаем текст из многострочного поля ввода и убираем пробелы по краям.
        entered_text = self.input_text.get("1.0", "end").strip()
        # Проверяем, ввел ли пользователь хоть какой-нибудь текст.
        if entered_text == "":
            # Показываем предупреждение, если поле осталось пустым.
            self.result_var.set("⚠️ Сначала введите строку для проверки.")
            # Обновляем текст очищенной строки для пустого состояния.
            self.normalized_var.set("Поле ввода пока пустое.")
            # Красим результат в оранжевый цвет предупреждения.
            self.result_label.config(fg="#B45309")
            # Завершаем работу метода, чтобы не выполнять дальнейшую проверку.
            return
        # Получаем очищенную строку без пробелов, знаков препинания и лишних символов.
        normalized_text = normalize_text(entered_text)
        # Проверяем, остались ли после очистки буквы или цифры.
        if normalized_text == "":
            # Показываем предупреждение, если после очистки строка стала пустой.
            self.result_var.set("⚠️ После очистки не осталось букв или цифр.")
            # Показываем пояснение в поле очищенной строки.
            self.normalized_var.set("Пустая строка после очистки.")
            # Красим результат в оранжевый цвет предупреждения.
            self.result_label.config(fg="#B45309")
            # Завершаем работу метода, потому что дальше сравнивать нечего.
            return
        # Вызываем функцию проверки палиндрома.
        palindrome_status = is_palindrome(entered_text)
        # Показываем пользователю очищенную строку.
        self.normalized_var.set(normalized_text)
        # Проверяем, что вернула функция проверки.
        if palindrome_status:
            # Показываем положительный результат для палиндрома.
            self.result_var.set("✅ Да, это палиндром.")
            # Красим положительный результат в зеленый цвет.
            self.result_label.config(fg="#166534")
        # Обрабатываем случай, когда строка не является палиндромом.
        else:
            # Показываем отрицательный результат.
            self.result_var.set("❌ Нет, это не палиндром.")
            # Красим отрицательный результат в красный цвет.
            self.result_label.config(fg="#991B1B")

    # Создаем метод для очистки поля ввода и результатов.
    def clear_fields(self):
        # Удаляем весь текст из поля ввода.
        self.input_text.delete("1.0", "end")
        # Возвращаем стандартный текст результата.
        self.result_var.set("Здесь появится результат проверки.")
        # Возвращаем стандартный текст очищенной строки.
        self.normalized_var.set("Здесь появится очищенная строка.")
        # Возвращаем стандартный темный цвет текста результата.
        self.result_label.config(fg="#1F2937")
        # Снова ставим курсор в поле ввода.
        self.input_text.focus()

    # Создаем метод для более красивого переноса длинного текста при изменении размера окна.
    def _handle_resize(self, event):
        # Вычисляем новую ширину переноса текста с небольшим запасом.
        wrap_width = max(self.winfo_width() - 120, 280)
        # Обновляем ширину переноса для текста результата.
        self.result_label.config(wraplength=wrap_width)
        # Обновляем ширину переноса для очищенной строки.
        self.normalized_label.config(wraplength=wrap_width)