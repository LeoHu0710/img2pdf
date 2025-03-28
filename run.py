from PIL import Image
import os

# 設定圖片的目錄及 PDF 檔名
image_folder = 'path'  # 例如 './images'
pdf_filename = 'path/output.pdf'

# 取得圖片列表並按檔名排序
image_files = sorted([f for f in os.listdir(image_folder) if f.endswith(('jpg', 'jpeg', 'png'))])

# 打開第一張圖片作為 PDF 的首頁
first_image_path = os.path.join(image_folder, image_files[0])
first_image = Image.open(first_image_path).convert('RGB')

# 轉換其餘的圖片
other_images = []
for file in image_files[1:]:
    image_path = os.path.join(image_folder, file)
    img = Image.open(image_path).convert('RGB')
    other_images.append(img)

# 儲存成 PDF
first_image.save(pdf_filename, save_all=True, append_images=other_images)
print(f"Image to PDF conversion successful, PDF path：{pdf_filename}")
