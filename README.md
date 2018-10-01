# hr-mgfn-automation

Решения к тестовым заданиям Мегафон на позицию разработчика автоматизации процессов.


## Структура проекта

* `gppl` — Задания по языкам общего назначения
    * `js` — JavaScript
    * `py` — Python
* `sql` — Задания по SQL


## Запуск

### JavaScript

Решение запускает веб-сервер и открывает соответствующую страницу 
в браузере по умолчанию.

```sh
cd hr-mgfn-automation/gppl/js

./run
```


### Python

Каждое из решений представлено отдельным модулем с CLI-интерфейсом.

```sh
cd hr-mgfn-automation/gppl/py

./a_mortgage.py
./b_multiplicity.py
./c_wordmorph.py
./d_matrix.py
./e_sorter.py
```


### SQL

Задание выполнено с помощью `sqlite`.

```sh
cd hr-mgfn-automation/sql

# Create database, fill with mock data
sqlite3 database.db < deploy.sql

# Create views, select from
sqlite3 database.db < views.sql

```
