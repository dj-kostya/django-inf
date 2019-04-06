# Сдам ЕГЭ

Дз по информатике

## Installation

Установка себе

```bash
git clone https://github.com/dj-kostya/django-inf
cd django-inf
pip install -r requirements.txt
```

## Уже развернутый сервер
[тут](http://djkostya.pythonanywhere.com/task)

http://djkostya.pythonanywhere.com/

## Роуты
* task/ -  Список всех доступных заданий
* task/{id} - Загрузить задание под номер {id}
* admin/ - Админка
## Учетка для админки
* логин: User
* пароль: 1234qwer
* Права: Только создание заданий и загрузка изображений

## Порядок создания
1) создать запись в таблицу tasks (with_image нужно ставить true, если у вас есть картинки для данного задания)
2) Загрузить картинки
3) Создать запись в taskimage (связать id задания и id картинки)
4) Поставить 5 Носореву, Долгих, Князев

## Планы на будущее 
* Сдать егэ на 100 =)
