#wap to find maximum ele from given list

def maxEle(li):
    max = li[0]
    for ind in range(0,len(li)):
        if(max < li[ind]):
            
            max = li[ind]
    return max


li = [ 12,21,23,45,87,67,98,99]
min_ele = maxEle(li)
print("maximum element is :" ,min_ele)


##wap to find minimum ele from given list
 
def minEle(li):
    min = li[0]
    for ind in range(0,len(li)):
        if(min > li[ind]):
            min = li[ind]
    return min


li = [ 12,21,23,45,87,67,98,99]
min_ele = minEle(li)
print("minimum element is :" ,min_ele)