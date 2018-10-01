# hr-mgfn-automation

Решения к тестовым заданиям Мегафон на позицию автоматизации процессов.


## Структура проекта

* `gppl` -- Задания по языкам общего назначения
    * `go` -- Go
    * `js` -- JavaScript
    * `py` -- Python
* `sql` -- Задания по SQL


## Запуск

### JS

```sh
cd hr-mgfn-automation/gppl/js
./run
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
