# TRANSACTION_LOAN


📌 Transaction Loan - Streaming Pipeline Overview

This pipeline streams loan transaction data from a MySQL source into an HDFS-backed Hive table using Kafka Connect + Debezium for Change Data Capture (CDC).

🔁 Data Flow
	1.	MySQL (Source)
Raw transaction_loan table acts as the CDC source.
	2.	Kafka Connect + Debezium (CDC)
Captures row-level changes and publishes them to a Kafka topic (transaction_data.transaction.transaction_loan).
	3.	Kafka Topic (Intermediate)
Holds CDC events in Avro or JSON format.
	4.	Kafka Sink Connector (HDFS/Hive)
Streams data from the Kafka topic into HDFS and writes into a Hive-managed external table (stg.transaction_loan).