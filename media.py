class Movie:
    """Class to handle movies"""

    # Constructor, initialize movie with parameters
    def __init__(self, title, year, summary, poster_image_url, trailer_youtube_url):
        self.title = title
        self.year = year
        self.summary = summary
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
    
    # Trigger browser to open the YouTube trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)