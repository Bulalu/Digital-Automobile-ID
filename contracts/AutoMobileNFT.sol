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
    Counters.Counter internal _tokenIdTracker;

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
    


    event LendingUpdate(uint256 tokenId, address user, uint64 expires );


    constructor() ERC4907("Drive NFT","SKRRR") {

    }


        /// @dev Returns an URI for a given token ID
    function _baseURI() internal view virtual override returns (string memory) {
        return baseTokenURI;
    }

    /// @dev Sets the base token URI prefix.
    function setBaseTokenURI(string memory _baseTokenURI) public {
        baseTokenURI = _baseTokenURI;
    }


    function _safeMint(address _user) internal returns (uint256){
        uint256 _tokenId = _tokenIdTracker.current();
        _safeMint(_user, _tokenId);
        _tokenIdTracker.increment();
        return _tokenId;
    }

    function mintCar() external payable {
        require(msg.value >= mintPrice, "Not enough amount to mint NFT");
        _safeMint(msg.sender);
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


    function getOwnerTokens(address _owner) public view returns (uint256[] memory) {
        uint256 count = balanceOf(_owner);
        uint256[] memory tokenIds = new uint256[](count);
        for(uint i = 0; i < count; i++) {
            tokenIds[i] = _ownedTokens[_owner][i];
        }
        return tokenIds;
    }

    // function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
    //     require(_isApprovedOrOwner(msg.sender, tokenId), "ERC721: caller is not owner nor approved");
    //     _setTokenURI(tokenId, _tokenURI);

    // }

}