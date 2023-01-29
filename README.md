# SweaCrawling-TelegramBot
삼성 익스퍼트 아카데미 시험 일정 확인 크롤러

텔레그램 봇을 사용하여 삼성 익스퍼트 아카데미의 시험 일정을 확인하는 크롤러입니다.

원하는 유형의 시험 일자가 나타나면 텔레그램 봇이 메세지를 보냅니다.

업데이트 내역
    
    20190711
        과도한 서버 요청을 제거
            매일 11시59분과 6시에 시험 일자 체크하는 방식으로 변경.
            시험 자동 함수는 매 시간을 로컬 타임으로 체크하여 시험 등록 시간이 되면 자동 로그인 및 신청으로 변경.
        
    20190708
        봇 토큰, 계정 정보를 등록할 Crawling.json 파일 추가
        Crawling.json 파일에서 "BotToken": "", "UserId": "", "UserPw": ""에 데이터 필수로 추가해야 실행됩니다.
        
        소스코드 기능별 분할 2차 진행.
        
        자동 신청 기능 추가.
            시험 일자가 나타나면 자동 신청 명령어들이 나타납니다.
            자동 신청을 등록하면 시험 신청 일자때 자동으로 시험 신청합니다.
         
        명령어 추가
            /suwon, /seoul 지역 설정 명령어 추가
            /startauto 자동 신청 명령어 추가.
        
        
    20190614
        소스코드 기능별 분할 및 재정리 1차 진행
        
    20190612
        명령어 추가
        이제 원하는 시험 유형을 선택해서 확인할 수 있습니다.
        
        /setmodeA
        /setmodeB
        /setmodeC
    
    
    20190612
        텔레그램 봇을 사용하여 삼성 익스퍼트 아카데미의 시험 일정을 확인하는 크롤러입니다.
        현재는 시험 일자가 나타나면 바로 알림이 오는 시스템입니다.
        각 시험 유형별로 선택하여 일정을 확인하는 기능을 탑재할 예정입니다.
        
        제공하는 명령어
        
        /sweastart
        /sweastop
