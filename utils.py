

def read_url_from_file(file_path):
  list_url = []
  with open(file_path) as f:
    list_url = f.readlines()
  return [url.strip() for url in list_url]

