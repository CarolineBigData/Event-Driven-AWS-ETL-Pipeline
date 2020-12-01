# Event-Driven-AWS-ETL-Pipeline

# Overview

In this project, I have built a serverless architecture to analyze the data directly from Amazon S3 using Amazon Athena and visualize the data in Amazon QuickSight. The data comes from Kaggle: https://www.kaggle.com/olistbr/brazilian-ecommerce?select=olist_order_items_dataset.csv. 

In the first part of this project is to build a automatically data pripeline. First, when new data drop in the raw bucket, the pipleline will automatically perform etl process, that transferring the raw data from csv to parquet and convert some string type columns into timestamp, the data will be stored in the processed data bucket. Second, it will load the processed data into Redshift.  

In the second part of the lab, you will use Amazon QuickSight to generate visualizations and meaningful insights from the data set in Amazon S3 using Athena tables you create during the first part of the lab. or you can directly query the same dataset in Amazon S3 from an Amazon Redshift data warehouse using Redshift Spectrum.

![github-small](https://user-images.githubusercontent.com/58568024/100686927-4fd83580-334d-11eb-9725-409262a52e39.png)
