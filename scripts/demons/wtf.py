from pinatapy import PinataPy
import os

pinata = PinataPy("fa0282df01c321189882", "CIQ5K8TTJUXQYZ2JF5JKVD2UQHDKEQX3ES")


jsony = {"name": "Test name v4", "description": "what you talkin bout Willis?", "image": "https://ipfs.io/ipfs/QmaAxEQRAGxq2eM9EgJfikQ4x92kLDT7jPhH6Ut3jnGnBa?filename=0.jpeg", "attributes": [{"trait_type": "model", "value": 55}]}

def main():
    response = pinata.pin_json_to_ipfs(json_to_pin=jsony)
    print(response)

main()