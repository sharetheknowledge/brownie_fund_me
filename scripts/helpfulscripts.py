from brownie import MockV3Aggregator,network, accounts, config
from web3 import Web3

FORKED_LOCAL_DEVELOPMENT=['mainnet-fork','mainnet-fork-dev']
LOCAL_BLOCKCHAIN_DEVELOPMENT=['development','ganache-local']

DECIMALS=8
STARTINGPRICE=200000000000

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_DEVELOPMENT or network.show_active()  in FORKED_LOCAL_DEVELOPMENT:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print("the active network is {}".format(network.show_active()))
    print("deploying Mock")
    if len(MockV3Aggregator)<=0:
        MockV3Aggregator.deploy(DECIMALS,STARTINGPRICE,{"from": get_account()})
    print("Mocks deployed")