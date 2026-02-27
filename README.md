# codtech-3
#  Real-Time Streaming Dashboard using Power BI

##  Project Overview
This project demonstrates how to build a **real-time dashboard** using Power BI and streaming data. The dashboard automatically updates whenever new data is received, enabling instant monitoring and live analytics. This type of system is commonly used in business intelligence, finance monitoring, IoT systems, and operational tracking.

---

##  Objective
To design and deploy a **live Power BI dashboard** that:
- Accepts streaming data
- Updates automatically
- Displays real-time insights visually

---

##  Tools & Technologies Used
- Power BI Service  
- Streaming Dataset (API)  
- Python (for data simulation)  
- JSON Data Format  

---

##  Implementation Steps

### 1️ Create Streaming Dataset
- Open Power BI Service  
- Go to **Workspace → New → Streaming Dataset**  
- Select **API**  
- Add fields such as:
  - Timestamp → DateTime
  - Sales → Number
  - Region → Text

---

### 2️ Push Streaming Data (Python Script)

```python
import requests
import json
import time
import random
from datetime import datetime

url = "YOUR_POWERBI_PUSH_URL"

while True:
    data = [{
        "Timestamp": str(datetime.now()),
        "Sales": random.randint(100,500),
        "Region": random.choice(["South","North","East","West"])
    }]
    
    requests.post(url, data=json.dumps(data))
    time.sleep(3)
