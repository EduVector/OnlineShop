# Online Shop

### 1. How to install (Windows / Linux / Mac)

```bash
git clone https://github.com/edu-vector/OnlineShop.git
```

### 2. Create virtual environment

```bash
py -m venv venv
```

### 3. Install Python libraries from requirements.txt
```bash
pip install -r requirements.txt
```

### 4. Set migrations
```bash
py manage.py makemigrations
py manage.py migrate
```

### 5. Create Superuser
```bash
py manage.py createsuperuser
```

### 6. Run project on your localhost
```bash
py manage.py runserver
```
