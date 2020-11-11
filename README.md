# Iperf 3 QoS Measurement
Testing automation using Iperf3 for QoS measurement.

## How to Use
1. Start `server.sh`.
`./server.sh -p [PORT] -i [INTERVAL] -f [FILENAME] -l [ITERATION]`
2. Start `client.sh`.
For UDP packet.
`./client.sh -s [SERVER_IP] -c udp -p [PORT] -b [BANDWIDTH] -t [TIME] -i [INTERVAL] -l [ITERATION]`
For TCP packet.
`./client.sh -s [SERVER_IP] -p [PORT] -b [BANDWIDTH] -t [TIME] -i [INTERVAL] -l [ITERATION]`

For Iperf documentation, please refers to this!
https://iperf.fr/iperf-doc.php
