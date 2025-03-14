
## 가상 환경 
> venv명령어를 통한 가상환경 셋팅입니다. 
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


### App 생성 

```
python manage.py startapp todo
```

### DB 생성 (반영) migrate  
```
python .\manage.py makemigrations
python manage.py migrate   
```

#### Admin 페이지 제작
```
python manage.py createsuperuser
```
