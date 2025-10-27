from flask import Flask, render_template, jsonify, request, redirect, url_for, session
import json, os

app = Flask(__name__)
app.secret_key = "collegebus-secret-key"

DATA_FILE = "bus_data.json"
USER_FILE = "users.json"

# -------------------- INITIAL SETUP --------------------
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({"buses": []}, f, indent=2)

if not os.path.exists(USER_FILE):
    users = {
        "admin": {"username": "admin", "password": "admin123", "role": "admin"},
        "driver1": {"username": "driver1", "password": "driver123", "role": "driver"}
    }
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=2)

def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def load_users():
    with open(USER_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=2)

# -------------------- STUDENT PAGE --------------------
@app.route("/")
def student_view():
    return render_template("index.html")

@app.route("/location_data")
def location_data():
    return jsonify(load_data())

# -------------------- LOGIN SYSTEM --------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        users = load_users()

        for user in users.values():
            if user["username"] == username and user["password"] == password:
                session["username"] = username
                session["role"] = user["role"]
                if user["role"] == "admin":
                    return redirect(url_for("admin_panel"))
                elif user["role"] == "driver":
                    return redirect(url_for("driver_view"))
        return render_template("login.html", error="❌ Invalid username or password")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# -------------------- ADMIN PANEL --------------------
@app.route("/admin", methods=["GET", "POST"])
def admin_panel():
    if session.get("role") != "admin":
        return redirect(url_for("login"))

    data = load_data()
    users = load_users()
    drivers = [u for u in users.values() if u["role"] == "driver"]

    if request.method == "POST":
        bus_no = request.form.get("bus_no")
        route = request.form.get("route")
        driver = request.form.get("driver")
        departure = request.form.get("departure_time")
        arrival = request.form.get("arrival_time")

        for bus in data["buses"]:
            if bus["bus_no"] == bus_no:
                bus["route"] = route
                bus["driver"] = driver
                bus["departure_time"] = departure
                bus["arrival_time"] = arrival
                break
        else:
            data["buses"].append({
                "bus_no": bus_no,
                "route": route,
                "driver": driver,
                "latitude": 19.2579,  # Titwala base location
                "longitude": 73.2007,
                "status": "Idle",
                "departure_time": departure,
                "arrival_time": arrival
            })

        save_data(data)
        return redirect(url_for("admin_panel"))

    return render_template("admin.html", buses=data["buses"], drivers=drivers)

@app.route("/admin/delete/<bus_no>")
def delete_bus(bus_no):
    if session.get("role") != "admin":
        return redirect(url_for("login"))

    data = load_data()
    data["buses"] = [bus for bus in data["buses"] if bus["bus_no"] != bus_no]
    save_data(data)
    return redirect(url_for("admin_panel"))


# -------------------- DRIVER PAGE --------------------
@app.route("/driver", methods=["GET", "POST"])
def driver_view():
    if session.get("role") != "driver":
        return redirect(url_for("login"))

    data = load_data()

    if request.method == "POST":
        bus_no = request.form.get("bus_no")
        lat = float(request.form.get("latitude"))
        lon = float(request.form.get("longitude"))
        status = request.form.get("status")

        for bus in data["buses"]:
            if bus["bus_no"] == bus_no:
                bus["latitude"] = lat
                bus["longitude"] = lon
                bus["status"] = status
                break
        save_data(data)
        return "✅ Location updated successfully!"
    return render_template("driver.html", buses=data["buses"])

if __name__ == "__main__":
    app.run(debug=True)
