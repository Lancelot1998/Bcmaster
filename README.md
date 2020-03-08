
# Prism
A real-time blockchain monitor and resource-related benchmark tool.<br> 
The current version can conduct the benchmark of eight blockchain projects:<br> 
"""<br> 
* Hyperledger Fabric (v1.1-1.4)<br> 
* Hyperledger Sawtooth<br> 
* Hyperledger Burrow<br> 
* Hyperledger Iroha<br> 
* Ethereum<br> 
* Parity<br> 
* IOTA<br> 
* EOS<br> 
"""<br> 
From the perspective of metrics, Prism currently covers:<br> 
"""<br> 
* Throughput (transactions per second)<br> 
* Transaction confirmation latency (second)<br> 
* Resource Efficiency (CPU, DISK I/O, Network, Memory...)<br> 
"""<br> 
# Description<br> 
This tool is based on docker technology.<br>
The mainly involved images contain cadvisor, prometheus, and grafana.<br> 