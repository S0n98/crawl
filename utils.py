import json
from datetime import datetime

def read_url_from_file(file_path):
  list_url = []
  with open(file_path) as f:
    list_url = f.readlines()
  return [url.strip() for url in list_url]

def log(file_name, data):
    file_path = "./log/" + file_name
    if isinstance(data, dict) or isinstance(data, list):
        data = json.dumps(data)
    data += "\r\n"
    current_time = datetime.today().strftime('%Y/%m/%d %H:%M:%S')
    data = current_time + " : " + data
    with open(file_path, 'a') as log_file:
        log_file.write(data)