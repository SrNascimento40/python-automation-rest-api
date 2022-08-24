import requests

url = "https://spotify23.p.rapidapi.com/artist_singles/"

querystring = {"id":"7L6u6TyhjuwubrcojPeNgf","offset":"0","limit":"20"}

key = input('Insira a key')

headers = {
	"X-RapidAPI-Key": key,
	"X-RapidAPI-Host": "spotify23.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
