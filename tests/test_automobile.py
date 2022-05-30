from brownie import accounts
from scripts.helpful_scripts import get_account
from scripts.deploy_automobile import deploy_automobile
import pytest



def test_lending():
    bob = accounts[0]
    alice = accounts[1]
    stu = accounts[2]

    expire = 86400 #one day
    automoblie = deploy_automobile()

    automoblie.mintCar({"from": bob})

    bobs_nft = automoblie.getOwnerTokens(bob)
    # print("Bob's NFTs", bobs_nft[0])
    print(automoblie.userOf(bobs_nft[0]) == bob)
    


    tx = automoblie.lendCar(0, alice, expire, {"from": bob})
    print(tx.events)
    bob_nft_balance = automoblie.balanceOf(bob)
    alice_nft_balance = automoblie.balanceOf(alice)

    print("Bobs NFT balance after lending: ", bob_nft_balance )
    print("Alice NFT balance after borrowing", alice_nft_balance)
    print(automoblie.userOf(bobs_nft[0]) == bob)
    