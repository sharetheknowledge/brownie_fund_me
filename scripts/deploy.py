from brownie import FundMe,MockV3Aggregator, accounts, config, network 
import time
from web3 import Web3




from scripts.helpfulscripts import LOCAL_BLOCKCHAIN_DEVELOPMENT, get_account,deploy_mocks, LOCAL_BLOCKCHAIN_DEVELOPMENT

def deploy_fund_me():
    account=get_account()
    print(account)
    if network.show_active() not in LOCAL_BLOCKCHAIN_DEVELOPMENT:
        price_feed_address=config['networks'][network.show_active()]['eth_usd_price_feed']
    #pass the price feed address to our FundMe contract 
        
    else:
        deploy_mocks()
        price_feed_address=MockV3Aggregator[-1].address
        
        
    # time.sleep(1)
    fund_me=FundMe.deploy(price_feed_address,{"from": account}, publish_source=config['networks'][network.show_active()]['verify'])
    time.sleep(1)
    print(f'Contract deployed at {fund_me.address}')
    return fund_me


def main():
    deploy_fund_me()