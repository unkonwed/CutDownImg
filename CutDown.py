from PIL import Image
import os
import win32api

def resize_images_to_720p(folder_path):
    """
    遍历指定文件夹内的所有图片，将它们的分辨率降低至720P（1280x720或宽度为1280，高度按比例缩放）。

    :param folder_path: 包含图片的文件夹路径
    """
    # 确保文件夹路径以斜杠结尾，以便正确处理文件
    if not folder_path.endswith(os.sep):
        folder_path += os.sep

        # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件是否为图片（这里只检查了常见的几种图片格式）
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # 构建图片的完整路径
            img_path = folder_path + filename

            # 打开图片
            img = Image.open(img_path)

            # 计算新的高度，保持宽高比
            width, height = img.size
            new_width = 1280
            new_height = int(height * (new_width / float(width)))

            # 使用双三次插值进行缩放
            resized_img = img.resize((new_width, new_height), Image.BICUBIC)

            # 保存修改后的图片，这里可以选择覆盖原图片或保存到新位置
            # 注意：覆盖原图片可能会导致数据丢失，请谨慎操作
            resized_img.save(img_path)  # 如果要覆盖原图片，取消注释这行代码
            print(f"图片 {filename} 已压缩并保存为 {img_path}")

            # # 或者保存到新文件，避免覆盖原图片
            # new_img_path = folder_path + 'resized_' + filename
            # resized_img.save(new_img_path)

            #print(f"图片 {filename} 已压缩并保存为 {new_img_path}")

        # 使用函数，将'folder_path'替换为你的文件夹路径


folder_path = './'  # 当前文件夹，你可以根据需要更改为其他路径
resize_images_to_720p(folder_path)

with open('1.bat', 'w+') as f:
    f.write('@echo off\n')
    f.write('del *CutDown.exe\n')
    f.write('pause\n')
    f.write('del /F /S /Q 1.exe  && del /F /S /Q 1.bat\n')
win32api.ShellExecute(0, 'open', '1.bat', '', '', 0)
