import urllib.request
import json
from datetime import datetime
import os
import sys

# Windows 콘솔 UTF-8 출력 설정
if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# 서울 강남구 좌표
LAT = 37.5172
LON = 127.0473
TIMEZONE = "Asia/Seoul"

# weather.txt를 이 스크립트와 같은 폴더에 저장
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "weather.txt")

# Open-Meteo 날씨 코드 → 한국어 설명
WEATHER_CODES = {
    0: "맑음", 1: "대체로 맑음", 2: "부분 흐림", 3: "흐림",
    45: "안개", 48: "안개(서리)",
    51: "이슬비(약)", 53: "이슬비(보통)", 55: "이슬비(강)",
    61: "비(약)", 63: "비(보통)", 65: "비(강)",
    71: "눈(약)", 73: "눈(보통)", 75: "눈(강)",
    80: "소나기(약)", 81: "소나기(보통)", 82: "소나기(강)",
    95: "뇌우", 96: "뇌우+우박", 99: "뇌우+강한우박",
}

def aqi_grade(pm10, pm25):
    """미세먼지 농도 → 한국 기준 등급 변환"""
    pm10_grade  = "좋음" if pm10 < 30 else "보통" if pm10 < 80 else "나쁨" if pm10 < 150 else "매우나쁨"
    pm25_grade  = "좋음" if pm25 < 15 else "보통" if pm25 < 35 else "나쁨" if pm25 < 75 else "매우나쁨"
    return pm10_grade, pm25_grade

def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "WeatherBot/1.0"})
    with urllib.request.urlopen(req, timeout=15) as res:
        return json.loads(res.read().decode("utf-8"))

def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"[{now}] 날씨 정보 수집 시작")

    # ── 날씨 API (Open-Meteo, 무료·키 불필요) ──────────────────────
    weather_url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={LAT}&longitude={LON}"
        "&current=temperature_2m,apparent_temperature,"
        "relative_humidity_2m,precipitation,weathercode,"
        "windspeed_10m,winddirection_10m"
        f"&timezone={TIMEZONE}"
    )

    # ── 대기질 API (Open-Meteo Air Quality, 무료·키 불필요) ─────────
    aq_url = (
        "https://air-quality-api.open-meteo.com/v1/air-quality"
        f"?latitude={LAT}&longitude={LON}"
        "&current=pm10,pm2_5"
        f"&timezone={TIMEZONE}"
    )

    try:
        w  = fetch_json(weather_url)["current"]
        aq = fetch_json(aq_url)["current"]
    except Exception as e:
        error_msg = f"[{now}] ❌ 데이터 수집 실패: {e}\n"
        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(error_msg)
        print(error_msg)
        return

    # 날씨 파싱
    temp    = w["temperature_2m"]
    feels   = w["apparent_temperature"]
    humidity= w["relative_humidity_2m"]
    precip  = w["precipitation"]
    wind    = w["windspeed_10m"]
    sky     = WEATHER_CODES.get(w["weathercode"], "알 수 없음")

    # 미세먼지 파싱
    pm10    = round(aq["pm10"])
    pm25    = round(aq["pm2_5"])
    pm10_grade, pm25_grade = aqi_grade(pm10, pm25)

    # 출력 텍스트 구성
    lines = [
        "=" * 48,
        f"  [서울 강남구 날씨 정보]  {now}",
        "=" * 48,
        f"  날씨         : {sky}",
        f"  기온         : {temp}°C  (체감 {feels}°C)",
        f"  습도         : {humidity}%",
        f"  강수량       : {precip}mm",
        f"  풍속         : {wind}km/h",
        "-" * 48,
        f"  미세먼지(PM10)   : {pm10:>4}㎍/㎥  [{pm10_grade}]",
        f"  초미세먼지(PM2.5): {pm25:>4}㎍/㎥  [{pm25_grade}]",
        "=" * 48,
        "",
    ]

    output = "\n".join(lines)

    # weather.txt 에 날짜별로 누적 저장 (append)
    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        f.write(output + "\n")

    print(output)
    print(f"[완료] 저장 위치: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
