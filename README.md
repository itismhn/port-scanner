# Basic TCP/IP Port Scanner 

simple port scanner tool using python and 
integrated with TOR in v2.0

## Usage
```
git clone https://github.com/itismhn/port-scanner.py
pip install -r requirement.txt
python3 port-scanner.py
```
## Using TOR
#### Step1 - Install dependencies
```
sudo apt update
pip install -r requirements.txt
sudo apt install tor
```
#### Step2 - Generate Hashed Controled Password
```
tor --hash-password <your password>
```
#### Step3 - Copy the hash then edit /etc/tor/torrc
```
sudo nano /etc/tor/torrc
```
Enable ControlPort, HashedControlPassword, CookieAuthentication
#### Step4 - Restart TOR Service
```
sudo systemctl restart tor
```
