import boto3
from datetime import datetime

ec2 = boto3.client('ec2')

def stop_ec2_instances(instance_ids):
    """
    Stop EC2s instances by IDs
    """
    try:
        print(f"{datetime.now()} - Stopping instances: {instance_ids}")
        ec2.stop_instances(InstanceIds=instance_ids)
        print("Instances stopped successfully.")
    except Exception as e:
        print(f"Error stopping instances: {str(e)}")


def start_ec2_instances(instance_ids):
    """
    Starting EC2s
    """
    try:
        print(f"{datetime.now()} - Starting instances: {instance_ids}")
        ec2.start_instances(InstanceIds=instance_ids)
        print("Instances started successfully.")
    except Exception as e:
        print(f"Error starting instances: {str(e)}")


# Check the status after actions
def check_instance_status(instance_ids):
    response = ec2.describe_instances(InstanceIds=instance_ids)
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instance ID: {instance['InstanceId']} - State: {instance['State']['Name']}")


check_instance_status(instance_ids_to_stop)
check_instance_status(instance_ids_to_start)

def schedule_operations():

    instance_ids = ['ec2-00000000000000000', 'ec2-00000000000000000']

    current_hour = datetime.now().hour

    if current_hour == 18:
        stop_ec2_instances(instance_ids)
    elif current_hour == 6:
        start_ec2_instances(instance_ids)
    else:
        print(f"{datetime.now()} - No action needed. Current hour: {current_hour}")


if __name__ == "__main__":
    schedule_operations()
