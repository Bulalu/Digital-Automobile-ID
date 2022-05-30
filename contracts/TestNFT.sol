// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract MyToken is  ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;

    Counters.Counter public _tokenIdCounter;

    constructor() ERC721("MyToken", "MTK") {}

    // function _baseURI() internal pure override returns (string memory) {
    //     return "giggity";
    // }

    //  function baseTokenURI() override public pure returns (string memory) {
    //     return "https://github.com/Bulalu/Digital-Automobile-ID/blob/main/img/";
    // }

    function safeMint(address to, string memory uri) public onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, uri);
    }

    // The following functions are overrides required by Solidity.

    // function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
    //     super._burn(tokenId);
    // }

  
//    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
//         // pug, shiba inu, st bernard
//         require(_isApprovedOrOwner(_msgSender(), tokenId), "ERC721: caller is not owner or not approved");
//         _setTokenURI(tokenId, _tokenURI);
//     }
}
