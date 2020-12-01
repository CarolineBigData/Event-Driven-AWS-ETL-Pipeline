import json
import boto3
def lambda_handler(event, context):

    # add your region_name
    glue = boto3.client(service_name='glue', region_name='us-east-1') 
    sns_con_cli = boto3.client(service_name="sns", region_name="us-east-1")
    
    # only 'Name' parameter
    workflow_run_id = glue.start_workflow_run(Name = 'order_data_workflow')
    sns_con_cli.publish(TargetArn="arn:aws:sns:us-east-1:055261340670:Order-Updates", Message="Order dataset has been successfully updated")

    print(f'workflow_run_id: {workflow_run_id}')