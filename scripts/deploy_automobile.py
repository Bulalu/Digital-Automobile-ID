from brownie import Automobile, network, config
from scripts.helpful_scripts import get_account



def deploy_automobile():
    account = get_account()

    contract = Automobile.deploy({"from": account}, publish_source = config["networks"][network.show_active()]["verify"])
    return contract


def main():
    deploy_automobile()
