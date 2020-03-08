# Prism
A real-time blockchain monitor and resource-related benchmark tool.<br> 
The current version can conduct the benchmark of eight blockchain projects:

"""
Hyperledger Fabric (v1.1-1.4)

Hyperledger Sawtooth

Hyperledger Burrow

Hyperledger Iroha

Ethereum

Parity

IOTA

EOS
"""

From the perspective of metrics, Prism currently covers:
"""
Throughput (transactions per second)

Transaction confirmation latency (second)

Resource Efficiency (CPU, DISK I/O, Network, Memory...)
"""

# Description
This tool is based on docker technology.

The mainly involved images contain cadvisor, prometheus, and grafana.
