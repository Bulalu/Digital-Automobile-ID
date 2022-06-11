from brownie import accounts, Automobile, chain
from scripts.helpful_scripts import get_account
import pytest
import brownie
from web3 import Web3
def deploy_automobile():
    owner = accounts[0]
    
    if len(Automobile) > 0:
        print("Here's the already deployed contract ser")
        return Automobile[-1]
    else:
        print("Deploying new contract!")
        contract = Automobile.deploy({"from": owner})
        return contract
        



def test_register():
    owner = accounts[0]
    bob = accounts[1]
    alice = accounts[2]
    contract = deploy_automobile()
    time_ = chain.time() + 24 * 3600
    amount = "0.05 ether"


    with brownie.reverts("Time  cannot be zero"):
        contract.register(0, {"from": bob, "value": amount})

    with brownie.reverts("Not enough ETH sent; check price!"):
        contract.register(time_, {"from": bob, "value": "0.04 ether"})

    contract.register(time_, {"from": bob, "value": amount}) 

    assert contract.borrowers(bob)["borrowingTime"] == time_
    assert contract.borrowers(bob)["balance"] == Web3.toWei(0.05, "ether")
    assert contract.borrowers(bob)["registered"] == True

    return contract


def test_lending():
    owner = accounts[0]
    bob = accounts[1]
    alice = accounts[2]
    time_ = chain.time() + 24 * 3600
    amount = "0.05 ether"
    token_id_1 = 1
    token_id_2 = 2

    contract = deploy_automobile()

    
    contract.mint(token_id_1, owner, {"from":owner})

    with brownie.reverts("User is not Registered"):
        contract.lendCar(token_id_1, bob, {"from": owner})

    contract.register(time_, {"from": bob, "value": amount}) 
    
    tx = contract.lendCar(token_id_1, bob, {"from": owner})
   
    assert "LendingUpdate" in tx.events
    assert contract.userOf(token_id_1) == bob
