import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter

# 創建主窗口
root = tk.Tk()
root.title("圖像處理應用程序")

# 創建變量來存儲圖像
image_path = ""
processed_image_path = ""

# 載入圖像
def load_image():
    global image_path
    image_path = filedialog.askopenfilename(title="請選擇圖像", filetypes=[("圖像文件", ".jpg .png .bmp .tiff")])
    if image_path:
        img = Image.open(image_path)
        # 將圖像顯示在GUI中
        photo = ImageTk.PhotoImage(img)
        canvas.image = photo
        canvas.create_image(0, 0, anchor='nw', image=photo)

def remove_background_and_crop(image_path):
    # 開啟圖片
    image = Image.open(image_path)

    # 轉成灰階
    image = image.convert('L')

    # 模糊化
    image = image.filter(ImageFilter.GaussianBlur(radius=5))

    # 找出邊框
    image_edges = image.filter(ImageFilter.FIND_EDGES)

    # 找出邊框框線
    image_lines = image_edges.filter(ImageFilter.FIND_EDGES)

    # 找出最外層邊框
    bbox = image_lines.getbbox()

    # 旋轉圖片
    angle = image_lines.rotate(-90, expand=True).getbbox()[2]
    image = image.rotate(-angle, expand=True)

    # 找出長方形位置
    width, height = image.size
    for y in range(height):
        for x in range(width):
            if image.getpixel((x, y)) < 255:
                image.putpixel((x, y), 255)
            else:
                image.putpixel((x, y), 0)

    bbox = image.getbbox()

    # 裁剪圖片
    image = image.crop(bbox)

    # 儲存圖片
    image.save("output.jpg")
    image.show()

# 處理圖像
def process_image():
    global processed_image_path
    if image_path:
        img = Image.open(image_path)
        # 轉換成黑色背景並裁剪
        img = remove_background_and_crop(img)
        # 保存處理後的圖像
        processed_image_path = "processed_" + image_path
        img.save(processed_image_path)
        # 將處理後的圖像顯示在GUI中
        photo = ImageTk.PhotoImage(img)
        processed_canvas.image = photo
        processed_canvas.create_image(0, 0, anchor='nw', image=photo)

# 創建GUI元素
load_button = tk.Button(root, text="載入圖像", command=load_image)
load_button.pack()

process_button = tk.Button(root, text="處理圖像", command=process_image)
process_button.pack()

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

processed_canvas = tk.Canvas(root, width=500, height=500)
processed_canvas.pack()

root.mainloop()
