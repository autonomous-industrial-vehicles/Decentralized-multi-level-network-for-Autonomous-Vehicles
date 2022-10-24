from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
print("web3 is connected: ", w3.isConnected())
abi = [{"inputs":[{"internalType":"uint256","name":"a","type":"uint256"}],"name":"multiply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"pure","type":"function"}]
address = "0x54861C1Da211eb17D70A8bAd6A38B151528105C6"
RegistroContract = w3.eth.contract(address=address, abi=abi)
#Registro = RegistroContract.at("0x54861C1Da211eb17D70A8bAd6A38B151528105C6")
result = RegistroContract.functions.multiply(4).call()
print(result)
