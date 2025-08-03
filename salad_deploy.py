import os
from datetime import datetime
from zoneinfo import ZoneInfo
import argparse
from salad_cloud_sdk import SaladCloudSdk
from salad_cloud_sdk.models import ContainerGroupCreationRequest
from dotenv import load_dotenv
load_dotenv()

# SaladCloud parameters
SALAD_API_KEY        = os.getenv("SALAD_API_KEY")
ORGANIZATION_NAME    = os.getenv("ORGANIZATION_NAME")
PROJECT_NAME         = os.getenv("PROJECT_NAME")
IMAGE_NAME           = os.getenv("IMAGE_NAME_TAG")
TAG                  = IMAGE_NAME.split(":")[-1] 

########################################
########################################

def deploy():

     # Extract the tag from the image name

    print("-----> Image and Tag")
    print(IMAGE_NAME,TAG)

    sdk = SaladCloudSdk(
        api_key=SALAD_API_KEY, 
        timeout=10000
    )

    request_body = ContainerGroupCreationRequest(
                name=TAG,        
                display_name=TAG,
                container={
                    "image": IMAGE_NAME,
                    "resources": {
                        "cpu": 16,
                        "memory": 24576,
                        "gpu_classes": ['ed563892-aacd-40f5-80b7-90c9be6c759b', # 4090 - 20GB
                                        '0d062939-7c01-4aae-a2b1-30e315124e51', # 4080 - 16GB
                                        'f1380143-51cd-4bad-80cb-1f86ee6b49fe', # 4070 Ti Super - 16GB
                                        'de00c90b-904b-4d9e-8fc9-1d9a08eb0932', # 4070 Ti - 12 GB
                                        '2b73eef8-be49-4667-8fc0-5c0cb127cfe0', # 4060 Ti - 16GB
                                       ],
                        "storage_amount": 53687091200,
                   },  # 50 GB
    
                   #"command": ['sh', '-c', 'sleep infinity' ],
       
                  "priority": "high",
                  "environment_variables": {}
                  
                },
                autostart_policy=True,
                restart_policy="always",
                replicas=1,
                country_codes=["us","ca","mx"   ],
                networking = {
                  "protocol": "http",
                  "port": 8888,
                  "auth": False,
                  "load_balancer": "least_number_of_connections",
                  "single_connection_limit": False,
                  "client_request_timeout": 100000,
                  "server_response_timeout": 100000
           },
       )

    print("-----> Request")
    print(request_body)


    result = sdk.container_groups.create_container_group(
                request_body=request_body,
                organization_name=ORGANIZATION_NAME,
                project_name=PROJECT_NAME
        )
    print(result)


if __name__ == "__main__":

    deploy()