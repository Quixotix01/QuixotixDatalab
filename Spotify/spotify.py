# creating dataset and analsying


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import requests

# Spotify API credentials
client_id = 'client id' #replace with your client id
client_secret = 'secret id' #replace with your client_secret id

# Authenticate with Spotify
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# List of Tamil artists
artists = ['Ilayaraja', 'A.R. Rahman', 'Yuvan Shankar Raja', 'Harris Jayaraj',
           'Vijay Antony', 'G.V. Prakash', 'Santhosh Narayanan', 'Anirudh Ravichander',
           'Hiphop Tamizha','Sean Roldan', 'Sam C.S.', 'Devi Sri Prasad', 'Ghibhran', 'Thaman']

# Function to get top tracks
def get_top_tracks(artist_name):
    results = sp.search(q=artist_name, type='artist')
    artist_id = results['artists']['items'][0]['id']
    top_tracks = sp.artist_top_tracks(artist_id)
    track_info = []
    for track in top_tracks['tracks']:
        track_info.append({
            'artist_name': artist_name,
            'track_name': track['name'],
            'popularity': track['popularity'],
            'duration_ms': track['duration_ms'],
            'album': track['album']['name'],
            'release_date': track['album']['release_date'],
'collaborating_artist': track['artists'][1]['name'] if len(track['artists']) > 1 else None,
            'explicit': track['explicit'],
            # Check if 'available_markets' exists before accessing it
            'number_of_markets': track['available_markets'] if 'available_markets' in track else None,  # Add this line
            'available_markets': ', '.join(track['available_markets']) if 'available_markets' in track else None  # Add this line
            })
    return track_info

# Collect data for all artists
all_data = []
for artist in artists:
    artist_tracks = get_top_tracks(artist)
    all_data.extend(artist_tracks)
    print(f"Data for {artist} collected.")

# Create a DataFrame
df = pd.DataFrame(all_data)
print(df)

# Save data to CSV
df = pd.DataFrame(all_data)
df.to_csv('tamil_music_artists_top_tracks.csv', index=False)

"""**Step 2: Analyze Popularity Over Time**

To determine the trending artist for each year, you can simulate this by aggregating popularity scores for each artist by year.
"""

df['year'] = pd.to_datetime(df['release_date'], format='%Y-%m-%d', errors='coerce').dt.year

# Aggregate popularity by artist and year
trending_by_year = df.groupby(['year', 'artist_name'])['popularity'].sum().reset_index()

# Determine the top artist for each year
trending_artist = trending_by_year.loc[trending_by_year.groupby('year')['popularity'].idxmax()]

# Save trending artist data to CSV
trending_artist.to_csv('spotify_trending_artist_by_year.csv', index=False)

"""**Step 3: Create Visualization**

Now, let's visualize the trends over the years. You can use matplotlib or seaborn to create a line plot or bar plot showing the top trending artist for each year.
"""

import matplotlib.pyplot as plt
import seaborn as sns

# Set the plot style
sns.set(style="whitegrid")

# Plot a bar plot of the trending artist by year
plt.figure(figsize=(12, 6))
sns.barplot(x='year', y='popularity', hue='artist_name', data=trending_artist, palette='viridis')
plt.title('Spotify Trending Artist by Year')
plt.ylabel('Total Popularity Score')
plt.xlabel('Year')
plt.xticks(rotation=45)
plt.legend(title='Artist', bbox_to_anchor=(1, 1), loc='upper left')

# Save the plot
plt.tight_layout()
#plt.savefig('trending_artist_by_year.png')
plt.show()

import os
if not os.path.exists('artist_plots'):
    os.makedirs('artist_plots')

# Plot top tracks for each artist
for artist in df['artist_name'].unique():
    artist_data = df[df['artist_name'] == artist].sort_values(by='popularity', ascending=False)

    # Create the plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x='popularity', y='track_name', data=artist_data, palette='muted')

    # Set the plot titles and labels
    plt.title(f"Top Tracks of {artist}", fontsize=16)
    plt.xlabel('Popularity', fontsize=14)
    plt.ylabel('Track Name', fontsize=14)

    # Save the plot as an image file
    plt.tight_layout()
    plt.savefig(f'artist_plots/{artist}_top_tracks.png')  # Save the plot for the current artist

    plt.close()  # Close the plot to free up memory

