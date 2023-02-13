import ccxt
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

binance_api_key = os.getenv('BINANCE_API_KEY')
binance_secret_key = os.getenv('BINANCE_SECRET_KEY')


# Inicializa una instancia de Binance
exchange = ccxt.binance({
    'apiKey': binance_api_key,
    'secret': binance_secret_key,
})

# Define las tres criptomonedas que utilizarás para el arbitraje triangular
symbol_1 = 'BTC/USDT'
symbol_2 = 'ETH/USDT'
symbol_3 = 'LTC/USDT'


async def check_arbitrage():
    # Obtén los precios en tiempo real de las tres criptomonedas
    price_1 = exchange.fetch_ticker(symbol_1)['last']
    price_2 = exchange.fetch_ticker(symbol_2)['last']
    price_3 = exchange.fetch_ticker(symbol_3)['last']

    # Calcula las diferencias de precios
    diff_1_2 = price_2 / price_1
    diff_2_3 = price_3 / price_2
    diff_1_3 = price_3 / price_1

    # Verifica si existe una oportunidad de arbitraje triangular
    if diff_1_2 > 1.005 and diff_2_3 < 0.995 and diff_1_3 < 0.995:
        # Compra ETH con BTC
        amount_eth = exchange.create_limit_buy_order(
            symbol_2, amount_btc / price_2, price_2 * 1.01)
        # Vende ETH por LTC
        amount_ltc = exchange.create_limit_sell_order(
            symbol_3, amount_eth, price_3 * 0.99)
        # Vende LTC por BTC
        amount_btc = exchange.create_limit_sell_order(
            symbol_1, amount_ltc, price_1 * 0.99)
        print("Operación de arbitraje triangular realizada con éxito")
    else:
        print("No existe una oportunidad de arbitraje triangular")


async def main():
    while True:
        await asyncio.gather(check_arbitrage())
        await asyncio.sleep(5)

asyncio.run(main())
