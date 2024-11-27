from speedtest import Speedtest

wifi=Speedtest()
print("Getting Download speed...")

download = wifi.download()

print(f"Download : {download/1024/1024:.2f}mbps")
upload = wifi.upload()
print("Gettting Upload speed : ")
print(f"Upload : {upload/1024/1024:.2f}mbps")


