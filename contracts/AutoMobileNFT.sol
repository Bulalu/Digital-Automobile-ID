// SPDX-License-Identifier: CC0-1.0
pragma solidity ^0.8.9;

import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "./ERC4907.sol";


// mint cars logic
// lending logic, rent fee
// how to feed data to the nfts, onchain vs offchain
// used cars vs New cars
// How will the user mint nft, either the contract mints a certain amount
// or users mint on they own
// ??

contract Automobile is ERC4907, Ownable {

    using Counters for Counters.Counter;
    Counters.Counter internal _tokenIds;

    /// @dev Base token URI used as a prefix by tokenURI().
    string public baseTokenURI;
    
    uint256 public mintPrice = 0.01 ether;
    // struct CarAttributes {
    //     uint256 price;rice
    //     uint32 manufactured;
    //     string color;
    //     string model;
    //     string brand;
    //     uint256 miles;
    //     bool accidentStatus;
    // }

    /// @notice token_id => CarAttributes
    // mapping(uint256 => CarAttributes) public tokenInfo;
    event NewCarNFTMinted(address sender, uint256 tokenId);


    event LendingUpdate(uint256 tokenId, address user, uint64 expires );


    constructor() ERC4907("Drive NFT","SKRRR") {

    }


   

    function mintCar() external payable {
        
        require(msg.value >= mintPrice, "Not enough amount to mint NFT");
        uint256 newItemId = _tokenIds.current();
        _safeMint(msg.sender, newItemId);

        // set nft data
        _setTokenURI(newItemId, "https://raw.githubusercontent.com/Bulalu/Digital-Automobile-ID/main/metadata/rinkeby/test_NFT.json");

        _tokenIds.increment();

        emit NewCarNFTMinted(msg.sender, newItemId);
    }

    function getTotalNFTsMintedSoFar() public returns(uint256 ) {
        return _tokenIds.current();
    }
    function withdraw() public onlyOwner {
        require(address(this).balance > 0, "Balance is zero ser");
        payable(owner()).transfer(address(this).balance);
    }
    function lendCar(uint256 tokenId, address user, uint64 expires) external {
        // require( expires > block.timestamp, "Invalid expire duration bro");
        setUser(tokenId, user, expires);
        
        // expires is in timestamp, you can use that to inform the user on UI
        // should a user to be lend the car, have any properties?
        // should there be a minimum/max expire time
        emit LendingUpdate( tokenId, user, expires);

    }


    // function getOwnerTokens(address _owner) public view returns (uint256[] memory) {
    //     uint256 count = balanceOf(_owner);
    //     uint256[] memory tokenIds = new uint256[](count);
    //     for(uint i = 0; i < count; i++) {
    //         tokenIds[i] = _ownedTokens[_owner][i];
    //     }
    //     return tokenIds;
    // }

    

}