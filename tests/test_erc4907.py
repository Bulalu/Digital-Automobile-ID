from brownie import accounts, ERC_DualRoles, chain
from scripts.helpful_scripts import get_account
from scripts.deploy_automobile import deploy_automobile
import pytest
import brownie

def deploy_erc_dual_roles():
    account = accounts[0]
    bob = accounts[1]

    contract = ERC_DualRoles.deploy("Test NFT", "TEST", {"from": account})
    
    
    return contract


# if the owner transfers the nft , it resets the user role

def test_lending():
    account = accounts[0]
    bob = accounts[1]
    alice = accounts[2]

    contract = deploy_erc_dual_roles()
    contract.mint(1, bob, {"from": bob})

    
    time_ = chain.time() + 100000

    contract.setUser(1, account, time_, {"from": bob})

    # transfer nft as user
    with brownie.reverts("ERC721: transfer caller is not owner nor approved"):
        contract.safeTransferFrom(account, alice, 1, {"from": account})

    # owner can not transfer nft when the expire duration is not yet reached
    with brownie.reverts("Token has not yet expired"):
        contract.safeTransferFrom(bob, alice, 1, {"from": bob})
    user_2 = contract.userOf(1)
    
    chain.sleep(contract.userExpires(1) + 100)
    print("Expires", contract.userExpires(1))
    # contract.safeTransferFrom(bob, alice, 1, {"from": bob})
    # print(account)
    # print(user_2)
    # assert user_2 == account
    assert user_2 == account
    print("Is time greater",chain.time() > contract.userExpires(1))

    print(contract.userOf(1))
    # chain.sleep(time_ + 100)
    
    
    
    # print(tx.events)
    # print("NFT balance",contract.balanceOf(account))
    print(contract.userOf(1))

    