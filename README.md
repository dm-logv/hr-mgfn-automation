# hr-mgfn-automation

Решения к тестовым заданиям Мегафон на позицию разработчика автоматизации процессов.


## Структура проекта

* `gppl` — Задания по языкам общего назначения
    * `js` — JavaScript
    * `py` — Python
    * `go` — Go
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


### Go

Требует установленного и настроенного окружения Go.

Каждый файл выполнен в виде отдельного CLI-инструмента, 
работающего через параметры командной строки.

```sh
cd hr-mgfn-automation/gppl/go 

# Build each file separately
for file in *.go; do go build "$file"; done

./a_mortgage
./b_multiplicity
./c_wordmorph
./d_matrix
./e_sorter
```

Ключи аргументов и значения по умолчанию можно узнать с помощью `-h`:

```sh
./a_mortgage -h
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
