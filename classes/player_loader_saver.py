import csv

class Player_Data:
    @staticmethod
    def load_player_stats(file_name):
        player_stats = []
        with open(file_name, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                player_stats.append(row)
        return player_stats
    
    @staticmethod
    def save_player_stats(file_name, player_stats):
        fieldnames = player_stats[0].keys()
        with open(file_name, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(player_stats)
    
    @staticmethod
    def create_player(file_name, default_stats):
        with open(file_name, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=default_stats.keys())
            writer.writeheader()
            writer.writerow(default_stats)

    @staticmethod
    def change_num_stat(profile, key, num):
        temp = profile[key] 
        temp = int(temp)
        temp += num
        return temp