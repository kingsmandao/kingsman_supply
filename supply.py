from flask import Flask
import requests

app = Flask(__name__)

wallets = ['terra1e3whnp6c5k3l7vhlg6eklctsu7a3njmhw86ldw',
'terra1tngx6dxcex3khd7qx6kcaewfd9qcz7l4qvcu4l',
'terra1n9aa8lxg4u7ywqahertuhwrlrljrjwle9xzutt',
'terra1lzvpwvjc088acpk0drj2ym7a7pplvazvl4zvv7',
]
TOTAL_SUPPLY = 100000000

def get_balance(wallet_addr):
	url = (
		'https://fcd.terra.dev/wasm/contracts/'
		'terra19mcqz609t5vcudfatwexuhta0mrs49fu9dqj2s/'
		'store?query_msg={"balance":{"address": "'
		f'{wallet_addr}"}}}}')
	print(url)
	try:
		r = requests.get(url).json()
		print(r)
		return int(int(r['result']['balance']) / 1000000)
	except Exception as e:
		print(e)
		return 0

@app.route("/")
def get_circulating_supply():
	circulating_supply = TOTAL_SUPPLY
	for wallet in wallets:
		circulating_supply -= get_balance(wallet)
	return str(circulating_supply)