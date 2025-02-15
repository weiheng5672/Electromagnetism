### 習題3-47

本習題的目的是探討介電質內部的電場是否具有合理性。

我們知道，物質是由帶正電的原子核與帶負電的電子組成，因此從微觀角度來看，物質中的電場應該是一團混亂的。我們是否能夠定義一個有意義的平均電場？這正是本習題要確認的。

在介電物質中取一個球型區域，我們要求：
- 該區域必須足夠大，以包含足夠多的分子，使得所有微觀起伏能被平均掉。
- 同時又要足夠小，使得其內部的巨觀細節仍能被描述。

這看似矛盾，但事實上，一個包含數千個分子的球型區域即可同時滿足這兩個條件。接下來，本習題將證明以下兩個關鍵結果：
1. 球型區域內部所有電荷所產生的平均電場，由該區域的總偶極矩決定。
2. 球型區域外部所有電荷所產生的平均電場，等於它們在球心處產生的電場。

對於外部電荷而言，球心與它們的距離在微觀尺度上是非常大的，因此它們可視為連續分布，微觀起伏會被距離效應所平均掉。最終，它們在球心的電場即為該區域的平均電場。

對於內部電荷而言，則是總偶極矩決定了平均電場。

綜合這兩點，我們可以確認，介電質內部的平均電場概念是合理的。實際上，所有在介電質內部計算出的電場，都是這種意義上的平均電場，而不是單純由某個特定原子核或電子產生的電場。

### 解

(a)
考慮一個半徑為 $R$ 的球型區域，球心位於原點。在距球心 $r$ 處（$r < R$）有一個點電荷 $q$，該電荷所產生的電場對整個球型區域的平均電場為：
$$
\mathbf{E}_{ave} = \frac{1}{\frac{4\pi}{3}R^3} \int \mathbf{E}\,d\tau = \frac{1}{\frac{4\pi}{3}R^3} \int \frac{q}{4\pi \epsilon_0}\frac{\hat{\gamma}}{\gamma^2}\,d\tau
$$

其中：
- $d\tau$ 為場點的位置積分變數，
- $\mathbf{r}$ 為源點，
- $\hat{\gamma}$ 是從 $\mathbf{r}$ 指向 $d\tau$ 的單位向量。

現在，想像該球型區域中並沒有單一點電荷，而是均勻帶電的球體，體積電荷密度為 $\rho$。此時，在 $\mathbf{r}$ 處產生的電場為：
$$
\mathbf{E}_{\rho} = \frac{1}{4\pi \epsilon_0} \int \frac{\rho}{\gamma^2}\,\hat{\gamma} d\tau
$$

在這個積分中，$d\tau$ 是源點，$\mathbf{r}$ 是場點，而 $\hat{\gamma}$ 則是從 $d\tau$ 指向 $\mathbf{r}$ 的單位向量。

比較這兩個積分：
- 由於它們的 $\hat{\gamma}$ 方向相反，
- 若取 $\rho = - \frac{q}{\frac{4\pi}{3}R^3}$，則兩個積分完全相同。

因此，
$$
\mathbf{E}_{ave} = \mathbf{E}_{\rho}
$$
這是一種相當巧妙的手法，避免了直接計算複雜的積分，便得到了結論。

(b)
前述的第二個積分可以透過高斯定律求解：

---
高斯定律 r < R
$$
\oint_S \mathbf{E} \cdot d\mathbf{a} = \frac{Q}{\epsilon_0}
$$

$$
\cancel{4\pi} \cancel{r^2} E(r) = \frac{1}{\epsilon_0} \frac{\cancel{4\pi}}{3} r^{\cancel{3}} \rho
$$

$$
E(r) = \frac{\rho r}{3\epsilon_0}
$$

$$
\mathbf{E} = E(r)\,\hat{r} = \frac{\rho r}{3\epsilon_0}\,\hat{r} = \frac{\rho}{3\epsilon_0}\,\vec{r}
$$

---

$$
\mathbf{E}_{ave} = \mathbf{E}_{\rho} = \frac{\rho}{3\epsilon_0}\,\mathbf{r} = \frac{1}{3\epsilon_0} \left(-\frac{q}{\frac{4\pi}{3}R^3} \right) \mathbf{r}
$$

$$
\mathbf{E}_{ave}  = \frac{1}{4\pi\epsilon_0} \left(- \frac{q}{R^3} \right) \mathbf{r} = \frac{-\mathbf{p}}{4\pi\epsilon_0 R^3}
$$

這裡需要強調的是，我們計算的是某一個點電荷在該球型區域內的平均電場，透過此過程，我們意外地發現結果中出現了電偶極矩，這恰好符合電偶極矩的定義：$\mathbf{p} = q\mathbf{r}$。

(c)
若球型區域內共有 $n$ 個點電荷 $q_1, q_2, ..., q_n$，其分別位於 $\mathbf{r}_1, \mathbf{r}_2, ..., \mathbf{r}_n$，則總平均電場為：
$$
\mathbf{E}_{ave} = \sum_{i=1}^{n} \frac{-q_i \mathbf{r}_i}{4\pi \epsilon_0 R^3} = \frac{-\mathbf{p}_{total}}{4\pi\epsilon_0 R^3}
$$

這證明了，球型區域內部電荷的總偶極矩決定了該區域的平均電場。

(d)
同樣的推導方式可應用於外部電荷，對於位於球外的電荷，
$$
\mathbf{E}_{ave} = \mathbf{E}_{\rho}
$$

---
高斯定律 r > R
$$
\oint_S \mathbf{E}_{\rho} \cdot d\mathbf{a} = \frac{Q}{\epsilon_0}
$$

$$
4\pi r^2 E_{\rho}(r) = \frac{1}{\epsilon_0} \frac{4\pi}{3} R^{3} \rho
$$

$$
E_{\rho}(r) = \frac{R^3 \rho}{3\epsilon_0r^2}
$$

$$
\mathbf{E}_{\rho} = \frac{R^3 \rho}{3\epsilon_0r^2}\,\hat{r}
$$

---

根據高斯定律，我們可以求得：

$$
\mathbf{E}_{ave} = \mathbf{E}_{\rho} = \frac{R^3}{3\epsilon_0r^2}\left(-\frac{q}{\frac{4\pi}{3}R^3} \right)\,\hat{r}
$$

$$
\mathbf{E}_{ave} = \frac{-q}{4\pi\epsilon_0r^2}\,\hat{r}
$$

這意味著，位於球外的電荷在該球型區域內的平均電場，恰好等於它在球心處產生的電場。

### 總結

我們證明了，對於球型區域內部的電荷，平均電場由總偶極矩決定；對於外部電荷，其平均電場等於它們在球心處產生的電場。這進一步說明，介電質內部的平均電場是一個合理且有意義的概念，為電介質中的電場計算提供了堅實的理論基礎。

