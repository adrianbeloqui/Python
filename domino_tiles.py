#[3|3]


def Tile(top, bottom):
    return {"top": top, "bottom": bottom}

def placeDominioTile(tileArray, newTile):
    if (newTile["bottom"] == tileArray[0]["top"]):
        tileArray.insert(0, newTile)
        return tileArray
    if (newTile["top"] == tileArray[len(tileArray)-1]["bottom"]):
        tileArray.append(newTile)
        return tileArray
    for i in xrange(len(tileArray)-1):
        if ((newTile["top"] == tileArray[i]["bottom"]) and (newTile["bottom"] == tileArray[i+1]["top"])):
            tileArray.insert(i+1, newTile)
            return tileArray
    return tileArray

#print placeDominioTile([Tile(1,1)], Tile(3,2))
#print placeDominioTile([Tile(2,1)], Tile(3,2))
#print placeDominioTile([Tile(1,3)], Tile(3,2))
#print placeDominioTile([Tile(2,1), Tile(1,3), Tile(3,5), Tile(5,6)], Tile(3,3))

def calculateDominoTiles(tilesArray):
    result = 0
    for i in xrange(len(tilesArray)-1):
        if (tilesArray[i]["bottom"] != tilesArray[i+1]["top"]):
            return -1
        result += tilesArray[i]["bottom"]
        result += tilesArray[i]["top"]

    return result


#print calculateDominoTiles([Tile(3,3)])
#print calculateDominoTiles([Tile(3,3), Tile(3,5)])
#print calculateDominoTiles([Tile(3,3), Tile(3,4), Tile(5,1)])
