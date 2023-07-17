#further inputs to implement:
##test_range
#add info buttons



import streamlit as st
from pwfunctions import find_consecutive_chars
from pwfunctions import random_pw
from pwfunctions import closest_distance

import time
import pandas as pd
import random

# ----- Start with app here -----#
if __name__ == "__main__":
    tab1, tab2 = st.tabs(["Main", "About"])

    with tab1:

        # Create a sidebar with three four inputs
        
        st.write("_Set a seed_")
        input_seed = st.number_input(label = "seed", min_value=0, max_value=10000000000, value=32575663, step=1, label_visibility = "collapsed")
        
        st.write(" ")
        st.write("_Number of passwords to generate_")
        input_num_pw = st.number_input(label = "num passwords", value=100, step=100, label_visibility = "collapsed")
        #st.write('The current number is ', input_num_pw)
        
        st.write(" ")
        st.write("_Password length_")
        c1, c2= st.columns(2)
        
        with c1:
            input_len_min = st.number_input("Min", min_value=4, max_value=15, value=7, step=1)
        with c2:
            input_len_max = st.number_input("Max", min_value=4, max_value=15, value=8, step=1)
        
        st.write(" ")
        st.write("_Password complexity_")
        
        c1, c2= st.columns(2)
        with c1:
            input_uppercase = st.checkbox("Include uppercase letters", value = True)
            input_lowercase = st.checkbox("Include lowercase letters")
        with c2:
            input_numbers = st.checkbox("Include numbers")
            input_special = st.checkbox("Include special characters")
        
        st.write(" ")
        st.write("_Advanced options_")
            
        input_IL = st.checkbox("Exclude I/l/1", value = True)
        input_O0 = st.checkbox("Exclude O/0", value = True)
        #input_lev = st.checkbox("Check for Levenshtein distance", value = True)
        input_editdis = st.number_input(label = "Edit distance/Levenshtein distance", value=1)

        ## I need a session so that download buttons do not reset themselves
        # Check if the 'show_buttons' key exists in session_state
        if 'show_buttons' not in st.session_state:
            st.session_state.show_buttons = False

        # Button to show or hide the download buttons
        if st.sidebar.button("create passwords"):
            st.session_state.show_buttons = True

        if st.session_state.show_buttons:
            start = time.time()

            random.seed(input_seed)
            
            ls = []
            i = 0
         
            while i < input_num_pw:
                pw = random_pw(len_min = input_len_min, 
                            len_max = input_len_max, 
                                uppercase = input_uppercase,
                                lowercase = input_lowercase,
                                numbers = input_numbers,
                                special = input_special,
                                cut_I_and_l = input_IL,
                                cut_O_and_0 = input_O0)
                
                if find_consecutive_chars(pw) < 0.5:
                    try:
                        ls.index(pw)
                    except ValueError:
                        
                        if len(ls) > 1:
                            # Get the closest match
                            
                            # to reduce the number of similarity comparisons, you can set a test range. The benefit is that a newly created password does not have to be checked against all other passwords in the list but only for the passwords within the test range
                            # test_range default is 1000, i.e., if available, 1000 passwords before and 1000 passwords after the newly created password will be tested on similarity. 
                            # the test range becomes important when optimizing very large samples of passwords, e.g., 100,000 
                            test_range = 10000 
                            
                            #this chunck sets the thresholds/indexes for the testing range   
                            ls.append(pw)
                            ls = sorted(ls)
                            pos_pw = ls.index(pw)
                            del ls[pos_pw]
                            test_from = pos_pw-test_range if pos_pw-test_range > 0 else 0  
                            test_to = pos_pw+test_range if pos_pw+test_range < len(ls) else len(ls)-1 
                                
                            #find the the password in the list with a minimum distance. 
                            #The distance can be use to test is against a similarity threshold, e.g., 1     
                            ls_dist = closest_distance(pw, ls[test_from:test_to])
                            min_dis = min(ls_dist)    
                            closest_match = ls[ls_dist.index(min_dis)]
                            
                            #only append list if similarity score is greater 1, that is, at least two change to the password must be made 
                            edistance = input_editdis
                            if min_dis > edistance:   
                                ls.append(pw)
                                i +=1      
                            else:
                                #this part is for troubleshooting or identifying if something goes wrong. 
                                print("length password list:", len(ls))
                                print("Password:", pw)
                                print("Closest match:", closest_match)
                                print("edit distance:", min_dis)
                        else:
                            #for the first generated password
                            ls.append(pw)
                            i +=1           

            #currently the list is ordered, de-order the list with shuffle. 
            random.shuffle(ls)
            #create a dataset for export from the list of passwords
            df = pd.DataFrame({'pw': ls})
                
            st.write(f"{len(df)} passwords were generated. Your passwords look like this:")    
            st.write(df.head())
            #st.write(tabulate(df[0:6], headers='keys', tablefmt='psql', showindex=False))
            
            end = time.time()
            t = end - start
            t_form = "{:.2f}"
            t = t_form.format(t)

            df_settings = pd.DataFrame({'setting': ['seed', 'N passwords', 'min length', 'max length', "complexity uppercase", "complexity lowercase", "complexity numbers", "complexity special", "exclude Il1", "exclude O0", "editdistance", "time in seconds"],
                                        'value': [input_seed, input_num_pw, input_len_min, input_len_max, input_uppercase, input_lowercase, input_numbers, input_special, input_IL, input_O0, input_editdis, t]} 
                           )
            

            #download buttons
            st.sidebar.download_button(
                label="Download data as CSV",
                data=df.to_csv(index = False).encode('utf-8'),
                file_name='passwords.csv',
                mime='text/csv',)
                
            st.sidebar.download_button(
                label="Download app settings",
                data=df_settings.to_csv(index = False, sep=';').encode('utf-8'),
                file_name='app_settings.csv',
                mime='text/csv',)

    with tab2:
        with open("README.md", "r") as file:
            content = file.read()

        st.markdown(content)

