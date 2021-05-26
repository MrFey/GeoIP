<img width="300" src="http://fey.toile-libre.org/ip-loc.png"></img>

GeoIP is a simple command line tool that uses ipinfo.io's public API to get informations on public IP address. Basically geoip retrieves localisation informations. 

This is Open source code. Feel free to modify and distribute it while you don't disturb ipinfo.io.

<h3> Set up </h3>

git clone https://github.com/MrFey/GeoIP.git <br>
cd ./GeoIP <br>
./setup.sh <br>

<h3> UsaGeoIPge </h3>

./geoip.py "IPv4 address"

<h3> Example </h3>
~$ ./geoip.py XXX.XXX.XXX.XXX <br>
[*] IP address XXX.XXX.XXX.XXX is located:<br>
[+] country:  Germany<br>
[+] region:  Bavaria<br>
[+] zip code:  88131<br>
[+] city:  Lindau<br>
