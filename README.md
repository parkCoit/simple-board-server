### **Simple Board Web Application (Backend)**

# Simple Board Web Application (Backend)

## 프로젝트 개요

이 프로젝트는 Django와 Django REST Framework를 사용하여 개발된 백엔드 서버입니다. RESTful API를 통해 클라이언트와 통신하며, MySQL을 데이터베이스로 사용하고 있습니다.

## 기술 스택

- **Django**: 웹 프레임워크
- **Django REST Framework**: API 설계 및 구현
- **MySQL**: 데이터베이스
- **JWT**: 사용자 인증
- **Google Cloud Platform**: 배포 플랫폼

## 주요 기능

- **게시물 관리**: CRUD 기능 제공
- **사용자 인증**: JWT 기반의 사용자 인증 시스템
- **데이터베이스 관리**: MySQL을 통해 데이터 저장 및 관리

## 배포

Google Cloud Platform의 Compute Engine을 사용하여 서버를 배포하였습니다.

## 실행 방법

1. 저장소를 클론합니다:
   ```bash
   git clone https://github.com/yourusername/simple-board-server.git
2. 프로젝트 디렉토리로 이동합니다:
   ```bash
   cd simple-board-server
3. 가상 환경을 설정하고 활성화합니다:
    ```bash
   python3 -m venv venv
   source venv/bin/activate
4. 필요한 패키지를 설치합니다:
    ```bash
   pip install -r requirements.txt
5. 데이터베이스 마이그레이션을 실행합니다:
    ```bash
   python manage.py migrate
6. 서버를 시작합니다:
    ```bash
   python manage.py runserver
