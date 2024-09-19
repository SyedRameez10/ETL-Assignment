# **ETL Pipeline using Python and PostgreSQL**

## **Overview**

This project implements a simple ETL (Extract, Transform, Load) pipeline using Python and PostgreSQL. It reads data from an Excel file, cleans and transforms the data, and loads it into a PostgreSQL database. 

## **Features**

### **Extract:** Reads data from a CSV or Excel file.
### **Transform:** Cleans the data, splits addresses into parts (house number, city, state, zip code), and sorts the data.
### **Load:** Loads the cleaned and transformed data into a PostgreSQL table.

## **Requirements**

To run this project, you will need the following:

- Python 3.x
* PostgreSQL
+ Required Python packages (listed in requirements.txt):
    - pandas 
    - openpyxl 
    - psycopg2 

## **Installation**

### Clone the repository:

git clone ``` https://github.com/SyedRameez10/ETL-Assignment.git ```

### **Install Python dependencies:**

Use the ```requirements.txt``` file to install the required Python packages:

``` pip install -r requirements.txt ```

### **Set up PostgreSQL:**

Ensure PostgreSQL is installed and running.
Create a new database.

### **Run the ETL pipeline**:
In your terminal, navigate to the project directory and run:

``` python main.py ```
