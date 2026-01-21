# Gel Image Auto Cropper (電泳膠片自動裁切工具)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pillow](https://img.shields.io/badge/Library-Pillow-green)
![Status](https://img.shields.io/badge/Status-Maintained-success)

## 專案背景 (Background)
本專案開發於 2022 年，應用於大學部的「生物核心技術實驗」課程。該課程以 **分子生物學中心法則 (Central Dogma)** 為骨幹，引導學生學習從基因到蛋白質的完整實驗流程：

1. **基因選殖**：以 GUS 酵素基因 (GUS gene) 為標的。
2. **基因轉殖與剪接**：DNA Splicing & Gene Transfer。
3. **基因表現**：在宿主細胞 (Host Cells) 中誘導表現。
4. **檢定與純化**：檢測 mRNA 表現量，並進行蛋白質收集與純化 (Purification)。

## 問題陳述 (Problem Statement)
在實驗過程中，學生需拍攝電泳膠片 (Electrophoresis Gels) 並將其黏貼於實驗紀錄簿 (Lab Notebook)。作為助教，我每週需要處理數十份學生的膠片照片，面臨以下痛點：
* **重複性高**：每張照片都需要手動旋轉、去除背景雜訊並裁切成統一矩形。
* **耗時**：人工處理每次耗費約1小時，且容易產生格式不一的問題。

## 解決方案 (Solution)
開發了一套基於 Python 的自動化影像處理工具，並使用 **Tkinter** 封裝成 GUI 介面，甚至打包為 `.exe` 執行檔供實驗室公用電腦直接使用。

### 主要功能
* **自動影像處理**：利用 `Pillow` 函式庫進行高斯模糊 (Gaussian Blur) 降噪、邊緣檢測 (Edge Detection) 與輪廓識別。
* **智慧裁切與旋轉**：自動偵測膠片邊框 (Bounding Box)，校正歪斜角度並裁切出完美矩形。
* **直觀操作介面**：助教或學生僅需一鍵載入圖片，即可獲得處理完成的檔案。

## 成果與效益 (Impact)
* **效率提升**：將每次原本需花費 **1 小時以上** 的人工修圖時間，縮短至 **30 秒** 內完成。
* **標準化**：確保所有學生的實驗紀錄圖片格式統一，提升實驗報告品質。
* **易用性**：打包後的執行檔無需安裝 Python 環境，成功部署於實驗室電腦供多屆助教使用。

## 實際演示 (Demo)

### 原始膠片 (Raw Data)
`![Raw Gel](data/demo/before.png)`

### 處理後成果 (Processed Output)
`![Processed Gel](data/demo/after.png)`

## 使用技術 (Tech Stack)
* **Language:** Python
* **GUI Framework:** Tkinter
* **Image Processing:** PIL (Pillow) - `Image`, `ImageTk`, `ImageFilter`

## 如何執行 (How to Run)
```bash
# Clone the repository
git clone [https://github.com/](https://github.com/)[YourUsername]/Gel-Image-Auto-Cropper.git

# Install dependencies
pip install -r requirements.txt

# Run the application

python src/main.py
