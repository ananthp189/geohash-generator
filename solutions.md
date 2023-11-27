# Aize technical task solutions

## Implementation

The solution for the problem statement has been shared as a python file  `geohash_generateor.py`, along with a `README.md` file. The same can also be found on [github](https://github.com/ananthp189/geohash-generator). The solution uses the open source libraries pandas, numpy and geohash.


## Architecture Design

How would you host and deploy a service for that solution? You can target any cloud provider service.

1) Prepare the Code:
Ensure the code is structured appropriately for deployment. Ensure that all dependencies are listed in a requirements.txt file.
2) Azure App Service:
Create an Azure App Service within appropriate resource group and subscription where the Python service will run.
3) Deploy the Code:
Deploy the code to Azure App Service using Github triggered deploy.
4) Configure Application Settings:
Review and set necessary environment variables and configuration settings in the Azure portal or using CLI . Including the scaling parameters , Triggering mechanisms etc.

Explain the design and any choices/assumptions you've made.

 This design provides a scalable and serverless architecture suitable for the service. Adjustments can be made based on specific requirements and constraints. The service reads the CSV file from Azure Blob Storage, transforms it, and returns the transformed CSV file to the client(another blob). Here is a high level design diagram and the assumptions made .
 
![solution.png](https://www.dropbox.com/scl/fi/vgv6xq04hp68c4jfw3ozh/solution.png?rlkey=jn17cy9l85uv3og0dn3f9f13z&dl=0&raw=1)

The python code is hosted on an azure function, its computational capabilities are configurable using azure portal/CLI. The csv file is input through a blob storage. The API and all resource management is handled  by azure and the solution is triggered using a blob trigger whenever a new csv file is added. When triggered , it takes in the new csv file , transforms it and stores it in the output blob storage.
 
Assumptions:
- Both source and target are assumed in this design and are same (azure blob storage chosen for simplicity).
- Azure account, subscriptions and costs are pre-approved . Manageability and ease of deployment was considered.
- The trigger mechanism for the service is assumed for simplicity to be from a blob trigger and to be in the form of a new csv file.
- the service needs mimimal resources for computing the geohash. The solution can be stateless and needs to store only the deduplicated unique geohashes for the coordinates.

## Evolution proposal

You are later asked to add a "[change data capture](https://en.wikipedia.org/wiki/Change_data_capture)" service in addition to the geohashing one.

Explain how you would design such a service, as you would in a technical proposal meeting with your coworkers.

To design a CDC service for above solution , We would need to focus in further on the objectives by discussing:
- The  types of changes in the source system to capture for a better understanding of the requirements. whether new files are added or existing files are updated?
- What triggers need to be fired on detecting these changes and what are the target systems. 
- Any existing CDC of choice like event grids to trigger azure function or any logs , metadata ,etc that are capturing the changes for the objective.  Consider  systems like apache HUDI (open source) and delta lake.
- Consider how the transformation logic will hold in various scenarios. 

These discussions will help in designing the CDC, and validate the use of event hub, azure function triggers ,data factory and appropriate capturing to be done for the changes detected.

In particular for the solution mentioned above, we could proceed with :
1) Azure Blob Storage with Event Grid/Hub : Utilize Azure Blob Storage as the data source to enable Event Grid on the storage account to capture events for blob changes.
2) Implementing an azure function to process change events, enable logging , monitoring triggered by Event Hub and subsequent storage of change data onto chosen target system.


## We value in the solution

- good software design
- use of data structures
- compliance with Python standards and modern usages
- instructions/documentation
- drawings/illustrations
