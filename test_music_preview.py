import os
import sys

# 模拟音乐管理的试听功能
def test_music_preview():
    # 模拟添加文件
    test_file = "yuanhangxing.mp3"
    
    # 检查文件是否存在
    print(f"测试文件: {test_file}")
    print(f"文件是否存在: {os.path.exists(test_file)}")
    print(f"文件绝对路径: {os.path.abspath(test_file)}")
    
    # 模拟保存到Qt.UserRole
    user_role_path = os.path.abspath(test_file)
    print(f"保存到UserRole的路径: {user_role_path}")
    
    # 模拟试听功能
    print("\n模拟试听功能:")
    print(f"从UserRole获取的路径: {user_role_path}")
    print(f"文件是否存在: {os.path.exists(user_role_path)}")
    
    if os.path.exists(user_role_path):
        print("文件存在，可以试听")
    else:
        print("文件不存在，无法试听")

if __name__ == "__main__":
    test_music_preview()
