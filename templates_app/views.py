from django.shortcuts import render

def home(request):
    """홈페이지 - 모든 템플릿 카테고리 선택 페이지"""
    context = {
        'title': '프리미엄 랜딩페이지 템플릿 갤러리',
        'description': '스타트업, 상품소개, 음식점, 교회/성당까지 다양한 업종을 위한 전문 템플릿',
    }
    return render(request, 'templates_app/home.html', context)

def startup_landing(request):
    """스타트업 랜딩페이지"""
    context = {
        'company_name': 'TechStart Pro',
        'company_slogan': '혁신적인 기술로 미래를 만들어갑니다',
        'company_subtitle': '인공지능과 빅데이터로 새로운 가치를 창조하는 테크 스타트업',
        'phone': '02-1234-5678',
        'email': 'contact@techstart.kr',
        'address': '서울시 강남구 테헤란로 123, 스타트업 캠퍼스',
        'established': '2023년 설립',
        'funding': 'Pre-Series A',
        'team_size': '25명',
        'ceo_name': '김혁신 대표',
        'services': [
            {'name': 'AI 솔루션', 'description': '맞춤형 인공지능 솔루션 개발'},
            {'name': '데이터 분석', 'description': '빅데이터 기반 비즈니스 인사이트'},
            {'name': '컨설팅', 'description': '디지털 트랜스포메이션 컨설팅'}
        ],
        'achievements': [
            '2024 한국 스타트업 대상 수상',
            '누적 투자유치 50억원',
            '글로벌 기업 10+ 파트너십',
            '특허 출원 15건'
        ]
    }
    return render(request, 'templates_app/startup_landing.html', context)

def product_landing(request):
    """상품소개 랜딩페이지"""
    context = {
        'product_name': 'SmartWatch Pro',
        'product_slogan': '당신의 건강한 하루를 책임집니다',
        'product_subtitle': '최첨단 헬스케어 기술이 담긴 프리미엄 스마트워치',
        'price': '299,000원',
        'original_price': '399,000원',
        'discount': '25%',
        'company': 'HealthTech Co.',
        'phone': '1588-1234',
        'email': 'support@healthtech.kr',
        'features': [
            {
                'icon': '❤️',
                'title': '심박수 모니터링',
                'description': '24시간 실시간 심박수 측정 및 이상 감지'
            },
            {
                'icon': '💧',
                'title': '방수 기능',
                'description': 'IP68 등급 완전 방수로 수영도 가능'
            },
            {
                'icon': '🔋',
                'title': '7일 배터리',
                'description': '한 번 충전으로 최대 7일 사용 가능'
            },
            {
                'icon': '📱',
                'title': '스마트 연동',
                'description': '스마트폰과 완벽 연동으로 편리한 사용'
            }
        ],
        'reviews': [
            {'rating': 5, 'name': '김고객', 'comment': '정말 만족스러운 제품이에요!'},
            {'rating': 5, 'name': '이사용', 'comment': '배터리가 정말 오래가네요.'},
            {'rating': 4, 'name': '박구매', 'comment': '디자인이 세련되고 기능도 좋아요.'}
        ],
        'shipping': '무료배송',
        'warranty': '2년 품질보증'
    }
    return render(request, 'templates_app/product_landing.html', context)

