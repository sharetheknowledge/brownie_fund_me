from brownie import FundMe, accounts

def read_contract():
    account=accounts[0]
    fund_me=FundMe[-1]
    owner=fund_me.owner()

    print(owner)


def main():
    read_contract()