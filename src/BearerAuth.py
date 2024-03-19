import requests


class BearerAuth(requests.auth.AuthBase):
    """
    Authentication Class for request parametrization in Client Functions.
    """
    def __init__(self, token):
        """
        Initialize Bearer Auth
        :param token: access token (without other parts of response body)
        """
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r
