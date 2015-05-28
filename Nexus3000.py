# Python
#Example of using python  Cisco api on nexus 3000.
#Bwahrmann 5-2015

#import cisco modules 

import cisco

# The cisco module must be called in order to use the CLI class "cisco.CLI" = module.class
# displaying router info
host = cisco.cli('show run | i hostname')
processor = cisco.cli('show version | i Processor')
kick = cisco.cli('show version | i kickstart',)



print "\nRouter info :\n%s%s%s\n\n" %(host, processor, kick)

# display boot flash

print "Bootflash Info:\n"
dirboot = cisco.cli('dir bootflash:','do_print')


print "****************************************************************\n\n"
print " Start of file transfer"
# file transfer script 
tsf = cisco.transfer(protocol='tftp', host='10.255.40.101', source='/SDN/SDN_Programming_Fundamentals/ftp/n3000-uk9.6.0.2.U3.7.bin_sdnclass02', dest='bootflash:n3000-uk9.6.0.2.U3.7.bin_sdnclass02', vrf='management', login_timeout=10, user='sdnclass', password='Educ@te!')

#verify file in bootflash: 
print "Bootflash Info:\n"
dirboot = cisco.cli('dir bootflash:n3000-uk9.6.0.2.U3.7.bin_sdnclass02','do_print')

#editing configuration 


def vlan1025(vlan, interface):
    print "****************************************************************\n\n"
    print " Now we will examine the interface configuration and update it."

    router_int  = cisco.CLI('show int eth1/25', do_print = False) #Gather tuple withj interface config
    router_int = router_int.get_output()
    router_vlan = cisco.CLI('show int vlan 1025', do_print = False)
    router_vlan = router_vlan.get_output()
    intmsg = router_int[0:1] #taking first slice of tuple which includes interface name
    vlmsg  = router_vlan[0:1]
    for word in intmsg:


        if interface in word:
            print "This is the current interface snapshot:\n\n"
            cisco.CLI("show run interface Ethernet1/25")

            print "The configuration will now be modified:\n\n"
            print "......................................\n\n"


            cisco.CLI("conf t ; interface Ethernet1/25 ; description bw_sdnclass02_vlan_1025")
            cisco.CLI("conf t ; interface Ethernet1/25 ; switchport mode access ; switchport access vlan 1025")
            print "This is the updated interface snapshot:\n\n"
            cisco.CLI('show run interface Ethernet1/25')

    for word in vlmsg:


        if vlan in word:
            print "This is the current VLAN interface snapshot:\n\n"
            cisco.CLI("show run interface Vlan1025")

            print "The configuration will now be modified:\n\n"
            print "......................................\n\n"


            cisco.CLI("conf t ; interface Vlan1025 ; description bw_sdnclass02_vlan_1025")

            print "This is the updated interface snapshot:\n\n"
			cisco.CLI("show run interface Vlan1025")
vlan1025("Vlan1025", "Ethernet1/25 ")







