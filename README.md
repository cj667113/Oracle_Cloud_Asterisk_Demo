# Oracle_Cloud_Demo

The goal of this demo was to create an Asterisk server configuration in Oracle Cloud, while also making two Web Server avaiable to be load balanced and an MySQL Server to hold username, password and extension numbers. The final configuration looks like:

![Oracle_Cloud_Demo](https://raw.githubusercontent.com/cj667113/Oracle_Cloud_Demo/master/images/Oracle_Cloud_Demo.jpg)

## Apache Servers & Load Balancer
I ran two apache servers with a slightly modified HTML code, so that the differences in the interconnected machines could be apparent when the load balancer connected me to an Apache Server. 

Routing table for the VCN had to be set to allow for internet connectivity.

Security Lists had to be modified so that incoming tcp traffic for port 80 could be recieved by the Apache Servers. Also to note that specific machine firewalls may also need to be modified to accept this traffic as well.

## Asterisk

I wanted to give the demo the ability to register SIP phones to Asterisk Servers. The Asterisk Servers would be interconnected through Local Peering Gateways. This way the registration of SIP trunks would be done over the private VCN subnet, while also letting the users call extensions that are registered to the other Asterisk Servers.

The routing table for the VCNs had to be set to allow for specific subnet traffic to be sent to the appropriate Local Peering Gateways.

Security Lists also had to be modified so that incoming udp traffic could be recieved by the Asterisk Servers. Also to note that specific machine firewalls may also need to be modified to accept this traffic as well. 

It was at this point, that I thought I could demo my python skills. I noticed how much of an annoyance it could be to configure the sip.conf associated with each Asterisk Server. I thought there had to be a better way to automate this task and a better way to store usernames, passwords and extension numbers associated with all of these Asterisk Servers. I decided to demploy a MySQL Database that would allow me to quickly add and remove users. Since I decided to go this route it would make sense to write a python script for the Asterisk Servers that would go out and query the MySQL database. The Servers would then look for a range of extension numbers that were associated with the server, and dynamically build the Asterisk Server's sip.conf file and restart the server.

## MySQL

When building the Mariadb MySQL server, I decided that it would be a good idea to reject all incoming traffic from the public interface except from a few necessary connections. This would secure the server to allow only incoming queries from the VCNs. By making changes to the database, the rest of the Asterisk Servers will reconfigure themselves to reflect the database's changes.
