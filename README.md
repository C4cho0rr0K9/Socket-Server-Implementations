#  Python TCP Echo Server (Concurrent)

##  Description
This repository contains a foundational example of network programming utilizing Python's standard `socket` library and the built-in `threading` module.

The project demonstrates how to implement a simple **TCP Server** that employs a **thread-based concurrency model** to handle multiple client connections simultaneously without blocking. The server's main function is to act as an **"Echo Server"**, sending back to the client the exact message it receives.

##  Key Features Demonstrated
* **Protocol:** **TCP** (Transmission Control Protocol) – Stream/Connection-oriented.
* **Concurrency:** Implemented using **Python's `threading`** module to manage several clients concurrently.
* **Networking Fundamentals:** Correct handling of socket lifecycle (`bind`, `listen`, `accept`, `send`, `recv`).
* **Error Handling:** Basic handling of client disconnections and network errors.

##  How to Run

Ensure you have **Python 3** installed on your system.

### 1.  Navigate to the Directory

Open your terminal and navigate to the `python-tcp-echo-server` directory.

<img width="1509" height="375" alt="Captura desde 2025-11-25 23-48-22" src="https://github.com/user-attachments/assets/d639b3a1-f250-495b-8107-d05c06021352" />


### 2.  Start the Server

In the first terminal window, execute the server script:

```bash
python3 server.py
```
The server will start listening on 127.0.0.1:65432

<img width="1509" height="375" alt="Captura desde 2025-11-25 23-48-22" src="https://github.com/user-attachments/assets/3bccc6d0-55a8-41f8-88be-29400693d204" />

### 3. Start the Client(s)

```bash
python3 client.py
```
The client will connect, send two test messages, and immediately print the server's "Echo" response before closing the connection.

<img width="1920" height="1034" alt="Captura desde 2025-11-25 23-52-50" src="https://github.com/user-attachments/assets/7b36cd68-750c-415b-943c-dfc8138e4ffa" />
