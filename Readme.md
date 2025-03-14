
## 가상 환경 
```
python -m venv venv
```

### 가상 환경 실행 
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

```
.\venv\Scripts\activate
```

## pip install
```
pip install Django django-filter djangorestframework Markdown 
```

### django project 생성
```
django-admin startproject config .
```


### django 실행
```
python manage.py runserver
```