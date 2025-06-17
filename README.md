# 🏛️ 교회/성당 랜딩페이지 템플릿 컬렉션

다양한 스타일의 전문적인 교회/성당 랜딩페이지 템플릿을 제공하는 Django 프로젝트입니다.

## ✨ 주요 특징

- **5가지 다른 디자인 스타일**의 랜딩페이지
- **반응형 디자인** - 모바일, 태블릿, 데스크톱 완벽 지원
- **최신 웹 기술** - HTML5, CSS3, JavaScript ES6+
- **보안 강화** - CSRF 보호, XSS 방지, HTTPS 지원
- **성능 최적화** - 캐싱, 압축, 최적화된 이미지
- **SEO 친화적** - 검색엔진 최적화
- **환경변수 관리** - 보안 정보 안전 관리

## 🎨 랜딩페이지 스타일

1. **Modern** (`/modern/`) - Glassmorphism & 3D 모던 디자인
2. **Traditional** (`/traditional/`) - 클래식 & 전통적인 스타일
3. **Product** (`/product/`) - E-commerce 제품 소개 스타일
4. **Restaurant** (`/restaurant/`) - 프리미엄 레스토랑 스타일
5. **Startup** (`/startup/`) - 스타트업 비즈니스 스타일

## 🚀 빠른 시작

### 1. 프로젝트 클론
```bash
git clone <repository-url>
cd church_builder
```

### 2. 가상환경 설정
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 3. 패키지 설치
```bash
pip install -r requirements.txt
```

### 4. 환경변수 설정
```bash
# .env.example을 복사해서 .env 파일 생성
cp .env.example .env

# .env 파일 편집하여 실제 값 입력
# 특히 SECRET_KEY는 반드시 변경하세요!
```

### 5. 데이터베이스 마이그레이션
```bash
python manage.py migrate
```

### 6. 서버 실행
```bash
python manage.py runserver
```

### 7. 브라우저에서 확인
- 메인 페이지: http://localhost:8000/
- 각종 랜딩페이지: http://localhost:8000/modern/, /traditional/, /product/, /restaurant/, /startup/

## ⚙️ 환경변수 설정

`.env` 파일에서 다음 설정들을 관리할 수 있습니다:

### 필수 설정
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 데이터베이스 설정
```env
# SQLite (기본값)
DATABASE_NAME=db.sqlite3

# PostgreSQL (운영 환경 권장)
DB_ENGINE=django.db.backends.postgresql
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

### 보안 설정
```env
CSRF_COOKIE_SECURE=False  # HTTPS 사용시 True
SESSION_COOKIE_SECURE=False  # HTTPS 사용시 True
USE_HTTPS=False  # HTTPS 사용시 True
```

### 기타 설정
```env
TIME_ZONE=Asia/Seoul
LANGUAGE_CODE=ko-kr
CACHE_TIMEOUT=300
LOG_LEVEL=INFO
```

## 🔧 운영 환경 배포

### 1. 환경변수 설정
```env
DEBUG=False
SECRET_KEY=production-secret-key-very-long-and-random
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
USE_HTTPS=True
CSRF_COOKIE_SECURE=True
SESSION_COOKIE_SECURE=True
```

### 2. PostgreSQL 데이터베이스
```env
DB_ENGINE=django.db.backends.postgresql
DB_NAME=your_production_db
DB_USER=your_db_user
DB_PASSWORD=secure_db_password
DB_HOST=your_db_host
```

### 3. 정적 파일 수집
```bash
python manage.py collectstatic
```

## 📁 프로젝트 구조

```
church_builder/
├── .env                    # 환경변수 파일 (Git에 포함 안됨)
├── .env.example           # 환경변수 템플릿
├── manage.py
├── requirements.txt
├── church_builder/        # Django 설정
│   ├── settings.py        # 환경변수 기반 설정
│   ├── urls.py
│   └── ...
├── templates_app/         # 메인 앱
│   ├── views.py
│   ├── urls.py
│   └── ...
├── templates/            # 템플릿 파일들
│   ├── base.html
│   └── templates_app/
│       ├── home.html
│       ├── modern_landing.html
│       ├── traditional_landing.html
│       ├── product_landing.html
│       ├── restaurant_landing.html
│       └── startup_landing.html
├── static/              # 정적 파일
└── logs/               # 로그 파일
```

## 🛠️ 개발 도구

- **Django 5.2.3** - 웹 프레임워크
- **python-decouple** - 환경변수 관리
- **Pillow** - 이미지 처리
- **HTML5/CSS3** - 마크업 및 스타일링
- **JavaScript ES6+** - 인터랙션

## 🔒 보안 기능

- CSRF 보호
- XSS 방지
- SQL 인젝션 방지
- 보안 헤더 설정
- HTTPS 지원
- 환경변수 기반 설정
- 로깅 및 모니터링

## 📝 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다.

## 🤝 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 지원

문의사항이나 버그 리포트는 Issues 탭을 이용해 주세요.

---

⭐ 이 프로젝트가 도움이 되었다면 별표를 눌러주세요!
