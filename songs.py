import tkinter as tk
from tkinter import messagebox
import requests

# Function to fetch lyrics
def get_lyrics():
    song_title = entry_title.get()
    artist_name = entry_artist.get()

    if not song_title or not artist_name:
        messagebox.showwarning("Input Error", "Please enter both song title and artist name.")
        return 

    try:
        lyrics = fetch_lyrics(song_title, artist_name)
        if lyrics:
            text_lyrics.delete(1.0, tk.END)
            text_lyrics.insert(tk.END, lyrics)
        else:
            messagebox.showinfo("No Lyrics Found", "Could not find lyrics for the specified song.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to fetch lyrics from Genius API
def fetch_lyrics(title, artist):
    api_key = "DpmPkxHlewaLEXJlJ2ICQl_HSueU3dKh9uE9"  # Replace with your Genius API key
    base_url = "https://genius.com"
    search_url = f"{base_url}"
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {"q": f"{title} {artist}"}

    response = requests.get(search_url, headers=headers, params=data)
    response.raise_for_status()
    hits = response.json()["response"]["hits"]
    if hits:
        song_path = hits[0]["result"]["path"]
        song_url = f"{base_url}{song_path}"
        song_response = requests.get(song_url)
        song_response.raise_for_status()
        lyrics = song_response.json()["response"]["song"]["lyrics"]
        return lyrics
    return None

# Set up the GUI
root = tk.Tk()
root.title("Lyrics Finder")

label_title = tk.Label(root, text="Song Title:")
label_title.grid(row=0, column=0, padx=10, pady=10)
entry_title = tk.Entry(root, width=50)
entry_title.grid(row=0, column=1, padx=10, pady=10)

label_artist = tk.Label(root, text="Artist Name:")
label_artist.grid(row=1, column=0, padx=10, pady=10)
entry_artist = tk.Entry(root, width=50)
entry_artist.grid(row=1, column=1, padx=10, pady=10)

button_fetch = tk.Button(root, text="Fetch Lyrics", command=get_lyrics)
button_fetch.grid(row=2, column=0, columnspan=2, pady=20)

text_lyrics = tk.Text(root, wrap=tk.WORD, width=60, height=20)
text_lyrics.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
