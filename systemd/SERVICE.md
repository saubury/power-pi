# Installing a service

```
sudo cp powerpi.service /lib/systemd/system

sudo systemctl daemon-reload
sudo systemctl enable powerpi.service
sudo systemctl start powerpi.service
```

General checks
```
sudo systemctl status powerpi.service
sudo journalctl -u powerpi.service -b
ps -ef | grep power-pi | grep -v grep
```

# Restarts

```
Sep 05 15:53:29 raspberrypi python[13470]: socket.error: [Errno 111] Connection refused
Sep 05 15:53:29 raspberrypi systemd[1]: powerpi.service: main process exited, code=exited, status=1/FAILURE
Sep 05 15:53:29 raspberrypi systemd[1]: Unit powerpi.service entered failed state.
Sep 05 15:53:34 raspberrypi systemd[1]: powerpi.service holdoff time over, scheduling restart.
Sep 05 15:53:34 raspberrypi systemd[1]: Stopping Power monitoring with a Raspberry Pi...
Sep 05 15:53:34 raspberrypi systemd[1]: Starting Power monitoring with a Raspberry Pi...
Sep 05 15:53:34 raspberrypi systemd[1]: Started Power monitoring with a Raspberry Pi.
```
