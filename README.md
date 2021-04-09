# adb-coursework

This application compares crime data during January 2021 for the West Midlands and Cambridge. 

## Prerequisites

To run the application PostgreSQL and Python need to be installed.

## Installation

Use Python's package manager [pip](https://pip.pypa.io/en/stable/) (or pip3 depending on Python version) to install the package [psycopg2](https://pypi.org/project/psycopg2/)


```bash
pip3 install psycopg2-binary
```

## Setting up a database and importing datasets into a table

Navigate to the root directory of the project and run the file setup.py. This creates and connects to the database, and creates a table. The police datasets for the West Midlands and Cambridge are then imported into the table.

```bash
python3 setup.py
```

Note: You may need to specify the user, password, host and port number to establish a connection toby editing the setup.py file as follows:

```python
user=<username>, password=<password>, host=<hostname>, port=<portnumber>
```
## Starting the application

To start the application, run the following command in the root directory of the project:

```python
python3 main.py
```
## Using the application

Once the application is running, 


## Stopping the application

Press ```q ``` to quit the application
