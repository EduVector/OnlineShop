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

## 2. How to pull from (GitHub/GitLab)

### 1. Check the status of your repository
```bash
git status
```

### 2. If you have any changes, commit them (Optional)
```bash
git add .
git commit -m "Your message"
```

### 3. Pull the latest changes from the remote repository
```bash
git pull origin main
```
