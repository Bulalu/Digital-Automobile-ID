from urllib import response
from brownie import MyToken, network, Automobile

# from scripts import deploy_to_pinatta
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests
import json
import os 

from scripts.deploy_automobile import deploy_automobile

import os
from pathlib import Path
import requests

PINATA_BASE_URL = "https://api.pinata.cloud/"
endpoint_file = "pinning/pinFileToIPFS"
endpoint_json = "pinning/pinJSONToIPFS"
# Change this filepath
filepathx = "./img/2.jpeg"
# filename = filepath.split("/")[-1:][0]
headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_API_SECRET"),
}



def upload_to_pinatta(filepath, json=None, file=None):
    with Path(filepath).open("rb") as fp:
        
        if json:
            image_binary = fp.read()
            image_binary = image_binary.decode("utf-8")
            filename = filepath.split("/")[-1:][0]
            endpoint = endpoint_json
            response = requests.post(
            PINATA_BASE_URL + endpoint,
            json={"pinataContent": image_binary},
            headers=headers,
        )
            print(response.json())
            hash = response.json()["IpfsHash"]
            uri = f"https://ipfs.io/ipfs/{hash}?filename={filename}"
            print(uri)
           
        elif file:
            image_binary = fp.read()
            filename = filepath.split("/")[-1:][0]
            endpoint = endpoint_file
            response = requests.post(
            PINATA_BASE_URL + endpoint,
            files={"file": (filename, image_binary)},
            headers=headers,
        )
            print(response.json())
            hash = response.json()["IpfsHash"]
            uri = f"https://ipfs.io/ipfs/{hash}?filename={filename}"
            print(uri)
       
        
        # print(response.json())
        # hash = response.json()["IpfsHash"]
        
        # uri = f"https://ipfs.io/ipfs/{hash}?filename={filename}"
        # print(uri)
        # return uri

def  main():

    nft_contract = Automobile[-1]
    metadata_file_name = f"./metadata/{network.show_active()}/test_NFT.json"
    sample_metadata = metadata_template

    if Path(metadata_file_name).exists():
        print(f"{metadata_file_name} already exists! Delete it to overwrite")
    else:
        print(f"Creating metadata file: {metadata_file_name}")
        sample_metadata["name"] = "Test name v4"
        sample_metadata["description"] = "what you talkin bout Willis?"
        # upload img
        image_path = "./img/0.jpeg"
        image_uri = upload_to_pinatta(image_path, file=True)
        sample_metadata["image"] = image_uri

        with open(metadata_file_name, "w") as file:
            json.dump(sample_metadata, file)
            uri = upload_to_pinatta(metadata_file_name, json=True)
            print(metadata_file_name)
            print("Metadata URI", uri)

    # mf("./metadata/rinkeby/test_NFT.json")
        



def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        print("image binary",image_binary)
        # print("I am the image URI", image_binary)
        # upload stuff
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"files":image_binary})
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri

def mf(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        print("image binary",image_binary)
        
        endpoint = endpoint_json
        print(PINATA_BASE_URL + endpoint)
        response = requests.post(
        PINATA_BASE_URL + endpoint,
        image_binary,
        headers=headers,
     )

        print(response)



# def test_transfer_of_lp_position(jelly_pool, lp_token, jelly_token, jelly_rewarder):
