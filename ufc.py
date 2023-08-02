import pandas as pd
import requests
import streamlit as st
from io import BytesIO
from streamlit_lottie import st_lottie
import pickle
import numpy as np
import sklearn
from streamlit_option_menu import option_menu

selected_fighter_1 = 0
selected_fighter_2 = 0
   
fighter_data = pd.read_csv('raw_fighter_details.csv')
   
st.set_page_config(layout='wide')
   
selected = option_menu('Main Menu',['Home',"Prediction vs Result",'contact','More Projects'],icons=['house','gear','envelope','book'],orientation='horizontal')

df_blue = pd.read_csv('df_blue.csv')
df_blue = df_blue.drop("Unnamed: 0",axis=1)
df_red = pd.read_csv('df_red.csv')
df_red = df_red.drop("Unnamed: 0",axis=1)
   #fighter_df = pd.read_json('fighters.json',lines = True)[['name','wins','losses','draws']]
if selected=='Home':
   st.header('UFC fight Winner Prediction System')
   l,m,r = st.columns((2,1,2),gap='large')
   
   
   ##weight_class = st.selectbox('Select Weight class',fighter_data['Weight'])
   ##df_blue = df_blue[df_blue['Weight_Blue']==weight_class]
   ##df_red = df_red[df_red['Weight_Red']==weight_class]
      
   
   
   with l:
       selected_fighter_1 = str(st.selectbox('Select a Fighter for Red corner',list(set(df_red['fighter_name_Red'])),key='first',index=256))
       selected_fighter_1_ = selected_fighter_1.replace(' ','')
       st.write(list(set(df_red['fighter_name_Red'])).index(selected_fighter_1))
       if(selected_fighter_1 == 'Conor McGregor'):
           st.image('images-of-some-famous-fighters/conor.png',width=360)
       elif(selected_fighter_1 == 'Josh Emmett'):
           st.image('images-of-some-famous-fighters/joshemmet.png',width=360)
       elif(selected_fighter_1 == 'Georges St-Pierre'):
           st.image('images-of-some-famous-fighters/gsp.png',width=360)
       elif(selected_fighter_1 == 'Zabit Magomedsharipov'):
           st.image('images-of-some-famous-fighters/zbt.png',width=360)
   
       else:
           fighter1_url = f"https://fightingtomatoes.com/images/fighters/{selected_fighter_1_}.jpg"
           resp1 = requests.get(fighter1_url)
           resp_bytesIO_1 = BytesIO(resp1.content)
   
           if(resp1.status_code!=200):
              fighter1_url = "https://fightingtomatoes.com/images/fighters/blank-fighter-image.jpg"
              resp1 = requests.get(fighter1_url)
              resp_bytesIO_1 = BytesIO(resp1.content)
   
           
           #fighter1_data = fighter_data[fighter_data['fighter_name']==selected_fighter_1]
           
           st.image(resp_bytesIO_1,width=400)
       #st.dataframe(fighter_df[fighter_df['name']==selected_fighter_1])
       st.dataframe(df_red[df_red['fighter_name_Red']==selected_fighter_1].iloc[0],use_container_width=True)
       
       pred_features = df_red[df_red['fighter_name_Red']==selected_fighter_1].iloc[0]
       
       
       
   
   with m:
       st.write('###')
       st.write('###')
       st.write('###')
       st.write('###')
       st.write('###')
       l1,m1,r1 = st.columns(3)
       with m1:
           st.markdown('# V/s',unsafe_allow_html=True)
   
   # blue
   #434 - Masvidal
   #181 - Usman
   ##430 - Volk
   ##483 - gsp
   ##496 - gilbert burns
   ##511 - islam
   ##517 - stipe
   ##530 - tony
   ##540 - whittaker
   ##538 - ankalaev
   ##546 - costa
   ##577 - chandler
   ##950 - cyril gane
   ##992 - dustin
   ##1046 - conor
   ##1049 - strickland
       
   
   with r:
   
       selected_fighter_2 = str(st.selectbox('Select a Fighter for Blue corner',list(set(df_blue['fighter_name_Blue'])),key='second',index=136))
       selected_fighter_2_ = selected_fighter_2.replace(' ','')
       st.write(list(set(df_blue['fighter_name_Blue'])).index(selected_fighter_2))
   
       if(selected_fighter_2 == 'Conor McGregor'):
           st.image('images-of-some-famous-fighters/conor.png',width=360)
       elif(selected_fighter_2 == 'Josh Emmett'):
           st.image('images-of-some-famous-fighters/joshemmet.png',width=360)
       elif(selected_fighter_2 == 'Georges St-Pierre'):
           st.image('images-of-some-famous-fighters/gsp.png',width=360)
       elif(selected_fighter_2 == 'Zabit Magomedsharipov'):
           st.image('images-of-some-famous-fighters/zbt.png',width=360)
       else:    
           fighter2_url = f"https://fightingtomatoes.com/images/fighters/{selected_fighter_2_}.jpg"
           resp2 = requests.get(fighter2_url)
           resp_bytesIO_2 = BytesIO(resp2.content)
   
           if(resp2.status_code!=200):
              fighter2_url = f"https://fightingtomatoes.com/images/fighters/blank-fighter-image.jpg"
              resp2 = requests.get(fighter2_url)
              resp_bytesIO_2 = BytesIO(resp2.content)
           
           st.image(resp_bytesIO_2,width=400)
   
       #st.dataframe(fighter_df[fighter_df['name']==selected_fighter_2])
       st.dataframe(df_blue[df_blue['fighter_name_Blue']==selected_fighter_2].iloc[0],use_container_width=True)
   
       blue_fighter_data = df_blue[df_blue['fighter_name_Blue']==selected_fighter_2].iloc[0]
       pred_features = pd.concat([pred_features, blue_fighter_data],axis=1,ignore_index=True)
   
   log_reg = pickle.load(open('models/log_reg.pickle','rb'))
   
   array1 = np.array(pred_features.iloc[1:13,0])
   array2 = np.array(pred_features.iloc[14:26,1])
   
   arr = np.concatenate((array1, array2)).reshape(-1,1)
   arr = arr.reshape(1,24)
   
   
   X_test = pd.DataFrame(arr, columns=['Height_Red','Weight_Red','Reach_Red','Stance_Red',
                                       'SLpM_Red','Str_Acc_Red','SApM_Red','Str_Def_Red',
                                       'TD_Avg_Red','TD_Acc_Red','TD_Def_Red','Sub_Avg_Red',
                                       'Height_Blue','Weight_Blue','Reach_Blue','Stance_Blue',
                                       'SLpM_Blue','Str_Acc_Blue','SApM_Blue','Str_Def_Blue',
                                       'TD_Avg_Blue','TD_Acc_Blue','TD_Def_Blue','Sub_Avg_Blue'])
   
   #st.dataframe(X_test)
   left, mid, right = st.columns(3)
   with mid:
       if(selected_fighter_1 != selected_fighter_2):
           if(st.button('Predict',type='primary',use_container_width=True)):
               if(log_reg.predict(X_test)==1):
                   st.header(f'{selected_fighter_1} wins')
               else:
                   st.header(f'{selected_fighter_2} wins')
       else:
           st.header('Both Fighters cannot be same')
           st.button('Predict',type='primary',use_container_width=True,disabled=True)
   
   #st.dataframe(pred_features)


#st.dataframe(df_blue[df_blue['fighter_name_Blue']=='Khabib Nurmagomedov'])

# didnt find
elif selected=="Prediction vs Result":
   st.header("Let's See How accurate the Predictions were!")
   c1,c2 = st.columns(2, gap='large')
   with c1:
      st.image('UFC 291 Predictions and Results/Pred4.jpeg',width=300)
      st.image('UFC 291 Predictions and Results/Pred3.jpeg',width=300)
   with c2:
      st.image('UFC 291 Predictions and Results/Pred2.jpeg',width=300)
      st.image('UFC 291 Predictions and Results/Pred1.jpeg',width=300)
   st.image('UFC 291 Predictions and Results/Result.jpg')
   
   



if selected=='contact':
   st.header('Contact me with :')
   st.write('Check out my [Github Profile](https://github.com/heisenberg3376)')
   st.write('check out my [Kaggle Profile](https://www.kaggle.com/phanendrasairam)')
   st.write('Check out my [Linkedin Profile](https://www.linkedin.com/in/phanendra-sai-ram-505313226/)')


