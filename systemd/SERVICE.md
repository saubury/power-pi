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
