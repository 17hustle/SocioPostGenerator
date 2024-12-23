import json
import pandas as pd

class FewShots():
    def __init__(self, file_path="PostGen/data/processed_posts.json"):  # Fixed typo in __init__
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)  # Automatically load posts during initialization

    def load_posts(self, file_path):
        with open(file_path, encoding="utf-8") as f:
            posts = json.load(f)
            df = pd.json_normalize(posts)  # Fixed typo in `pd.json.normalize`
            # Adding a column called as length in the existing df
            df["length"] = df["line_count"].apply(self.categorize_length)  # Fixed self.df to df
            all_tags = df['tags'].apply(lambda x: x).sum()  # Fixed self.df to df
            self.unique_tags = set(list(all_tags))  # Removes duplicate tag items
            self.df = df

    def categorize_length(self, line_count):
        if line_count < 5:
            return "Short"
        elif 5 <= line_count <= 10:
            return "Medium"
        else:
            return "Long"

    def get_tags(self):
        return self.unique_tags

    def get_filtered_posts(self, length, language, tag):
        df_filtered = self.df[
            (self.df['language'] == language) &
            (self.df['length'] == length) &
            (self.df['tags'].apply(lambda tags: tag in tags))
        ]
        return df_filtered.to_dict(orient="records")  # Fixed typo "record" to "records"

if __name__ == "__main__":
    fs = FewShots()
    posts = fs.get_filtered_posts("Short", "English", "Job Search")
    print(posts)
