from brownie import Automobile, MyToken, network, config
from scripts.helpful_scripts import get_account, OPENSEA_URL



sample_token_uri = "https://ipfs.io/ipfs/QmfJEyPxYGymfVXG1mjb4UGupwPUfvACCaqdUvrS7YphTA"
token_uri = "https://ipfs.io/ipfs/QmbFMke1KXqnYyBBWxB74N4c5SBnJMVAiMNRcGu6x1AwQH?filename=test_NFT.json"

def deploy_test_nft():
    account = get_account()

    # contract = MyToken.deploy({"from": account}, publish_source = config["networks"][network.show_active()]["verify"])
    contract = MyToken[-1]
    contract.safeMint(account, sample_token_uri, {"from": account})
    print(f"Awesome, you can view your NFT at {OPENSEA_URL.format(contract.address, contract._tokenIdCounter() - 1)}")
    print("Please wait up to 20 minutes, and hit the refresh metadata button.")
    print("tokenURI ",contract.tokenURI(contract._tokenIdCounter() - 1))
    return contract


def main():
    deploy_test_nft()



