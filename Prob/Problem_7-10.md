**Problem 7.10**  
A square loop (side $a$) is mounted on a vertical shaft and rotated at angular velocity $\omega$ (Fig. 7.19). 

![Figure 7.19](Figs/FIGURE%207.19.png)

A uniform magnetic field $B$ points to the right. 

Find the $\mathcal{E}(t)$ for this alternating current generator.

解：

#### **1. 定性分析**
當線圈處於圖示位置（設此時角度為 $0^\circ$），左右兩側導線的運動方向與磁場垂直，因此此時感應電動勢最大。  

當線圈轉至 $90^\circ$ 位置時，導線運動方向與磁場平行，此時感應電動勢為零。  

---

#### **2. 運動電動勢**
左右兩側導線的線速度為：
$$
v = \frac{\omega a}{2}
$$
根據勞倫茲力，單條導線的電動勢為：
$$
\mathcal{E}_{\text{單邊}} = v B \sin \omega t \times a
$$
由於線圈有兩側貢獻，因此總電動勢為：
$$
\mathcal{E} = 2 \times \mathcal{E}_{\text{單邊}} = 2 v B \sin \omega t  \times a
$$
$$
= \omega a^2 B \sin \omega t
$$

透過右手定則，電流方向是順時針，由於底下那兩個環的構造，電流方向不會變化。

---

#### **3. 磁通量法**
線圈的磁通量為：
$$
\Phi = B \cdot a^2 \cos \omega t
$$
由於底部環狀結構的影響，每轉半圈可視為磁通持續增加，冷次定律表示感應電流將是順時針。根據磁通量規則：
$$
\mathcal{E} = -\frac{d\Phi}{dt} = \omega B a^2 \sin \omega t
$$

很多時候會使用冷次定律確認方向，磁通量規則只計算大小，不管那個負號，

但這題如果使用磁通量規則，由於我們已在磁通表示式中選擇了向右為磁通正方向，

此時根據右手定則，迴路的正方向為逆時針，

負號留著剛好能夠配合，直接帶入結果剛好符合實際情況。

---

### **結論**
感應電動勢為：
$$
\mathcal{E}(t) = \omega B a^2 \sin \omega t
$$
並且感應電流方向為順時針。