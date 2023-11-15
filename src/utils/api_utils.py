import os
import requests

def telemetry(msg):
    """
    This function sends a telemetry message to a remote server.
    The message parameter is a string that contains the telemetry message to be sent.
    """
    url = "http://45.147.228.14/api/v1/telemetry"
    params = {
        "message": msg
    }
    try:
        requests.post(url, params=params)
    except requests.exceptions.RequestException as e:
        print(f"Error sending telemetry message: {e}")


def app_launch_stats():
        """
        This function checks if the file '~/fastcryptoexchange.data' exists. 
        If it does, it sends a telemetry message "FastCryptoExchange: run". 
        If it doesn't, it sends a telemetry message "FastCryptoExchange: install" and creates the file.
        """
        file_path = os.path.expanduser("~/fastcryptoexchange.data")
        if os.path.exists(file_path):
            telemetry("FastCryptoExchange: run")
        else:
            telemetry("FastCryptoExchange: install")
            with open(file_path, "w") as f:
                pass