# IMPORTING LIBRARIES

import pandas as pd

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# ----------------------------------------------------------------------------------------------------------------------
# GET PRODUCT DETAILS
def get_product_link():

    t_shirt_details={'product_link':[]}

    driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

    #driver.maximize_window()

    driver.get('https://www.myntra.com/men-tshirts'); # Website URL 

    for i in range(20):  # How many Page you want to scrap
        try:pro_link=driver.find_elements(By.XPATH,'//*[@id="desktopSearchResults"]/div[2]/section/ul/li/a')
        except:pro_link=None
        t_shirt_details['product_link'].extend([i.get_attribute('href') for i in pro_link])

        # Go to next page
        driver.find_element(By.XPATH,"//a[contains(text(),'Next')]").click()

        time.sleep(3)

    return t_shirt_details


#--------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------------------------
# OVERALL DETAILS OF THE PRODUCT
def over_all_details():

    # To GET PRODUCT DETAILS
    pro_duct_link=get_product_link()
    df=pd.DataFrame(pro_duct_link)

    # TO SAVE CSV
    df.to_csv('product_links.csv',index=False,encoding='utf-8-sig') 


    over_all={'ProductName':[],'ProductDef':[],'DiscountPrice':[],'OriginalPrice':[]
            ,'DiscountPercent':[],'Ratings':[],'ReviewText':[],'UserName':[],'DateReviewd':[],'ImagesLink':[],'ProductLink':[]}

    for i in pro_duct_link['product_link']:

        driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

        try:
            driver.get(i);

            try:pro_name=driver.find_element(By.XPATH,'//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[1]/h1[1]').text
            except:pro_name=None
        

            try:pro_def=driver.find_element(By.XPATH,'//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[1]/h1[2]').text 
            except:pro_def=None 
        

            try:disc_price=driver.find_element(By.XPATH,'//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[1]/div/p[1]/span[1]/strong').text
            except:disc_price=None 
            

            try:org_price=driver.find_element(By.XPATH,'//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[1]/div/p[1]/span[2]/s').text   
            except:org_price=None


            try:dis_percent=driver.find_element(By.XPATH,'//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/div[1]/div/p[1]/span[3]').text
            except:dis_percent=None 
        

            # To acess the comment section
            try:review_page=driver.find_element(By.XPATH,'//*[@id="mountRoot"]/div/div[1]/main/div[2]/div[2]/main/div/div/a').get_attribute('href')
            except:review_page=None
            



            try:driver.get(review_page);
            except:None

            try:rating=driver.find_elements(By.XPATH,'//*[@id="detailedReviewsContainer"]/div/div[1]/div[1]/span')
            except:rating=None

            try:review_text=driver.find_elements(By.XPATH,'//*[@id="detailedReviewsContainer"]/div/div[1]/div[2]')
            except:review_text=None


        

            try:user_name=driver.find_elements(By.XPATH,'//*[@id="detailedReviewsContainer"]/div/div[2]/div[1]/span[1]')
            except:user_name=None


            try:date=driver.find_elements(By.XPATH,'//*[@id="detailedReviewsContainer"]/div/div[2]/div[1]/span[2]')
            except:date=None
        

            try:reviwer_pro_img=driver.find_elements(By.XPATH,'//*[@id="mountRoot"]/div/main/div[2]/div[2]/div[2]/div/div[2]/div/div/img')
            except:reviwer_pro_img=None
        





            over_all['ProductName'].append(pro_name)
            over_all['ProductDef'].append(pro_def)
            over_all['DiscountPrice'].append(disc_price)
            over_all['OriginalPrice'].append(org_price)
            over_all['DiscountPercent'].append(dis_percent)

            rs=[[j.text for j in rating]]
            over_all['Ratings'].extend(rs)

            rt=[[k.text for k in review_text]]
            over_all['ReviewText'].extend(rt)

            un=[[l.text for l in user_name]]
            over_all['UserName'].extend(un)

            dr=[[m.text for m in date]]
            over_all['DateReviewd'].extend(dr)

            im=[[n.get_attribute('src') for n in reviwer_pro_img]]
            over_all['ImagesLink'].extend(im)

            over_all['ProductLink'].append(i)

            time.sleep(5)

        except:
            over_all    

 
 
#--------------------------------------------------------------------------------------------------------------------------------------

# GET PRODUCT DETAILS
total_details=over_all_details()
df_1=pd.DataFrame(total_details)

# TO SAVE CSV
df_1.to_csv('myntra_mens_t_shirt_details.csv',index=False,encoding='utf-8-sig')

#--------------------------------------------------------------------------------------------------------------------------------------





