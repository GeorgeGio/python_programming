

class Band:


    number_of_bands = 0
    genre_list = ["pop","classical","rock"]

    def __init__(self,band_name,genre,albums_released=0):

        if item is not Band.genre_list:


            print(f"{genre} This is not a genre i know")
            #
            genre = "unkown genre"



        self.band_name = band_name
        self.albums_released = albums_released
        self.genre = genre
        Band.number_of_bands += 1

    def print_stats(self):
        print(f"The {self.genre} band {self.band_name} has {self.albums_released} albums")



my_band = Band("Queen","rock",15)
my_band.print_stats()
print(my_band.print_stats())
