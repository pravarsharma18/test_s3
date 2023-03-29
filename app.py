from flask import Flask, jsonify
from index import response, get_all_bucket_objects

app = Flask(__name__)


@app.route('/')
def home():
    print(response.get("Buckets"))
    return jsonify({"buckets": response.get("Buckets")})

@app.route('/<bucket_name>')
def get_bucket_files(bucket_name):
    try:
        objs = get_all_bucket_objects(bucket_name)
        data = [{"key": obj['Key'], "last_modified": obj['LastModified'], "size": obj['Size']} for i, obj in enumerate(objs['Contents'])]
        return jsonify({"data": data})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
