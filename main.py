from flask import Flask, request, jsonify, Response
import os
import json
from geopy.geocoders import Nominatim

# Nominatim 객체 생성
geo_local = Nominatim(user_agent='South Korea', timeout=None)


def get_address_from_coordinate(lat, lng):
    try:
        address = geo_local.reverse([lat, lng], exactly_one=True, language='ko')
        detail_address = address.address  # 상세주소
        address_parts = detail_address.split(',')

        area1 = address_parts[-3].strip()  # 서울
        area2 = address_parts[-4].strip()  # 은평구
        area3 = address_parts[-5].strip()  # 대조동
        full_address = f"{area1} {area2} {area3}"  # 서울 은평구 대조동

        return {
            "full_address": full_address,
            "area1": area1,
            "area2": area2,
            "area3": area3
        }

    except:
        return [0, 0]


app = Flask(__name__)


@app.route('/find_district', methods=['GET'])
def find_district_api():
    lon = float(request.args.get('lon'))
    lat = float(request.args.get('lat'))

    address = get_address_from_coordinate(lat, lon)

    response_json = json.dumps(address, ensure_ascii=False)
    return Response(response=response_json, status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3030)
