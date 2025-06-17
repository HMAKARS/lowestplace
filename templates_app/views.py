from django.shortcuts import render

def home(request):
    """홈페이지 - 템플릿 선택 페이지"""
    context = {
        'title': '성당/교회 홈페이지 템플릿',
        'description': '전통적인 성당 스타일과 현대적인 교회 스타일 중 선택하세요.',
    }
    return render(request, 'templates_app/home.html', context)

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
