
(a) Find the vector area of a hemispherical bowl of radius R.

$d\vec{a} = \hat{r} \, R d\theta \cdot R\sin\theta d\phi = \hat{r} \, R^2\sin\theta d\theta d\phi$

$$
\int_{\text{bowl }} d\vec{a} = \iint_{\text{bowl }}\hat{r} \, R^2\sin\theta d\theta d\phi
$$

記得這時候 $\hat{r}$ 不能移出積分


$\hat{r}=\hat{x}(\hat{r}\cdot\hat{x})+\hat{y}(\hat{r}\cdot\hat{y})+\hat{z}(\hat{r}\cdot\hat{z})$

$\hat{r}=\hat{x}(\sin\theta\cos\phi)+\hat{y}(\sin\theta\sin\phi)+\hat{z}(\cos\theta)$

要將 $\hat{r}$ 表示成直角座標才能夠繼續進行下去

上面那兩行不是背出來的，也不是查出來的

要說背也是有一個脈絡的，並非強記

$$
\int_{\text{bowl }} d\vec{a} = \hat{x} \iint_{\text{bowl }}(\sin\theta\cos\phi)R^2\sin\theta d\theta d\phi
$$

$$
+\hat{y} \iint_{\text{bowl }}(\sin\theta\sin\phi)R^2\sin\theta d\theta d\phi
$$

$$
+\hat{z} \iint_{\text{bowl }}(\cos\theta)R^2\sin\theta d\theta d\phi
$$

先觀察x和y的分量，可以看出由於存在對整個三角函數週期積分的部分，兩者必為零，其餘部分都不再重要，以...表示。

$$
\int_{\text{bowl }} d\vec{a} = \hat{x} [...]\int_{0}^{2\pi}\cos\phi d\phi
$$

$$
+\hat{y} [...]\int_{0}^{2\pi}\sin\phi d\phi
$$

$$
+\hat{z} \, R^2\int_{0}^{\pi/2}(\cos\theta)\sin\theta d\theta \int_{0}^{2\pi}d\phi
$$

所以只剩下z分量。

$$
\int_{\text{bowl }} d\vec{a} = \hat{z} \,2\pi R^2 \int_{0}^{\pi/2}-(\cos\theta)d(\cos\theta)
$$

$$
= \hat{z} \,2\pi R^2 \left[ \frac{-\cos^2\theta}{2} \right]_{0}^{\pi/2}
$$

$$
= \hat{z} \,2\pi R^2 \left[ 0 - (-\frac{1}{2}) \right]
$$

$$
= \hat{z} \,\pi R^2
$$

---

(e) Show that

$$
\oint(\vec{c}\cdot\vec{r})d\vec{l} = \vec{a} \times \vec{c}
$$

推導之前，先用中文進行表述

有個封閉迴路，每一小段的微分向量是 $d\vec{l}$

迴路形成的有向面積(vector area)是 $\vec{a}$

$\vec{c}$ 是常數向量，$\vec{r}$ 是原點到 $d\vec{l}$ 的位置向量

「常數向量」和 $\vec{r}$ 內積後的純量，乘以 $d\vec{l}$ 再進行迴路積分

等於「迴路形成的有向面積」和「常數向量」 的叉積

藉由 Prob. 1.61e

$$
\int_S \nabla T \times d\vec{a} = - \oint_P T \, d\vec{l}
$$

令 $T = \vec{c}\cdot\vec{r} $

$$
\nabla T = \nabla (\vec{c}\cdot\vec{r})
$$

$$
=\vec{c} \times ( \nabla \times \vec{r} ) + \vec{r} \times ( \nabla \times \vec{c} )
$$

$$
+( \vec{c} \cdot \nabla )\vec{r} + ( \vec{r} \cdot \nabla ) \vec{c} = ( \vec{c} \cdot \nabla )\vec{r}
$$

等號左邊

$$
\int_S \nabla T \times d\vec{a} = \int_S ( \vec{c} \cdot \nabla )\vec{r} \times d\vec{a}
$$

$$
= \int_S (\vec{c} \cdot \nabla r) \hat{r} \times d\vec{a} =\int_S (\vec{c} \cdot \hat{r}) \hat{r} \times d\vec{a}
$$

$$
=\int_S \vec{c}\times d\vec{a} = \vec{c} \times \vec{a}
$$

等號右邊

$$
-\oint_P T \, d\vec{l} = -\oint_P (\vec{c}\cdot\vec{r}) d\vec{l}
$$

綜上所述

$$
-\oint_P (\vec{c}\cdot\vec{r}) d\vec{l} = \vec{c} \times \vec{a}
$$

$$
\oint_P (\vec{c}\cdot\vec{r}) d\vec{l} = \vec{a} \times \vec{c}
$$
