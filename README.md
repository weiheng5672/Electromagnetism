# 學習電磁學筆記倉庫

本倉庫為個人學習電磁學的筆記，主要內容基於 Griffiths 的《Introduction to Electrodynamics 4/e》。

## 參考書籍

在學習過程中，筆記穿插以下參考書籍的內容，以提供更全面的理解：
- **David J. Griffiths**，《Introduction to Electrodynamics 4/e》
- **Cheng**，《Field and Wave Electromagnetics 2/e》
- **RAO**，《Elements of Engineering Electromagnetics 6/e》
- **費曼**，《費曼物理學講義 第二冊》

## 習題與計算

習題部分，涉及計算的內容將透過 Python 實現，以提高計算效率並增進理解。

---

## 環境安裝與設定

為確保程式碼能夠順利運行，請依照以下步驟安裝必要的軟體與環境設定。

### 1. 必要軟體

請先安裝以下軟體：
1. [Conda](https://docs.conda.io/en/latest/miniconda.html)
2. [PyCharm Community](https://www.jetbrains.com/pycharm/download/)

### 2. 建立與設定 Conda 環境

1. 安裝 Conda 後，打開 PowerShell。
2. 執行以下指令來建立 Conda 環境並安裝必要的 Python 套件。

   #### 建立新的 Conda 環境
   ```bash
   conda create --name Griffiths_env python=3.9
   ```

   #### 確認環境建立成功
   ```bash
   conda env list
   ```
   確認列表中有 `Griffiths_env` 之後，啟動該環境。

   #### 啟動 Conda 環境
   ```bash
   conda activate Griffiths_env
   ```
   確認提示符的最前方變成 `(Griffiths_env)`，表示環境已啟動。

   #### 安裝必要的 Python 套件
   ```bash
   pip install numpy scipy sympy matplotlib
   ```
   安裝過程中可能會要求確認，輸入 `y` 以繼續。

### 3. 設定 PyCharm

1. 打開 PyCharm Community。
2. 選擇 `Open`，然後選取存放程式碼的資料夾。
3. 設定 Python 解釋器：
   1. 進入 `File -> Settings -> Project -> Python Interpreter`
   2. 點選 `Add Interpreter -> Add Local Interpreter -> Select Existing`
   3. 類型選擇 `Conda`
   4. 環境選擇 `Griffiths_env`
   5. 按下 `OK`，等待右下方的進度條跑完。

### 4. 執行 Python 程式

1. 在 PyCharm 中選擇要執行的 Python 檔案。
2. 點擊上方的 `▶` 按鈕，即可執行程式。

---

