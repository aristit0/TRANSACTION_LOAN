import mysql.connector
from faker import Faker
import random
import time

fake = Faker()

conn = mysql.connector.connect(
    host='cdpm1.cloudeka.ai',
    user='cloudera',
    password='Admin123',
    database='transaction'
)

cursor = conn.cursor()

def insert_loan():
    customer_id = fake.uuid4()
    loan_amount = round(random.uniform(5000, 100000), 2)
    interest_rate = round(random.uniform(1.5, 10.0), 2)
    loan_term = random.choice([12, 24, 36, 60])
    status = random.choice(["approved", "pending", "rejected", "paid"])
    issued_date = fake.date_time_between(start_date='-2y', end_date='now')

    sql = """
    INSERT INTO transaction_loan (customer_id, loan_amount, interest_rate, loan_term_months, loan_status, issued_date)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (customer_id, loan_amount, interest_rate, loan_term, status, issued_date)
    cursor.execute(sql, values)
    conn.commit()

for i in range(1000000):
    insert_loan()
    print(f"Inserted record {i + 1}")
    time.sleep(1)  # 5-second delay