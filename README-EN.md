# DirectLink
[中文版本](README.md)

Intranet P2P direct connection tool based on UDP hole punching  
Developer: hnxinyu2005  
Developer GitHub: https://github.com/hnxinyu2005  
Project URL: https://github.com/hnxinyu2005/DirectLink 

## Project Introduction

### Brief Overview
It aims to achieve P2P direct connection between two devices without exchanging IP addresses through a server.  
If direct connection fails or the hole punching success rate is too low, it will fall back to using traditional connection methods.

### Motivation for the Project
I first envisioned developing a program that would allow me to remotely play games with friends in other locations, such as *Minecraft*, which does not support remote multiplayer under normal circumstances. This is my first project created on the GitHub community, so I have structured it to the standards of a formal open-source project as much as possible—including writing a proper README document and following standard project structure, among other things. I regard this as a learning opportunity: I have not only gained knowledge related to network communication but also been gradually learning how to deliver a well-built project.

### Current Notice
The current development version plans to implement P2P hole punching using a **time synchronization** approach. This solution may be removed in later versions, mainly because time-synchronized hole punching is sensitive to device clocks, network latency, and NAT types. Its stability and success rate are limited in complex networks (e.g., cross-region connections, mobile hotspots, symmetric NAT). To ensure reliable hole punching, it may be replaced with a more general hole-punching strategy.

## Development Status

### Current Stage Version
**v0.1.0 - Initial Prototype (LAN only)**
This version implements a basic LAN communication module based on Python, supporting **bidirectional communication** between two computers **within the same local area network (LAN)**. Cross-LAN/public network communication is not supported for the time being, and this is a prototype version of the core underlying communication.  
Only the **sending and receiving of simple strings** is implemented at this stage to verify the feasibility of LAN communication, and extended functions such as file transfer are not supported temporarily.

### How to Use (Only Applicable to Version v0.1.0)
1. Prepare two computers: Device A (sender) and Device B (receiver), ensuring both devices are **on the same local area network (LAN)**.

2. On Device B, open cmd and enter the following command to obtain the intranet IPv4 address:

    ```cmd
    ipconfig
    ```
   
    Locate the "IPv4 Address" in the output and record it (usually starting with 192.168.x.x);

3. On Device B, run the following command in cmd to start the receiving program:

    ```cmd
    python main.py receive
    ```

4. On Device A, enter the following command in cmd to send a message:

    ```cmd
    python main.py send <Device B's IPv4 address> "<message content>"
    ```
   
    Example:

    ```cmd
    python main.py send 192.168.1.186 "Hello, DirectLink!"
    ```
   
    This command is used to send the string: "Hello, DirectLink!" to 192.168.1.186.

5. The received message will be visible in the cmd window on Device B.

## How the Program Works
Under development, to be added later.

## Disclaimer and Usage Statement
This project is currently under development. It is planned to be a learning and experimental tool based on UDP hole punching technology, designed to help developers understand the principles of intranet penetration and peer-to-peer communication.

### Core Statement
Regardless of the development stage of the project, users must agree to and comply with the following terms:
- **Non-commercial Use**: This project is for **personal study, technical research and non-commercial purposes only** (e.g., gaming with friends). Commercial use or unauthorized network services are strictly prohibited.
- **No Warranty and Risk Assumption**: This software is provided "as is" without any express or implied warranties, including but not limited to warranties of merchantability, fitness for a particular purpose and non-infringement. **Users assume all risks and consequences arising from the use of this software.**
- **Compliance**: Users must **strictly abide by the laws and regulations of their country/region and the rules of their network service providers**. Using this tool for any illegal, malicious or unauthorized network activities is prohibited. If used in Chinese mainland, users shall additionally comply with relevant Chinese laws and regulations, and ensure all files/data transmitted via this tool are legal and compliant. **Establishing any network connection between Chinese mainland and overseas regions, or conducting any cross-border network communication through this tool is strictly prohibited.**
- **Data Security**: This tool **plans to encrypt** data during transmission, but users should still protect personal privacy and sensitive information and avoid use in insecure network environments. **Any adverse consequences caused by the use of this software, including information leakage, device attacks, data loss, etc., shall be borne by the user.**

### Important Notice
- This project is under continuous development. Its features are not yet complete and have not undergone security testing, so there may be stability, compatibility, and security issues. **Do not use in a production environment.**
- The developer shall not bear any legal or related liabilities for any adverse consequences caused by the use of this tool, including device damage, data loss/leakage, network interruption, or legal disputes.

## TODO
This version is a Release version, to be added later.

Last updated: 2026-02-14
