https://en.wikipedia.org/wiki/Euler_method

|   t |   x |   y |  vx |  vy |  ax |  ay |
| --: | --: | --: | --: | --: | --: | --: |
|   0 |   0 |   0 |  20 |  30 |   0 | -10 |
|   1 |  20 |  30 |  20 |  20 |   0 | -10 |
|   2 |  40 |  50 |  20 |  10 |   0 | -10 |
|   3 |  60 |  60 |  20 |   0 |   0 | -10 |
|   4 |  80 |  60 |  20 | -10 |   0 | -10 |
|   5 | 100 |  50 |  20 | -20 |   0 | -10 |
|   6 | 120 |  30 |  20 | -30 |   0 | -10 |
|   7 | 140 |   0 |  20 | -40 |   0 | -10 |

Motion equations:

$$
a_x = \Delta v_x
$$

$$
a_y = \Delta v_y
$$

$$
v_x = \Delta x
$$

$$
v_y = \Delta y
$$

For orbits, when $G = 1$ we have the equations:

$$
force = \frac{mass_{other}}{r^2}
$$

$$
a_x = \frac{\Delta x \cdot force}{r}
$$

$$
a_y = \frac{\Delta y \cdot force}{r}
$$
