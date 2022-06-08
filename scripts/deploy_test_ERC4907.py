from brownie import ERC_DualRoles, network, config
from scripts.helpful_scripts import get_account, OPENSEA_URL



def deploy():
    account = get_account()
    
    if len(ERC_DualRoles) > 0:
        print("Here's the latest Already deployed contract")
        contract = ERC_DualRoles.deploy("Test NFT", "TEST", {"from": account}, publish_source = config["networks"][network.show_active()]["verify"])
        return contract
    else:
        print("Deploying the contract, captain")
        contract = ERC_DualRoles.deploy("Test NFT", "TEST", {"from": account}, publish_source = config["networks"][network.show_active()]["verify"])
        return contract


def main():
    deploy()