# TODO: описать базовый класс

class Human:
    """
        Базовый класс для всех людей.
        Arg:
            _age (int): Возраст человека. Должен являться непубличным, чтобы предотвратить
                        случайное изменение извне.
            _height (float): Рост человека. Должен являться непубличным, чтобы обеспечить
                             контроль над изменениями роста.
            _name (str):  Имя человека. Должно являться непубличным, чтобы избежать
                           некорректных изменений.
        """
    def __init__(self, age: int, height: float, name: str):
        """
                Инициализация атрибутов Человека.
                Args:
                    age (int): Возраст человека.
                    height (float): Рост человека.
                    name (str): Имя человека.
                """
        self._age = age
        self._height = height
        self._name = name

    #Базовые геттеры и сеттеры
    #Они наследуются
    @property
    def age(self)->int:
        """"Получить возраст человека"""
        return self._age

    @age.setter
    def age(self, n_age: int):
        """Установление нового возвраста человека
        Arg:
            n_age(int): Новый возраст человека
        Raises:
            TypeError: Если аргумент не является целым числом
            ValueError: Если аргумент отрицательный
            """
        if not isinstance(n_age, int):
            raise TypeError("Возраст должен бфть целочисленного типа")
        if n_age<0:
            raise ValueError("Возраст не может быть отрицательным")
        self._age = n_age

    @property
    def height(self)->float:
        """Получить рост человека"""
        return self._height

    @height.setter
    def height(self, n_height: float):
        """Установить новый рост человека.
        Arg:
            n_height (float): Новый рост человека.
        Raises:
            TypeError: Если новый рост не является числом.
            ValueError: Если новый рост является отрицательный.
        """
        if not isinstance(n_height, (float, int)):
            raise TypeError("Рост должен быть числом")
        if n_height < 0:
            raise ValueError("Вес не может быть отрицательным")
        self._height = n_height

    @property
    def name(self)->str:
        """Получить имя человека"""
        return self.name

    def __str__(self) -> str:
        """Строковое представление человека."""
        return f'I am {self.__class__.__name__}. I am {self.age} years old. I am {self.name}.'

    def __repr__(self) -> str:
        """Представление человека для отладки."""
        return f'{self.__class__.__name__}(age={self.age}, height={self.height}, name={self.name})'

    def age_in_months(self)->int:
        """Получить возраст человека в годах"""
        return self.age * 12


# TODO: описать дочерний класс

class Man(Human):
    """
    Класс для мужчин, которые унаследовали от класса Human

    Атрибуты:
        _Humanrace(str): Раса мужчины. Должен быть непублияным, чтобы предотвратить
                        случайное изменение извне
    """
    #Переопределенный метод инициализации (перегружен)
    def __init__(self, age:int, height:float, name:str, Humanrace:str ):
        """
        Инциализация атрибутов Человека.

        Args:
            age(int): влзраст человека
            height(float): рост человека
            name(str): имя человека
            Humanrace(str): раса человека
        """
        super().__init__(age, height, name)
        self._Humanrace = Humanrace

    @property
    def Humanrace(self)->str:
        """Получить расу человека"""
        return self._Humanrace

    #Перегруженный метод __str__
    def __str__(self) -> str:
        """Строковое представление мужчины с указанием расы"""
        return f'I am a{self.Humanrace} man. I am {self.age} years old. I am {self.name}'

    #Перегруженный метод __repr__

    def __repr__(self)->str:
        """Представление мужчины для отладки"""
        return f'{self.__class__.__name__}(age={self.age}, height={self.height}, name={self.name}, Humanrace={self.Humanrace})'

    def breathe(self)->str:
        """Метод, который показывает дыхание мужчины

        Returns:
                str: Сообщение о том, что мужчина дышит
        """
        return f'The{self.Humanrace} man is breathing'

