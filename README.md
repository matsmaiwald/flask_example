# Minimal example of a flask app
## Set up

1. Clone the repo
```
git clone git@github.com:matsmaiwald/flask_example.git
```

2. Create a virtual environment
```
python3 -m venv flask_example_env
```

3. Activate the virtual environment
```
source flask_example_env/bin/activate
```

4. Install the required packages
```
pip install -r requirements.txt
```

5. Tell flask where the app is located
```
export FLASK_APP=app.py
```

## Run the app
```
flask run
```

## Run a script that calls the app
In a new terminal window
```
python3 client.py
```