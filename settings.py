import random

TOKEN = "5045841524:AAEPe3fQ7qOebErRgQlvayImGsYpkRpYNHc"


class Data:
    def __init__(self) -> None:
        self.compliment_file_path = 'data/compliment.txt'
        self.photo_file_path = 'data/photos.txt'
    

    def get_random_compliment(self) -> str:
        with open(self.compliment_file_path) as f:
            f = f.readlines()
        random.shuffle(f)
        return f[0][:-1]
    

    def get_random_photo(self) -> str:
        with open(self.photo_file_path) as f:
            f = f.readlines()
        random.shuffle(f)
        return f[0][:-1]
    

    def pull_photo_txt_fill(self) -> None:
        with open(self.photo_file_path, mode='w') as f:
            f.write('\n'.join(['data/photos/photo_' + str(i) + '.jpeg' for i in range(1, 20)]) + '\n')
            f.close()
    

if __name__ == "__main__":
    d = Data()
    print(d.get_random_compliment())
    d.pull_photo_txt_fill()