"""**Artist Popularity Over Time**

A line plot showing the total popularity of each artist per year
"""

# Group the data by artist and year
df['year'] = pd.to_datetime(df['release_date'], format='%Y-%m-%d', errors='coerce').dt.year
popularity_by_year = df.groupby(['year', 'artist_name'])['popularity'].sum().reset_index()

# Plot the popularity trend over time for each artist
plt.figure(figsize=(12, 6))
sns.lineplot(x='year', y='popularity', hue='artist_name', data=popularity_by_year, marker='o', palette='tab10')
plt.title('Artist Popularity Over Time')
plt.ylabel('Total Popularity')
plt.xlabel('Year')
plt.xticks(rotation=45)
plt.legend(title='Artist', bbox_to_anchor=(1, 1), loc='upper left')
plt.tight_layout()
#plt.savefig('popularity_over_time.png')
plt.show()

"""**Track Duration vs. Popularity**

A scatter plot with track duration on the x-axis and popularity on the y-axis.
"""

plt.figure(figsize=(10, 6))
sns.scatterplot(x='duration_ms', y='popularity', hue='artist_name', data=df, palette='Set2', s=100)
plt.title('Track Duration vs Popularity')
plt.xlabel('Duration (ms)')
plt.ylabel('Popularity')
plt.tight_layout()
#plt.savefig('duration_vs_popularity.png')
plt.show()

"""**Distribution of Popularity Scores**

A box plot showing the distribution of popularity scores for each artist.
"""

plt.figure(figsize=(12, 6))
sns.boxplot(x='artist_name', y='popularity', data=df, palette='pastel')
plt.title('Distribution of Popularity Scores by Artist')
plt.ylabel('Popularity')
plt.xlabel('Artist')
plt.xticks(rotation=45)
plt.tight_layout()
#plt.savefig('popularity_distribution.png')
plt.show()

"""**Top Albums per Artist**

A grouped bar plot showing the popularity of different albums by artist
"""

# Group by artist and album
album_popularity = df.groupby(['artist_name', 'album'])['popularity'].sum().reset_index()

# Plot
plt.figure(figsize=(14, 7))
sns.barplot(x='popularity', y='album', hue='artist_name', data=album_popularity, palette='husl')
plt.title('Top Albums by Artist')
plt.xlabel('Total Popularity')
plt.ylabel('Album')
plt.tight_layout()
#plt.savefig('top_albums_by_artist.png')
plt.show()

"""**Heatmap of Artist Collaboration**

A heatmap showing the frequency of collaborations between different artists.
"""

# Create a matrix of artist collaborations (if data contains collaborations)
collaboration_matrix = pd.crosstab(df['artist_name'], df['collaborating_artist'])  # Assuming you have this column
plt.figure(figsize=(10, 8))
sns.heatmap(collaboration_matrix, annot=True, cmap='coolwarm', fmt='d')
plt.title('Artist Collaboration Heatmap')
plt.tight_layout()
#plt.savefig('artist_collaboration_heatmap.png')
plt.show()

"""**Top Tracks by Market Availability**

A bar plot showing the number of markets where each artist's top tracks are available.
"""

# Calculate the number of markets where tracks are available
df['number_of_markets'] = df['available_markets'].apply(lambda x: len(x) if x is not None else 0)
# Use a lambda function to handle None values - if the value is None, assign 0, otherwise calculate the length.

plt.figure(figsize=(10, 6))
sns.barplot(x='artist_name', y='number_of_markets', data=df, estimator='mean', palette='Blues_d')
plt.title('Average Market Availability by Artist')
plt.ylabel('Number of Markets')
plt.xlabel('Artist')
plt.xticks(rotation=45)
plt.tight_layout()
#plt.savefig('market_availability.png')
plt.show()

"""**Explicit Content Analysis**

A pie chart showing the ratio of explicit to non-explicit tracks
"""

plt.figure(figsize=(6, 6))
explicit_count = df['explicit'].value_counts()
explicit_count.plot.pie(autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'], labels=['Non-Explicit', 'Explicit'])
plt.title('Explicit vs Non-Explicit Tracks')
plt.tight_layout()
#plt.savefig('explicit_content_pie.png')
plt.show()
