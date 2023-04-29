#начни тут создавать приложение с умными заметками
import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QInputDialog, QGroupBox, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QButtonGroup, QLineEdit, QTextEdit, QListWidget

notes = {
    "добро пожаловать! " : {
        "текст" : "это самое лучшее приложение для заметок в мире! Первый пробный месяц бесплатно.",
        "теги" : ["добро","инструкция"]
    }
}

with open ("notes_data.json", "w") as file:
    json.dump(notes, file)

def add_note():
    note_name, ok = QInputDialog.getText(window, "Добавить заметку", "название заметки")
    if ok and note_name != "":
        notes[note_name] = {"текст" : "", "теги" : []}
        list_notes.addItem(note_name)
        list_2notes.addItems(notes[note_name]["теги"])

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]["текст"] = text_field.toPlainText()
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)

def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        with open("notes_data.json", "w") as file:
            json.dump(notes, file)
        text_field.clear()
        list_notes.clear()
        list_notes.addItems(notes)
        list_2notes.clear()
        
def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        teg = tag.text() 
        if not teg in notes[key]["теги"]:
            notes[key]["теги"].append(teg)
            list_2notes.addItem(teg)
            tag.clear()
            with open("notes_data.json", "w") as file:
                json.dump(notes, file, sort_keys=True, ensure_ascii=False)

def del_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del 












app = QApplication([])

window = QWidget()
window.setWindowTitle('Умные заметки')

text_field = QTextEdit()
text_field.setText('Создание заметок')

h_layou = QLabel()

BoosLain_h = QHBoxLayout()
lain_v_ans1 = QVBoxLayout()
lain_v_ans2 = QVBoxLayout()

lain_h_1TopList = QHBoxLayout()
text1 = QLabel('Список заметок')
lain_h_1TopList.addWidget(text1)

lain_h_1List = QHBoxLayout()
list_notes = QListWidget()
lain_h_1List.addWidget(list_notes)

lain_h_1List_Baton_1 = QHBoxLayout()
btn_creat1 = QPushButton('Создать заметку')
btn_delet1 = QPushButton('Удалить заметку')
lain_h_1List_Baton_1.addWidget(btn_creat1)
lain_h_1List_Baton_1.addWidget(btn_delet1)

lain_h_1List_Baton_2 = QHBoxLayout()
btn_save1 = QPushButton('Сохранить заметку')
lain_h_1List_Baton_2.addWidget(btn_save1)

lain_h_2TopList = QHBoxLayout()
text2 = QLabel('Список тегов')
lain_h_2TopList.addWidget(text2)

lain_h_2List = QHBoxLayout()
list_2notes = QListWidget()
lain_h_2List.addWidget(list_2notes)

lain_h_2List_Baton_1 = QHBoxLayout()
btn_creat2 = QPushButton('Создать тег')
btn_delet2 = QPushButton('Открепить тег')
lain_h_2List_Baton_1.addWidget(btn_creat2)
lain_h_2List_Baton_1.addWidget(btn_delet2)

lain_h_2List_Baton_2 = QHBoxLayout()
btn_save2 = QPushButton('Сохранить тег')
lain_h_2List_Baton_2.addWidget(btn_save2)

lain_h_Tag = QHBoxLayout()
tag = QLineEdit()
tag.setPlaceholderText('Введите тег...')
lain_h_Tag.addWidget(tag)

lain_v_ans1 = QVBoxLayout()
lain_v_ans1.addWidget(text_field)
lain_v_ans2 = QVBoxLayout()
lain_v_ans2.addLayout(lain_h_1TopList)
lain_v_ans2.addLayout(lain_h_1List)
lain_v_ans2.addLayout(lain_h_1List_Baton_1)
lain_v_ans2.addLayout(lain_h_1List_Baton_2)
lain_v_ans2.addLayout(lain_h_2TopList)
lain_v_ans2.addLayout(lain_h_2List)
lain_v_ans2.addLayout(lain_h_Tag)
lain_v_ans2.addLayout(lain_h_2List_Baton_1)
lain_v_ans2.addLayout(lain_h_2List_Baton_2)

BoosLain_h.addLayout(lain_v_ans1)
BoosLain_h.addLayout(lain_v_ans2)

window.setLayout(BoosLain_h)

def show_notes():
    key = list_notes.selectedItems()[0].text()
    text_field.setText(notes[key]["текст"])
    list_2notes.clear()
    list_2notes.addItems(notes[key]["теги"])

list_notes.itemClicked.connect(show_notes)

with open ("notes_data.json", "r") as file:
    notes = json.load(file)
list_notes.addItems(notes)

btn_creat1.clicked.connect(add_note)
btn_save1.clicked.connect(save_note)
btn_delet1.clicked.connect(del_note)
btn_creat2.clicked.connect(add_tag)

window.show()
app.exec()