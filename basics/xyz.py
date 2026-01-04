class Solution(object):
    def findMinArrowShots(self, points):
        n = len(points)
        answer=[]
        for i in range(n):
            j = 0
            while j < n:
                if points[i][0] < points[j][1]:
                    answer.append([points[i],points[j]])
                else:
                    answer.append([points[j]])    
                j +=1    
        return answer 



        
        