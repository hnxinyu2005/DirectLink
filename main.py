# main.py
from logging import exception

project_name = "DirectLink"
project_description = "Intranet P2P direct connection tool based on UDP hole punching"
project_author = "hnxinyu2005"
project_URL = "https://github.com/hnxinyu2005/DirectLink"
project_warning = """
    Any illegal use of this software is strictly prohibited.
    Users shall bear all legal responsibilities for violations."""

def main():
    print("Name: " + project_name)
    print("Description: " + project_description)
    print("Author: " + project_author)
    print("URL: " + project_URL)
    print()
    print("Warning: " + project_warning)
    print()

    print("[Main] 初始化")

    try:
        from core.udp import create_udp_socket
        udp_socket = create_udp_socket()
        print("[Main] UDP 服务已启动")
    except Exception as error:
        print(f"[Error] UDP 服务启动失败：{error}")

if __name__ == "__main__":
    main()