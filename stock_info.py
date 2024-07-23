# 24.07.23 Streamlit 실습

import streamlit as st
import pandas as pd
import FinanceDataReader as fdr
import datetime
import matplotlib.pyplot as plt
import matplotlib 
from io import BytesIO
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px


today = datetime.datetime.now()
next_year = today.year + 1
jan_1 = datetime.date(next_year, 1, 1)
dec_31 = datetime.date(next_year, 12, 31)

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False


with st.sidebar:
    st.header('회사 이름과 기간을 입력하세요')
    txt_company = st.text_input(label='회사 이름')

    
   # st.caption('시작일 - 종료일')
    d = st.date_input(
       "시작일-종료일",
        (jan_1, datetime.date(next_year, 1, 7)),
        format="YYYY.MM.DD",
    )

    show_data = st.button('주가 데이터 확인')

st.title('무슨 주식을 사야 부자가 되려나...')

# caching
# 인자가 바뀌지 않는 함수 실행 결과를 저장 후 크롬의 임시 저장 폴더에 저장 후 재사용
if show_data:
    @st.cache_data
    def get_stock_info():
        base_url =  "http://kind.krx.co.kr/corpgeneral/corpList.do"    
        method = "download"
        url = "{0}?method={1}".format(base_url, method)   
        df = pd.read_html(url, header=0, encoding='cp949')[0]
        df['종목코드']= df['종목코드'].apply(lambda x: f"{x:06d}")     
        df = df[['회사명','종목코드']]
        return df

    def get_ticker_symbol(company_name):     
        df = get_stock_info()
        code = df[df['회사명']==company_name]['종목코드'].values    
        ticker_symbol = code[0]
        return ticker_symbol

    # 코드 조각 추가
    ticker_symbol = get_ticker_symbol(txt_company)     
    start_p = d[0]               
    end_p = d[1] + datetime.timedelta(days=1) 
    df = fdr.DataReader(f'KRX:{ticker_symbol}', start_p, end_p)
    df.index = df.index.date
    st.subheader(f"[{txt_company}] 주가 데이터")
    st.dataframe(df.tail(7))

    excel_data = BytesIO()      
    df.to_excel(excel_data)

    # 라인
   # df = px.data.iris()  # iris is a pandas DataFrame
    fig = px.line(df, x=df.index, y="Open").update_layout(xaxis_title='날짜', yaxis_title='시작')
    event = st.plotly_chart(fig)

    def convert_df(df):
     return df.to_csv(index=False).encode('utf-8')

    csv = convert_df(df)

    col1, col2 = st.columns(2)
    
    with col1:
        st.download_button(
        "csv 파일 다운로드",
        csv,
        "file.csv",
        "text/csv",
        key='download-csv'
    )
    with col2:
        st.download_button("엑셀 파일 다운로드", 
            excel_data, file_name='stock_data.xlsx')
