import queue

class LeaderBoard :
    def __init__(self):
        self._scores = {}

    def addScore(self, playerId,score):
        if playerId in self._scores.keys():
            self._scores[playerId] = 0

        self._scores[playerId] += score

    def top(self,K):
        x,y = lambda a ,b : a-b
        minHeap = queue.PriorityQueue(x)
        for score in self._scores.values():
            minHeap.put(score)
            if minHeap.qsize() >K :
                minHeap.task_done()

        sum =0
        for a in minHeap.get():
            sum += a
        return sum
    
    def reset(self,playerId):
        self._scores[playerId] =0