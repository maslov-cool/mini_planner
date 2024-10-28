import io
import sys
import datetime

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Минипланировщик</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="gridLayoutWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>801</width>
      <height>551</height>
     </rect>
    </property>
    <layout class="QGridLayout" name="gridLayout">
     <item row="0" column="0">
      <layout class="QVBoxLayout" name="verticalLayout">
       <item>
        <widget class="QTimeEdit" name="timeEdit"/>
       </item>
       <item>
        <widget class="QCalendarWidget" name="calendarWidget"/>
       </item>
       <item>
        <widget class="QLineEdit" name="lineEdit"/>
       </item>
       <item>
        <widget class="QPushButton" name="addEventBtn">
         <property name="text">
          <string>Добавить задачу</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item row="0" column="1">
      <widget class="QListWidget" name="eventList"/>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class SimplePlanner(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)  # Загружаем дизайн

        self.addEventBtn.clicked.connect(self.action)
        self.tasks = {}

    def action(self):
        if self.lineEdit.text():
            self.tasks[datetime.datetime(self.calendarWidget.selectedDate().year(),
                                         self.calendarWidget.selectedDate().month(),
                                         self.calendarWidget.selectedDate().day(),
                                         self.timeEdit.time().hour(), self.timeEdit.time().minute())] = (
                self.lineEdit.text())
            self.eventList.clear()
            self.eventList.addItems([f'{i} - {self.tasks[i]}'for i in sorted(self.tasks.keys())])



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimplePlanner()
    ex.show()
    sys.exit(app.exec())
