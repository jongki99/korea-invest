#kis_domstk module 을 찾을 수 없다는 에러가 나는 경우 sys.path에 kis_domstk.py 가 있는 폴더를 추가해준다.
import kis_auth as ka
import kis_domstk as kb

import pandas as pd

import sys

# 토큰 발급
# ka.auth('vps', ) # 이건 모의투자.
ka.auth('prod', ) # 이건 실전투자.



#rt_data = kb.get_inquire_price(itm_no="071050")
itm_no = "005930"


# [국내주식] 기본시세 > 주식현재가 시세 (종목번호 6자리)
rt_data = kb.get_inquire_price(itm_no=itm_no)
#005930
print()

print(rt_data)
print(rt_data.stck_prpr+ " " + rt_data.prdy_vrss)    # 현재가, 전일대비


# # [국내주식] 기본시세 > 주식현재가 체결 (종목번호 6자리)
# rt_data = kb.get_inquire_ccnl(itm_no=itm_no)
# print(rt_data)


# # [국내주식] 기본시세 > 주식현재가 일자별 (종목번호 6자리 + 기간분류코드)
# # 기간분류코드    D : (일)최근 30거래일  W : (주)최근 30주   M : (월)최근 30개월
# # 수정주가기준이며 수정주가미반영 기준을 원하시면 인자값 adj_prc_code="2" 추가
# rt_data = kb.get_inquire_daily_price(itm_no=itm_no, period_code="D")
# print(rt_data)



# # [국내주식] 기본시세 > 주식현재가 호가 (종목번호 6자리)
# # 잔량 정보: 
# rt_data = kb.get_inquire_asking_price_exp_ccn(itm_no=itm_no)
# print(rt_data)

# # [국내주식] 기본시세 > 주식현재가 예상체결 (출력구분="2" + 종목번호 6자리)
# rt_data = kb.get_inquire_asking_price_exp_ccn(output_dv="2", itm_no=itm_no)
# print(rt_data)


# # [국내주식] 기본시세 > 국내주식기간별시세(일/주/월/년) (종목번호 6자리)
# rt_data = kb.get_inquire_asking_price_exp_ccn(itm_no=itm_no)
# print("[국내주식] 기본시세 > 국내주식기간별시세(일/주/월/년)", rt_data)


# # [국내주식] 기본시세 > 국내주식기간별시세(일/주/월/년) (기간별 데이터 Default는 일별이며 조회기간은 100일전(영업일수 아님)부터 금일까지)
# # output_dv=1 과 2 가 있는데... 값이 영 다르다... -_-;
# rt_data_obj = kb.get_inquire_daily_itemchartprice(output_dv="1", itm_no=itm_no)
# print("[국내주식] 기본시세 > 국내주식기간별시세(일/주/월/년) output_dv=1", rt_data_obj)
# rt_data_obj = kb.get_inquire_daily_itemchartprice(output_dv="2", itm_no=itm_no)
# print("[국내주식] 기본시세 > 국내주식기간별시세(일/주/월/년) output_dv=2", rt_data_obj)



# # [국내주식] 기본시세 > 주식현재가 당일시간대별체결 (현재가 : 주식현재가, 전일대비, 전일대비율, 누적거래량,전일거래량, 대표시장한글명))
# rt_data = kb.get_inquire_time_itemconclusion(itm_no=itm_no)
# print("[국내주식] 기본시세 > 주식현재가 당일시간대별체결", rt_data)


# # [국내주식] 기본시세 > 주식현재가 당일시간대별체결 (시간대별체결내역)
# rt_data = kb.get_inquire_time_itemconclusion(output_dv='1', itm_no=itm_no)  # 기준시각 미지정시 현재시각 이전 체결 내역이 30건 조회됨
# print("[국내주식] 기본시세 > 주식현재가 당일시간대별체결 (시간대별체결내역) output_dv=1", rt_data)
# rt_data = kb.get_inquire_time_itemconclusion(output_dv='2', itm_no=itm_no, inqr_hour='100000') # 지정 기준시각 이전 체결 내역이 30건 조회됨
# print("[국내주식] 기본시세 > 주식현재가 당일시간대별체결 (시간대별체결내역) output_dv=2", rt_data)




# # [국내주식] 주문/계좌 > 주식현금주문 (매수매도구분 buy,sell + 종목번호 6자리 + 주문수량 + 주문단가)
# # 지정가 기준이며 시장가 옵션(주문구분코드)을 사용하는 경우 kis_domstk.py get_order_cash 수정요망!
# rt_data = kb.get_order_cash(ord_dv="buy",itm_no="071050", qty=10, unpr=65000)
# print(rt_data.KRX_FWDG_ORD_ORGNO + "+" + rt_data.ODNO + "+" + rt_data.ORD_TMD) # 주문접수조직번호+주문접수번호+주문시각



# # [국내주식] 주문/계좌 > 주식주문(정정취소) (한국거래소전송주문조직번호 5자리+원주문번호 10자리('0'을 채우지 않아도됨)+정정취소구분코드+정정및취소주문수량+잔량전부주문여부)
# # 지정가 기준이며 시장가 옵션(주문구분코드)을 사용하는 경우 kis_domstk.py get_order_rvsecncl 수정요망!
# rt_data = kb.get_order_rvsecncl(ord_orgno="06010", orgn_odno="0000224003", ord_dvsn="00", rvse_cncl_dvsn_cd="01", ord_qty=0, ord_unpr=64900, qty_all_ord_yn="Y")
# print(rt_data.KRX_FWDG_ORD_ORGNO + "+" + rt_data.ODNO + "+" + rt_data.ORD_TMD) # 주문접수조직번호+주문접수번호+주문시각




# # [국내주식] 주문/계좌 > 주식정정취소가능주문내역조회
# rt_data = kb.get_inquire_psbl_rvsecncl_lst()
# print(rt_data)




# # [국내주식] 주문/계좌 > 주식일별주문체결(현황)조회
# # dv="01"   01:3개월 이내 국내주식체결내역 (월단위 ex: 2024.04.25 이면 2024.01월~04월조회)
# # dv="02"   02:3개월 이전 국내주식체결내역 (월단위 ex: 2024.04.25 이면 2024.01월이전)
# rt_data = kb.get_inquire_daily_ccld_obj(dv="01")
# print(rt_data)

# # [국내주식] 주문/계좌 > 주식일별주문체결(내역)조회
# # dv="01"   01:3개월 이내 국내주식체결내역 (월단위 ex: 2024.04.25 이면 2024.01월~04월조회)
# # dv="02"   02:3개월 이전 국내주식체결내역 (월단위 ex: 2024.04.25 이면 2024.01월이전)
# rt_data = kb.get_inquire_daily_ccld_lst(dv="01")
# print(rt_data)


