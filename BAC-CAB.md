證明 \( \mathbf{A} \times (\mathbf{B} \times \mathbf{C}) = (\mathbf{A} \cdot \mathbf{C})\mathbf{B} - (\mathbf{A} \cdot \mathbf{B})\mathbf{C} \)（即 **BAC-CAB 定則**），使用 **Levi-Civita 符號** 和 **愛因斯坦求和約定** 進行推導。

---

为了证明向量三重积公式 \( \mathbf{A} \times (\mathbf{B} \times \mathbf{C}) = (\mathbf{A} \cdot \mathbf{C})\mathbf{B} - (\mathbf{A} \cdot \mathbf{B})\mathbf{C} \)（即 BAC-CAB 定則），我们使用 Levi-Civita 符号和爱因斯坦求和约定进行推導。

首先，向量叉积可以用 Levi-Civita 符号表示。左边向量三重积 \(\mathbf{A} \times (\mathbf{B} \times \mathbf{C})\) 的第 \(m\) 个分量为：
\[
[\mathbf{A} \times (\mathbf{B} \times \mathbf{C})]_m = \epsilon_{mni} A_n (\mathbf{B} \times \mathbf{C})_i
\]
其中，\(\mathbf{B} \times \mathbf{C}\) 的第 \(i\) 个分量为：
\[
(\mathbf{B} \times \mathbf{C})_i = \epsilon_{ijk} B_j C_k
\]

将 \(\mathbf{B} \times \mathbf{C}\) 的分量代入左边表达式，得到：
\[
[\mathbf{A} \times (\mathbf{B} \times \mathbf{C})]_m = \epsilon_{mni} A_n \epsilon_{ijk} B_j C_k
\]

接下来处理两个 Levi-Civita 符号的乘积 \(\epsilon_{mni} \epsilon_{ijk}\)。利用 Levi-Civita 符号的恒等式：
\[
\epsilon_{imn} \epsilon_{ijk} = \delta_{mj} \delta_{nk} - \delta_{mk} \delta_{nj}
\]
其中，\(\epsilon_{mni}\) 可以写成 \(\epsilon_{imn}\)，因此：
\[
\epsilon_{mni} \epsilon_{ijk} = \epsilon_{imn} \epsilon_{ijk} = \delta_{mj} \delta_{nk} - \delta_{mk} \delta_{nj}
\]

代入后，左边的分量表达式变为：
\[
[\mathbf{A} \times (\mathbf{B} \times \mathbf{C})]_m = (\delta_{mj} \delta_{nk} - \delta_{mk} \delta_{nj}) A_n B_j C_k
\]

展开并简化这两个项：
1. 第一项 \(\delta_{mj} \delta_{nk} A_n B_j C_k\) 简化为 \(B_m (A_n C_n)\)，即 \(B_m (\mathbf{A} \cdot \mathbf{C})\)；
2. 第二项 \(-\delta_{mk} \delta_{nj} A_n B_j C_k\) 简化为 \(-C_m (A_n B_n)\)，即 \(-C_m (\mathbf{A} \cdot \mathbf{B})\)。

因此，左边的分量表达式为：
\[
[\mathbf{A} \times (\mathbf{B} \times \mathbf{C})]_m = B_m (\mathbf{A} \cdot \mathbf{C}) - C_m (\mathbf{A} \cdot \mathbf{B})
\]

这对应右边的向量表达式：
\[
(\mathbf{A} \cdot \mathbf{C})\mathbf{B} - (\mathbf{A} \cdot \mathbf{B})\mathbf{C}
\]

因此，向量三重积公式得证：
\[
\boxed{ \mathbf{A} \times (\mathbf{B} \times \mathbf{C}) = (\mathbf{A} \cdot \mathbf{C})\mathbf{B} - (\mathbf{A} \cdot \mathbf{B})\mathbf{C} }
\]