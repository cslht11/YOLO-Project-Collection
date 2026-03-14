# 原始文件路径
file_path = r'D:\A_Python\YOLO_RAW\data\ImageSets\val.txt'

# 添加目录前缀并直接写回原文件
prefix = 'D:/A_Python/YOLO_RAW/'
with open(file_path, 'r+') as file:
    lines = file.readlines()
    file.seek(0)  # 将文件指针移回文件开头
    file.truncate()  # 清空文件内容

    # 写入修改后的行
    for line in lines:
        modified_line = prefix + line.strip()
        file.write(modified_line + '\n')
