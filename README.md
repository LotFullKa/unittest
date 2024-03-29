### src
В папке src храняться несколько структур, которые вам нужно закончить реализовывать

### tests
В папке test храняться тесты кесы
```
tests:
--> TestCalculator.py
    --> TestCalculator (test suite)
        --> test_add (test case)
        --> test_div (test case)
--> TestGeometry.py
    --> TestPoint (test suite)
        --> test_init (test case)
        --> test_str (test case)    
```

# Запуск тестов
У unittest есть удобный интерфейс запуска тестов из командной строки.

1. Можно запускать отдельные тесты (из корня проекта)
    
    ```python -m unittest tests/test_geometry.py```
2. Можно запустить поиск всех тестов

    ```python -m unittest discover tests```

## Mock 
Иногда при тестировании функционала нам требуется контролируемый ответ от серды исполнения.
Для таких целей существует `Mock` (см. tests/test_geometry.py)


## Покрытие кода
Для оценки покрытия кода в unittest мы будем использовать `nose`
    
    sudo apt install python3-nose
    pip install coverage

Для того чтобы узнать процент покрытия проекта тестами

    nosetests3 --with-coverage --cover-erase
