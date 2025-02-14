
### 習題4-5
---
$\mathbf{p}_1$ 是向上的（理想）電偶極子，$\mathbf{p}_2$ 是向右的（理想）電偶極子，兩者相距 $r$。

1. $\mathbf{p}_1$ 受到 $\mathbf{p}_2$ 作用的力矩是多少？  
2. $\mathbf{p}_2$ 受到 $\mathbf{p}_1$ 作用的力矩又是多少？

---
### 解

偶極子造成的電場如下
$$
\mathbf{E}_{\text{dip}}(r, \theta) = \frac{p}{4\pi\epsilon_0 r^3} \left( 2\cos\theta \, \hat{r} + \sin\theta \, \hat{\theta} \right).
$$


$\mathbf{p}_2$ 是躺著指向右方的，直接參照公式帶入，$\mathbf{p}_1$ 的位置會是在 $\theta= \pi$。

$\mathbf{p}_2$ 在 $\mathbf{p}_1$位置造成的電場如下
$$
\mathbf{E}_{21}(r, \pi) = \frac{-2\,p_2}{4\pi\epsilon_0 r^3}  \, \hat{r}
$$

這個時候，$\hat{r}$ 是指向左的，$-\hat{r}$ 是指向右
$$
\mathbf{E}_{21} = \frac{2\,p_2}{4\pi\epsilon_0 r^3}  \, \hat{x}
$$

---

1. $\mathbf{p}_1$ 受到 $\mathbf{p}_2$ 作用的力矩

$$
\mathbf{N}_{21} =  \mathbf{p}_1 \times \mathbf{E}_{21} =  p_1 \,\hat{z}  \times \frac{2\,p_2}{4\pi\epsilon_0 r^3}  \, \hat{x}
$$

$$
 =  \frac{2\,p_1\,p_2}{4\pi\epsilon_0 r^3}  \, \hat{y}
$$

---

$\mathbf{p}_1$ 在 $\mathbf{p}_2$位置造成的電場如下
$$
\mathbf{E}_{12}(r, \frac{\pi}{2}) = \frac{p_1}{4\pi\epsilon_0 r^3} \, \hat{\theta}
$$

這個時候，$\hat{\theta}$ 是指向下
$$
\mathbf{E}_{12} = \frac{-p_1}{4\pi\epsilon_0 r^3} \, \hat{z}
$$

---

2. $\mathbf{p}_2$ 受到 $\mathbf{p}_1$ 作用的力矩

$$
\mathbf{N}_{12} =  \mathbf{p}_2 \times \mathbf{E}_{12} =  p_2 \,\hat{x}  \times \frac{-p_1}{4\pi\epsilon_0 r^3} \, \hat{z}
$$

$$
 =  \frac{p_1\,p_2}{4\pi\epsilon_0 r^3}  \, \hat{y}
$$