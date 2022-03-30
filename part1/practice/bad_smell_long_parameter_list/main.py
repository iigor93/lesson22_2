# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self):
        self.speed = 1
        self.x_coordinate = 0
        self.y_coordinate = 0

    def _is_fly_or_crawl(self, is_fly: bool, crawl: bool):
        if is_fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

    def _speed_calc(self, is_fly: bool, crawl: bool):
        self._is_fly_or_crawl(is_fly, crawl)
        if is_fly:
            self.speed *= 1.2
        if crawl:
            self.speed *= 0.5

    def _position_calc(self, direction):
        if direction == 'UP':
            self.y_coordinate += self.speed
        elif direction == 'DOWN':
            self.y_coordinate -= self.speed
        elif direction == 'LEFT':
            self.x_coordinate -= self.speed
        elif direction == 'RIGTH':
            self.x_coordinate += self.speed

        return 1, 2

    def move(self, field, direction, is_fly, crawl):
        self._speed_calc(is_fly, crawl)
        self._position_calc(direction)

        field.set_unit(x=self.x_coordinate, y=self.y_coordinate, unit=self)