def restaurant_landing(request):
    """음식점 랜딩페이지"""
    context = {
        'restaurant_name': 'Gourmet Place',
        'restaurant_slogan': '진정한 맛의 여행을 시작하세요',
        'restaurant_subtitle': '신선한 재료와 전통 요리법으로 만드는 프리미엄 다이닝 경험',
        'phone': '02-1588-1234',
        'email': 'info@gourmetplace.kr',
        'address': '서울시 강남구 가로수길 123',
        'chef_name': '김셰프',
        'established': '2018년 오픈',
        'awards': '미슐랭 가이드 선정 레스토랑',
        'specialties': [
            {
                'name': '시그니처 스테이크',
                'description': '최고급 한우를 숙성시켜 만든 시그니처 요리',
                'price': '85,000원',
                'image': '🥩'
            },
            {
                'name': '트러플 파스타',
                'description': '이탈리아산 트러플과 생파스타의 완벽한 조화',
                'price': '45,000원',
                'image': '🍝'
            },
            {
                'name': '랍스터 리조또',
                'description': '신선한 랍스터와 크리미한 리조또의 환상적 만남',
                'price': '65,000원',
                'image': '🦞'
            },
            {
                'name': '시즈널 디저트',
                'description': '계절마다 바뀌는 셰프 특선 디저트',
                'price': '18,000원',
                'image': '🍰'
            }
        ],
        'reviews': [
            {'rating': 5, 'name': '김미식가', 'comment': '정말 잊을 수 없는 맛이었어요!'},
            {'rating': 5, 'name': '박요리사', 'comment': '셰프의 정성이 느껴지는 요리였습니다.'},
            {'rating': 4, 'name': '이맛집', 'comment': '분위기도 좋고 서비스도 최고예요.'}
        ],
        'operating_hours': {
            'lunch': '11:30 - 15:00',
            'dinner': '17:30 - 22:00',
            'weekend': '11:30 - 22:00',
            'holiday': '월요일 휴무'
        }
    }
    return render(request, 'templates_app/restaurant_landing.html', context)

def traditional_template(request):
    """전통적인 성당 템플릿"""
    context = {
        'church_name': '성 마리아 성당',
        'church_subtitle': '하느님의 사랑이 머무는 곳',
        'phone': '02-1234-5678',
        'email': 'info@stmaria.or.kr',
        'address': '서울시 강남구 성당로 123',
        'mass_times': {
            'sunday': ['토요일 오후 7:00 (주일 미사)', '일요일 오전 7:00, 9:00, 11:00', '일요일 오후 6:00'],
            'weekday': ['월~금 오전 6:30, 오후 7:00', '토요일 오전 6:30'],
            'confession': ['매일 미사 30분 전', '토요일 오후 5:00~6:30'],
            'special': ['묵주기도: 매일 오후 6:30', '성체조배: 매월 첫 금요일']
        }
    }
    return render(request, 'templates_app/traditional.html', context)

def modern_template(request):
    """현대적인 교회 템플릿 - 성문교회 스타일"""
    context = {
        'church_name': '성문교회',
        'church_subtitle': '함께 걷는 믿음의 여정',
        'phone': '02-9876-5432',
        'email': 'hello@seongmoon.church',
        'address': '서울시 서초구 교회로 456',
        'website': 'www.seongmoon.church',
        'worship_times': {
            'sunday_main': '일요일 오전 11:00',
            'youth': '일요일 오후 2:00',
            'dawn': '매일 오전 5:30',
            'wednesday': '수요일 오후 7:30',
            'friday': '금요일 오후 11:00 (월 1회)',
            'online': '365일 24시간'
        },
        'stats': {
            'years': 30,
            'members': '1,200+',
            'groups': 45,
            'services': '200+'
        },
        'pastors': [
            {'title': '담임목사', 'name': '이영익 목사'},
            {'title': '부목사', 'name': '김은혜 목사'},
            {'title': '교육목사', 'name': '박성장 목사'},
            {'title': '전도사', 'name': '최사랑 전도사'}
        ]
    }
    return render(request, 'templates_app/modern.html', context)

def modern_landing(request):
    """현대적인 교회 랜딩페이지"""
    context = {
        'church_name': '새소망 교회',
        'church_slogan': '예수님과 함께하는 새로운 시작',
        'church_subtitle': '모든 세대가 함께 성장하는 따뜻한 공동체',
        'phone': '02-1234-5678',
        'email': 'welcome@newsohope.church',
        'address': '서울시 강남구 소망로 123',
        'sunday_service': '일요일 오전 11시',
        'online_service': '실시간 온라인 예배',
        'pastor_name': '김은혜 목사',
        'established': '1995년 설립',
        'members': '500여 성도'
    }
    return render(request, 'templates_app/modern_landing.html', context)

def traditional_landing(request):
    """전통적인 성당 랜딩페이지"""
    context = {
        'church_name': '성 요셉 성당',
        'church_slogan': '하느님의 평화가 머무는 거룩한 공간',
        'church_subtitle': '기도와 묵상, 나눔이 있는 신앙 공동체',
        'phone': '02-9876-5432',
        'email': 'parish@stjoseph.or.kr',
        'address': '서울시 서초구 성당로 456',
        'sunday_mass': '주일 오전 11시',
        'weekday_mass': '평일 오전 6시 30분',
        'pastor_name': '박평안 신부',
        'established': '1962년 설립',
        'tradition': '60년 전통'
    }
    return render(request, 'templates_app/traditional_landing.html', context)

