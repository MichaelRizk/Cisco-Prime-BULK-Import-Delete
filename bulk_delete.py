
import urllib3, requests, json, time
from getpass import getpass
from requests.auth import HTTPBasicAuth





#disable Cert warning, not a best Practice 
urllib3.disable_warnings()


print
print
# Request user API Credentials
api_user=raw_input('Enter API usr:')
api_pwd= getpass()

# Load Json template generator script
import del_render_jinja2
data = json.load(open('del_output.json'))

# Remove PRIME-SERVER and add a working hostname or IP address
url = 'https://PRIME-SERVER/webacs/api/v2/op/devices/deleteDevices.json'

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

  
# by practice i found that Prime will need sometime to add the delete Job  
print "\nDeleteing IPs from Prime .....please wait "
time.sleep(10)
   
##Show Prime API response in a cleaner way
job_status = r_json['mgmtResponse']['deleteDeviceResult'][0]['deleteStatuses']['deleteStatus']
 
print "\n=================================================="
print " Bulk Delete Job Status:"
print "-----------------------------\n"
for item in job_status:
    for key, value in item.items():
            print str(key)+':'+str(value)
print "\n===================================================\n"
print "\n---------- End of script ----------"








