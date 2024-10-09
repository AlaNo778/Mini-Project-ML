ข้อแนะนำการใช้งาน
1.ควรใช้ python version 3.12.5
2.ตำแหน่งของ ไฟล์ best_medel_MLP.pkl ควรอยู่ตำแหน่งเดียวกันกับ ไฟล์์ App
3.ควรติดตั้ง library จากไฟล์ requirments.txt
	3.1 pip install scikit-learn
	3.2 pip install joblib
	3.3 pip install streamlit

วิธีการใช้งาน 
1.เปิด comma prompt
2.สร้าง venv โดยใช้ คำสั่ง python -m venv App_env
3.เข้าสู่ venv โดยใช้คำสั่ง App_env\Scripts\activate.bat
4.cd เข้าไปในตำแหน่งของ ไฟล์
5.ใช้คำสั่ง streamlit run app.py หรือ python -m streamlit run app.py
