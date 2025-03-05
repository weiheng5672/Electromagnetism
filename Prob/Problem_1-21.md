這個習題是在確認del算子的乘法規則

del運算子可以作用在純量場和向量場

兩個純量場，相乘，是純量場 

兩個純量場，點積，是純量場

梯度可以作用在上述兩者

純量場乘以向量場，是向量場

兩個向量場，叉積，是向量場

上述可以分別可計算，散度，旋度

共有六種乘積規則其中兩向量場點積的梯度，兩向量場叉積的散度和旋度，這三個是比較複雜的
。
其餘的三種，都可以用萊布尼茲規則去理解，前面微分後面不微分+前面不微分後面微分。

儘管如此比較複雜的那三個，這裡介紹一種比較trick，較有啟發性的推導方式，

嚴格來說不能說是推導，只能說是驗證或者確認。

兩向量場點積的梯度，可以exploit向量三重積的BAC-CAB。

兩向量場叉積的散度，可以exploit純量三重積。

兩向量場叉積的旋度，可以exploit向量三重積的BAC-CAB。


### 直接應用萊布尼茲規則即可處理的三種運算

#### 兩純量場相乘的梯度
$$
\nabla ( \phi \psi ) = \nabla ( \phi  )\psi + \nabla (  \psi )\phi
$$

#### 純量場乘以向量場的散度
$$
\nabla \cdot (\phi \mathbf{A}) = \nabla \phi \cdot  \mathbf{A} + \phi (\nabla \cdot  \mathbf{A})
$$
當del算子作用在純量場，以梯度作用，結果再和向量場點積，當del算子作用在向量場，以散度作用

#### 純量場乘以向量場的旋度
$$
\nabla \times (\phi \mathbf{A}) = \nabla \phi \times  \mathbf{A} + \phi (\nabla \times  \mathbf{A})
$$
當del算子作用在純量場，以梯度作用，結果再和向量場叉積，當del算子作用在向量場，以旋度作用。注意這裡 $\phi \mathbf{A}$ 不能寫成 $\mathbf{A} \phi$，不然結果會是錯的，這不為什麼，畢竟這裡嚴格來說本來就不算推導，只是一種方便理解的、啟發性的確認方式，考試這樣寫應該是沒分的，真的要證明應該是要在直角坐標，直接展開每個分量。

## 較複雜，需要額外技巧的三種運算 

#### 兩向量場叉積的散度 
$$
\nabla \cdot (\mathbf{A} \times \mathbf{B})
$$

根據純量三重積
$\nabla \cdot (\mathbf{A} \times \mathbf{B}) = - \mathbf{A} \cdot (\nabla \times \mathbf{B})$  
但是$\nabla$ 在右邊變成只對 $\mathbf{B}$ 作用  

$\nabla \cdot (\mathbf{A} \times \mathbf{B}) = - \mathbf{B} \cdot (\mathbf{A} \times \nabla) = \mathbf{B} \cdot (\nabla \times \mathbf{A})$  
這時$\nabla$ 在右邊變成只對 $\mathbf{A}$ 作用  

所以，結合兩者，這樣等號兩邊的 $\nabla$，就都對 $\mathbf{A}$ 也對 $\mathbf{B}$ 作用到。
$$
\nabla \cdot (\mathbf{A} \times \mathbf{B}) = \mathbf{B} \cdot (\nabla \times \mathbf{A}) - \mathbf{A} \cdot (\nabla \times \mathbf{B})
$$

有別於在直角座標展開分量確認，這或許不太嚴謹，但比較方便理解和記憶。  

#### 兩向量場點積的梯度
$$
\nabla (\mathbf{A} \cdot \mathbf{B})
$$

$\mathbf{A} \times (\nabla \times \mathbf{B}) = \nabla (\mathbf{A} \cdot \mathbf{B}) - \mathbf{B} (\mathbf{A} \cdot \nabla)$

