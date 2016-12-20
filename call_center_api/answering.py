# -*- coding: utf-8 -*-
import numpy as np
from machine_learning import Machine

class Answer(object):
    def __init__(self, trained):
        self.clf_8 = trained

    # 분류된 디렉토리에서 답변
    def answer_bot(self, keyword):
        clf_8 = self.clf_8
        question = []
        x = keyword
        question.append(x)
        y = np.array(question)

        result = clf_8.predict(y)

        # 가족관계 증명민원 답변
        if result == 0:
            data = []
            a = "질문 : " + keyword
            b = "디렉토리 : 가족관계 증명민원"
            c = "답변 : " + """안녕하세요. 서울생활 행복도우미 120다산콜센터 지식파트너입니다.

    ◈ 가족관계증명서 기재사항은 다음과 같습니다.

    ① 본인의 등록 기준지(본적)
       ※ 등록기준지 변동사항이 있는 경우 : 직전 등록기준지와 현재 등록기준지 표기
          단, 2008년 이전 등록기준지를 변경했다면 제적등본(호적등본)을 추가 확인 해야함
    ② 성명
    ③ 성별
    ④ 본
    ⑤ 출생년월일 및 주민등록번호
    ⑥ 부모, 배우자, 자녀의 인적사항 (기재범위는 3대에 한하며, 양자와 양부모도 포함)

       ※ 가족관계증명서상 이름옆에 한자로 표기됨 ( 본인외 기재범위 대상자는 모두 한자 확인가능)
       ※ 가족관계증명서상 국적 취득사실은 표기되지 않음 (기본증명서상에만 표기)
       ※ 가족관계증명서상  본인외의 배우자, 자녀, 부모의 등록기준지는 기재되어있지 않음

    ☞ 서울시 기준으로 안내되는 내용인 점 참고바랍니다.
    ☞ 해당 자료는 자료를 게시한 시점에서 유효함을 안내해드리며, 법령 개정 및 정책 변경에 따라 변경될
    수 있습니다.
    ☞ 더 궁금하신 사항은 다산콜센터 문자상담(☏02-120) 또는
    트위터상담(@120seoulcall)을 통해서도 안내  받으실 수 있습니다.
    드린 답변이 궁금증 해소에 도움이 되셨기를 바라며, 행복한 하루 보내시기 바랍니다! """

            data.append(a)
            data.append(b)
            data.append(c)
            return data

        # 교통민원 답변
        elif result == 1:
            data = []
            a = "질문 : " + keyword
            b = "디렉토리 : 교통민원"
            c = "답변 : " + """안녕하세요. 서울생활 행복도우미 120다산콜센터 지식파트너입니다.
            ◈  자동차 명의이전 시 처리비용 카드 결제 여부 입니다.

    ▶ 명의이전시 발생되는 비용
      ① 증지:1,000원, 인지:3000원 (현금 납부만 가능)
         ※ 양수인 주소지 서울시 아닌 타 지역인 경우 증지 : 1,500원

     ② 취득세(7%) : 등록세와 취득세가 합해져서 취득세로 변경됨
          매매금액과 시가표준액 중 높은 금액으로 산정 (높은 금액이 과세표준임)
           - 카드결제 가능함.
           - 취득세는 당일 납부해야 함.
           - 본인 요청시 금액 2회로 나누어 분할납부 가능함
           - 카드결제시 양수인명의 카드가 아닌 타인 것도 가능 합니다

     ③ 도시철도공채(채권) : 취득과표의 6% (영업용은 취득과표의 3%)
           ※ 현금 납부만 가능

    ※ 지역번호판에서 전국번호판으로 변경 시 추가비용 등록수수료 1,300원
    번호판대금7,600원(중/소형) 추가됨 (카드 결제 가능)


    ♣ 카드결제 가능한 사항은 취득세와 번호판 대금에 대해서 가능하니 방문 하여 확인 바랍니다.^^"""

            data.append(a)
            data.append(b)
            data.append(c)
            return data

        # 부동산, 건축민원 답변
        elif result == 2:
            data = []
            a = "질문 : " + keyword
            b = "디렉토리 : 부동산, 건축민원"
            c = "답변 : " + """안녕하세요. 서울생활 행복도우미 120다산콜센터 지식파트너입니다.
            안녕하세요. 서울생활 행복도우미 120다산콜센터 지식파트너입니다.



    ◈ 전입신고 방법
    - 신 거주지 동주민센터 방문
    - 인터넷 (민원24)
    - 모바일신고 (민원24 앱)

    ◈ 미성년자 다른 세대로 편입시 신전입지 세대주 방문할 경우 방문자 신분증, 본인도장 및 서명,
    이전 주소지 세대주 도장 지참하면 전입신고 가능합니다.

    ◈ 또한 미성년자 친권자 방문시 방문자 신분증, 세대주 신분증 및 도장, 이전 주소지 세대주의 도장 지참하면 됩니다.



    * 해당 자료는 자료를 게시한 시점에서 유효함 안내해드리며, 법령 개정 및 정책 변경에 따라 변경될 수 있습니다*"""

            data.append(a)
            data.append(b)
            data.append(c)
            return data

        # 서울특별시 답변
        elif result == 3:
            data = []
            a = "질문 : " + keyword
            b = "디렉토리 : 서울특별시"
            c = "답변 : " + """안녕하세요. 서울생활 행복도우미 120다산콜센터 지식파트너입니다.
            ◈ 서울시내 보건소 중 야간에 보건증 검사 가능한 곳은 없습니다.
    ▶ 강남보건소의 경우 유흥업소 종사자 보건증이 아닌 일반 보건증의 경우 점심시간(12시~1시)에
       검사 가능합니다.
    ▶ 마포보건소, 서대문보건소, 성동보건소, 양천보건소, 영등포보건소, 은평보건소, 종로보건소의
       경우 점심시간(12시~1시) 검사 가능합니다.


    ☞ 서울시 기준으로 안내되는 내용인 점 참고바랍니다.
    ☞ 해당 자료는 자료를 게시한 시점에서 유효함을 안내해드리며, 법령 개정 및 정책 변경에 따라 변경
    될 수 있습니다."""

            data.append(a)
            data.append(b)
            data.append(c)
            return data

        # 여권, 비자민원 답변
        elif result == 4:
            data = []
            a = "질문 : " + keyword
            b = "디렉토리 : 여권, 비자민원"
            c = "답변 : " + """안녕하세요. 서울생활 행복도우미 120다산콜센터 지식파트너입니다.
            ◈ 부모님께서 방문이 어렵다면 미성년자 본인이 아래 구비서류 지참하여 신청 가능합니다.

    ◈ 접수일 포함하여 신원조회상 이상이 없을 경우 주말, 공휴일 제외 업무일 기준 3~4 일째 발급됩니다.

    ◈ 미성년자는 2016년 기준 1998년생 생일 지나지 않은자 입니다.

    ◈ 미성년자 본인 방문 구비서류 입니다.
    ▶ 미성년자 신분증
    ▶ 최근 6개월이내 촬영한 미성년자 여권 전용사진 1매
    ▶ 연령에 따른 수수료
    ▶ 법정대리인의 인감 증명서 또는 본인서명사실확인서
    ▶ 법정대리인의 인감도장날인된 법정대리인동의서[별지 제1호의 2]
      → (본인서명사실확인서 지참 시 서명)
    ▶ 법정 대리인 신분증 원본
    ▶ 구 여권 (유효기간이 남은 경우)


    ◈ 신규 발급 수수료
    ▶ 만 8세 이상 (5년) : 45,000원
    ▶ 만 8세 이상 알뜰여권 (5년) : 42,000원
    ▶ 단수여권 (1년) : 20,000원

    ◈ 미성년자의 나이, 방문자 등 조건에 따라 구비서류 등은 달라질 수 있습니다.

    ◈ 여권 관련 양식은 외교부 여권안내 홈페이지 민원서식 양식 다운로드 가능 합니다."""

            data.append(a)
            data.append(b)
            data.append(c)
            return data

        # 의료보건제도 답변
        elif result == 5:
            data = []
            a = "질문 : " + keyword
            b = "디렉토리 : 의료보건제도"
            c = "답변 : " + """안녕하세요. 서울생활 행복도우미 120다산콜센터 지식파트너입니다.
            ◈ 보건증 재발급은 유효기간 1년 이내 검사받은 보건소에서 가능합니다.
    ▶ 단, 보건소마다 동주민센터 교부 가능여부가 상이하니 정확한 사항은 검사받은 보건증으로 문의
       주시거나 서울지역인 경우 서울시 120다산콜센터로 문의 부탁드립니다."""

            data.append(a)
            data.append(b)
            data.append(c)
            return data

        # 주민등록증 발급 답변
        else:
            data = []
            a = "질문 : " + keyword
            b = "디렉토리 : 주민등록증 발급"
            c = "답변 : " + """안녕하세요. 서울생활 행복도우미 120다산콜센터 지식파트너입니다.
            ◈ 주민등록증 신규 발급시 본인확인소명 자료는 학생증, 청소년증, 없으면 부모님 동반해야 합니다.

    ◈ 주민등록증 신규발급 안내
    ▶ 발급처 : 현 주민등록지 동주민센터
    ▶ 신고기한 : 만 17세가 되는 달의 다음달부터 1년 이내
    ▶ 구비서류
         - 주민등록 발급 신청서 (동주민센터에 비치)
         - 6개월 이내 촬영한  3cm*4cm 또는 3.5cm*4.5cm 귀와 눈썹이 보이는 탈모 상반신 사진
         - 본인 확인 소명 (학생증, 청소년증, 유효한 여권 없으면 부모님 동반)
            * 본인 소명자료가 없을경우
               → 주민등록지의 통장이 확인하거나 만 17세 이상의 동일 세대원, 배우자, 직계혈족 또
                   는 형제 자매가 신분증명서 지참하여 동행 바랍니다.
    ▶ 처리기간 : 신고인 신청일로부터 3주 정도 소요
    ▶ 수수료 : 없음 (단, 등기우편 수령 시 우편료 납부해야 함)"""

            data.append(a)
            data.append(b)
            data.append(c)
            return data