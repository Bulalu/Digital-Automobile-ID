import json
import os
from pathlib import Path
import requests
import json
PINATA_BASE_URL = "https://api.pinata.cloud/"
endpoint = "pinning/pinFileToIPFS"
endpoint = "pinning/pinJSONToIPFS"
# Change this filepath
filepathx = "./img/1.jpeg"
# filename = filepath.split("/")[-1:][0]
headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_API_SECRET"),
    "Content-Type": "application/json"
}

filepath = "./metadata/rinkeby/test_NFT.json"

def deploy_to_pinatta(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        image_binary = image_binary.decode("utf-8")
        print(image_binary)
        filename = filepath.split("/")[-1:][0]
        response = requests.post(
            PINATA_BASE_URL + endpoint,
            json={"pinataContent": image_binary},
            headers=headers,
        )
        print(response.json())
        hash = response.json()["IpfsHash"]
        
        uri = f"https://ipfs.io/ipfs/{hash}?filename={filename}"
        print(uri)
        return uri

def test_json():
    filepath = './metadata/rinkeby/test_NFT.json'
    with Path(filepath).open("rb") as json_file:
        json_data = json.load(json_file)
        response = requests.post(
            PINATA_BASE_URL + endpoint,
            json=json_data,
            headers=headers,
        )

    print(type(json_data))
    print(response.json())
def main():
    # deploy_to_pinatta(filepath=filepathx)
    deploy_to_pinatta(filepath)
    


# {'IpfsHash': 'QmNqZpxbHpWXpbjcDfyAWVw1VPeBcDBBmQyn3vpnP57p8w', 'PinSize': 4603, 'Timestamp': '2022-05-30T12:29:52.453Z', 'isDuplicate': True}
# https://ipfs.io/ipfs/QmNqZpxbHpWXpbjcDfyAWVw1VPeBcDBBmQyn3vpnP57p8w?filename=1.jpeg