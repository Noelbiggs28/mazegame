
class High_Scores():
    def __init__(self):
        self.high_scores = []

    # Load high scores from a file (if any)
    def load_high_scores(self, file_path):
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    name, score = line.strip().split(',')
                    self.high_scores.append((name, int(score)))
        except FileNotFoundError:
            pass

    # Save high scores to a file
    @staticmethod
    def save_high_scores(file_path, list_of_scores):
        list_of_scores.sort(key=lambda x: x[1], reverse=True)
        list_of_scores = list_of_scores[:5]
        with open(file_path, 'w') as file:
            for name, score in list_of_scores:
                file.write(f"{name},{score}\n")

        return list_of_scores


