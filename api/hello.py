# api/hello.py
import json

def handler(request):
    return json.dumps({"message": "Hello from Vercel Python!"}), 200, {'Content-Type': 'application/json'}
