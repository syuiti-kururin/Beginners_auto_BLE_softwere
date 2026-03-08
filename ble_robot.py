#v2
#2026/03/08/21:43
import asyncio
import threading
import tkinter as tk
from bleak import BleakClient

#your pico dvice's unipue UUID, check with "sudo hci leccan" on terminal
ADDRESS = "2C:CF:67:CC:B5:B4"
#your "ble_simple_peripheral" code's TX characteristic UUID defuults to "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"
UART_TX = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"
#your "ble_simple_peripheral" code's RX characteristic UUID defuults to "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"
UART_RX = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"

# BLEクライアントとイベントループのグローバル変数
client =None
client = BleakClient(ADDRESS)
loop = None
loop = asyncio.new_event_loop()

# BLE受信
def notify_handler(sender, data):
    msg = data.decode()
    log_box.insert(tk.END, "RX: " + msg + "\n")
    log_box.see(tk.END)

# BLE接続
async def connect_ble():
    global client
    status_label.config(text="Connecting...")
    await client.connect()

    if client.is_connected:
        status_label.config(text="Connected")
        await client.start_notify(UART_TX, notify_handler)
    else:
        status_label.config(text="Disconnected")

# コマンド送信
async def send_cmd(cmd):
    global client

    if client and client.is_connected:
        await client.write_gatt_char(UART_RX, cmd.encode())
        log_box.insert(tk.END, "TX: " + cmd + "\n")
        log_box.see(tk.END)

def send(cmd):
    asyncio.run_coroutine_threadsafe(send_cmd(cmd), loop)



# GUI
root = tk.Tk()
root.title("ROBO BLE Controller")

status_label = tk.Label(root, text="Disconnected")
status_label.pack()

connect_btn = tk.Button(root, text="Connect", command=lambda: asyncio.run_coroutine_threadsafe(connect_ble(), loop))
connect_btn.pack()


# --- 操作ボタン ---

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Forward", width=10, command=lambda: send("F")).grid(row=0, column=1)

tk.Button(frame, text="Left", width=10, command=lambda: send("L")).grid(row=1, column=0)
tk.Button(frame, text="Stop", width=10, command=lambda: send("X")).grid(row=1, column=1)
tk.Button(frame, text="Right", width=10, command=lambda: send("R")).grid(row=1, column=2)

tk.Button(frame, text="Back", width=10, command=lambda: send("B")).grid(row=2, column=1)


# --- 自動モード ---

auto_frame = tk.Frame(root)
auto_frame.pack()

tk.Button(auto_frame, text="AUTO", width=10, command=lambda: send("A")).pack(side="left")
tk.Button(auto_frame, text="Manual", width=10, command=lambda: send("Op")).pack(side="left")


# --- ログ表示 ---

log_box = tk.Text(root, height=15, width=50)
log_box.pack()



# asyncio event loop


def start_loop():
    global loop
    asyncio.set_event_loop(loop)
    loop.run_forever()


threading.Thread(target=start_loop, daemon=True).start()

root.mainloop()
