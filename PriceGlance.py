import xml.etree.ElementTree as ET
import urllib.request
import urllib.error
import sys

import argparse
parser=argparse.ArgumentParser(
	description="PriceGlance is a python utility for quickly retrieving data for Market Quick Views",
	epilog= "https://github.com/Azeranth/PriceGlance")
parser.add_argument("--database", help="Item ID and display name database file. Defaults to 'ItemTypeDatabase' in install directory")
parser.add_argument("file", nargs='+', help="File containing Market Quick View config")
args=parser.parse_args()

def RequestFromIdList(_idList):
	print("Requesting " + _idList + "...")
	return urllib.request.Request("https://api.evemarketer.com/ec/marketstat?typeid=" + _idList, headers={'User-Agent': 'Mozilla/5.0'})

def GetTreeFromRequest(_request):
	try:
		return ET.fromstring(urllib.request.urlopen(_request, timeout=10).read())
	except urllib.error.HTTPError:
		print("Failed to retrieve requested data")
		raise SystemExit(129)

def ImportDb(path=sys.path[0] + "/ItemTypeDatabase"):
	_db = {}
	with open(path, "r", encoding="utf8") as idbh:
		for line in idbh:
			_db[line.split(' ')[0]] = ' '.join(line.split(' ')[1:]).rstrip()
	return _db

def ExportDb(_db ,path=sys.path[0] + "/ItemTypeDatabase"):
	with open(path, "w", encoding="utf8") as idbh:
		for record in _db:
			idbh.write(record + ' ' + _db[record] + '\n')

def LoadQuickView(path):
	with open(path, "r", encoding="utf8")as mqvh:
		lines = mqvh.read().split('\n')
		lines[0] = lines[0].split(',')
		lines[0] = [int(i) for i in lines[0]]
		return lines

DbPath = args.database if args.database else sys.path[0] + "/ItemTypeDatabase"
TypeDbDict = ImportDb()
viewList = args.file
print(args.file)

for viewPath in viewList:
	view = LoadQuickView(viewPath)
	for idList in view[1:]:
		for typeResult in GetTreeFromRequest(RequestFromIdList(idList)).findall(".//type"):
			print(TypeDbDict[typeResult.get("id")])
			print("\tBuy")
			for field in view[0]:
				print('\t' + typeResult[0][field].tag[:7] + "\t: " + typeResult[0][field].text)
			print("\tSell")
			for field in view[0]:
				print('\t' + typeResult[1][field].tag[:7] + "\t: " + typeResult[1][field].text)