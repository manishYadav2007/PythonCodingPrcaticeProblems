






def find_favourite_singer(n, playlists):
        counts = {}
        max_f = 0

        for i in playlists:
                counts[i] = counts.get(i, 0) + 1 
                max_f = max(max_f, counts[i])
        n = 0
        for j in counts.values():
                if j == max_f:
                        n += 1
        return n  



n = int(input())
playlists = list(map(int, input().split()))  


result = find_favourite_singer(n, playlists)
print(result)