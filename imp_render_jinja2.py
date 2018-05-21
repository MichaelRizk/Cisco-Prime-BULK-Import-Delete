import jinja2
import os
 
print "\n*************************************************************************"
print " Please Note:\n"
print "'Host IPs to be imported to Prime must separated by comma , with NO spaces'"
print "'Example x.x.x.x,y.y.y.y,z.z.z.z'"
print "'It is your responsibility to make sure the IPs are correct'"
print "**************************************************************************\n"
ip_input = raw_input('Type Host IP/s separated by comma:')


list=ip_input.split(",")
list=[str(a) for a in list]

loader = jinja2.FileSystemLoader(os.getcwd())


jenv = jinja2.Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)

 
template = jenv.get_template('imp_template.j2')



out= template.render(ip_list=list)


#save to file
with open("imp_output.json", "wb") as fh:
   fh.write(out)
