import os

def extract_place_old(filename):
    first = filename.find('_')
    partial = filename[first + 1:]
    second = partial.find('_')
    return partial[:second]

def extract_place(filename):
    return filename.split("_")[1]

def make_place_directories(places):
    for place in places:
        if not os.path.exists(place):
            os.mkdir(place)

def organzie_photos(directory):
    os.chdir(directory)
    originals = os.listdir()
    places = []
    for filename in originals:
        places.append(extract_place(filename))
    make_place_directories(set(places))
    for filename in originals:
        place = extract_place(filename)
        os.rename(filename, os.path.join(place, filename))

if __name__ == '__main__':
    organzie_photos('photos')