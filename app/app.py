from flask import Flask, render_template, request, redirect, url_for
from utils.ai_helper import generate_response
from app.models import MoodEntry, CBTEntry, UserData,CheckInEntry
import json
from datetime import datetime
from dataclasses import asdict
from app.resources import MoodForm, CBTForm, CheckInForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'replace-this-with-a-secure-random-key'
DATA_FILE = "app/data/user_data.json"

# Load user data
def load_data() -> UserData:
    try:
        with open(DATA_FILE, "r") as f:
            raw = json.load(f)
            # If raw is a list, convert to new dict format
            if isinstance(raw, list):
                moods = [MoodEntry(**m) for m in raw]
                return UserData(moods=moods, cbt_sessions=[])
            # If raw is a dict, use new format
            moods = [MoodEntry(**m) for m in raw.get("moods", [])]
            cbt = [CBTEntry(**c) for c in raw.get("cbt_sessions", [])]
            return UserData(moods=moods, cbt_sessions=cbt)
    except FileNotFoundError:
        return UserData()

# Save user data

def save_data(user_data: UserData):
    with open(DATA_FILE, "w") as f:
        json.dump(asdict(user_data), f, indent=2)

@app.route("/")
def home():
    return render_template("home.html")



@app.route("/mood", methods=["GET", "POST"])
def mood():
    form = MoodForm()
    data = load_data()
    if form.validate_on_submit():
        new_entry = MoodEntry(
            date=form.date.data.strftime('%Y-%m-%d'),
            mood=form.mood.data,
            notes=form.notes.data
        )
        data.moods.append(new_entry)
        save_data(data)
       
    return render_template("mood.html", form=form)

@app.route("/cbt", methods=["GET", "POST"])
def cbt():
    form = CBTForm()
    data = load_data()
    if form.validate_on_submit():
        new_entry = CBTEntry(
            date=form.date.data.strftime('%Y-%m-%d'),
            thought=form.thought.data,
            ai_response="(AI processing would go here)"
        )
        data.cbt_sessions.append(new_entry)
        save_data(data)
       
    return render_template("cbt.html", form=form)
@app.route("/checkin")
def checkin():
    form = CheckInForm()
    data = load_data()
    if form.validate_on_submit():
        new_entry = CheckInEntry(
            date=form.date.data.strftime('%Y-%m-%d'),
            mood=form.mood.data,
            notes=form.notes.data
        )
        data.checkins.append(new_entry)
        save_data(data)
        # Redirect to a history page or similar after submission
        # return redirect(url_for("checkin_history"))  # Uncomment if you have a history page
    return render_template("checkin.html")

