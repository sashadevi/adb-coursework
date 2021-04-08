# adb-coursework

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) (or pip3 depending on Python version) to install the package [psycopg2](https://pypi.org/project/psycopg2/)

If there is an error you may have to install it by running:

```bash 
sudo apt install libpq-dev python3-dev
```

Then run 

```bash
pip3 install psycopg2
```

## Setting up databases and importing data into tables

Run the file setup.py (in the root directory) to connect and create the database by running:

```bash
python3 setup.py
```

Note: you may need to specify the user, password, host and port port number by editing the setup.py file as follows:

```python
user=<username>, password=<password>, host=<hostname>, port=<portnumber>
```