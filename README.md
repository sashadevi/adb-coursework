# adb-coursework

## Prerequisits 

This application requires PostgreSQL and Python for it to work. Please make sure that both of these are installed before using the application.

## Installation

Use Python's package manager [pip](https://pip.pypa.io/en/stable/) (or pip3 depending on Python version) to install the package [psycopg2](https://pypi.org/project/psycopg2/)


```bash
pip3 install psycopg2-binary
```

## Setting up databases and importing data into tables

Run the file setup.py (in the root directory) to connect and create the database:

```bash
python3 setup.py
```

Note: you may need to specify the user, password, host and port number by editing the setup.py file as follows:

```python
user=<username>, password=<password>, host=<hostname>, port=<portnumber>
```