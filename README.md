# Автотесты для сайта hh.ru

[hh.ru](https://hh.ru/)
![img_1.png](img/hh.png)

## Особенности проекта

- Запуск web UI автотестов в Selenoid
- Сборка проекта в Jenkins
- Отчеты Allure Report
- Оповещения о тестовых прогонах в Telegram
- Отчеты с видео, скриншотом, логами, исходной моделью разметки страницы


## Список проверок, реализованных в web UI автотестах
- Выбор города
- Поиск работы
- Поиск резюме
- Поиск компании
- Проверка выполненых задач
## Используемый стэк

![img_2.png](img_2.png)
![img_1.png](img_1.png)
![img.png](img/img.png)
![img_2.png](img/img_22.png)
![img_3.png](img/img_3.png)
![img_1.png](img/img_1.png)

## Запуск тестов из терминала
### Для запуска всех автотестов выполнить в cli:
> python -m venv .venv  
> source .venv/bin/activate   
> pip install -r requirements.txt   
> pytest .

### Получение отчета allure:
> allure serve allure-results
> 
> 
## Проект в Jenkins
[Jekins](https://jenkins.autotests.cloud/job/hw_14_python_/)


### Запуск автотестов в Jenkins:
1. Открыть проект в [Jekins](https://jenkins.autotests.cloud/job/hw_14_python_/)


2. Нажать кпопку ![img_1.png](img/bn.png)


## [Allure отчет](https://jenkins.autotests.cloud/job/hw_14_python_/13/allure/)

![img.png](img/allure.png)


### [Результат прохождения теста](https://jenkins.autotests.cloud/job/hw_14_python_/13/allure/#suites)
![img.png](img/allure2.png)

## [Оповещения в Telegram](https://ru.wikipedia.org/wiki/Telegram)
![img.png](img/telegram.png)

## [Видео прохождения автотестов](https://selenoid.autotests.cloud/video/93ce3d0fe17922d2d1efc4071cda460d.mp4)
<img title="Selenoid" src="img/sc.gif"/>



 