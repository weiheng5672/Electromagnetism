
### 習題4-5
---
- 一個（理想）偶極子 p 位於無限大接地導體平面上方距離 z 處。
- 偶極子與垂直於平面的方向成角度 θ。

1. 求作用在 p 上的力矩。
2. 如果偶極子可以自由旋轉，它最終會停留在什麼方向？

---

### 解

#### 影像法

- 想像一個鏡向偶極子位於對稱於導體平面的位置
- 兩個偶極子相距 2z
- 把影像偶極子的位置是為座標原點，影像偶極子的指向是 +z 方向
- 注意，原圖的偶極子是從左下指向右上，↗
  - 這表示負電荷在左下(距導體較近)、正電荷在右上(距導體較遠)
  - 負電荷的影像電荷是正電荷(距導體較近)
  - 正電荷的影像電荷是負電荷(距導體較近)
- 所以，影像偶極子會是右下指向左上，↖
- 此時，想像影像偶極子↖位於原點，並指向 +z 方向

影像偶極子在偶極子的位置，造成的電場如下
$$
\mathbf{E}_{\text{image}}(2z, \theta) = \frac{p}{4\pi\epsilon_0 (2z)^3} \left( 2\cos\theta \, \hat{r} + \sin\theta \, \hat{\theta} \right).
$$

以下是重點，在這樣的座標選取下，真正的偶極子要如何表示?

在這樣的極座標選取下，偶極子的位置座標是 $( 2z, \theta )$ ，在該位置的單位向量是 $\hat{r}, \hat{\theta}$

偶極子與 $\hat{r}$ 的夾角是 $\theta$

$$
\mathbf{p} = p\cos\theta \, \hat{r} + p\sin\theta \, \hat{\theta}
$$

---
1. 作用在 p 上的力矩

$$
\mathbf{N} =  \mathbf{p} \times \mathbf{E}_{\text{image}} 
$$

$$
= \left( p\cos\theta \, \hat{r} + p\sin\theta \, \hat{\theta}\right) \times \frac{p}{4\pi\epsilon_0 (2z)^3} \left( 2\cos\theta \, \hat{r} + \sin\theta \, \hat{\theta} \right).
$$

$$
= \frac{p^2}{4\pi\epsilon_0 (2z)^3} \left( \cos\theta\sin\theta \, \hat{\phi} - 2\sin\theta\cos\theta \, \hat{\theta} \right)
$$

$$
= \frac{p^2\sin\theta\cos\theta}{4\pi\epsilon_0 (2z)^3} \left( -\hat{\theta} \right)
$$

$$
= \frac{p^2\sin 2\theta}{4\pi\epsilon_0 (16z^3)} \quad (\text{指出紙面}) 
$$

---

2. 如果偶極子可以自由旋轉

$0 < \theta < \frac{\pi}{2}$ ，逆時鐘旋轉，$\theta = 0$，偶極子指向上，此時力矩為零。

$\frac{\pi}{2} < \theta < \pi$ ，順時鐘旋轉，$\theta = \pi$，偶極子指向下，此時力矩為零。