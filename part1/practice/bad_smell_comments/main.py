# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    def move(self, field, field_x, field_y, direction, fly, crawl, speed=1):

        if fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if fly:
            speed *= 1.2

            if direction == 'UP':
                new_y = field_y + speed
                new_x = field_x

            elif direction == 'DOWN':
                new_y = field_y - speed
                new_x = field_x

            elif direction == 'LEFT':
                new_y = field_y
                new_x = field_x - speed

            elif direction == 'RIGHT':
                new_y = field_y
                new_x = field_x + speed

        if crawl:
            speed *= 0.5
            if direction == 'UP':
                new_y = field_y + speed
                new_x = field_x
            elif direction == 'DOWN':
                new_y = field_y - speed
                new_x = field_x
            elif direction == 'LEFT':
                new_y = field_y
                new_x = field_x - speed
            elif direction == 'RIGHT':
                new_y = field_y
                new_x = field_x + speed

            field.set_unit(x=new_x, y=new_y, unit=self)
