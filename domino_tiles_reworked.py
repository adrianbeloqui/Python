from functools import namedtuple

Tile = namedtuple('Tile', ['top', 'bottom'])

def placeDominoTile(tiles, newTile):
    if not tiles:
        return [newTile]
    elif len(tiles) == 1:
        if tiles[0].bottom == newTile.top:
            tiles.append(newTile)
            return tiles
        elif tiles[0].top == newTile.bottom:
            tiles.insert(0, newTile)
            return tiles
    else:
        for index, tile in enumerate(tiles):
            try:
                if tile.bottom == newTile.top and newTile.bottom == tiles[index + 1].top:
                    tiles.insert(index + 1, newTile)
                    return tiles
            except IndexError:
                if tile.bottom == newTile.top:
                    tiles.append(newTile)
    return tiles

print(placeDominoTile([], Tile(1, 1)))
print(placeDominoTile([Tile(1,1)], Tile(3,2)))
print(placeDominoTile([Tile(2,1)], Tile(3,2)))
print(placeDominoTile([Tile(1,3)], Tile(3,2)))
print(placeDominoTile([Tile(2,1), Tile(1,3), Tile(3,5), Tile(5,6)], Tile(3,3)))
print(placeDominoTile([Tile(2,1), Tile(1,3), Tile(3,5), Tile(5,6)], Tile(1,1)))
print(placeDominoTile([Tile(2,1), Tile(1,3), Tile(3,5), Tile(5,6)], Tile(6,4)))

def calculateDominoTiles(tiles):
    res = 0
    for index, tile in enumerate(tiles):
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