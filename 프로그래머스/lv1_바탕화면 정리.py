def solution(wallpaper):
    lux, luy = len(wallpaper), len(wallpaper)
    rdx, rdy = 0,0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#' and j < luy:
                luy = j
            if wallpaper[i][j] == '#' and i < lux:
                lux = i
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#' and rdy < j:
                rdy = j
            if wallpaper[i][j] == '#' and rdx < i:
                rdx = i
    return [lux, luy, rdx+1, rdy+1]