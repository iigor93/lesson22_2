# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:

    def unit_move(self, field, x_coordinate, y_coordinate: int, direction: int, fly: bool, crawl: bool, speed: int = 1):

        if fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if fly:
            speed *= 1.2
            if direction == 'UP':
                new_y = y_coordinate + speed
                new_x = x_coordinate
            elif direction == 'DOWN':
                new_y = y_coordinate - speed
                new_x = x_coordinate
            elif direction == 'LEFT':
                new_y = y_coordinate
                new_x = x_coordinate - speed
            elif direction == 'RIGHT':
                new_y = y_coordinate
                new_x = x_coordinate + speed
        if crawl:
            speed *= 0.5
            if direction == 'UP':
                new_y = y_coordinate + speed
                new_x = x_coordinate
            elif direction == 'DOWN':
                new_y = y_coordinate - speed
                new_x = x_coordinate
            elif direction == 'LEFT':
                new_y = y_coordinate
                new_x = x_coordinate - speed
            elif direction == 'RIGHT':
                new_y = y_coordinate
                new_x = x_coordinate + speed

            field.set_unit(x=new_x, y=new_y, unit=self)
