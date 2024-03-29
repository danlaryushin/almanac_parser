# Спортивный Альманах

Сервис для парсинга и обработки статистики спортивных событий за последние 5 лет. Информации сохраняется в базе данных для последующей обработки аналитиками.

- Для работы парсера необходимо получить токен у сервиса BetsAPI.
  
В парсере намеренно не использовались ассинхронные фреймворки, ввиду ограничений количества запросов со стороны статистического портала.

## Инструкция по локальному запуску проекта
Склонируйте репозиторий
```
git clone https://github.com/danlaryushin/almanac_parser.git
```
Создайте виртуальное окружение
```
cd almanac_parser
```
```
python -m venv venv
```
Установите зависимости
```
pip install -r requirements.txt
```
Запустите проект
```
python main.py
```
После завершения парсинга, вся статистика будет доступна в файле basket.db

## Автор 
[Даниил Ларюшин](https://github.com/danlaryushin)
