from collections import deque

def solution(cacheSize, cities):
    cities = deque(cities)
    cache = {}
    time = 0
    
    while cities:
        city = cities.popleft().lower()
        if cache.get(city) != None: # cache hit
            time += 1 # 일단 경과한 시간은 1초
            for i in cache.keys():
                cache[i] += 1
                
            cache[city] = 0 # hit한 city에 대해 0초로 다시 초기화
            
            
        else: # cache miss
            time += 5 # 일단 경과한 시간은 5초
            for i in cache.keys():
                cache[i] += 5
                
            if cacheSize == 0:
                continue
            
            elif len(cache) < cacheSize: 
                cache[city] = 0 # 캐시에 공간이 남았을 경우 city를 새로 추가해주고 0초로 초기화
                
            else:
                cachelist = list(cache.items())
                cachelist.sort(key=lambda x:-x[1])
                cache.pop(cachelist[0][0])
                cache[city] = 0
    
    return time