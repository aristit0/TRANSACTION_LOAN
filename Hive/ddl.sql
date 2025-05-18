CREATE EXTERNAL TABLE `transaction`.`transaction_loan`(
`loan_id` bigint COMMENT 'from deserializer',
`customer_id` string COMMENT 'from deserializer',
`loan_amount` string COMMENT 'from deserializer',
`interest_rate` string COMMENT 'from deserializer',
`loan_term_months` int COMMENT 'from deserializer',
`loan_status` string COMMENT 'from deserializer',
`issued_date` bigint COMMENT 'from deserializer',
`updated_at` string COMMENT 'from deserializer')
ROW FORMAT SERDE
'org.apache.hive.hcatalog.data.JsonSerDe'
STORED AS INPUTFORMAT
'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
'hdfs://cloudeka-hdfs/warehouse/tablespace/external/hive/transaction.db/transaction.transaction.transaction_loan'
TBLPROPERTIES (
'bucketing_version'='2',
'transient_lastDdlTime'='1747322364')
