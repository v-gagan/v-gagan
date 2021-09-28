from azure.cosmosdb.table.tableservice import TableService,ListGenerator

table_service_out = TableService(account_name='', account_key='')
table_service_in = TableService(account_name='', account_key='')

#query 100 items per request, in case of consuming too much menory load all data in one time
query_size = 100

#save data to storage2 and check if there is lefted data in current table，if yes recurrence
def queryAndSaveAllDataBySize(tb_name,resp_data:ListGenerator ,table_out:TableService,table_in:TableService,query_size:int):
    for item in resp_data:
        #remove etag and Timestamp appended by table service
        del item.etag
        del item.Timestamp
        print("instet data:" + str(item) + "into table:"+ tb_name)
        table_in.insert_entity(tb_name,item)
    if resp_data.next_marker:
        data = table_out.query_entities(table_name=tb_name,num_results=query_size,marker=resp_data.next_marker)
        queryAndSaveAllDataBySize(tb_name,data,table_out,table_in,query_size)


tbs_out = table_service_out.list_tables()

for tb in tbs_out:
    #create table with same name in storage2
    table_service_in.create_table(tb.name)
    #first query 
    data = table_service_out.query_entities(tb.name,num_results=query_size)
    queryAndSaveAllDataBySize(tb.name,data,table_service_out,table_service_in,query_size)





{
    "value": [
        {
            "id": "",
            "name": "",
            "url": "",
            "description": "",
            "collection": {
                "id": "",
                "name": "",
                "url": "",
                "collectionUrl": ""
            },
            "defaultTeam": {
                "id": "",
                "name": "",
                "url": ""
            }
        },
        {
            "id": "",
            "name": "",
            "url": "",
            "description": "",
            "collection": {
                "id": "",
                "name": "",
                "url": "",
                "collectionUrl": ""
            },
            "defaultTeam": {
                "id": "8bd35c5e-30bb-4834-a0c4-d576ce1b8df7",
                "name": "Fabrikam-Fiber-GitTeam",
                "url": "https://dev.azure.com/fabrikam-fiber-inc/_apis/projects/6ce954b1-ce1f-45d1-b94d-e6bf2464ba2c/teams/8bd35c5e-30bb-4834-a0c4-d576ce1b8df7"
            }
        }
    ],
    "count": 2
}




body = 
[
   { 
     "op": "add", 
     "path": "/fields/System.Title", 
     "from": None, 
     "value": "Sample task"
   },
   {
     "op": "add", 
     "path": "/fields/System.IterationPath",
     "from": None,
     "value": "Labs_TelAviv\Sprint32"
   }
] 









_BATCH_ACCOUNT_NAME = 'mybatchaccount'
_BATCH_ACCOUNT_KEY = ''
_BATCH_ACCOUNT_URL = ''
_STORAGE_ACCOUNT_NAME = ''
_STORAGE_ACCOUNT_KEY = ''



blob_service_client = BlobServiceClient(
        account_url="https://{}.{}/".format(
            config._STORAGE_ACCOUNT_NAME,
            config._STORAGE_ACCOUNT_DOMAIN
        ),
        credential=config._STORAGE_ACCOUNT_KEY
    )


input_file_paths = [os.path.join(sys.path[0], 'taskdata0.txt'),
                    os.path.join(sys.path[0], 'taskdata1.txt'),
                    os.path.join(sys.path[0], 'taskdata2.txt')]

input_files = [
    upload_file_to_container(blob_service_client, input_container_name, file_path)
    for file_path in input_file_paths]








from azure.identity import ClientSecretCredential
from azure.mgmt.subscription import SubscriptionClient

subscription_id = ""
client_id = ""
secret = ""
tenant_id = ""

creds = ClientSecretCredential(client_id=client_id, client_secret=secret,tenant_id=tenant_id)
subscription_client = SubscriptionClient(creds)

locations = subscription_client.subscriptions.list_locations(subscription_id)
for location in locations:
    print(location.name)
