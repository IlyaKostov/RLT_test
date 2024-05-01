# RLT Test Task

---

Алгоритм агрегации статистических данных о зарплатах сотрудников компании по временным промежуткам.

## Установка проекта

---

Клонируйте репозиторий  

Создайте виртуальную среду  
```bash
python -m venv env
```  

Активируйте виртуальную среду  
На Windows
```bash
.\env\Scripts\activate
```
на Linux
```bash
./env/bin/activate
```


Установите зависимости  
```bash
pip install -r requirements.txt
```

Создать в корне проекта файл .env и внести в него все переменные окружения по образцу из файла .env.sample

Запустите проект  
```bash
python main.py
```

### Стэк

---


- Python 3.11
- Aiogram 3.5
- БД: MongoDB


