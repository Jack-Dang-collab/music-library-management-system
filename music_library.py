from user_interface import UserInterface

class MusicLibrary(UserInterface):

  def __init__(self, tracks, playlists):
    super().__init__(self)
    self.tracks = tracks
    self.playlists = playlists

  def display_tracks(self):
    if not self.tracks:
      print(self.get_colored_text(self.YELLOW, 'No tracks found.'))
      return

    print(self.get_colored_text(self.MAIN_COLOR, '--- All tracks ---'))
    for track in self.tracks:
      self.print_track_details(track)
      print('')

  def print_track_details(self, track):
    print(self.get_colored_text(self.MAIN_COLOR, f'Title: {track["title"]}'))
    print(self.get_colored_text(self.GREEN, f'Artist: {track["artist"]}'))
    print(self.get_colored_text(self.GREEN, f'Album: {track["album"]}'))
    print(self.get_colored_text(self.GREEN, f'Genre: {track["genre"]}'))
    print(self.get_colored_text(self.GREEN, f'Release Year: {track["release_year"]}'))
    print(self.get_colored_text(self.GREEN, f'Duration: {track["duration"]}'))

  def add_track(self):
    print(self.get_colored_text(self.MAIN_COLOR, '--- Add New Track ---'))
    title = input(self.get_colored_text(self.GREEN, 'Title: '))
    artist = input(self.get_colored_text(self.GREEN, 'Artist: '))
    album = input(self.get_colored_text(self.GREEN, 'Album: '))
    genre = input(self.get_colored_text(self.GREEN, 'Genre: '))
    release_year = input(self.get_colored_text(self.GREEN, 'Release Year: '))
    duration = input(self.get_colored_text(self.GREEN, 'Duration: '))

    track = {
      'title': title,
      'artist': artist,
      'album': album,
      'genre': genre,
      'release_year': release_year,
      'duration': duration
    }
    self.tracks.append(track)
    print(self.get_colored_text(self.GREEN, 'Track added successfully.'))

  def update_track(self):
    print(self.get_colored_text(self.MAIN_COLOR, '--- Update Track ---'))
    title = input(self.get_colored_text(self.MAIN_COLOR, 'Enter the title of the track to update: '))

    for track in self.tracks:
      if track['title'].lower() == title.lower():
        print(self.get_colored_text(self.GREEN, 'Track found. Enter the new details:'))
        track['title'] = input(self.get_colored_text(self.GREEN, f'Title ({track["title"]}): ')) or track['title']
        track['artist'] = input(self.get_colored_text(self.GREEN, f'Artist ({track["artist"]}): ')) or track['artist']
        track['album'] = input(self.get_colored_text(self.GREEN, f'Album ({track["album"]}): ')) or track['album']
        track['genre'] = input(self.get_colored_text(self.GREEN, f'Genre ({track["genre"]}): ')) or track['genre']
        track['release_year'] = input(self.get_colored_text(self.GREEN, f'Release Year ({track["release_year"]}): ')) or track['release_year']
        track['duration'] = input(self.get_colored_text(self.GREEN, f'Duration ({track["duration"]}): ')) or track['duration']

        print(self.get_colored_text(self.GREEN, 'Track updated successfully.'))
        return

    print(self.get_colored_text(self.YELLOW, 'Track not found.'))

  def delete_track(self):
    print(self.get_colored_text(self.MAIN_COLOR, '--- Delete Track ---'))
    title = input(self.get_colored_text(self.MAIN_COLOR, 'Enter the title of the track to delete: '))

    deleted_from_playlists = []  # Store the playlists from which the track is deleted

    for playlist in self.playlists:
      for track in playlist['tracks']:
        if track['title'].lower() == title.lower():
          playlist['tracks'].remove(track)
          deleted_from_playlists.append(playlist['name'])

    if deleted_from_playlists:
      print(self.get_colored_text(self.MAIN_COLOR, 'Track removed from the following playlists:'))
      for playlist_name in deleted_from_playlists:
        print(self.get_colored_text(self.GREEN, playlist_name))
    
    # Remove the track from the main track list
    for track in self.tracks:
      if track['title'].lower() == title.lower():
        self.tracks.remove(track)
        print(self.get_colored_text(self.GREEN, 'Track deleted successfully.'))
        return

    print(self.get_colored_text(self.YELLOW, 'Track not found.'))

  def create_playlist(self):
    print(self.get_colored_text(self.MAIN_COLOR, '--- Create Playlist ---'))
    name = input(self.get_colored_text(self.MAIN_COLOR, 'Enter the name of the playlist: '))
    playlist = {
      'name': name,
      'tracks': []
    }
    self.playlists.append(playlist)
    print(self.get_colored_text(self.GREEN, 'Playlist created successfully.'))

  def add_track_to_playlist(self):
    print(self.get_colored_text(self.MAIN_COLOR, '--- Add Track to Playlist ---'))
    track_title = input(self.get_colored_text(self.MAIN_COLOR, 'Enter the title of the track to add: '))

    for playlist in self.playlists:
      print(self.get_colored_text(self.MAIN_COLOR, f'--- {playlist["name"]} ---'))
      print(self.get_colored_text(self.MAIN_COLOR, 'Tracks:'))
      for track in playlist['tracks']:
          print(self.get_colored_text(self.GREEN, track['title']))
      print(self.get_colored_text(self.MAIN_COLOR, '---'))

    playlist_name = input(self.get_colored_text(self.MAIN_COLOR, 'Enter the name of the playlist to add the track to: '))

    for playlist in self.playlists:
      if playlist['name'].lower() == playlist_name.lower():
        for track in self.tracks:
          if track['title'].lower() == track_title.lower():
            playlist['tracks'].append(track)
            print(self.get_colored_text(self.GREEN, 'Track added to playlist successfully.'))
            return

    print(self.get_colored_text(self.YELLOW, 'Playlist or track not found.'))

  def view_all_playlists(self):
    if not self.playlists:
      print(self.get_colored_text(self.YELLOW, 'No playlists found.'))
      return

    print(self.get_colored_text(self.MAIN_COLOR, '--- All Playlists ---'))
    for playlist in self.playlists:
      print(self.get_colored_text(self.MAIN_COLOR, f'Playlist: {playlist["name"]}'))
      print(self.get_colored_text(self.MAIN_COLOR, 'Tracks:'))
      if not playlist['tracks']:
        print(self.get_colored_text(self.YELLOW, 'No tracks found.'))
      else:
        for track in playlist['tracks']:
          self.print_track_details(track)
      print(self.get_colored_text(self.MAIN_COLOR, '--------------------'))

  def search_music(self):
    print(self.get_colored_text(self.MAIN_COLOR, '--- Search Music ---'))
    search_query = input(self.get_colored_text(self.MAIN_COLOR, 'Enter the search query: '))

    matching_tracks = []
    matching_playlists = []

    for track in self.tracks:
      if (
        search_query.lower() in track['title'].lower() or
        search_query.lower() in track['artist'].lower() or
        search_query.lower() in track['album'].lower() or
        search_query.lower() in track['genre'].lower()
      ):
        matching_tracks.append(track)

    for playlist in self.playlists:
      if search_query.lower() in playlist['name'].lower():
        matching_playlists.append(playlist)

    if matching_tracks:
      print(self.get_colored_text(self.MAIN_COLOR, f'--- Matching Tracks for "{search_query}" ---'))
      for track in matching_tracks:
        self.print_track_details(track)
        print(self.get_colored_text(self.MAIN_COLOR, '---'))
    else:
      print(self.get_colored_text(self.YELLOW, 'No matching tracks found.'))

    if matching_playlists:
      print(self.get_colored_text(self.MAIN_COLOR, f'--- Matching Playlists for "{search_query}" ---'))
      for playlist in matching_playlists:
        print(self.get_colored_text(self.MAIN_COLOR, f'Playlist: {playlist["name"]}'))
        print(self.get_colored_text(self.MAIN_COLOR, 'Tracks:'))
        if not playlist['tracks']:
          print(self.get_colored_text(self.YELLOW, 'No tracks found.'))
        else:
          for track in playlist['tracks']:
            print(self.get_colored_text(self.MAIN_COLOR, '-'))
            self.print_track_details(track)
            print(self.get_colored_text(self.MAIN_COLOR, '-'))
        print(self.get_colored_text(self.MAIN_COLOR, '---'))
    else:
      print(self.get_colored_text(self.YELLOW, 'No matching playlists found.'))

  def delete_playlist(self):
    print(self.get_colored_text(self.MAIN_COLOR, '--- Delete Playlist ---'))
    playlist_name = input(self.get_colored_text(self.MAIN_COLOR, 'Enter the name of the playlist to delete: '))

    for playlist in self.playlists:
      if playlist['name'].lower() == playlist_name.lower():
        self.playlists.remove(playlist)
        print(self.get_colored_text(self.GREEN, 'Playlist deleted successfully.'))
        return

    print(self.get_colored_text(self.YELLOW, 'Playlist not found.'))