$= \nabla (\mathbf{A} \cdot \mathbf{B}) - (\mathbf{A} \cdot \nabla) \mathbf{B}$

$\nabla (\mathbf{A} \cdot \mathbf{B}) = \mathbf{A} \times (\nabla \times \mathbf{B}) + (\mathbf{A} \cdot \nabla) \mathbf{B}$

注意，此時右側的 $\nabla$ 只對 $\mathbf{B}$ 作用  

$\mathbf{B} \times (\nabla \times \mathbf{A}) = \nabla (\mathbf{B} \cdot \mathbf{A}) - \mathbf{A} (\mathbf{B} \cdot \nabla)$

$= \nabla (\mathbf{B} \cdot \mathbf{A}) - (\mathbf{B} \cdot \nabla) \mathbf{A}$

$\nabla (\mathbf{B} \cdot \mathbf{A}) = \mathbf{B} \times (\nabla \times \mathbf{A}) + (\mathbf{B} \cdot \nabla) \mathbf{A}$

注意，此時右側的 $\nabla$ 只對 $\mathbf{A}$ 作用  

綜上所述，$\nabla (\mathbf{A} \cdot \mathbf{B})$ 的右側應該是上述兩者相加  
$$
\nabla (\mathbf{A} \cdot \mathbf{B}) = \mathbf{A} \times (\nabla \times \mathbf{B}) + \mathbf{B} \times (\nabla \times \mathbf{A})
$$

$$
+(\mathbf{A} \cdot \nabla) \mathbf{B}+(\mathbf{B} \cdot \nabla) \mathbf{A} 
$$

這個公式相當複雜，該如何記憶?

從右邊的第一、二項去辨認，利用BAC-CAB，辨認出其餘部分，這也是上述的整個脈絡，關鍵在於辨認出算符在對誰作用。

#### 兩向量場叉積的旋度
$$
\nabla \times (\mathbf{A} \times \mathbf{B})
$$


$\nabla \times (\mathbf{A} \times \mathbf{B}) = \mathbf{A} (\nabla \cdot \mathbf{B}) - \mathbf{B} (\nabla \cdot \mathbf{A})$

看起來好像沒辦法進行下去  

但注意，等號左邊，$\nabla$ 同時作用在 $\mathbf{A}$ 和 $\mathbf{B}$

右邊第一項，$\nabla$ 只作用在 $\mathbf{B}$，需要湊出作用在 $\mathbf{A}$ 的項

右邊第二項，$\nabla$ 只作用在 $\mathbf{A}$，需要湊出作用在 $\mathbf{B}$ 的項

$\mathbf{A} (\nabla \cdot \mathbf{B})$ 交換 $\mathbf{B}$ 和 $\nabla$ 就能湊出作用在 $\mathbf{A}$ 的項  

$$
\mathbf{A} (\mathbf{B} \cdot \nabla) = (\mathbf{B} \cdot \nabla) \mathbf{A}
$$

$\mathbf{B} (\nabla \cdot \mathbf{A})$ 交換 $\mathbf{A}$ 和 $\nabla$ 就能湊出作用在 $\mathbf{B}$ 的項  

$$
\mathbf{B} (\mathbf{A} \cdot \nabla) = (\mathbf{A} \cdot \nabla) \mathbf{B}
$$

所以，等號右邊要額外多這兩項

$$
\nabla \times (\mathbf{A} \times \mathbf{B}) = \mathbf{A} (\nabla \cdot \mathbf{B}) -\mathbf{B} (\nabla \cdot \mathbf{A})
$$

$$
+(\mathbf{B} \cdot \nabla) \mathbf{A} - (\mathbf{A} \cdot \nabla) \mathbf{B}
$$

最後，再次強調，這裡嚴格來說不算推導，只是一種方便理解的、啟發性的確認方式，考試這樣寫應該是沒分的，真的要證明應該是要在直角坐標，直接展開每個分量。
