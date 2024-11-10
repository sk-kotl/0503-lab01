# Стало настолько скучно...
...что я решил довольно сильно доработать приложение в плане интерфейса и, в какой-то степени, кода программы.

Эта версия необязательна для проверки, но она сильно улучшена.

# Запускается под любым дистрибутивом Linux.
На ОС Windows нормально не работает Gtk, из-за чего интерфейс может не работать или не запускаться.

Для работы подойдет любой дистрибутив Linux, но необходимо установить необходимые библиотеки.
## Что необходимо установить перед запуском
Для запуска требуются такие компоненты, как Gtk, python3 и matplotlib.

Для установки используем команду `sudo apt install python3 python3-matplotlib python3-gi python3-gi-cairo gir1.2-gtk-3.0 -y`.
## Как запустить программу
Для запуска программы используем команду `python3 app.py` внутри папки проекта.

**Если использовать вне папки проекта, то программа может создавать свой временный файл для себя, заменив _возможно_ существующий файл у вас.**
### Не считаю за ошибку
- Если AB и BC равны 100+, а AC значительно меньше AB/AC и рисунок выходит как одна линия. 
    - В теории такой треугольник действительно существует, но это невозможно отрисовать нормально.
- Прием очень больших чисел (1000000000000000...).
    - Python принимает за число - значит так и должно быть, вот оно и работает.