
### 習題2-3



### 解

$$
\int_{0}^{L}\frac{1}{4\pi\epsilon_0}\frac{\lambda dx(\hat{z}z-\hat{x}x)}{(x^2+z^2)^{3/2}}
$$


$$
= \hat{z} \frac{\lambda z}{4\pi\epsilon_0}\int_{0}^{L}\frac{dx}{(x^2+z^2)^{3/2}}
$$

$$
-\hat{x}\frac{\lambda}{4\pi\epsilon_0}\int_{0}^{L}\frac{xdx}{(x^2+z^2)^{3/2}}
$$

$$
\int_{0}^{L}\frac{dx}{[x^2+z^2]^{3/2}} = \left[ \frac{x}{z^2\sqrt{x^2+z^2}} \right]_{0}^{L}
$$

$$
= \frac{L}{z^2\sqrt{L^2+z^2}}
$$

$$
\int_{0}^{L}\frac{xdx}{[x^2+z^2]^{3/2}} = \int_{0}^{L}\frac{d(x^2)}{2(x^2+z^2)^{3/2}}
$$

$$
= \left[\frac{-1}{(x^2+z^2)^{1/2}}\right]_{0}^{L}
$$

$$
= \frac{-1}{\sqrt{L^2+z^2}} - \frac{-1}{\sqrt{z^2}}
$$

$$
=  \frac{1}{z} - \frac{1}{\sqrt{L^2+z^2}}
$$

$$
\hat{z} \frac{\lambda z}{4\pi\epsilon_0}\left[\frac{L}{z^2\sqrt{L^2+z^2}}\right]
-\hat{x}\frac{\lambda}{4\pi\epsilon_0}\left[\frac{1}{z} - \frac{1}{\sqrt{L^2+z^2}}\right]
$$

$$
= \frac{\lambda }{4\pi\epsilon_0}\left[\hat{z}\frac{zL}{z^2\sqrt{L^2+z^2}}
-\hat{x}\left( \frac{1}{z} - \frac{1}{\sqrt{L^2+z^2}} \right) \right]
$$

$$
= \frac{\lambda }{4\pi\epsilon_0}\left[\hat{z}\frac{L}{z^2\sqrt{1+L^2/z^2}}
-\hat{x}\left( \frac{1}{z} - \frac{1}{\sqrt{L^2+z^2}} \right) \right]
$$

如果 $z >> L$

$$
\sqrt{1+L^2/z^2} = 1
$$

$$
\frac{1}{z} - \frac{1}{\sqrt{L^2+z^2}} = 0
$$

電場

$$
\hat{z}\frac{1}{4\pi\epsilon_0}\frac{\lambda L}{z^2} = \hat{z}\frac{1}{4\pi\epsilon_0}\frac{Q}{z^2}
$$
