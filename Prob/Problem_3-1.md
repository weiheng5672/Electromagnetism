### 習題3-1


### 解

$$
\frac{1}{4\pi R^2} \frac{q}{4\pi \epsilon_0} \int \frac{R^2 \sin\theta d\theta d\phi}{\sqrt{z^2+R^2-2zR\cos\theta}}
$$

$$
= \frac{2\pi R^2}{4\pi R^2} \frac{q}{4\pi \epsilon_0} \int_{0}^{\pi} \frac{ \sin\theta d\theta}{\sqrt{z^2+R^2-2zR\cos\theta}}
$$

$$
= \frac{1}{2} \frac{q}{4\pi \epsilon_0} \int_{0}^{\pi} \frac{ d (-\cos\theta) }{\sqrt{z^2+R^2-2zR\cos\theta}}
$$

---

$$
\frac{d}{d (-\cos\theta)} \sqrt{z^2+R^2-2zR\cos\theta}
$$

$$
= \frac{ 2zR }{2\sqrt{z^2+R^2-2zR\cos\theta}}
$$

$$
\frac{d}{d (-\cos\theta)} \left[ \frac{\sqrt{z^2+R^2-2zR\cos\theta}}{zR} \right] 
$$

$$
= \frac{1}{\sqrt{z^2+R^2-2zR\cos\theta}}
$$

---

$$
\int_{0}^{\pi} \frac{ d (-\cos\theta) }{\sqrt{z^2+R^2-2zR\cos\theta}}
$$

$$
= \left[ \frac{\sqrt{z^2+R^2-2zR\cos\theta}}{zR} \right]_{0}^{\pi} 
$$

$$
= \frac{1}{zR}\left[ \sqrt{z^2+R^2+2zR} - \sqrt{z^2+R^2-2zR} \right]
$$

$$
= \frac{1}{zR}\left[ \sqrt{(z+R)^2} - \sqrt{(z-R)^2} \right]
$$

如果 $z < R$

$$
= \frac{1}{zR}\left[ (z+R) - (R-z) \right]
$$

$$
= \frac{2z}{zR} = \frac{2}{R} 
$$

---

$$
\frac{1}{2} \frac{q}{4\pi \epsilon_0} \int_{0}^{\pi} \frac{ d (-\cos\theta) }{\sqrt{z^2+R^2-2zR\cos\theta}}
$$

$$
=\frac{1}{2} \frac{q}{4\pi \epsilon_0} \frac{2}{R} 
$$

$$
=\frac{q}{4\pi \epsilon_0 R} 
$$

以上 是在計算 半徑為R的球面上 由一個球內點電荷 所產生的電位的平均值

當 $z > R$

就是在計算 由一個球外點電荷 所產生的電位的平均值

$$
\frac{1}{zR}\left[ \sqrt{(z+R)^2} - \sqrt{(z-R)^2} \right]
$$

的結果會是

$$
= \frac{1}{zR}\left[ (z+R) - (z-R) \right]
$$

$$
= \frac{2R}{zR} = \frac{2}{z}
$$

$$
\frac{1}{2} \frac{q}{4\pi \epsilon_0} \int_{0}^{\pi} \frac{ d (-\cos\theta) }{\sqrt{z^2+R^2-2zR\cos\theta}}
$$


$$
=\frac{1}{2} \frac{q}{4\pi \epsilon_0} \frac{2}{z} 
$$

$$
=\frac{q}{4\pi \epsilon_0 z} 
$$

這正好是 球外點電荷 在球心的電位

綜上所述

半徑為R的球面上 電位的平均值 分成兩部分
球外電荷 造成的平均值 等於 在球心的電位
球內電荷 造成的平均值 等於 $Q_{en}/4\pi \epsilon_0 R$

其中 $Q_{en}$ 是球面包圍的總電荷

儘管以上是針對一個點電荷計算
但根據重疊原理 對任意電荷分布都成立
