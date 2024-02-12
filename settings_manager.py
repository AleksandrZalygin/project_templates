import os
import json
import uuid
from settings import settings  # Импорт класса настроек из файла settings

class settings_manager(object):
    # Имя файла настроек
    __file_name = "settings.json"
    # Уникальный номер
    __unique_number = None
    # Словарь с данными
    __data = {}
    
    # Настройки инстанс
    __settings = settings()  # Создание экземпляра класса настроек

    # Метод __new__ для реализации паттерна Singleton
    def __new__(cls):
        if not hasattr(cls, 'instance'):  # Проверка наличия экземпляра
            cls.instance = super(settings_manager, cls).__new__(cls)
        return cls.instance
    
    # Инициализатор класса, который присваивает уникальный номер
    def __init__(self) -> None:
        self.__unique_number =  uuid.uuid4()  # Генерация уникального идентификатора

    # Геттер для доступа к данным
    @property
    def data(self) -> {}:
        return self.__data
    
    # Геттер для доступа к уникальному номеру в виде строки
    @property
    def unique_number(self) -> str:
        return str(self.__unique_number.hex)

    # Метод для преобразования данных и установки настроек
    def convert(self):
        if len(self.__data) == 0:  # Проверка наличия данных
            raise Exception("Невозможно создать объект типа settings.py")
        
        fields = dir(self.__settings.__class__)  # Получение атрибутов класса настроек
        for field in fields:
            if field in self.__data.keys():
                setattr(self.__settings, field, self.__data[field])  # Установка значения атрибута

    # Метод для открытия файла настроек
    def open(self, file_name: str) -> bool:
        if not isinstance(file_name, str) or file_name == "":  # Проверка аргументов
            raise Exception("ERROR: Неверный аргумент!")
                
        self.__file_name = file_name.strip()  # Обновление имени файла

        try:
            self.__open()  # Вызов приватного метода для открытия файла
        except:
            return False

        return True

    # Приватный метод для открытия файла настроек
    def __open(self):
        file_path = os.path.split(__file__)  # Разделение пути к файлу
        settings_file = "%s/%s" % (file_path[0], self.__file_name)  # Формирование пути к файлу настроек
        if not os.path.exists(settings_file):  # Проверка существования файла
            raise Exception("ERROR: Невозможно загрузить настройки! Не найден файл %s", settings_file)

        with open(settings_file, "r") as read_file:
            self.__data = json.load(read_file)  # Загрузка данных из файла в словарь          
