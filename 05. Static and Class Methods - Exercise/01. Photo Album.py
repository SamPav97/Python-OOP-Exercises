from math import ceil
class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for page in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(ceil(photos_count/4))

    def add_photo(self, label):
        count = 0
        for ind_page in range(len(self.photos)):
            count += 1
            if len(self.photos[ind_page]) >= 4:
                continue
            else:
                self.photos[ind_page].append(label)
                return f"{label} photo added successfully on page " \
                       f"{count} slot {len(self.photos[ind_page])}"
        return "No more free slots"

    def display(self):
        res = "-----------"+"\n"
        for page in self.photos:
            temp = []
            for _ in page:
                temp.append("[]")
            res += " ".join(temp)
            res += "\n""-----------""\n"
        return res


album = PhotoAlbum(4)

print(album.from_photos_count(8))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.add_photo("party with friends"))
print(album.add_photo("party with friends"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())


