# Event-Driven-AWS-ETL-Pipeline

# Overview

In this project, I have built a serverless architecture to analyze the data directly from Amazon S3 using Amazon Athena and visualize the data in Amazon QuickSight. The data comes from Kaggle: https://www.kaggle.com/olistbr/brazilian-ecommerce?select=olist_order_items_dataset.csv. 

In this project, I have built a serverless architecture to analyze the data directly from Amazon S3 using Amazon Athena and visualize the data in Amazon QuickSight.

In the first part of this project is to build an automatically data pipeline. First, when new data drop in the raw bucket, the pipeline will automatically perform ETL process, that transferring the raw data from CSV to parquet and convert some string type columns into timestamp, the data will be stored in the processed data bucket. and  I loaded the processed data into Redshift. When the. whole ETL workflow success, I got the notification from Amazon SNS.

In the second part of the project, I used Amazon QuickSight to generate visualizations and meaningful insights from the processed data bucketS3 using Athena tables that I created in Glue. and I directly queried the same dataset in Amazon S3 from an Amazon Redshift data warehouse using Redshift Spectrum.

![github-small](https://user-images.githubusercontent.com/58568024/100687733-d3465680-334e-11eb-9c2b-f97e1f665763.png)

# resources

1. Three S3 buckets to store the following:
* AWS Glue ETL job script
* Raw data
* Processed data
2. One Lambda functions to do the following:
* Initiate the ETL workflow upon upload of new data in the raw zone
3. An AWS Glue database
4. Two AWS Glue tables to store the following:
* Raw data
* Processed data
5. Two ETL jobs 
* convert the raw data from CSV into Apache Parquet format 
* load data into Redshift
6. One SNS topic to notify when the data sucessfully load into redshift
7. One QuickSight Analysis
8. One external table in Redshift Spectrum for query 
