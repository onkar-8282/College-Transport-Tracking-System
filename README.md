# 🚌 College Transport Tracking System

A web-based system to track **college buses in real-time** using **Flask** and **OpenStreetMap**.  
This project provides different dashboards for **Students**, **Drivers**, and **Administrators**.

---

## 🚀 Features

### 🎓 For Students
- 🗺️ Real-time bus location tracking on the map  
- 🚌 Bus route and stop details  
- 🔍 Filter to check the required bus  
- ⏰ Bus timings and current status  

### 👨‍✈️ For Drivers
- ▶️ Start and 🛑 End trip logging  
- 📍 Update real-time location manually or via GPS  
- 🧭 Route navigation assistance  

### 👩‍💼 For Administrators
- ➕ Add / ✏️ Edit / 🗑️ Delete bus details  
- 👨‍✈️ Add new driver accounts from the admin panel  
- 🌍 Track all buses live on a single map  
- 🔄 Auto-refresh for live status and data updates  

---

## 🧰 Tech Stack

| Component | Technology |
|------------|-------------|
| **Backend** | Python (Flask) |
| **Frontend** | HTML, CSS, JavaScript |
| **Map API** | Leaflet + OpenStreetMap (Free, No API Key Needed) |
| **Database** | JSON Files (`bus_data.json`, `users.json`) |
| **Hosting (Optional)** | Render / Railway / PythonAnywhere |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone this Repository
```bash
git clone https://github.com/your-username/college-transport-tracking.git
cd college-transport-tracking
```
### 2️⃣ Install Required Libraries
```bash
pip install flask
```
### 3️⃣ Run the Application
```bash
python app.py
```
### 4️⃣ Open in Browser
```cpp
http://127.0.0.1:5000
```
### 🔑 Default Login Details
| Role         | Username   | Password    | URL       |
| ------------ | ---------- | ----------- | --------- |
| 🧑‍💼 Admin  | `admin`    | `admin123`  | `/admin`  |
| 👨‍✈️ Driver | `driver1`  | `driver123` | `/driver` |
| 🎓 Student   | (no login) | —           | `/`       |
### 📁 Folder Structure
```pgsql
college_transport_tracking/
│
├── app.py
├── bus_data.json
├── users.json
└── templates/
    ├── index.html        # Student Interface (Map + Filter + Timings)
    ├── admin.html        # Admin Panel (Add/Edit/Delete Buses)
    ├── driver.html       # Driver Panel (Location Update)
    └── login.html        # Login Page
```
### 🌍 Default Location
The system is preconfigured for Titwala:
```makefile
Latitude: 19.2579
Longitude: 73.2007
```
### 🧠 Future Enhancements

- 📱 GPS-based auto-location for drivers (via mobile browser)
- 🔔 Notifications for delays or bus arrival
- 🗃️ Migrate data from JSON → SQLite or MySQL
- ⚡ WebSocket or Socket.IO for instant updates
- 🔐 Student login & attendance integration
