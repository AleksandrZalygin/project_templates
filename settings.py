class settings:
    # Определение приватных атрибутов класса
    __inn = ""
    __account = ""
    __correspondent_account = ""
    __bic = ""
    __name = ""
    __type_of_property = ""
    
    # Геттеры для получения значений атрибутов
    @property
    def inn(self):
        return self.__inn

    @property
    def account(self):
        return self.__account

    @property
    def correspondent_account(self):
        return self.__correspondent_account

    @property
    def bic(self):
        return self.__bic
    
    @property
    def name(self):
        return self.__name
    
    @property
    def type_of_property(self):
        return self.__type_of_property

    # Сеттеры для установки значений атрибутов с проверкой входных данных
    @inn.setter
    def inn(self, value: str):
        if not isinstance(value, str) or len(value) != 12:
            raise Exception("Некорректный аргумент!")
        
        self.__inn = value.strip()

    @account.setter
    def account(self, value: str):
        if not isinstance(value, str) or len(value) != 11:
            raise Exception("Некорректный аргумент!")
        
        self.__account = value.strip()

    @correspondent_account.setter
    def correspondent_account(self, value: str):
        if not isinstance(value, str) or len(value) != 11:
            raise Exception("Некорректный аргумент!")
        
        self.__correspondent_account = value.strip()

    @bic.setter
    def bic(self, value: str):
        if not isinstance(value, str) or len(value) != 9:
            raise Exception("Некорректный аргумент!")
        
        self.__bic = value.strip()

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise Exception("Некорректный аргумент!")
        
        self.__name = value.strip()

    @type_of_property.setter
    def type_of_property(self, value: str):
        if not isinstance(value, str) or len(value) != 5:
            raise Exception("Некорректный аргумент!")
        
        self.__type_of_property = value.strip()
