
import urllib3, requests, json, time
from getpass import getpass
from requests.auth import HTTPBasicAuth





#disable Cert warning 
urllib3.disable_warnings()

print
print
# Request user API Credentials
api_user=raw_input('Enter API usr:')
api_pwd= getpass()

# Load Json template generator script
import imp_render_jinja2
data = json.load(open('imp_output.json'))

# Remove PRIME-SERVER and add a working hostname or IP address
url = 'https://PRIME-SERVER/webacs/api/v3/op/devices/bulkImport.json'

headers = {"Content-Type": "application/json"}


#Call REST API resource
response = requests.put(url, data=json.dumps(data), auth=HTTPBasicAuth(api_user, api_pwd), headers=headers, verify=False)

    
# Assuming Prime is up 99.9% most of the time Any Error will throw same output which is most likely Auth issue, if you have time you can customize it    
try:
   # decode response as json   
   r_json=response.json()
except  ValueError:
    print "\n----- Error -----\n"    
    print "---- AUTH FAILED ----" 
    print "\n--- End of script ---"    
    exit(0)

    
print "\nImporting IPs to Prime .....please wait "
    
#Show Prime API response in a cleaner way
job_status = r_json['mgmtResponse']['bulkImportResult'][0]['message']
 
job_name = r_json['mgmtResponse']['bulkImportResult'][0]['jobName']

print "\n=================================================="
print " Import Job Creation Result:"
print "-----------------------------\n"
print " job_name: %s " % (job_name) 
print " job_status: %s " % (job_status) 
print "===================================================\n"
print "\n Fetching Job Execution Result....\n"

# by practice i found that Prime will need sometime to add the Import Job  
time.sleep(10)
print "\n Fetching Job Execution Result.... please wait\n"

time.sleep(10)
print "\n please wait .....\n"

time.sleep(10)

# Remove PRIME-SERVER and add a working hostname or IP address
resource_url = "https://PRIME-SERVER/webacs/api/v3/op/jobService/runhistory.json?jobName="#url= resource_url+job_name
url= resource_url+job_name
response = requests.get(url, auth=HTTPBasicAuth(api_user, api_pwd), verify=False)
js_json=response.json()


# Filter out specific data from API Response
resultStatus = json.dumps(js_json['mgmtResponse']['job'][0]['runInstances']['runInstance'][0]['resultStatus'])
completionTime = json.dumps(js_json['mgmtResponse']['job'][0]['runInstances']['runInstance'][0]['completionTime']) 


 
if resultStatus == '"FAILURE"':
     value = json.dumps(js_json['mgmtResponse']['job'][0]['runInstances']['runInstance'][0]['results']['result'][0]['value'])    
     print "===================   Error   ======================"
     print " Import Job Execution Result:"
     print "-----------------------------\n"
     print "Job resultStatus: %s" % resultStatus  
     print "Job Failure reason: %s" % value
     print "Job Failed Time: %s" % completionTime
     print "\==================   Error   ======================\n"

elif resultStatus == '"PARTIALSUCCESS"':
     print "===================   Error   ======================"
     print " Import Job Execution Result:"
     print "-----------------------------\n"
     print "Job resultStatus: %s" % resultStatus
     print "Job Failure reason: Wrong entry detected"
     print "Job Failed Time: %s" % completionTime
     print "===================   Error   ======================\n"  
else:
     print "\n=================================================="
     print " Import Job Execution Result:"
     print "-----------------------------\n"
     print "Job resultStatus: %s" % resultStatus
     print "Job completion Time: %s" % completionTime
     print "===================================================\n"
     
print "---------- End of script -----------"
