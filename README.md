# BCmaster (Prism)
A real-time blockchain monitor and comprehensive analyzing tool.<br> 
The current version can conduct the benchmark of `eight` blockchain projects:<br> 
* **Hyperledger Fabric (v1.1-1.4)**<br> 
* **Hyperledger Sawtooth**<br> 
* **Hyperledger Burrow**<br> 
* **Hyperledger Iroha**<br> 
* **Ethereum**<br> 
* **Parity**<br> 
* **IOTA**<br> 
* **EOS**<br> 

From the perspective of metrics, Prism currently covers:<br> 
* **Throughput** (transactions per second)<br> 
* **Transaction confirmation latency** (second)<br> 
* **Resource Efficiency** (CPU, DISK I/O, Network, Memory, Power...)<br> 
* **Stability** (From both peer-level and network-level)<br> 
* **Security Level** (Under Sybil attacks and DDoS attacks)<br> 
* **Interactivity** (Data processing and encryption)<br> 

# Description<br> 
This tool is based on docker technology.<br>
The mainly involved images contain cadvisor, prometheus, and grafana.<br> 
The data flow is `cadvisor` to `Prometheus` to `Grafana`, which is a famous framework for cluster monitoring.
* Attacks: This folder contains the codes for launching attacks, including DDoS attacks and Sybil attacks. Note that there also exist several third-party tools that can realize the attacks, e.g., [Hibernet](https:https://github.com/All3xJ/Hibernet "悬停显示") and [slowhttptest](https://github.com/shekyan/slowhttptest "悬停显示").
* Private-chain benchmark results: This folder contains the results of our practical benchmarking on self-deployed `private blockchain networks`.<br>
* Public-chain benchmark results collection: Since we cannot conduct benchmarking on `public blockchain network`. This folder contains the benchmarking results of public blockchain networks collected from public-available `blockchain exporters`.<br>
* ATG, ATP, ATS: They refer to Automatic Transaction `Genenator`, `Packer`, or `Sender`, which are used to generate `benchmarking workload`.

# Tips
The resources for deploying private blockchain networks, such as `hyperledger fabric`, `Sawtooth`, `Burrow`, etc., can be found at Lancelot1998's other repositories. :blush:<br>
* [Fabric-10-node](https://github.com/Lancelot1998/Fabric-10-node "悬停显示"): Contain some scripts and configuration files for deploying a 10-node `Hyperledger Fabric (v1.0-v1.4)` network.<br>
* [Burrow-10-node](https://github.com/Lancelot1998/Burrow-10-node "悬停显示"): Contain some scripts and configuration files for deploying a 10-node `Hyperledger Burrow` network.<br>
* [Sawtooth-10-node](https://github.com/Lancelot1998/Sawtooth-10-node "悬停显示"): Contain some scripts and configuration files for deploying a 10-node `Hyperledger Sawtooth (PoET)` network.<br>
* [Iroha-10-node](https://github.com/Lancelot1998/Iroha-10-node "悬停显示"): Contain some scripts and configuration files for deploying a 10-node `Hyperledger Iroha` network.<br>

# Notice
* This is the 1st version of BCmaster, for detailed usage guidance, please wait for our update!!!<br>
* Some of the statistics in the Fig. 3 of paper "Effective Scaling of Blockchain Beyond Consensus Innovations and Moore's Law: Challenges and Opportunities" can be found in folder public-chain benchmark results collection!!!
