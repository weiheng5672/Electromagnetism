
我們現在在直角座標系 $(x, y, z)$ 下推導 $\nabla \times \vec{A} = \vec{B}$ 在邊界條件的表達式，確認 **A 場法向微分的不連續性**。

我們取邊界法向方向為 $z$ 軸，即 **邊界是 $z = 0$ 平面**，以得到最後的邊界條件。

### **1. 旋度在直角座標系的展開**
旋度的定義是

$$
(\nabla \times \vec{A})_i = \epsilon_{ijk} \frac{\partial A_k}{\partial x_j}
$$

展開各分量：

$$
B_x =(\nabla \times \vec{A})_x = \frac{\partial A_z}{\partial y} - \frac{\partial A_y}{\partial z}
$$

$$
B_y =(\nabla \times \vec{A})_y = \frac{\partial A_x}{\partial z} - \frac{\partial A_z}{\partial x}
$$

$$
B_z =(\nabla \times \vec{A})_z = \frac{\partial A_y}{\partial x} - \frac{\partial A_x}{\partial y}
$$


### **2. B 場的邊界條件**
我們已知 B 場的邊界條件為：

$$
\vec{B}_{\text{above}} - \vec{B}_{\text{below}} = \mu_0 (\vec{K} \times \hat{n})
$$

現在我們考慮邊界在 **$z = 0$** 平面，法向方向為 **$\hat{n} = \hat{z}$**，則：

$$
\vec{B}_{\text{above}} - \vec{B}_{\text{below}} = \mu_0 (\vec{K} \times \hat{z})
$$

計算右手邊的交叉積：

$$
\vec{K} \times \hat{z} =
\begin{vmatrix}
\hat{x} & \hat{y} & \hat{z} \\
K_x & K_y & K_z \\
0 & 0 & 1
\end{vmatrix}
=(K_y, -K_x, 0)
$$

因此，B 場的邊界條件在各分量上的表達為：

$$
B_x^{\text{above}} - B_x^{\text{below}} = \mu_0 K_y
$$

$$
B_y^{\text{above}} - B_y^{\text{below}} = -\mu_0 K_x
$$

$$
B_z^{\text{above}} - B_z^{\text{below}} = 0
$$

這告訴我們：
- **B 場的切向分量 $B_x, B_y$ 是不連續的**，其不連續量與 $K$ 相關。
- **B 場的法向分量 $B_z$ 是連續的**。


### **3. 用旋度公式換成 A 場**
用 B 場的旋度公式替換：

$$
B_x = \frac{\partial A_z}{\partial y} - \frac{\partial A_y}{\partial z},
$$

$$
B_y = \frac{\partial A_x}{\partial z} - \frac{\partial A_z}{\partial x}.
$$

帶入邊界條件：

$$
\left( \frac{\partial A_z}{\partial y} - \frac{\partial A_y}{\partial z} \right)_{\text{above}}
-\left( \frac{\partial A_z}{\partial y} - \frac{\partial A_y}{\partial z} \right)_{\text{below}}
= \mu_0 K_y
$$

$$
\left( \frac{\partial A_x}{\partial z} - \frac{\partial A_z}{\partial x} \right)_{\text{above}}
-\left( \frac{\partial A_x}{\partial z} - \frac{\partial A_z}{\partial x} \right)_{\text{below}}
= -\mu_0 K_x
$$

簡化後，我們得到：

$$
\frac{\partial A_y}{\partial z} \bigg|_{\text{above}} - \frac{\partial A_y}{\partial z} \bigg|_{\text{below}} = -\mu_0 K_y
$$

$$
\frac{\partial A_x}{\partial z} \bigg|_{\text{above}} - \frac{\partial A_x}{\partial z} \bigg|_{\text{below}} = -\mu_0 K_x
$$

這可以合併寫成向量形式：

$$
\frac{\partial \vec{A}}{\partial z} \bigg|_{\text{above}} - \frac{\partial \vec{A}}{\partial z} \bigg|_{\text{below}} = -\mu_0 \vec{K}
$$

這就是 **A 場在 $z = 0$ 平面上的法向微分不連續性邊界條件**，將z換乘n就是課文中的公式。


### **4. 結論**
- **A 場本身在邊界是連續的**，即

  $$
  \vec{A}_{\text{above}} = \vec{A}_{\text{below}}
  $$

- **A 場的法向微分會產生不連續性**，即

  $$
  \frac{\partial \vec{A}}{\partial z} \bigg|_{\text{above}} - \frac{\partial \vec{A}}{\partial z} \bigg|_{\text{below}} = -\mu_0 \vec{K}
  $$

這告訴我們：
- **表面電流 $\vec{K}$ 會影響 A 場的法向變化率，而不影響 A 場本身的值**。
- **這與 B 場的邊界條件一致**，因為 A 場的旋度是 B 場，所以 A 場的變化率與 B 場的跳躍行為直接相關。

以下進一步解析這些概念。

### **A場在邊界上的連續性**

$$
\vec{A}_{\text{above}} = \vec{A}_{\text{below}}
$$

A場跨過邊界不會發生跳躍。

這種連續性類似於電位跨過表面電荷的行為，A場跨越表面電流也是連續的。

### **兩側A場的法向導數相減，平行於表面**

在表面電流的影響下，A場的法向變化必須遵循以下條件：

$$
\frac{\partial \vec{A}}{\partial n} \bigg|_{\text{above}} - \frac{\partial \vec{A}}{\partial n} \bigg|_{\text{below}} = -\mu_0 \vec{K}
$$

根據安培定律，表面電流會產生B場的切向變化。

又根據上述推導，A場的法向導數，等於B場的切向分量

所以，B場在邊界的切向變化，會表現為A場的法向導數在邊界兩側的變化

---