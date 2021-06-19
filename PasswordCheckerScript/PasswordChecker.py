import requests
import hashlib
import sys

def  req_api_data(query_char):
	url = 'https://api.pwnedpasswords.com/range/' + query_char
	res = requests.get(url)

	if res.status_code != 200:
		raise RuntimeError(f'ERROR FETCHING: {res.status_code}, CHECK API AND TRY AGAIN')
	return res

def get_count(hashes, tail_hash):
	hashes =  (line.split(':') for line in hashes.text.splitlines())
	for h, count in hashes:
		if h == tail_hash:
			return count
	return 0

def api_check(password):
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	first5_char, tail = sha1password[:5], sha1password[5:]
	response = req_api_data(first5_char)
	return get_count(response, tail)

def main(args):
	for password in args:
		count = api_check(password)
		if count:
			print(f'{password} has been hacked {count} times, time to change your password')
		else:
			print(f'{password} is secure')
	return 'done'

if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))