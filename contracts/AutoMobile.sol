pragma solidity ^0.8.9;

import "@openzeppelin/contracts/token/ERC721/ERC721SemiNumerable.sol";



// mint cars logic
// lending logic
// how to feed data to the nfts
// ??

contract Automobile is ERC721SemiNumerable {

    using Counters for Counters.Counter;
    Counters.Counter internal _tokenIdTracker;

    constructor() ERC721("Drive NFT","SKRRR") {

    }

    function _safeMint(address _user) internal returns (uint256){
        uint256 _tokenId = _tokenIdTracker.current();
        _safeMint(_user, _tokenId);
        _tokenIdTracker.increment();
        return _tokenId;
    }

}