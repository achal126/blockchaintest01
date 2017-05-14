from hyperledger.client import Client
import time

def deploy_chaincode():
    c = Client(base_url="http://192.168.33.10:7050")
    deploy = c.chaincode_deploy()
    print "Chain code is being deployed"
    time.sleep(30)
    if deploy['result']['status']=='Ok':
        return deploy['result']['message']
    else:
        return deploy['result']['status'] + "is the error"

def query_chaincode(chaincode_name, WineID):
    c = Client(base_url="http://192.168.33.10:7050")
    query=c.chaincode_query(chaincode_name=chaincode_name,function="GetWineInfo", args=[WineID])
    print query
    return query['result']['status'], query['result']['message']

def invoke_chaincode(chaincode_name, function, WineID, OwnerInfo):
    c = Client(base_url="http://192.168.33.10:7050")
    invoke=c.chaincode_invoke(chaincode_name=chaincode_name, function=function, args=[WineID,OwnerInfo])
    return invoke['result']['status']


