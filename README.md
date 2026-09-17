# Selenium SauceDemo UI Tests

Проект автоматизированного UI-тестирования интернет-магазина
[SauceDemo](https://www.saucedemo.com/) на Python.

## Технологии

- Python
- Selenium WebDriver
- Pytest
- Page Object Model
- Google Chrome

## Что проверяют тесты

- успешная авторизация;
- авторизация с неправильными данными;
- блокировка пользователя;
- отображение товаров;
- добавление товаров в корзину;
- удаление товара из корзины;
- сортировка товаров по цене;
- проверка обязательных полей заказа;
- успешное оформление заказа;
- выход из аккаунта.

## Структура проекта

```text
selenium-saucedemo-tests/
├── pages/
│   ├── locators.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Установка

Клонировать репозиторий:

```bash
git clone https://github.com/Olesia2001/selenium-saucedemo-ui-tests.git
cd selenium-saucedemo-tests
```

Создать виртуальное окружение:

```bash
python -m venv venv
```

Активировать его в Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

## Запуск тестов

Запустить все тесты:

```bash
pytest -v
```

Запустить только smoke-тесты:

```bash
pytest -m smoke -v
```

Запустить регрессионные тесты:

```bash
pytest -m regression -v
```

Запустить конкретный тест:

```bash
pytest tests/test_login.py::test_successful_login -v
```

## Скриншоты при падении

Если тест падает, скриншот автоматически сохраняется в папке:

```text
screenshots/
```