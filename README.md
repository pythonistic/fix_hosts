# fix_hosts
Assign DHCPD client-hostname entries to /etc/hosts

## Problem
I use a program, [bandwidthd](http://freecode.com/projects/bandwidthd), to keep track of my bandwidth usage and see what's happening
on my home network.  It pulls IP addresses from `/etc/hosts` -- but if the host isn't there, the graph will indicate you need to
configure the hostname.

Since I'm not currently running DNS or dnsmasq, but I am running `dhcpd`, I neeeded some way to put the self-assigned client names
in my `/etc/hosts` file.

## Operation
Running as a cron job, `fix_hosts.py` will parse the `/var/lib/dhcp/dhcpd.leases` file, pull out the IP address and `client-hostname`
associations, and append them to a base copy of `/etc/hosts`.

This script requires root permissions to run.

## Requirements

* Python 3.x
* /usr/bin/env
* dhcpd (or the equivalent)

## Installation
1. Copy the script into a convenient location.
2. Modify the script, if required.

   The script expects your leases to be `/var/lib/dhcp/dhcpd.leases` and your hosts file in `/etc/hosts`.

3. Create a `/etc/hosts.base` file.

   ```bash
   sudo cp /etc/hosts /etc/hosts.base
   ```

4. Add a cron entry for fix_hosts.py

   I added mine to `/etc/cron.d`

   ```
   SHELL=/bin/sh
   PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

   */5 * * * *   root	/path/to/fix_hosts.py
   ```

