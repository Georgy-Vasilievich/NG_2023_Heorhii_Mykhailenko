import urllib.request

def getUrlStatus(urlList):
	for url in urlList:
		try:
			status = urllib.request.urlopen(url).getcode()

			if status == 200 or status == 302:
				print("OK")
				continue
		except urllib.error.HTTPError as e:
			pass

		print("FAIL")
