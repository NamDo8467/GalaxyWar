# Galaxy War
This game is about shooting galaxy invaders. There are 5 levels in total, you have to shoot the small invaders in the first four levels and a big boss at level 5. For every bullet that hits the enemy, you will gain 10 points but try to dodge all the enemy's bullets because the game is over as soon as you get shot.

# Scrolling background image algorithm
```
tiles = math.ceil(SCREEN_HEIGHT / background.get_height()) + 1
scroll = 0

for i in range(0,tiles):
        screen.blit(background, (0, background.get_height() * (-i) + scroll))
    scroll += 3
    if abs(scroll) > background.get_height(): 
        scroll = 0
```
`tiles` represents the number of images needed to fill the entire screen

The idea is that you have 2 background images (`tiles` is equal to 2 in this project) next to each other vertically on the screen. The cordinate of the first one is `(0, 0)` and the second one is `(0, - bg.get_height() * 1)`. The second image y-coordinate is negative because, in pygame, the top corner has a negative value. For example, if you are at (0,100) then if you want to go up by 10, your next location is (0,90). Therefore, the first image is at `(0,0)`, then the second one is on top of it which is `(0, -bg.get_height() * 1)`

Next, you move the images down by however many you want. To do that, you need to set a variable called `scroll = 0` and increase this variable every time. When this variable is equal to or larger than the background image height, reset this variable to 0.

Coordinate of images when:
- `scroll = 0` : `(0, 0)` and `(0, -background.g.get_height())`
- `scroll = 3` : `(0, -3)` and `(0, -background.get_height() - 3)`
- `scroll = 6` : `(0, -6)` and `(0, -background.get_height() - 6)`
- ...
  
When the `scroll` is equal to or larger than the background height, then it resets itself to 0
