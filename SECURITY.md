# 🚨 보안 비상 매뉴얼

> **키 노출이 의심될 때 즉시 이 파일을 펼치세요.**
> 순서대로 따라가면 됩니다. 침착하게, 하나씩.

---

## STEP 1 — 무엇이 노출됐는지 확인

| 서비스 | 키 모양 예시 | 관리 콘솔 |
|--------|-------------|-----------|
| OpenRouter | `sk-or-v1-***` | https://openrouter.ai/keys |
| Oracle Cloud | API 서명 키 (PEM 파일) | https://cloud.oracle.com → Identity → API Keys |
| WordPress | Application Password / DB 비번 | 워드프레스 관리자 → 사용자 → 프로필 |
| GitHub | `ghp_***` / `github_pat_***` | https://github.com/settings/tokens |

노출된 키의 종류를 먼저 특정하세요.

---

## STEP 2 — 즉시 폐기 (Revoke)

### OpenRouter
1. https://openrouter.ai/keys 접속
2. 해당 키 옆 **Delete** 클릭
3. 새 키 발급 → `.env` 파일에 교체

### Oracle Cloud API Key
1. Oracle Console → 우상단 프로필 → **My Profile**
2. **API Keys** 탭 → 해당 키 **Delete**
3. 새 키 페어 생성 → `~/.ssh/oracle-server.key` 교체

### GitHub Personal Access Token
1. https://github.com/settings/tokens
2. 해당 토큰 **Delete**
3. 새 토큰 발급 → `.env` 파일에 교체

---

## STEP 3 — 환경변수 교체

```bash
# .env 파일 열기 (메모장 또는 에디터)
notepad C:\Users\User\OneDrive\바탕 화면\Claude_Study\claude_workspace\.env

# 교체 후 저장. 키는 절대 코드 파일에 붙여넣지 마세요.
```

`.env` 파일 형식 예시:
```
OPENROUTER_API_KEY=sk-or-v1-새로운키값
ORACLE_API_KEY=새로운값
```

---

## STEP 4 — 사용 이력 확인

노출된 키가 이미 악용됐을 수 있습니다.

| 서비스 | 확인 방법 |
|--------|-----------|
| OpenRouter | https://openrouter.ai/activity — 비정상 요청 확인 |
| Oracle | Console → Audit → **Audit Logs** — 낯선 IP/작업 확인 |
| GitHub | https://github.com/settings/security-log — 최근 활동 확인 |

**낯선 활동이 보이면:** 해당 서비스 고객센터 또는 보안팀에 즉시 신고하세요.

---

## STEP 5 — 재발 방지

- [ ] `.gitignore`에 `.env` 추가됐는지 확인
- [ ] 코드에 키가 하드코딩된 곳 없는지 검색 (`grep -r "sk-or" .`)
- [ ] 앞으로 키는 항상 `.env` 파일에만 저장
- [ ] Git 커밋 전 `git diff`로 키 포함 여부 확인

---

## 연락처 / 참고

- Claude Code에게 "키 노출 의심이야" 라고 말하면 이 매뉴얼 순서로 안내받을 수 있습니다.
- 작업 폴더: `C:\Users\User\OneDrive\바탕 화면\Claude_Study\claude_workspace`
- SSH 키 위치: `~/.ssh/oracle-server.key`

---

*마지막 업데이트: 2026-05-08*
