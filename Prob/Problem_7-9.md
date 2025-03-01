
**Problem 7.9**

An infinite number of different surfaces can be fit to a given boundary line, and yet, in defining the magnetic flux through a loop,  

$$
\Phi = \int \mathbf{B} \cdot d\mathbf{a}
$$

I never specified the particular surface to be used. Justify this apparent oversight.


**解：**  

由於**磁場的散度恆為零**，即  

$$
\nabla \cdot \mathbf{B} = 0
$$

根據高斯定理，這意味著對**任意封閉曲面** $S$，磁通量的通量積分必為零：  

$$
\oint_S \mathbf{B} \cdot d\mathbf{a} = 0
$$

這保證了，只要**兩個不同的曲面共享相同的邊界**，它們的磁通量必然相等。  

假設**封閉迴路** $C$，以及**兩個不同的曲面** $S_1$ 和 $S_2$，它們都以 $C$ 為邊界，那麼 $S_1$ 和 $S_2$ 共同構成一個完整的封閉曲面 $S$。對此封閉曲面 $S$ 應用高斯定理：  

$$
\oint_S \mathbf{B} \cdot d\mathbf{a} = \int_{S_1} \mathbf{B} \cdot d\mathbf{a} + \int_{S_2} \mathbf{B} \cdot d\mathbf{a} = 0
$$

由於 $S_2$ 的法線方向相對於 $S_1$ 取反，因此可得  

$$
\int_{S_1} \mathbf{B} \cdot d\mathbf{a} = \int_{S_2} \mathbf{B} \cdot d\mathbf{a}
$$

這證明了磁通量與所選曲面無關，只依賴於邊界 $C$，因此在磁通量的定義中不必特別指定曲面。
