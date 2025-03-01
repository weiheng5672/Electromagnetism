**Problem 7.8**  
A square loop of wire (side $a$) lies on a table, a distance $s$ from a very long straight wire, which carries a current $I$, as shown in Fig. 7.18.

![Figure 7.18](Figs/FIGURE%207.18.png)

(a) Find the flux of $B$ through the loop.  

(b) If someone now pulls the loop directly away from the wire, at speed $v$, what emf is generated? In what direction (clockwise or counterclockwise) does the current flow?  

(c) What if the loop is pulled to the right at speed $v$?

解：
(a)
$$
\int \vec{B}\cdot d\vec{l} = \mu_0 I
$$

$$
2\pi r B = \mu_0 I
$$

$$
B = \frac{\mu_0 I}{2\pi r}
$$

$$
\Phi = \int \vec{B}\cdot d\vec{a} = \int_{s}^{s+a} \frac{\mu_0 I a}{2\pi r}dr
$$

$$
=  \frac{\mu_0 I a}{2\pi} \int_{s}^{s+a} \frac{dr}{r} = \frac{\mu_0 I a}{2\pi} \, \mathrm{ln}\left[\frac{s+a}{a}\right]
$$

(b)
遠離導線，磁場變少，上半部是指出紙面的磁場變少，

根據冷次定率，右手定則，感應電流是逆時針方向。

$$
\mathcal{E} = \frac{d\Phi}{dt} = \frac{\mu_0 I a}{2\pi} \, \frac{d}{dt}\mathrm{ln}\left[\frac{s+a}{a}\right]
$$

$$
=\frac{\mu_0 I a}{2\pi}\frac{a}{s+a}\frac{ds}{dt} = \frac{\mu_0 I a^2v}{2\pi(s+a)}
$$

(c)
此時雖然左右兩側都會切割磁力線，但方向互相抵消，總電動勢為零
