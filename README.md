# Reverse Geocoder 
간단한의 geocoding 서버이다. 주소를 알고 싶은 좌표를 요청으로 보내면 해당 좌표가 속한 도시, 시군구, 읍면동을 반환한다.

간단하게 python 으로 개발 하였고 flask 를 사용하여 서버로 띄울 수 있게 구현하였다.

# 실행시키는 방법
도커 이미지를 pull 받아 바로 실행이 가능하다.
```
docker run -d -p 3030:3030 --name reverse qjvk2880/reverse_geocoder:1.0.0
```

# API 문서
이 API는 위도와 경도 좌표를 기반으로 해당 좌표가 속한 시군구 정보를 조회할 수 있는 기능을 제공합니다. GET 요청으로 좌표를 보내면 시군구 정보를 반환합니다.
### Base URL
`http://<서버-IP>:3030`

`<서버-IP>`를 실제 Flask 애플리케이션이 실행 중인 IP 주소 또는 도메인으로 대체하세요.

## 엔드포인트

### 1. 시군구 정보 조회

- **엔드포인트:** `/find_district`
- **메서드:** `GET`
- **설명:** 주어진 위도와 경도 좌표에 해당하는 시군구의 정보를 반환합니다.

#### 요청 파라미터

| 파라미터 | 타입   | 필수 여부 | 설명                                |
|----------|--------|-----------|-------------------------------------|
| `lon`    | float  | 필수      | 조회할 위치의 경도 (Longitude)      |
| `lat`    | float  | 필수      | 조회할 위치의 위도 (Latitude)       |

#### 성공 응답

```json
{
  "full_address": "충청남도 공주시 의당면",
   "area1": "충청남도",
   "area2": "공주시",
   "area3": "의당면"
}
```

- full_address: 주어진 좌표가 속하는 전체 주소 정보
- area1: 주어진 좌표가 속하는 도, 시 정보
- area2: 주어진 좌표가 속하는 시,군,구 정보
- area1: 주어진 좌표가 속하는 읍,면,동 정보
- 대한민국 시군구에 속하지 않는 좌표의 경우 모두 null 로 반환

  
#### 오류 응답
```json
{
  "error": "해당 좌표는 시군구에 속하지 않습니다."
}
```
- error: 좌표 형식이 올바르지 않거나 오류인 경우

#### 요청 예시
```bash
curl -X GET "http://<서버-IP>:3030/find_district?lon=126.9780&lat=37.5665"
```

# 주의점
- 도커 이미지 파일의 크기가 186 MB 이다.
