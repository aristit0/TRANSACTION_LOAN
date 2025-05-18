# 🧾 TRANSACTION_LOAN Streaming Pipeline

This repository contains the configuration and flow for streaming loan transaction data from a MySQL database to a Hive table using Kafka and Debezium CDC.

---

## 📚 Overview

This pipeline enables real-time streaming of `transaction_loan` table changes from a MySQL source into Hive using the following components:

- **MySQL** as the transactional data source
- **Debezium** for capturing change data (CDC)
- **Kafka Connect** for handling source and sink connectors
- **Kafka** as the event transport layer
- **HDFS + Hive** for long-term storage and querying

---

## 🔁 Data Flow

1. **Source: MySQL**
   - The `transaction_loan` table contains raw loan transaction data.

2. **CDC: Debezium + Kafka Connect (Source Connector)**
   - Captures inserts, updates, and deletes in real time.
   - Publishes each change event to a Kafka topic.

3. **Streaming Layer: Apache Kafka**
   - Topic: `transaction_data.transaction.transaction_loan`

4. **Sink: Kafka Connect HDFS Sink**
   - Writes the CDC events from Kafka into HDFS in a structured format (e.g., Avro/Parquet).
   - Integrates with Hive as an external table.

5. **Destination: Hive Table**
   - Table: `stg.transaction_loan`
   - Used for querying and analytical processing.

---

## 📂 Hive Table Schema

> Example structure (optional):

```sql
CREATE EXTERNAL TABLE stg.transaction_loan (
  loan_id STRING,
  customer_id STRING,
  amount DECIMAL(15,2),
  interest_rate DECIMAL(5,2),
  loan_date DATE
)
STORED AS PARQUET
LOCATION 'hdfs:///warehouse/stg/transaction_loan/';