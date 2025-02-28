**Problem 7.1**  

Two concentric metal spherical shells, of radius $a$ and $b$, respectively, are separated by weakly conducting material of conductivity $\sigma$.  

(a) If they are maintained at a potential difference $V$, what current flows from one to the other?  

(b) What is the resistance between the shells?  

(c) Notice that if $b \gg a$, the outer radius $b$ is irrelevant. How do you account for that? 

Exploit this observation to determine the current flowing between two metal spheres, each of radius $a$, immersed deep in the sea and held quite far apart, if the potential difference between them is $V$. (This arrangement can be used to measure the conductivity of seawater.)

解：

$$
J = \frac{I}{4\pi r^2} = \sigma E
$$

$$
E = \frac{I}{4\pi \sigma r^2}
$$

$$
V = V_a - V_b = -\int_{b}^{a} \vec{E}\cdot d\vec{l}
$$

$$
=-\int_{b}^{a} \frac{I}{4\pi \sigma r^2}\hat{r}\cdot dr\hat{r}
$$

$$
=\frac{I}{4\pi \sigma}\int_{b}^{a} \frac{-dr}{r^2}
$$

$$
=\frac{I}{4\pi \sigma} \left[ \frac{1}{r} \right]_{b}^{a} = \frac{I}{4\pi \sigma} \left[ \frac{1}{a} - \frac{1}{b}\right]
$$

$$
I = \frac{4\pi \sigma}{\frac{1}{a} - \frac{1}{b}}V \tag{a}
$$

$$
R = \frac{V}{I} = \frac{1}{4\pi \sigma} \left[ \frac{1}{a} - \frac{1}{b}\right] \tag{b}
$$

如果 $b \gg a$

$$
R = \frac{1}{4\pi \sigma a}
$$

利用這個公式，我們可以測量海水的導電度

在一艘船的頭尾兩端，放下兩顆半徑為 $a$ 的金屬球，至海水深處

使他們之間的電位差維持在 $V$，測量此時導線中的電流 $I$

但是要注意，這裡因為有兩顆球，一顆電流流出去，另一顆電流流回來，所以這兩顆球，相當於是串聯電阻

總電阻為 
$$
2R= \frac{1}{2\pi \sigma a} = \frac{V}{I}
$$

海水的導電度
$$
\sigma = \frac{1}{2\pi  a} \frac{I}{V}
$$

其中，$V$ 和 $a$ 是給定的，$I$是測量到的

這題比較讓人乍看下困惑的就是，這邊好像是一個開放的迴路，但我們卻把它視為封閉的電路。

這合理嗎?合理。為什麼，因為這邊只是看似開放，實際上是封閉迴路，要把海水看作導電介質。

另外就是，直覺上，我會認為，從一顆球流出的電流，怎麼也不可能完全從另一顆球流回去吧。

確實如此，但這邊大可不需要想那麼多，就如同，看似熟悉的真實電阻元件，內部也是有它製造工藝的細節和複雜性，但我們從來沒去管過那些事情，也沒什麼問題，這裡也是一樣。

我們不去管電流從一顆金屬球到另一顆金屬球的具體過程，其實題目也暗示了我們可以不去管，透過沒給定他們之間的距離，暗示了我們不必在乎，電流在海水中的流動細節。

其實所謂的導電度，就是一種整體性的宏觀參數，測量導電度的時候，我們不需要去追蹤電子實際上的運動細節。

