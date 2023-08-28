# scrapy_parser_pep
---
## Что умеет парсер?
- Сбор информации о PEP, подсчет количества статусов PEP
- Сохранение в папку results/ в формате CSV

## Технологии
- Python 3.9
- Scrapy

## Установка:
- Клонируйте проект парсера на свой компьютер:
```
git@github.com:hydrospirt/scrapy_parser_pep.git
```
- Установите и активируйте виртуальное окружение
```
py -3.9 -m venv venv
source venv/Scripts/Activate
```
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
## Инструкции для запуска
Для запуска парсера используте комманду:
```
scrapy crawl pep
```
Пример вывода:
![Результат Парсинга](https://github.com/hydrospirt/scrapy_parser_pep/blob/main/example.png?raw=true)

# Автор
Эдуард Гумен - GitHub: https://github.com/hydrospirt