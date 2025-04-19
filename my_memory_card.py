#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGroupBox,
    QRadioButton,
    QPushButton,
    QLabel,
    QButtonGroup,
)
from random import shuffle, randint


class Question:
    # содержит вопрос, правильный и три неправильных ответа
    def __init__(self, question, right_answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3


app = QApplication([])

window = QWidget()
window.setWindowTitle("Memory Card")
window.resize(300, 200)

"""Интерфейс приложения Memory Card"""
btn_OK = QPushButton("Ответить")  # кнопка ответа
lb_question = QLabel("В каком году была основана Москва?")  # текст вопроса

#Создаем панель для вопроса
RadioGroupBox = QGroupBox("Варианты ответов")  # группа на экране для переключателей с ответами
btn1 = QRadioButton("1147")
btn2 = QRadioButton("1242")
btn3 = QRadioButton("1861")
btn4 = QRadioButton("1943")

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn1)
RadioGroup.addButton(btn2)
RadioGroup.addButton(btn3)
RadioGroup.addButton(btn4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()  # вертикальные будут внутри горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(btn1)  # два ответа в первый столбец
layout_ans2.addWidget(btn2)
layout_ans3.addWidget(btn3)  # два ответа во второй столбец
layout_ans3.addWidget(btn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)  # разместили столбцы в одной строке

RadioGroupBox.setLayout(layout_ans1)  # готова "панель" с вариантами ответов

#Создаем панель для результата
AnsGroupBox = QGroupBox("Результат")
lb_result = QLabel('Правильно/Неправильно')
lb_correct = QLabel('Правильный ответ')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=Qt.AlignLeft)
layout_res.addWidget(lb_correct, alignment=Qt.AlignCenter)
AnsGroupBox.setLayout(layout_res)



layout_H1 = QHBoxLayout()  # вопрос
layout_H2 = QHBoxLayout()
layout_H3 = QHBoxLayout()  # кнопка "Ответить"

layout_H1.addWidget(lb_question, alignment=Qt.AlignCenter)

layout_H2.addWidget(RadioGroupBox)
layout_H2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_H3.addStretch(1)
layout_H3.addWidget(btn_OK, stretch=2)  # кнопка должна быть большой
layout_H3.addStretch(1)

# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()


layout_card.addLayout(layout_H1, stretch=2)
layout_card.addLayout(layout_H2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_H3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)  # пробелы между содержимым

window.setLayout(layout_card)


"""Функционал приложения"""
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_correct(result):
    # показывает результат - правильно/неправильно
    lb_result.setText(result)
    show_result()


def ask(question: Question):
    shuffle(answers)
    answers[0].setText(question.right_answer)
    answers[1].setText(question.wrong_answer1)
    answers[2].setText(question.wrong_answer2)
    answers[3].setText(question.wrong_answer3)
    lb_question.setText(question.question)
    lb_correct.setText(question.right_answer)
    show_question()

def check_answer():
    # проверяет ответ пользователя
    global score, total
    if answers[0].isChecked():
        show_correct("Правильно!")
        score += 1

    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct("Неправильно!")

    print('Статистика:\n- Всего вопросов:', total)
    print('- Правильных ответов:', score)
    print('- Рейтинг:', round(score / total * 100, 0), '%')



    
def next_question():
    # задает следующий вопрос из списка вопросов
    # global current_question
    global total
    total += 1
    print('Статистика:\n- Всего вопросов:', total)
    current_question = randint(0, len(questions_list) - 1)
    if current_question >= len(questions_list):
        current_question = 0
    question = questions_list[current_question]
    ask(question)


def click_OK():
    # определяет, надо показать слудующий вопрос или проверить ответ
    if btn_OK.text() == "Ответить":
        check_answer()  # проверяет ответ
    else:
        next_question()  # показывает следующий вопрос

answers = [btn1, btn2, btn3, btn4]
# current_question = -1
total = 0
score = 0

questions_list = []
questions_list.append(
    Question("Государственный язык Бразилии", "Португальский", "Английский", "Испанский", "Бразильский")
)
questions_list.append(Question("Национальная хижина якутов", "Ураса", "Юрта", "Иглу", "Хата"))
questions_list.append(Question("Какого цвета нет на флаге России?", "Зелёный", "Красный", "Белый", "Синий"))
questions_list.append(
    Question(
        "Когда первый человек вышел в открытый космос?", "В 1965 году", "В 1957 году", "В 1979 году", "В 1997 году"
    )
)
questions_list.append(Question("В каком году закончилась Северная война?", "1699", "1809", "1940", "1721"))
questions_list.append(Question("В каком году люди впервые высадились на Луну?", "1969", "1951", "1988", "1971"))
next_question()

btn_OK.clicked.connect(click_OK)



window.show()
app.exec()