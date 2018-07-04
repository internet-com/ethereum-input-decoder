from ethereum_input_decoder import ContractAbi, Utils
import json

if __name__ == "__main__":
    # This is our example contract:
    #   https://www.etherchain.org/account/ab7c74abc0c4d48d1bdad5dcb26153fc8780f83e#code
    with open('contract_abi_ab7c74abc0c4d48d1bdad5dcb26153fc8780f83e.json', 'r') as f:
        abi = f.read()

    ca = ContractAbi(json.loads(abi))

    # This is the constructor arguments:
    #   https://etherscan.io/address/0xab7c74abc0c4d48d1bdad5dcb26153fc8780f83e#code
    print(ca.describe_constructor(Utils.str_to_bytes(
        "000000000000000000000000000000000000000000000000000000000000006000000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000de0b6b3a764000000000000000000000000000000000000000000000000000000000000000000040000000000000000000000002903cadbe271e057edef157340b52a5898d7424f000000000000000000000000ba7ca1bcf210c1b37cf5818816c4a819c3040ea700000000000000000000000014cd6536d449e3f6878f2d6859e1ff92ae0990e60000000000000000000000000c24441e42277445e38e02dfc3494577c05ba46b")))
    # constructor None ((address[]) _owners = ('0x2903cadbe271e057edef157340b52a5898d7424f', '0xba7ca1bcf210c1b37cf5818816c4a819c3040ea7', '0x14cd6536d449e3f6878f2d6859e1ff92ae0990e6', '0x0c24441e42277445e38e02dfc3494577c05ba46b'), (uint256) _required = 2, (uint256) _daylimit = 1000000000000000000) returns ()


    # This is one input transaction:
    #   https://www.etherchain.org/tx/1e9ed6236afb884fe7cad9a807886ba61b9e9a2fc944a991e3e8725d2158c7b2
    print(ca.describe_input(Utils.str_to_bytes(
        "0xfedd60920000000000000000000000000595d187cac88f04466371eff3a6b6d1b12fb013b92dd9476601c067bcd9730c83d54263fbc0da1c2c01f05a834199427aa3fad40000000000000000000000005c3766a9a906aa17e16dbbdaac0c93d41c0d057f")))
    # f