import requests

url = "https://spotify23.p.rapidapi.com/artist_singles/"

querystring = {"id":"7L6u6TyhjuwubrcojPeNgf","offset":"0","limit":"20"}

headers = {
	"X-RapidAPI-Key": "a43789bc5emshd1679925331c266p1cba21jsn76d120ed7583",
	"X-RapidAPI-Host": "spotify23.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)