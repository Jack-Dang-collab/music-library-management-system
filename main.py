import data_storage
import music_library
import user_interface

# Load data
tracks, playlists = data_storage.load_data()

# Create instances
library = music_library.MusicLibrary(tracks, playlists)
ui = user_interface.UserInterface(library)

# Run the program
ui.run()

# Save data
data_storage.save_data(library.tracks, library.playlists)
