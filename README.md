# claude-workspace

니브라우의 Claude Code 작업 공간입니다.

---

## 폴더 구조

```
claude-workspace/
│
├── CLAUDE.md          # Claude Code 행동 지침 (핵심 규칙)
├── SECURITY.md        # 키 노출 비상 매뉴얼
├── .gitignore         # Git 제외 파일 목록
├── README.md          # 이 파일
│
├── docs/              # 작업 산출물
│   ├── portfolio.html     # 개인 포트폴리오 웹페이지
│   ├── weather_fetch.py   # 강남구 날씨·미세먼지 자동 수집 스크립트
│   └── run_weather.bat    # 날씨 스크립트 실행용 배치파일
│
└── tasks/             # 작업 기록
    ├── todo.md            # 오늘 할 일 체크리스트
    └── progress.md        # 완료 작업 누적 기록
```

> **업로드 제외 파일** (`.gitignore` 처리)
> `.env` · `*.key` · `*.pem` · `resume_sample.pdf` · `weather.txt`

---

## 파일별 용도

| 파일 | 용도 |
|------|------|
| `CLAUDE.md` | Claude Code가 자동으로 읽는 행동 규칙. 수정 시 직접 편집. |
| `SECURITY.md` | API 키 노출 의심 시 즉시 열기 |
| `docs/portfolio.html` | 브라우저에서 바로 열 수 있는 포트폴리오 페이지 |
| `docs/weather_fetch.py` | 매일 오전 9시 날씨·미세먼지를 `weather.txt`에 저장 |
| `tasks/todo.md` | 작업 시작 전 확인 |
| `tasks/progress.md` | 작업 완료 후 기록 |

---

## 날씨 자동 수집 설정

`docs/weather_fetch.py`는 **API 키 없이** 서울 강남구 날씨와 미세먼지를 가져옵니다.

- 데이터 출처: [Open-Meteo](https://open-meteo.com/) (무료)
- 자동 실행: 윈도우 작업 스케줄러 → 매일 오전 9시 → `run_weather.bat`
- 수동 실행: `run_weather.bat` 더블클릭

---

## 보안 규칙 요약

- `.env` 파일은 절대 Git에 올리지 않는다
- API 키는 코드에 직접 쓰지 않는다
- 키가 노출됐으면 `SECURITY.md` 순서대로 즉시 대응

---

*작업 환경 구축일: 2026-05-08*
