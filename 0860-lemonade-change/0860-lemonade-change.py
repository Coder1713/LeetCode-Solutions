class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        drawer={5:0,
        10:0
        }
        for bill in bills:
            if bill==5:
                drawer[5]+=1
            elif bill==10:
                if drawer[5]==0:
                    return False
                else:
                    drawer[10]+=1
                    drawer[5]-=1
            else:
                if drawer[10]>0 and drawer[5]>0:
                    drawer[10]-=1
                    drawer[5]-=1
                elif drawer[5]>=3:
                    drawer[5]-=3
                else:
                    return False
        return True
                

        
