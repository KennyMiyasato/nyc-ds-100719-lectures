import csv 
import matplotlib.pyplot as plt
with open('data.csv') as f:
# we are using DictReader because we want our information to be in dictionary format.
    reader = csv.DictReader(f)
    # some more code
    #for row in reader:
    #    print(row['number'], row['year'], row['artist'])
    songs = [{'number':int(row['number']),
                  'year':int(row['year']),
                  'album':row['album'],
                  'artist':row['artist'],
                  'genre':row['genre'].split(', '),
                  'subgenre':row['subgenre'].split(', ')}
                for row in reader]

def findByName(album):
    for song in songs:
        if song['album'] == album:
            return song
    return None
    
def findByRank(rank):
    for song in songs:
        if song['number'] == rank:
            return song
    return {}

def findByYear(year):
    albums = []
    for song in songs:
        if song['year'] == year:
            albums.append(song)
    if albums:
        return albums
    else:
        return []
    
def findByYears(startYear,endYear):
    results = []
    for year in list(range(startYear,endYear+1)):
        results.extend(findByYear(year))
    if results:
        return results
    else:
        return []
    
#def findByRanks(startRank,endRank):
#    rankResults = []
#    for rank in list(range(startRank,endRank+1)):
#        #print(findByRank(rank))
#        rankResults.extend(findByRank(rank))
#        #print(' ')
#        #print(rankResults)
#        #print(' ')
#    if rankResults:
#        return rankResults
#    else:
#        return None
    
def findByRanks(start_rank,end_rank):
    result = [findByRank(rank) for rank in list(range(start_rank,end_rank+1))]
    return result if result else []

def allTitles():
    titles = []
    for song in songs:
        titles.append(song['album'])
    return titles

def allArtists():
    artists = []
    for song in songs:
        artists.append(song['artist'])
    return artists

def topArtist():
    uniq_artists = list(set(all_artists()))
    counts = {}
    for artist in uniq_artists:
        counts[artist] = all_artists().count(artist)
    count = 0
    top = None
    for key, value in counts.items():
        if value > count:
            count = value
            top = key
    return top

def mostPopularWord():
    allWords=[]
    for title in allTitles():
        allWords.extend(title.lower().split())
        
    uniqueWords = list(set(allWords))
    counts = {}
    for word in uniqueWords:
        counts[word] = allWords.count(word)
    count = 0
    top = None
    for key, value in counts.items():
        if value > count:
            count = value
            top = key
    return top

def __decades():
    start = 1950
    decades= []
    for index in list(range(0,7)):
        decades.append((start,start+9))
        start += 10
    return decades

def plotHistAlbums():
    histData = {}
    for decade in __decades():
        histData[f'{decade[0]} - {decade[1]}'] = len(findByYears(decade[0],decade[1]))
#    print(result)
    decades = []
    numberAlbums = []
    for key, value in histData.items():
        decades.append(key)
        numberAlbums.append(value)
    
        
#    plt.figure(figsize =(8,6))
#    plt.hist(number_albums,bins=len(decades), edgecolor = 'black')
#    plt.xticks(number_albums, decades)
#    plt.show()
        
    all_years = [song['year'] for song in songs]
        
    plt.figure(figsize =(10,6))
    plt.hist(all_years,bins=8, edgecolor = 'black')
    plt.axis([1950,2020,0,200])
    plt.xticks(mid_decade_yr,mid_decade_yr)
    plt.xlabel('Year')
    plt.ylabel('Number of Albums')
    plt.title('Albums released by year')
    plt.show()

