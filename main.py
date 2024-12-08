# импортируем библиотеки
from tkinter import *
from tkinter import filedialog, messagebox
# импортируем модуль для работы с диалогом выбора файлов
import webbrowser

# импортируем библиотеку для парсинга HTML
# Главное окно приложения
window = Tk()
# Заголовок окна
window.title('Авторизация')
# Размер окна
window.geometry('600x400')
# Можно ли изменять размер окна - нет
window.resizable(True, True)

# Кортежи и словари, содержащие настройки шрифтов и отступов
font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

# Переменная для чекбокса
remember_var = BooleanVar()


# Обработчик нажатия на кнопку 'Войти'
def clicked():
    remember_me = remember_var.get()  # Получаем состояние чекбокса
    option_menu = selected_option.get()
def open_website():
    webbrowser.open("https://github.com")

# Кнопка "Войти"
send_btn = Button(window, text='Войти', command=open_website)
send_btn.pack(**base_padding)


# Запуск основного цикла приложения
window.mainloop()