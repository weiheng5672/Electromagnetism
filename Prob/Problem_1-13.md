### 習題1-13

$$
\nabla\gamma = \nabla\sqrt{(x - x')^2 + (y - y')^2 + (z - z')^2}
$$

$$
\nabla\gamma =
\frac{\partial \gamma}{\partial x} \,\hat{\mathbf{x}} +
\frac{\partial \gamma}{\partial y} \,\hat{\mathbf{y}} +
\frac{\partial \gamma}{\partial z} \,\hat{\mathbf{z}} 
$$

$$
\frac{\partial \gamma}{\partial x} = \frac{1}{2} \cdot \frac{2(x - x')}{\sqrt{(x - x')^2 + (y - y')^2 + (z - z')^2}} 
$$

$$
= \frac{x - x'}{\sqrt{(x - x')^2 + (y - y')^2 + (z - z')^2}}
= \frac{x - x'}{\gamma}
$$

Similarly,  

$$
\frac{\partial \gamma}{\partial y} = 
\frac{y - y'}{\gamma}
\quad
\frac{\partial \gamma}{\partial z} = 
\frac{z - z'}{\gamma}
$$

Thus,
$$
\nabla \gamma =
\frac{x - x'}{\gamma} \hat{\mathbf{x}}+
\frac{y - y'}{\gamma} \hat{\mathbf{y}}+
\frac{z - z'}{\gamma} \hat{\mathbf{z}}
$$

$$
= \frac{\vec{\gamma}}{\gamma} = \hat{\gamma}
$$


針對$\nabla \gamma = \hat{\gamma}$

可以這樣理解：

對一個以任意點為中心的「距離純量場」進行梯度運算，其結果會得到一個「向量場」。

這個向量場在空間中每一點的方向，都是從中心逕向（radial）朝外指出的單位向量。

由於各點的方向不同，因此它並非「常數向量場」。

這個計算過程看似繁瑣，但幾何結論非常純粹。

梯度的核心本質就是「純量在空間中的最大變化率」，而其方向則「指向數值增長最快的方向」。

以空間中任意一點來說：

關於方向： 數值增長最快的方向自然是「逕向朝外」，也就是遠離中心點的方向。
關於大小： 語意上看似有些繞口，但就是「當你每往外移動一個單位的距離，距離函數的值就剛好增加一個單位」。因此，這個變化率的大小（模長）恆等於 $1$。

透過這種幾何直覺，我們就能輕鬆記住這個公式：$\nabla \gamma = \hat{\gamma}$。當中心點 $x', y', z'$ 為原點時，即為熟知的 $\nabla r = \hat{r}$。

另一個幾何視角：方向餘弦

此外，若我們仔細觀察這個看似複雜的計算過程，會發現 $\nabla \gamma$ 的每一個分量，恰好就是位移向量在各個座標軸上的「方向餘弦」。

以 $x$ 方向的分量 $\frac{\partial \gamma}{\partial x}$ 為例，我們可以這樣直觀理解：

當沿著 $x$ 軸每增加一個單位時，整體的位移距離會增加多少？

這在幾何上相當於去尋找位移向量與 $x$ 軸正方向的夾角關係。

因為距離函數在 $x$ 方向的變化率，正巧等同於「沿 $x$ 軸方向的單位向量」與「總位移方向單位向量」的點積（Dot Product），亦即該位移方向在 $x$ 軸上的投影比例。


---


(a)
$$
\nabla(\gamma^2) = \nabla \left[{(x - x')^2 + (y - y')^2 + (z - z')^2} \right]
$$

$$
\nabla(\gamma^2) =
\frac{\partial (\gamma^2)}{\partial x} \,\hat{\mathbf{x}} +
\frac{\partial (\gamma^2)}{\partial y} \,\hat{\mathbf{y}} +
\frac{\partial (\gamma^2)}{\partial z} \,\hat{\mathbf{z}} 
$$

$$
\frac{\partial (\gamma^2)}{\partial x} = 2(x - x')
$$

Similarly,  

$$
\frac{\partial (\gamma^2)}{\partial y} = 2(y - y')
\quad
\frac{\partial (\gamma^2)}{\partial z} = 2(z - z')
$$

Thus,
$$
\nabla (\gamma^2) =
2(x - x') \hat{\mathbf{x}}+
2(y - y') \hat{\mathbf{y}}+
2(z - z') \hat{\mathbf{z}}
$$

$$
= 2\vec{\gamma}
$$

或者，透過連鎖律

$$
\nabla(\gamma^2) = 2\gamma\,\nabla(\gamma)
$$

$$
= 2\gamma\,\hat{\gamma} = 2\vec{\gamma}
$$

(b)
$$
\nabla \left( \frac{1}{\gamma} \right) = \frac{-1}{\gamma^2}\,\nabla(\gamma) = \frac{-\hat{\gamma}}{\gamma^2}
$$

(c)
$$
\nabla \left( \gamma^n \right) = n\gamma^{n-1}\,\nabla(\gamma) = n\gamma^{n-1} \, \hat{\gamma}
$$