def business_service_landing(request):
    """IT/통신 솔루션 기업 랜딩페이지 - 다보링크 스타일"""
    context = {
        'company_name': 'TechLink Solutions',
        'company_slogan': '차세대 무선 통신 기술의 리더',
        'company_subtitle': '무선 LAN · IoT · 네트워크 보안 전문 기업',
        'phone': '031-123-4567',
        'email': 'info@techlink.co.kr',
        'address': '경기도 성남시 분당구 테크노파크 123',
        'website': 'www.techlink.co.kr',
        'established': '2000년',
        'team_size': '50여 명',
        'projects': '500여 건',
        'services': [
            {
                'title': '무선 LAN 솔루션',
                'description': 'Wi-Fi 6/6E 기반 기업용 무선 네트워크 구축 및 관리',
                'icon': '📡',
                'features': ['Wi-Fi 6/6E 지원', '클라우드 관리', '실시간 모니터링', '자동 최적화']
            },
            {
                'title': 'IoT 플랫폼',
                'description': 'IoT 디바이스 통합 관리 및 데이터 분석 플랫폼',
                'icon': '🌐',
                'features': ['디바이스 관리', '데이터 수집', '실시간 분석', 'API 연동']
            },
            {
                'title': '네트워크 보안',
                'description': '차세대 보안 솔루션으로 안전한 네트워크 환경 구축',
                'icon': '🔒',
                'features': ['침입 탐지', '트래픽 분석', '보안 정책', '실시간 대응']
            },
            {
                'title': '통합 관제',
                'description': 'AI 기반 지능형 네트워크 관제 및 운영 자동화',
                'icon': '🤖',
                'features': ['AI 분석', '자동 대응', '성능 최적화', '장애 예측']
            }
        ],
        'achievements': [
            {
                'title': '대기업 고객사',
                'count': '100+',
                'description': '삼성, LG, SK 등 대기업 파트너십'
            },
            {
                'title': '프로젝트 성공률',
                'count': '99%',
                'description': '높은 프로젝트 성공률과 고객 만족도'
            },
            {
                'title': '기술 특허',
                'count': '25건',
                'description': '핵심 무선 통신 기술 특허 보유'
            },
            {
                'title': '해외 진출',
                'count': '15개국',
                'description': '글로벌 시장 진출 및 현지화'
            }
        ],
        'testimonials': [
            {
                'company': 'S전자',
                'position': 'IT팀장',
                'name': '김**',
                'comment': '안정적인 무선 네트워크 구축으로 업무 효율성이 크게 향상되었습니다. 기술력과 지원 서비스 모두 만족스럽습니다.'
            },
            {
                'company': 'L화학',
                'position': '인프라 담당자',
                'name': '박**',
                'comment': 'IoT 플랫폼 도입 후 생산성이 30% 향상되었습니다. 실시간 모니터링 기능이 특히 유용합니다.'
            },
            {
                'company': 'K대학교',
                'position': '전산팀장',
                'name': '이**',
                'comment': '캠퍼스 전체 무선 네트워크를 안정적으로 운영할 수 있게 되었습니다. 학생들의 만족도도 높아졌습니다.'
            }
        ]
    }
    return render(request, 'templates_app/business_service_landing.html', context)

def temple_landing(request):
    """사찰 랜딩페이지 - 전통 불교 사찰 스타일"""
    context = {
        'temple_name': '금강사',
        'temple_slogan': '마음의 평화와 깨달음의 길',
        'temple_subtitle': '천년의 역사와 전통을 간직한 수행도량',
        'phone': '033-123-4567',
        'email': 'info@keumgang.or.kr',
        'address': '강원도 평창군 대관령면 금강길 108',
        'sunday_prayer': '일요일 오전 10시',
        'weekday_prayer': '매일 새벽 4시 30분',
        'abbot_name': '혜안 스님',
        'established': '신라 문무왕 7년 (서기 667년)',
        'tradition': '1350년 전통'
    }
    return render(request, 'templates_app/temple_landing.html', context)
