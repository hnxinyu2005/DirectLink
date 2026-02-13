# DirectLink
Intranet P2P direct connection tool based on UDP hole punching  
Developer: hnxinyu2005  
Developer GitHub: https://github.com/hnxinyu2005  
Project URL: https://github.com/hnxinyu2005/DirectLink  

## Project Introduction
### Brief summary
We are committed to achieving peer-to-peer (P2P) direct connection between two endpoints **without exchanging IP addresses via a server**. If this is unachievable or the hole punching success rate is too low, we will switch to traditional connection methods.  
### The original intention of doing the project
I initially wanted to develop a program that allows me to play games remotely with friends in other locations, such as Minecraft, which does not support remote online play under normal circumstances. This is my first project created on GitHub, so I tried to make it as formal as possible, including writing a proper README document and following standard project structure. I regard this as a learning opportunity. I have not only learned knowledge about network communication but also gradually learned how to build a good project.  
### Current prompt
The version currently under development is expected to adopt a **time-synchronized approach** for P2P hole punching. This scheme may be removed in later versions, primarily because time-synchronized hole punching is sensitive to device clock accuracy, network latency, and NAT types. Its stability and success rate are limited in complex networks (e.g., cross-region connections, mobile hotspots, symmetric NAT). To ensure reliable connectivity in subsequent versions, it may be replaced with a more general hole punching strategy.  

## Development Status
### Current Stage Version:
**v0.1.0 - Initial Prototype (LAN only)**  
This version implements a basic LAN communication module using Python, supporting **two-way communication** between two computers **within the same LAN**. It does not yet support cross-LAN or public network communication, serving as a prototype of the core underlying communication.  
### How to use: (Only applicable for this release)