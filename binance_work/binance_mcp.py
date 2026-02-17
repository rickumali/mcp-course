from mcp.server.fastmcp import FastMCP
import requests
from typing import Any

mcp = FastMCP("Binance MCP")


def get_symbol_from_name(name: str) -> str:
    if name.lower() in ["bitcoin", "btc"]:
        return "BTCUSDT"
    elif name.lower() in ["ethereum", "eth"]:
        return "ETHUSDT"
    else:
        return name.upper()


@mcp.tool()
def get_price(symbol: str) -> Any:
    """
    Get the current price of a crypto asset from Binance

    Args:
        symbol (str): The symbol of the crypto asset

    Returns:
        Any: The current price of the crypto asset
    """
    symbol = get_symbol_from_name(symbol)
    url = f"https://api.binance.us/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


@mcp.tool()
def get_price_price_change(symbol: str) -> Any:
    """
    Get price change of a crypto asset for the last 24 hours from Binance

    Args:
        symbol (str): The symbol of the crypto asset

    Returns:
        Any: The price change of the crypto asset for last 24 hours
    """
    symbol = get_symbol_from_name(symbol)
    url = f"https://api.binance.us/api/v3/ticker/24hr?symbol={symbol}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["priceChange"]


if __name__ == "__main__":
    mcp.run(transport="stdio")
