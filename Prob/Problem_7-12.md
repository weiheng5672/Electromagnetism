
問題：  
一個長螺線管，半徑為 $a$，由交流電驅動，使得其內部磁場為正弦變化：
$$
B(t) = B_0 \cos(\omega t) \hat{z}
$$
在螺線管內部，放置一個與其同軸的圓形導線迴圈，該迴圈的半徑為 $a/2$，電阻為 $R$。求迴圈內的感應電流隨時間的變化。

---

解：  
首先，座標系統的設定令圓形迴圈的面積方向為 $+z$ 方向，即逆時針方向為正。

磁通量為：
$$
\Phi = \left(\frac{\pi a^2}{4} \right) B_0 \cos(\omega t)
$$

感應電動勢為：
$$
\mathcal{E} = -\frac{d}{dt} \left[ \left(\frac{\pi a^2}{4} \right) B_0 \cos(\omega t) \right]
$$

計算導數：
$$
\mathcal{E} = \left(\frac{\pi a^2 \omega}{4} \right) B_0 \sin(\omega t)
$$

根據歐姆定律，感應電流為：
$$
I = \left(\frac{\pi a^2 \omega}{4R} \right) B_0 \sin(\omega t)
$$

檢查方向性：

由於 $\cos(\omega t)$ 在 $t=0$ 時為最大值且隨時間減少，因此磁通量變化率最初為負，使得感應電動勢為正。

這表示在前半個週期內（$0 \leq \omega t < \pi$），感應電流方向為逆時針；

在後半個週期（$\pi \leq \omega t < 2\pi$）內，感應電流則為順時針。

---

