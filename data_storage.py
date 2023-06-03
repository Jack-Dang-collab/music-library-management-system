import json

def save_data(tracks, playlists):
  data = {
    'tracks': tracks,
    'playlists': playlists
  }
  with open('data.json', 'w') as file:
    json.dump(data, file)

def load_data():
  try:
    with open('data.json', 'r') as file:
      data = json.load(file)
      return data['tracks'], data['playlists']
  except FileNotFoundError:
    return [], []
