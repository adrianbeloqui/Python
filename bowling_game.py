def playGame(ballsPlayed):
    score = 0
    frame = 10
    i = 0
    while ( i < len(ballsPlayed)):
        if (frame > 1):
            #If it is a STRIKE
            if (ballsPlayed[i] == 10):
                score += 10
                score += ballsPlayed[i + 1]
                score += ballsPlayed[i + 2]
                frame -= 1
            #If it is a SPARE
            elif (ballsPlayed[i] + ballsPlayed[i + 1] == 10):
                score += ballsPlayed[i]
                score += ballsPlayed[i + 2]
                frame -= 1
            else:
                score += ballsPlayed[i]
                frame -= 0.5
        #If it is the last frame
        else:
            #If it is a STRIKE or SPARE (don't matter, they all have 3 scores to record)
            if ballsPlayed[i] == 10 or (ballsPlayed[i] + ballsPlayed[i + 1] == 10):
                score += ballsPlayed[i]
                score += ballsPlayed[i + 1]
                score += ballsPlayed[i + 2]
                break
            #If it's just a normal frame
            else:
                score += ballsPlayed[i]
                score += ballsPlayed[i + 1]
                break
        i += 1
    return score


def main():
    ballsNum = int(raw_input().strip())
    ballsPlayed = []
    while (ballsNum > 0):
        ballsPlayed.append(int(raw_input().strip()))
        ballsNum -= 1
    score = playGame(ballsPlayed)
    print score
    return

main()
