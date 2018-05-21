import jinja2, os, json

print "\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
print "      >>Warning YOU ARE ABOUT TO DELETE DEVICES FROM CISCO PRIME <<             "
print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
print "\n******************************************************************************"
print " Please Note:\n"
print "'Host IPs to be DELETED from Prime must be separated by comma , with NO spaces'"
print "'Example x.x.x.x,y.y.y.y,z.z.z.z'"
print "'It is your responsibility to make sure the IPs are correct'"
print "*******************************************************************************\n"


ip_input = raw_input('Type Host IP/s separated by comma:')


list=ip_input.split(",")
list=[str(a) for a in list]

loader = jinja2.FileSystemLoader(os.getcwd())


jenv = jinja2.Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)

 
template = jenv.get_template('del_data.j2')

list = json.dumps(list)

out= template.render(ip_list=list)


#save to file
with open("del_output.json", "wb") as fh:
   fh.write(out)
