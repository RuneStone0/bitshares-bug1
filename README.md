# Setup using Virtual Env
```
virtualenv -p python3 venv
source venv/bin/active
pip3 install -r requirements.txt
grep -Rli 'wss://node.testnet.bitshares.eu' * | xargs -i@ sed -i 's/wss:\/\/node.bitshares.eu/wss:\/\/node.testnet.bitshares.eu/g' @
RUN wget -O venv/lib/python3.6/site-packages/bitshares/transactionbuilder.py https://raw.githubusercontent.com/bitshares/python-bitshares/27701d4f9d92ee2eecdc8001633083f856546820/bitshares/transactionbuilder.py
```

# Run using Docker
```
docker build -t bug1 . && docker run bug1
```

# testnet accounts
testnet-bah123
	Password:	P5JM2R2wTYDXYjPnoSkPAGE7pffM8wH5CCAepC2UpbBcB
	Owner Key: 	5KgxJbDfwQqS9WCGwYqzwx61uzr9Y85PJsiWccoKciYBeWqxknv
	Active key:	5Kj1QiA9Z9ZZ4zAKar36cestZdZKdCExRvu58NV2wMnn2g6BBRR

testnet-bob123
	Password:	P5KNSgyG9FbQKdTszHJHQ86pfus7XZwy12uBhZKWAXHX7
	Active Key:	5HugdBgwL69ibVAbPv63F36u4hxZYuQPTY7TfAPmDwHkbZZgufh
	Owner Key:	5JBwTxLh1jW3WVdxqbjwRE2gScxDtTAM4gFVVYXpHCT52ub3oGv
