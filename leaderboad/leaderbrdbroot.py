class LeaderBoard :
    def __init__(self) :
        self._scores = { }

    def addScore(self, playerId, score):
        if playerId not in self._scores.keys():
             self._scores[playerId] = 0

        self._scores[playerId] += score
 
    def top(self,K):
        values = list(self._scores.values())

        sorted(values,reverse=True)

        sum =0
        for i in range(0,K) :
            sum += values[i]

        return sum
    
    def reset(self,playerI):
        self._scores[playerI] =0