from settings import settings  # Импорт класса настроек
from settings_manager import settings_manager  # Импорт класса менеджера настроек
import unittest  # Импорт модуля для тестирования

class test_settings(unittest.TestCase):
    
    # Тест для проверки создания менеджера настроек и уникальности идентификаторов
    def test_check_create_manager(self):
        manager1 = settings_manager()  # Создание первого экземпляра менеджера
        manager2 = settings_manager()  # Создание второго экземпляра менеджера
        
        # Вывод уникальных идентификаторов для визуальной проверки
        print(str(manager1.unique_number))
        print(str(manager2.unique_number))
    
        # Проверка уникальности идентификаторов
        assert manager1.unique_number == manager2.unique_number
    
    # Тест для проверки установки и получения данных в объекте настроек
    def test_check_get_data_in_settings(self):
        # Подготовка
        item = settings()  # Создание экземпляра настроек
        
        # Действие: установка значений атрибутов
        item.inn = "012345678978"
        item.account = "01234567890"
        item.correspondent_account = "01234567890"
        item.bic = "123456789"
        item.name = "Romashka"
        item.type_of_property = "12345"
        
        # Проверка: сравнение установленных значений с ожидаемыми
        assert item.inn == "012345678978"
        assert item.account == "01234567890"
        assert item.correspondent_account == "01234567890"
        assert item.bic == "123456789"
        assert item.name == "Romashka"
        assert item.type_of_property == "12345"
        
    # Тест для проверки метода конвертации данных в объекте менеджера настроек
    def test_check_manager_convert(self):
        # Подготовка
        manager = settings_manager()  # Создание экземпляра менеджера
        manager.open("settings.json")  # Открытие файла настроек
        
        # Действие: конвертация данных
        manager.convert()       
        
        # Проверка: проверка успешного выполнения конвертации
        
    # Тест для проверки открытия файла настроек
    def test_check_open_settings(self):
        # Подготовка
        manager = settings_manager()  # Создание экземпляра менеджера
        
        # Действие: попытка открытия файла настроек
        result = manager.open("settings.json")
        
        # Проверка: проверка успешного открытия файла и загрузки данных
        print(manager.data)
        assert result == True
        
    # Тест для проверки загрузки настроек из несуществующего файла
    def test_loading_settings_nonexistent_file(self):
        manager = settings_manager()  # Создание экземпляра менеджера
        with self.assertRaises(Exception):  # Ожидание возникновения исключения
            manager.open("nonexistent_file.json")  # Попытка открытия несуществующего файла

    # Тест для проверки обработки исключений при загрузке некорректного файла настроек
    def test_loading_settings_exceptions_invalid__file(self):
        manager = settings_manager()  # Создание экземпляра менеджера
        with self.assertRaises(Exception):  # Ожидание возникновения исключения
            manager.open("invalid_settings.json")  # Попытка открытия некорректного файла настроек
