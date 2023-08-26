# Проект курса Stepik по Selenium Python + POM
 
Ссылка на курс: [Клик](https://stepik.org/course/575).

Проект, разработанный в рамках курса Stepik по автоматизации тестирования с использованием Selenium и паттерна Page Object Model (POM).

## Инструменты

- Python 3.10
- Selenium
- PyTest
- WebdriverManager

Структура проекта
tests/ - директория с тестовыми файлами
pages/ - директория с классами страниц (Page Object Model)
conftest.py - файл конфигурации для инициализации драйвера

## Установка и настройка

1. Создайте виртуальное окружение:
   ```shell
   python -m venv venv

2. Установите зависимости из файла requirements.txt:
   ```shell
   pip install -r requirements.txt

3. Для запуска тестов используйте команду:
   ```shell
   pytest tests/* --browser_name=firefox
