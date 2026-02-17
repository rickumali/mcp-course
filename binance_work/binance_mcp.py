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


def get_price(symbol: str) -> Any:
    symbol = get_symbol_from_name(symbol)
    url = f"https://api.binance.us/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print("Starting Binance MCP")
    mcp.run()
