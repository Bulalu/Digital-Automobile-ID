// SPDX-License-Identifier: CC0-1.0
pragma solidity ^0.8.9;

import "@openzeppelin/contracts/utils/Counters.sol";
import "./ERC4907.sol";


// mint cars logic
// lending logic, rent fee
// how to feed data to the nfts, onchain vs offchain
// used cars vs New cars

// ??

contract Automobile is ERC4907 {

    using Counters for Counters.Counter;
    Counters.Counter internal _tokenIdTracker;


    struct CarAttributes {
        uint256 price;
        uint32 manufactured;
        string color;
        string model;
        string brand;
        uint256 miles;
        bool accidentStatus;
    }

    /// @notice token_id => CarAttributes
    mapping(uint256 => CarAttributes) public tokenInfo;
    
    event LendingUpdate(uint256 tokenId, address user, uint64 expires );
    constructor() ERC4907("Drive NFT","SKRRR") {

    }

    function _safeMint(address _user) internal returns (uint256){
        uint256 _tokenId = _tokenIdTracker.current();
        _safeMint(_user, _tokenId);
        _tokenIdTracker.increment();
        return _tokenId;
    }

    function mintCar() external {
        _safeMint(msg.sender);
    }

    function lendCar(uint256 tokenId, address user, uint64 expires) external {
        require( expires > block.timestamp, "Invalid expire duration bro");
        setUser(tokenId, user, expires);
        
        // expires is in timestamp, you can use that to inform the user on UI
        // should a user to be lend the car, have any properties?
        // should there be a minimum/max expire time
        emit LendingUpdate( tokenId, user, expires);

    }

}