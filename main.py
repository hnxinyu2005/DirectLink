# main.py

import sys

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
        from core.udp import create_udp_socket, udp_send, udp_receive
        from utils.config import UDP_PORT

        udp_socket = create_udp_socket()
        print("[Main] UDP 服务已启动")

        if len(sys.argv) < 2:
            print("使用提示：")
            print("   接收模式：python main.py receive")
            print("   发送模式：python main.py send <目标IP> \"<消息内容>\"")
            return

        if sys.argv[1] == "receive":
            print("[Main] 接收模式，等待消息（按下Ctrl+C退出）")
            while True:
                try:
                    udp_receive(udp_socket)
                except KeyboardInterrupt:
                    print("[Main] 接收模式已退出")
                    break

        elif sys.argv[1] == "send":
            if len(sys.argv) < 4:
                print("[Error] 发送需要指定格式：python main.py send <目标IP> \"<消息内容>\"")
                return

            # 提取信息
            target_ip = sys.argv[2]
            message = sys.argv[3]

            udp_send(udp_socket, target_ip, UDP_PORT, message)
            print("[Main] 消息发送完成")

        else:
            print(f"[Error] 无效的模式\"{sys.argv[1]}\"，可选：receive / send")

    except Exception as error:
        print(f"[Error] UDP 服务启动失败：{error}")

if __name__ == "__main__":
    main()