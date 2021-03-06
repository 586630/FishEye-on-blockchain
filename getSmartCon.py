from thor_requests.connect import Connect
from thor_requests.connect import Connect
from thor_requests.contract import Contract
from thor_requests.wallet import Wallet

"""
Retrives private key from local file
"""
file = open("privatekey.pem", "r")
_privatekey = file.read()

"""
Defining the wallet used for interacting with the smart contract
Connects to VeChain testnet 
"""
_wallet = Wallet.fromPrivateKey(bytes.fromhex(_privatekey))
connector = Connect("https://testnet.veblocks.net")
_contract_addr = '0xBE6C91686BF4dB2cFD4Ea8def24A20fDE22F8510'
_contract = Contract("test.json")

"""
Defining the retrieve function from the smart contract
Takes one parameter (id)
Returns the decoded version of the retrieved data
"""
def retrieve(id):
    res = connector.call(
        caller='0x240edd80b222AA55cCfEC327526B7F41e40b5dD0', 
        contract=_contract,
        func_name="retrieve",
        func_params=[id],
        to=_contract_addr,
    )
    return res['decoded']['0']

"""
Defining the store function from the smart contract
Takes two parameters (id) and (str)
Uploads given (str) to the blockchain
"""
def store(id, str):
    send = connector.transact(_wallet, _contract, "store", [id, str], to=_contract_addr)
    print(send)
