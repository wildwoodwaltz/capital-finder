from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    url_components = parse.urlsplit(self.path)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)

    if "name" in dic:
      url = "https://restcountries.com/v3.1/capital/"
      query = dic["name"]

      response = requests.get(url + dic["name"])
      
      data = response.json()
      
      country = data[0]["name"]
      ans = str(country["common"])
      results = f"{query} is the capital of {ans}"

      self.send_response(200)
      self.send_header("Content-type","text/plain")
      self.end_headers()

      self.wfile.write(results.encode())

    return
