# A survey on whether the mainstream IoT-oriented blockchains provide IR interfaces.

## Abbreviations Desription

API refers to **A**pplication **P**rogramming **I**nterface;

RPC means **R**emote **P**rocedure **C**all; 

SDK means **S**oftware **D**evelop-ment **K**it.

## Table

|BC Applications| Chain Type| Market Cap| Rank| Support IR?| IR Formats| Application case in IoT|
|:---:|:-:|:-:|:-:|:-:|:-:|:-:|
| [Ethereum (ETH)](https://ethereum.org) [[Code](https://github.com/ethereum/go-ethereum)]| Public|  $241,529,132,838 |2|√| [JSON-RPC (Python/C++/Go)](https://eth.wiki/json-rpc/API)|[Slock.it, an Ethereum-based application enabling the secure economy of things](https://blog.slock.it/tagged/ethereum)|
|[Cardano (ADA)](https://cardano.org/) |Public|$38,328,227,233 |5|√|[JSON-RPC (Haskell)](https://testnets.cardano.org/en/virtual-machines/kevm/resources/rpc-endpoints.md/)|[Worldwide IoT-layer cryptocurrency, cooperated with Ethiopia’s Education Ministry](https://medium.com/illumination/cardano-ada-joins-with-ethiopias-education-ministry-and-helium-hnt-wants-to-build-a-worldwide-75c107795bf3)|
| [Polkadot (DOT)](https://polkadot.network/)[[code](https://github.com/paritytech/polkadot)]| Public |  $13,150,505,918 |9|√|[JSON-RPC (JavaScript)](https://polkadot.js.org/apps/#/js)|[OBONOMICS, a Polkadot-based IoT platform for smart robots managements in industry 4.0](https://robonomics.network/)||
|[IOTA](https://www.iota.org/)|Public | $1,817,214,038 | 48 | √| [REST API](https://pkg.go.dev/github.com/iotaledger/iota.go/v2#pkg-types) & [Go](https://github.com/iotaledger/iota.go)/[C](https://github.com/iotaledger/iota.c)/[JavaScript](https://github.com/iotaledger/iota.js)/[Python SDK](https://github.com/iotaledger/iota-java)|[Instant vehicle-to-vehicle transactions, cooperated with Bosch](https://www.iota.org/solutions/partnerships)|
|[IOTEX](https://iotex.io/research/) [[code](https://github.com/iotexproject/iotex-core)]|Pulic|$223,393,504.10|167|√|[JSON-RPC & JavaScript SDK](https://docs.iotex.io/reference/node-core-api-grpc)|[Blockchain-based mobile payment, cooperated with China Mobile IoT Alliance](https://ieeexplore.ieee.org/document/8977822)|
|[Conflux](https://confluxnetwork.org/zh/) [[code](https://github.com/Conflux-Chain/conflux-rust)]|Public |$215,035,458.73|178|√|[JSON-RPC (RUST) & JavaScript SDK](https://conflux-chain.github.io/conflux-doc/json-rpc/)|[Fast human-to-machine payments, cooperated with Shanghai government](https://technode.com/2020/01/22/the-chinese-blockchain-startup-taking-on-scalability/)|
|[DAML](https://daml.com/) [[Code](https://github.com/digital-asset/daml)] | Public | N/A |N/A | √  | [gRPC](https://docs.daml.com/getting-started/installation.html) & [JSON-RPC](https://docs.daml.com/json-api/index.html)| [Digital Asset, a revolutionized supply chain based on DAML smart contracts, cooperated with VMware](https://aws.amazon.com/cn/blockchain/) |
|[Corda](https://www.corda.net/) [[Code](https://github.com/corda/corda)]|Private |N/A|N/A|√|[Java/Kotlin SDK](https://docs.corda.net/)|[Aerotrax, a Corda-based Dapp for the maintenance and repair tracking of aircraft parts, in the aviation industry](https://www.r3.com/wp-content/uploads/2020/11/US_268_Corda_for_Supply_Chain_FS_V5.pdf)|
| [Parity](https://parity.io) [[Code](https://github.com/openethereum/parity-ethereum)]|Private |  N/A |N/A|√|[Json-RPC](https://testnets.cardano.org/en/virtual-machines/kevm/resources/rpc-endpoints.md/)|  [Lightweight Ethereum client, to support resource-constrained IoT devices](https://blog.slock.it/tagged/ethereum)|
|[Hyperledger Fabric](https://www.hyperledger.org/) [[code](https://github.com/hyperledger/fabric)] | Private | N/A | N/A |√ |[REST API & Node.js/Python SDK](https://wiki.hyperledger.org/display/fabric/Hyperledger+Fabric+SDKs)| [My Sensor, a fabric-empowered platform for tracking and certifying the historical series of Radon gas concentration](https://github.com/newham/fabric-iot) |
|[Hyperledger Sawtooth](https://www.hyperledger.org/use/sawtooth) [[code](https://github.com/hyperledger/sawtooth-core)] | Private | N/A | N/A |√ | [REST API & Go/JavaScript/Python SDK](https://sawtooth.hyperledger.org/docs/core/releases/latest/app_developers_guide/using_the_sdks.html)| [FishNet, a seafood supply chain to ensure the traceability and provenance of fishes](https://demo.bitwise.io/fish/#!/)| 
| [Quorum](https://consensys.net/quorum) [[Code](https://github.com/ConsenSys/quorum)]|Private |N/A|N/A|√|[JSON-RPC](https://github.com/ConsenSys/quorum/tree/master/rpc) & [JavaScript SDK](https://fisco-bcos-documentation.readthedocs.io/en/latest/docs/api.html)|[Smart Smart contract-based food supply temperature control](https://github.com/chainstack/quorum-iot-tutorial)| 
|[FISCO BCOS](http://www.fisco-bcos.org/) [[code](https://github.com/FISCO-BCOS/FISCO-BCOS-DOC)]|Private |N/A|N/A|√|[JSON-RPC/Java SDK](https://fisco-bcos-documentation.readthedocs.io/zh_CN/latest/docs/sdk/index.html)|[Supply chain finance, such as livestock tracing and insurance issuing](http://www.fisco-bcos.org/)|
|[Helium](https://www.helium.com/) [[code](https://github.com/helium)]|Private |N/A|N/A|√|[JSON-RPC (C++)](https://github.com/heliumchain/helium/blob/master/src/rpcclient.cpp)|[5G, a wireless blockchain network](https://www.helium.com/5G)|


## Reference

The rank data from [CoinMarket](https://coinmarketcap.com)


