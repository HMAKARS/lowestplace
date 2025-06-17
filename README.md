# 🏛️ Church Builder - 성당/교회 홈페이지 제작 솔루션

성당 및 교회를 위한 전문적인 홈페이지 템플릿을 제공하는 Django 기반 웹 애플리케이션입니다.

## ✨ 주요 기능

- **2가지 스타일 템플릿 제공**
  - 🏰 **전통 성당 스타일**: 가톨릭 성당을 위한 경건하고 고급스러운 디자인
  - 🏠 **현대 교회 스타일**: 프로테스탄트 교회를 위한 밝고 현대적인 디자인

- **반응형 웹 디자인**: 모바일, 태블릿, 데스크톱 모든 기기에서 최적화
- **Django 템플릿 시스템**: 재사용 가능하고 커스터마이징 가능한 구조
- **동적 콘텐츠 관리**: 교회/성당 정보를 쉽게 수정 가능

## 🛠️ 기술 스택

- **Backend**: Django 5.2.3
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (개발용)
- **Python**: 3.13+

## 📁 프로젝트 구조

```
from_the_lowest_place/
├── church_builder/          # Django 프로젝트 설정
│   ├── settings.py         # 프로젝트 설정
│   ├── urls.py            # 메인 URL 설정
│   └── ...
├── templates_app/          # 템플릿 앱
│   ├── views.py           # 뷰 로직
│   ├── urls.py            # 앱 URL 설정
│   └── ...
├── templates/              # Django 템플릿
│   ├── base.html          # 베이스 템플릿
│   └── templates_app/     # 앱별 템플릿
│       ├── home.html      # 홈페이지
│       ├── traditional.html # 전통 성당 템플릿
│       └── modern.html    # 현대 교회 템플릿
├── static/                 # 정적 파일
│   ├── css/
│   ├── js/
│   └── images/
├── requirements.txt        # Python 패키지 목록
└── manage.py              # Django 관리 스크립트
```

## 🚀 설치 및 실행

### 1. 가상환경 활성화
```bash
source .venv/bin/activate  # macOS/Linux
# 또는
.venv\\Scripts\\activate   # Windows
```

### 2. 패키지 설치
```bash
pip install -r requirements.txt
```

### 3. 데이터베이스 마이그레이션
```bash
python manage.py migrate
```

### 4. 개발 서버 실행
```bash
python manage.py runserver
```

### 5. 브라우저에서 확인
```
http://127.0.0.1:8000/
```

## 📖 사용법

### 홈페이지
- `http://127.0.0.1:8000/` - 메인 페이지에서 두 템플릿을 선택할 수 있습니다.

### 템플릿 미리보기
- `http://127.0.0.1:8000/traditional/` - 전통 성당 스타일 템플릿
- `http://127.0.0.1:8000/modern/` - 현대 교회 스타일 템플릿

### 템플릿 커스터마이징

#### 1. 기본 정보 수정
`templates_app/views.py` 파일에서 교회/성당 정보를 수정할 수 있습니다:

```python
# 현대 교회 템플릿 정보 수정 (성문교회 스타일)
def modern_template(request):
    context = {
        'church_name': '성문교회',               # 교회명 변경
        'church_subtitle': '함께 걷는 믿음의 여정',  # 부제목 변경
        'phone': '02-9876-5432',              # 전화번호 변경
        'email': 'hello@seongmoon.church',    # 이메일 변경
        'address': '서울시 서초구 교회로 456',     # 주소 변경
        # 5가지 교회 비전은 템플릿에 하드코딩되어 있음
        # ...
    }
```

#### 2. 디자인 수정
- CSS 스타일은 각 템플릿 파일 내의 `<style>` 태그에서 수정
- 색상, 폰트, 레이아웃 등을 자유롭게 커스터마이징 가능

#### 3. 새로운 페이지 추가
1. `templates_app/views.py`에 새 뷰 함수 추가
2. `templates_app/urls.py`에 URL 패턴 추가
3. `templates/templates_app/`에 새 템플릿 파일 생성

## 🎨 템플릿 특징

### 🏰 전통 성당 스타일
- **색상**: 브라운, 골드 계열의 고급스러운 색상
- **대상**: 가톨릭 성당, 전통적인 종교 공동체
- **특징**: 
  - 경건하고 고급스러운 분위기
  - 십자가 아이콘과 성경 구절 강조
  - 미사 시간, 고해성사 등 가톨릭 특화 정보
  - 클래식한 서체와 레이아웃

### 🏠 현대 교회 스타일  
- **색상**: 블루, 오렌지 계열의 현대적이고 역동적인 색상
- **모델**: 성문교회를 참고한 전문적인 교회 디자인
- **특징**:
  - 5가지 교회 비전 체계 (Healing Family, Glorifying God, Great Commission, Training Disciples, Next Generation)
  - 현대적이고 역동적인 분위기
  - 애니메이션과 그라데이션 효과
  - 체계적인 사역 구조와 훈련 시스템 강조
  - 선교와 가정 사역에 특화된 콘텐츠

## 📱 반응형 디자인

- **모바일 퍼스트**: 모바일 환경을 우선으로 설계
- **브레이크포인트**: 768px 기준으로 모바일/데스크톱 최적화
- **터치 친화적**: 모바일에서 사용하기 쉬운 인터페이스
- **빠른 로딩**: 최적화된 CSS와 이미지

## 🔧 개발 환경 설정

### Django 설정 파일 주요 항목
```python
# church_builder/settings.py

# 언어 및 시간대
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'

# 정적 파일 설정
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# 미디어 파일 설정
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

## 🚀 배포 가이드

### 1. 프로덕션 설정
- `DEBUG = False`로 변경
- `ALLOWED_HOSTS` 설정
- 시크릿 키 환경변수 분리
- PostgreSQL 또는 MySQL 데이터베이스 연결

### 2. 정적 파일 수집
```bash
python manage.py collectstatic
```

### 3. 웹서버 설정
- Nginx + Gunicorn 조합 권장
- HTTPS 인증서 설정
- CDN 연동 (선택사항)

## 🤝 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.

## 📞 문의사항

프로젝트에 대한 문의사항이나 개선 제안이 있으시면 Issues를 통해 연락주세요.

---

> **개발 목적**: 성당 및 교회 타겟팅 홈페이지 제작 솔루션 개발  
> **개발 환경**: Django Framework, Python 3.13+  
> **개발 상태**: 베타 버전 (개발 진행 중)

