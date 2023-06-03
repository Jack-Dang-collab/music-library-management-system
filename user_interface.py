class UserInterface:
  # ANSI escape codes for colors
  MAIN_COLOR = "\033[38;5;208m"
  GREEN = "\033[92m"
  YELLOW = "\033[33m"
  RED = "\033[91m"
  RESET_COLOR = "\033[0m"

  def __init__(self, music_library):
    self.music_library = music_library

  def get_colored_text(self, color, text):
    return f'{color}{text}{self.RESET_COLOR}'

  def main_menu(self):
    print(self.get_colored_text(self.MAIN_COLOR, '----------------------------------- MUSIC LIBRARY MANAGEMENT SYSTEM -----------------------------------'))
    print(self.get_colored_text(self.MAIN_COLOR, '1. Add New Track'))
    print(self.get_colored_text(self.MAIN_COLOR, '2. View All Tracks'))
    print(self.get_colored_text(self.MAIN_COLOR, '3. Update Track'))
    print(self.get_colored_text(self.MAIN_COLOR, '4. Delete Track'))
    print(self.get_colored_text(self.MAIN_COLOR, '5. Create Playlist'))
    print(self.get_colored_text(self.MAIN_COLOR, '6. Add Track to Playlist'))
    print(self.get_colored_text(self.MAIN_COLOR, '7. Delete Playlist'))
    print(self.get_colored_text(self.MAIN_COLOR, '8. View All Playlists'))
    print(self.get_colored_text(self.MAIN_COLOR, '9. Search Music'))
    print(self.get_colored_text(self.MAIN_COLOR, '10. Exit'))

  def run(self):
    while True:
      self.main_menu()
      choice = input(self.get_colored_text(self.MAIN_COLOR, 'Enter your choice (1-10): '))

      if choice == '1':
        self.music_library.add_track()
      elif choice == '2':
        self.music_library.display_tracks()
      elif choice == '3':
        self.music_library.update_track()
      elif choice == '4':
        self.music_library.delete_track()
      elif choice == '5':
        self.music_library.create_playlist()
      elif choice == '6':
        self.music_library.add_track_to_playlist()
      elif choice == '7':
        self.music_library.delete_playlist()
      elif choice == '8':
        self.music_library.view_all_playlists()
      elif choice == '9':
        self.music_library.search_music()
      elif choice == '10':
        print(self.get_colored_text(self.MAIN_COLOR, 'Exiting...'))
        break
      else:
        print(self.get_colored_text(self.RED, 'Invalid choice. Please try again.'))
