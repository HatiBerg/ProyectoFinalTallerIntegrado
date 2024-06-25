import csv
from streamers.models import Streamer

def import_streamers(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Streamer.objects.create(
                name = row['name'],
                language = row['language'],
                type = row['type'],
                most_streamed_game = row['most_streamed_game'],
                average_stream_duration	 = row['average_stream_duration'],
                followers_gained_per_stream = row['followers_gained_per_stream'],
                avg_viewers_per_stream = row['avg_viewers_per_stream'],
                avg_games_per_stream = row['avg_games_per_stream'],
                total_time_streamed = row['total_time_streamed'],
                total_followers = row['total_followers'],
                total_views = row['total_views'],
                total_games_streamed = row['total_games_streamed'],
                active_days_per_week = row['active_days_per_week'],
                most_active_day = row['most_active_day'],
                day_with_most_followers_gained = row['day_with_most_followers_gained']
            )

if __name__ == '__main__':
    csv_file_path = 'C:/Users/resid/GitHub/ProyectoFinalTallerIntegrado/dataset_updated.csv'
    import_streamers(csv_file_path)