from brownie import accounts, ERC_DualRoles, chain
from scripts.helpful_scripts import get_account
from scripts.deploy_automobile import deploy_automobile
import pytest


def deploy_erc_dual_roles():
    account = accounts[0]
    bob = accounts[1]

    contract = ERC_DualRoles.deploy("Test NFT", "TEST", {"from": account})
    
    
    return contract



def test_lending():
    account = accounts[0]
    bob = accounts[1]

    contract = deploy_erc_dual_roles()
    contract.mint(1, bob, {"from": account})

    user_1 = contract.userOf(0)
    time_ = chain.time() + 100000

    contract.setUser(1, account, time_, {"from": bob})

    user_2 = contract.userOf(0)
    # print(account)
    # print(user_2)
    # assert user_2 == account
    assert contract.userOf(1) == account
    # print("NFT balance",contract.balanceOf(account))

    