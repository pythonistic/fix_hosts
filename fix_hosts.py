#!/usr/bin/env python3

import re

pattern = re.compile(r"lease ([0-9.]+) {.*?client\-hostname \"(.+?)\";.*?}", re.MULTILINE | re.DOTALL)
hosts = {}

with open("/var/lib/dhcp/dhcpd.leases", "r") as lease_file:
    leases = lease_file.read()
    
    for match in pattern.finditer(leases):
        hosts[match.group(1)] = match.group(2)

hosts_base = ""
with open("/etc/hosts.base", "r") as hosts_base_file:
    hosts_base = hosts_base_file.read()

with open("/etc/hosts", "w") as hosts_file:
    hosts_file.write("# DO NOT MODIFY\n# Change /etc/hosts.base to make changes to this file.\n\n")	
    hosts_file.write(hosts_base)
    hosts_file.write("\n\n# DHCPD lease hostnames\n")
    for (ip, hostname) in hosts.items():
        hosts_file.write("%s\t%s\n" % (ip, hostname))

