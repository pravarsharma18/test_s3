from flask import Flask, jsonify, request
from index import response, get_all_bucket_objects, get_all_bucket_folder, create_s3_bucket

app = Flask(__name__)


@app.route('/')
def home():
    print(response.get("Buckets"))
    return jsonify({"buckets": response.get("Buckets")})

@app.route('/<bucket_name>')
def get_bucket_folder(bucket_name):
    try:
        objs = get_all_bucket_objects(bucket_name)
        folder = request.args.get("folder")
        if folder:
            objs = get_all_bucket_folder(bucket_name, folder)
        try:
            data = [{"key": obj['Prefix']} for i, obj in enumerate(objs['CommonPrefixes'])]
        except: # noqa
            data = [{"key": obj['Key'], "last_modified": obj['LastModified'], "size": obj['Size']} for i, obj in enumerate(objs['Contents'])]
        return jsonify({"data": data})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/create', methods=['POST'])
def create_bucket():
    try:
        data = request.get_json()
        bucket_name = data.get("bucket_name")
        location = data.get("location")
        if not bucket_name:
            return jsonify({"bucket_name": "Bucket name is required."})
        if not location:
            return jsonify({"location": "Bucket location is required."})
        print(data)
        res = create_s3_bucket(bucket_name, location)
        print()
        print(res)
        return jsonify({"detail": str(res)})
    except Exception as e:
        return jsonify({"error": str(e)})

# @app.route('/<bucket_name>/<folder>')
# def get_bucket_files(bucket_name):
#     try:
#         folder = request.GET.get("folder")
#         print(folder)
#         objs = get_all_bucket_folder(bucket_name, folder)
#         print(objs)
#         # data = [{"key": obj['Prefix']} for i, obj in enumerate(objs['CommonPrefixes'])]
#         return jsonify({"data": str(objs)})
#     except Exception as e:
#         return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
