################## TEST NET #####################
BITSHARES_NODE = ["wss://node.testnet.bitshares.eu"]
NOBROADCAST = False
ACCOUNT_PREFIX = "testnet-"
REGISTRAR = {
	"account_name": "testnet-bah123",
	"private_key": "5KgxJbDfwQqS9WCGwYqzwx61uzr9Y85PJsiWccoKciYBeWqxknv",
	"password": "P5JM2R2wTYDXYjPnoSkPAGE7pffM8wH5CCAepC2UpbBcB"
}
MEMBER = {
	"account_name": "testnet-bob123",
	"private_key": "5HugdBgwL69ibVAbPv63F36u4hxZYuQPTY7TfAPmDwHkbZZgufh",
	"password": "P5KNSgyG9FbQKdTszHJHQ86pfus7XZwy12uBhZKWAXHX7"
}
ASSET = "PEG.FAKEUSD:TEST"
#################################################


from bitshares import BitShares
from bitshares.account import Account
from bitshares.market import Market
from bitshares.instance import set_shared_bitshares_instance

def RandomString(length, chars="dul"):
	"""
		Creates a random string.
		params: length defines the length of the string to be generated
		params: chars defines which characters to be included
					d = digits
					u = uppercase letters
					l = lowercase letters
	"""
	import random, string
	length = length
	charsset = ""
	if "d" in chars:
		charsset = charsset + string.digits
	if "u" in chars:
		charsset = charsset + string.ascii_uppercase
	if "l" in chars:
		charsset = charsset + string.ascii_lowercase
	return ''.join(random.SystemRandom().choice(charsset) for _ in range(length))

def suggest_brain_key():
	from graphenebase.account import BrainKey
	bkObject = BrainKey()
	newBrainkey = BrainKey(bkObject.suggest())
	result = {
		"brain_private_key": newBrainkey.get_brainkey(),
		"public_key": str(newBrainkey.get_public()),
		"private_key": str(newBrainkey.get_private())
	}
	return result

def create_account():
	# Prepare for new account name
	data = suggest_brain_key()
	data["account_name"] = ACCOUNT_PREFIX+RandomString(length=12, chars="d")

	# Create account
	bts_obj = BitShares(
		node=BITSHARES_NODE, 
		keys=REGISTRAR["private_key"], 
		nobroadcast=NOBROADCAST,
		bundle=False,
		debug=True)
	account = bts_obj.create_account(
		account_name=data["account_name"], 
		registrar=REGISTRAR["account_name"],
		referrer=REGISTRAR["account_name"],
		password=data["private_key"],
		storekeys=False)
	bts_obj.clear()
	
	print(" * Created new account: " + str(data))
	print(account)
	print()

def buy(ordertype, base, price, amount, expiration=None, killfill=False, 
	account=None, returnOrderId=False):
	from bitsharesbase.account import PasswordKey, PublicKey
	active_key = str(PasswordKey(
		account=MEMBER["account_name"], 
		password=MEMBER["password"], 
		role="active").get_private_key())
	bts_obj = BitShares(
		node=BITSHARES_NODE, 
		keys=active_key, 
		nobroadcast=NOBROADCAST)
	market = Market(base, bitshares_instance=bts_obj)
	order = market.buy(price, amount, expiration, killfill, account, returnOrderId)
	print(" * Placed order: " + str(market.buy(price, amount, expiration, 
		killfill, account, returnOrderId)))
	bts_obj.clear()
	print()

def fails():
	import time
	time.sleep(99999)
	create_account()
	buy("buy", ASSET, price=1, amount=1, account=MEMBER["account_name"])
	create_account()
	# bitshares.exceptions.MissingKeyError

fails()