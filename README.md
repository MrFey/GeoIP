geoip is a simple command line tool that uses ipinfo.io's public API to get informations on public IP address. Basically geoip retrieves localisation informations. 

This is Open source code feel free to modify and distribute it since you don't disturb ipinfo.io.

NB: This is not a ipinfo.io tool. GeoIP just uses their API.

<h3> Set up </h3>

~$ git clone https://github.com/MrFey/GeoIP.git <br>
~$ cd ./GeoIP
~$ ./setup.sh

<h3> UsaGeoIPge </h3>

./geoip "IPv4 address"

<h3> Example </h3>
~$ ./geoip XXX.XXX.XXX.XXX <br>
[*] IP address XXX.XXX.XXX.XXX is located:<br>
[+] country:  Germany<br>
[+] region:  Bavaria<br>
[+] postal code:  88131<br>
[+] city:  Lindau<br>
