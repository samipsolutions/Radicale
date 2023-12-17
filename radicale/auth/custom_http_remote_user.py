"""
Authentication backend that uses the user specified header.

It's intended for use with a reverse proxy. Be aware as this will be insecure
if the reverse proxy is not configured properly.

"""

from radicale import config, types
from typing import Tuple, Union
from radicale.auth import none


class Auth(none.Auth):
    def __init__(self, configuration: "config.Configuration") -> None:
        super().__init__(configuration)
        # Read the custom header name from configuration
        # Assuming the header name is stored under 'auth' section with key 'remote_user_header'
        self.custom_header_name = configuration.get("auth", "remote_user_header")

    def get_external_login(self, environ: types.WSGIEnviron) -> Union[Tuple[()], Tuple[str, str]]:
        # Use the custom header name to extract the username
        return environ.get(self.custom_header_name, "")
