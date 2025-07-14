from flask import Blueprint, request, jsonify, render_template
from app.webhook.extensions import mongo

webhook_bp = Blueprint('webhook_bp', __name__)

@webhook_bp.route('/')
def index():
    return render_template('index.html')

@webhook_bp.route('/webhook', methods=['POST'])
def webhook():
    print("🔥 Webhook endpoint was hit!")
    data = request.json
    event = request.headers.get('X-GitHub-Event')
    print(f"📦 Received event: {event}")

    if event == "push":
        try:
            author = data['pusher']['name']
            to_branch = data['ref'].split("/")[-1]
            timestamp = data['head_commit']['timestamp']

            mongo.db.events.insert_one({
                "author": author,
                "to_branch": to_branch,
                "timestamp": timestamp,
                "action": "push"
            })

            print(f"✅ {author} pushed to {to_branch} on {timestamp}")
        except Exception as e:
            print("❌ Push event error:", e)

    elif event == "pull_request":
        try:
            pr = data['pull_request']
            author = pr['user']['login']
            from_branch = pr['head']['ref']
            to_branch = pr['base']['ref']
            timestamp = pr['created_at']

            mongo.db.events.insert_one({
                "author": author,
                "from_branch": from_branch,
                "to_branch": to_branch,
                "timestamp": timestamp,
                "action": "pull_request"
            })

            print(f"✅ {author} created PR from {from_branch} to {to_branch} on {timestamp}")
        except Exception as e:
            print("❌ Pull request event error:", e)

    return jsonify({"message": "Event processed"}), 200

@webhook_bp.route('/events', methods=['GET'])
def get_events():
    try:
        data = list(mongo.db.events.find({}, {"_id": 0}).sort("timestamp", -1))
        print(f"📤 Sending {len(data)} events to frontend")
        return jsonify(data)
    except Exception as e:
        print("❌ Error fetching events:", e)
        return jsonify([]), 500
