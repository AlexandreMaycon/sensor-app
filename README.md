# Sensor App

### Clone repository
```bash
https://github.com/AlexandreMaycon/sensor-app.git
```

### Install the dependencies
```bash
pip install -r requirements.text
```

### Create a .env
**Note:** You need to create a file and set the database infos, exemple:
```bash
HOST=test
USER=test
PASSWORD=test
HOST=test
DATABASE=test
```

### Run project
```bash
python -m uvicorn App.Routes.main:app --reload
```

### DB
**To create the schema and the tables you can find in the directory /sql/**

### Run tests
```bash
python -m unittest discover -s .\tests\Cases -p "test_*.py"
```

### Access doc
http://localhost:8000/docs

### To see the index you use
**Live Server**
