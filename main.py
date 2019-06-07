#Install module first
#pip install google_images_download
from google_images_download import google_images_download

print '==============[Download Gambar]==============\n'
keywordCariGambar = raw_input('Keyword Gambar: ')
limitCariGambar = raw_input('Berapa banyak gambar yang ingin diunduh? ')

respone = google_images_download.googleimagesdownload()

search_queries = [keywordCariGambar]

def downloadimages(query):
	arguments = {"keywords": query, "format": "jpg", "limit": limitCariGambar, "print_urls": True, "size": "medium"}
	try:
		respone.download(arguments)
	except FileNotFoundError:
		arguments = {"keywords": query, "format": "jpg", "limit": limitCariGambar, "print_urls": True, "size": "medium"}
		try:
			respone.download(arguments)
		except:
			pass

for query in search_queries:
	downloadimages(query)
	print()