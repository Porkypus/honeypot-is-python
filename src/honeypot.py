from utils import make_request


class Honeypot:
    BASE_URL = "https://api.honeypot.is"

    def is_honeypot(
        self,
        address: str,
        chainID: int = None,
        pair: str = None,
        simulate_liquidity: bool = None,
    ):
        endpoint = "v2/IsHoneypot"
        params = {"address": address}
        if chainID:
            params["chainID"] = chainID
        if pair:
            params["pair"] = pair
        if simulate_liquidity:
            params["simulateLiquidity"] = simulate_liquidity

        return make_request(self, endpoint, params)

    def get_contract_verification(self, address: str, chainID: int = None):
        endpoint = "v2/GetContractVerification"
        params = {"address": address}
        if chainID:
            params["chainID"] = chainID

        return make_request(self, endpoint, params)

    def get_top_holders(self, address: str, chainID: int):
        endpoint = "v1/GetPairs"
        params = {"address": address, "chainID": chainID}
        return make_request(self, endpoint, params)

    def get_pairs(self, address: str, chainID: int = None):
        endpoint = "v1/GetPairs"
        params = {"address": address}
        if chainID:
            params["chainID"] = chainID

        return make_request(self, endpoint, params)
