def make_album(singerName, albumName, songNumber=''):
    albumInfo = {'singer': singerName, 'album': albumName}
    if songNumber:
        albumInfo["amount"] = songNumber
    return albumInfo


while True:
    print("Please enter the album info: ")
    print("(Enter 'q' to quit.)")
    a = input("Please enter the singer name: ")
    if a == 'q':
        break
    b = input("Please enter the album name: ")
    if b == 'q':
        break
    c = input("Please enter the number of the songs: ")
    if c == 'q':
        break
    album = make_album(a, b, c)
    print(album)
