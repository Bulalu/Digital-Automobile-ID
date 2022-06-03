from brownie import Automobile, network, config
from scripts.helpful_scripts import get_account, OPENSEA_URL



def deploy_automobile():
    account = get_account()
    
    if len(Automobile) > 0:
        print("Here's the latest Already deployed contract")
        contract = Automobile[-1]
    else:
        print("Deploying the contract, captain")
        contract = Automobile.deploy({"from": account}, publish_source = config["networks"][network.show_active()]["verify"])

    tx = contract.mintCar({"from": account, "value": "0.01 ether"})
    tx.wait(1)
    token_id = tx.events["NewCarNFTMinted"]["tokenId"]
    print("tokenId", token_id)
 
    print(f"Awesome, you can view your NFT at {OPENSEA_URL.format(contract.address, token_id)}")
    print("Please wait up to 20 minutes, and hit the refresh metadata button.")
    return contract


def main():
    deploy_automobile()

#brownie run scripts/deploy_automobile.py --network rinkeby