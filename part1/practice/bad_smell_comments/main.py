class Unit:

    CRAWLING_COEF: float = 0.5
    FLYING_COEF: float = 1.2

    def perform_move(self,
                     field,
                     x_coord: int,
                     y_coord: int,
                     direction: str,
                     is_flying: bool,
                     is_crawling: bool,
                     speed: int = 1) -> None:

        if is_flying and is_crawling:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_flying:
            speed *= self.FLYING_COEF
        if is_crawling:
            speed *= self.CRAWLING_COEF

        if direction == 'UP':
            new_y = y_coord + speed
            new_x = x_coord
        elif direction == 'DOWN':
            new_y = y_coord - speed
            new_x = x_coord
        elif direction == 'LEFT':
            new_y = y_coord
            new_x = x_coord - speed
        elif direction == 'RIGHT':
            new_y = y_coord
            new_x = x_coord + speed

        field.set_unit(x=new_x, y=new_y, unit=self)
