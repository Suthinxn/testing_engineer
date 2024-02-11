# Testing case

Basic Testing

**Structure**

```
Project
|
|__ <name>
|    |
|    |__ name.py
|    
|__ Tests
		|__test_name.py
```


## How to install ?
**Windows:**

    pip install coverage nose2

**Linux:**

    pip install coverage nose2

## How to Work?
**Linux:**

    python3 -m unittest -v tests/test_name.py

**OSX:**

    python -m unittest -v tests/test_name.py

**Windows:**

    python -m unittest -v tests/test_name.py

or

    py -m unittest -v tests/test_name.py

## How to test with Coverage

 

    nose2 -v --with-coverage

or

    nose2 -v --with-coverage --coverage-report html

or

    nose2 -v –with-coverage --coverage <package_name>

## Creator
name : Suthinan Rongphon
Student ID : 6610110341

