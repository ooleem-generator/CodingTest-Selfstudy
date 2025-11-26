def solution(genres, plays):
    #songdata = list(zip(plays, list(range(len(plays)))))
    total_play_count = {}
    songs_by_genre = {}
    
    data = list(zip(genres, plays, list(range(len(plays)))))
    for genre, play, idx in data:
        if not total_play_count.get(genre):
            total_play_count[genre] = play
            songs_by_genre[genre] = [(play, idx)]
        else:
            total_play_count[genre] += play
            songs_by_genre[genre].append((play, idx))
            
    #print(total_play_count)
    #print(songs_by_genre)
    answer = []
    total_play_count = list(total_play_count.items())
    total_play_count.sort(key=lambda x:-x[1])
    for total in total_play_count:
        song_list = songs_by_genre[total[0]]
        song_list.sort(key=lambda x:(x[0],-x[1]))
        for _ in range(2):
            if not song_list:
                break
            play, idx = song_list.pop()
            answer.append(idx)
    
    
    return answer