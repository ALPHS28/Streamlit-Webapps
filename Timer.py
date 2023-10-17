import streamlit as st
import time

def count_down(ts):
    with st.empty():
        while ts:
            min,sec =divmod(ts,60)
            st.header('{:02d}:{:02d}'.format(min,sec))
            time.sleep(1)
            ts=ts-1
        st.write("Time Up")
        



def main():
    st.header("Timer")
    time_min = st.number_input("Enter the Time in Minutes",min_value=1,value=25)
    time_sec=time_min*60
    if st.button("START"):
        count_down(time_sec)
if __name__=="__main__":
    main()
