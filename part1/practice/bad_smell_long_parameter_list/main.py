from typing import Optional


class Unit:

    CRAWLING_COEF: float = 0.5
    FLYING_COEF: float = 1.2

    def __init__(self, field, status, x, y):
        self.field = field
        self.status: str = status
        self.speed: int = 1
        self.x: float = x
        self.y: float = y

    def __get_speed(self) -> Optional[float]:
        if self.status == 'is_flying':
            return self.speed * self.FLYING_COEF
        if self.status == 'is_crawling':
            return self.speed * self.CRAWLING_COEF
        raise ValueError('Рожденный ползать летать не должен!')

    def move(self, direction: str) -> None:

        speed: float = self.__get_speed()

        if direction == 'UP':
            self.field.set_unit(y=self.y + speed, x=self.x, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y=self.y - speed, x=self.x, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y=self.y, x=self.x - speed, unit=self)
        elif direction == 'RIGHT':
            self.field.set_unit(y=self.y, x=self.x + speed, unit=self)
        else:
            raise ValueError('Не туда идешь')
