from functools import namedtuple

Tile = namedtuple('Tile', ['top', 'bottom'])

def calculateDominoTiles(tiles):
    res = 0
    for index, tile in zip(range(len(tiles)), tiles):
        try:
            if tile.bottom != tiles[index + 1].top:
                return -1
        except IndexError:
            pass
        res += tile.top + tile.bottom
    return res

print(calculateDominoTiles([Tile(3,3)]))
print(calculateDominoTiles([Tile(3,3), Tile(3,5)]))
print(calculateDominoTiles([Tile(3,3), Tile(3,4), Tile(5,1)]))