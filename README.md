## О методе

В данной работе представлена реализация метода регуляризации, описанного в статье 

IAN KNOWLES, ROBERT J. RENKA "METHODS FOR NUMERICAL DIFFERENTIATION OF NOISY DATA"

Он позволяет искать производные и их ошибки для зашумленных данных.
Чтобы получить больше информации, смотрите [Differentiation of noisy data](https://ejde.math.txstate.edu/conf-proc/21/k3/knowles.pdf)

## Содержание

В данном репозитории содержатся несколько файлов:

*regularization.py* - основной файл с реализацией метода

*documentation.md* - документация к функциям и переменным файла regularization.py

*example_solar.py* - пример использования метода для построения кинематических кривых корональных выбросов массы для события 25.02.2014

*example_func.py* - пример использования метода на математической функции

## Необходимые библиотеки

Для того, чтобы файл запускался на вашей локальной машине, необходимо установить следующие библиотеки:

+ numpy
+ scipy
+ tqdm

Для установки данных библиотек пропишите в командной строке соответствующие команды:

```python
pip install numpy
pip install scipy
pip install tqdm
```

[!IMPORTANT](Позже здесь появится функция установки этого пакета через pip install)