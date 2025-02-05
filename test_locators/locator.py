# locators/signup_locators.py
from selenium.webdriver.common.by import By


class Locators:
    #Signup page
    SIGNUP_LINK_XPATH = (By.XPATH, '//a[text()="Sign up"]')
    EMAIL_FIELD_ID = (By.ID,"email")
    PASSWORD_FIELD_ID =(By.ID, "password")
    CONTINUE_BUTTON_XPATH =(By.XPATH, "//button[@data-action-button-primary='true']")

    #Login page
    Username_ID=(By.ID,"username")
    Password_ID=(By.ID,"password")
    SUBMIT_BUTTON_XPATH = (By.XPATH,"//button[contains(@class, 'bg-[#2FA0A0]') and contains(@class, 'rounded-lg') and contains(@class, 'w-full') and contains(@class, 'py-3')]")

    #Dashboard
    DASHBOARD_XPATH =  (By.XPATH,"//span[text()='Dashboard']")

    #Social links
    LINKEDIN_XPATH = (By.XPATH,'//*[@id="__next"]/footer/div/ul[2]/li[1]/a')
    YOUTUBE_XPATH = (By.XPATH,'//*[@id="__next"]/footer/div/ul[2]/li[2]/a')

    #Fileupload
    FILE_UPLOAD_XPATH = (By.XPATH, '//input[@type="file"]')
    COMPLIANCE_GRAPH_XPATH = "//div[@id='reactgooglegraph-1']"
    WIN_GRAPH_XPATH = (By.XPATH,'//h6[text()="Priority: Low - High"]')
    STORY_BOARD_PDF = (By.XPATH,'//div[@class="grid grid-cols-4 gap-2"]')
    COMPLIANCE_CHECKLIST_XPATH = (By.XPATH,"//div[@class='flex items-center justify-between']/h2[text()='Compliance Checklist']")
    WIN_THEME_XPATH = (By.XPATH,'//h2[text()="Win Theme"]')
    STORY_BOARD_XPATH = (By.XPATH,"//h2[@class='font-medium mb-2'][text()='Story Board']")

    #profile
    PROFILE_IMAGE_XPATH = (By.XPATH,"//div[@class='flex items-center justify-center gap-2 h-42']")
    PROFILE_SETTINGS_XPATH = (By.XPATH,"(//a[@href='/profileSetting'])[1]")#//a[@href='https://qa-marketing.cognogent.com/profile' and normalize-space(text())='Profile Setting']
    CONTACT_US_XPATH = (By.XPATH,"//a[text()='Contact Us']")
    #themes
    LIGHT_THEME= (By.XPATH, '//div[@class="w-5.5 h-5.5 rounded-[10px] p-1 "]')
    DARK_THEME= (By.XPATH, "(//div[contains(@class, 'w-5.5') and contains(@class, 'h-5.5') and contains(@class, 'rounded-[10px]')])[2]")
    #privacy and terms
    PRIVACY_XPATH=(By.XPATH,"//a[@href='/privacy' and text()='Privacy']")
    TERMS_XPATH=(By.XPATH,"//a[text()='Terms of use']")
    #home Page
    HOME_PAGE_XPATH= (By.XPATH,"//img[contains(@src, 'Cognogent-logo.1341b2ab.png')]")
    UL_ELEMENT_XPATH=(By.XPATH, "//ul[@class='navbar-nav nav-tabbs mx-auto mb-2 mb-lg-0']")

    #Session
    SESSION_XPATH=(By.XPATH,"//button[@class='w-7 h-7 rounded bg-[#2FA0A0] grid place-items-center']")
    POPUP_XPATH=(By.XPATH,"//p[@class='text-[11px]' and contains(text(), 'You can create only 5 sessions')]")
    SESSION_PLUS_XPATH=(By.XPATH,"//button[@class='w-7 h-7 rounded bg-[#2FA0A0] grid place-items-center']")
    NEW_SESSION_XPATH=(By.XPATH,'(//h2[text()="New Session"])[1]')
    THREE_DOTS_XPATH =(By.XPATH,"//div[@class='flex items-center justify-between content']//button[@id='radix-:r3:' and contains(@class, 'more-btn')]")
    #Session Delete
    DELETE_XPATH= (By.XPATH,"//div[@role='menuitem' and contains(@class, 'cursor-default') and contains(@class, 'select-none') and .//text()='Delete']")
    CONTINUE_XPATH=(By.XPATH,"//button[text()='Continue']")
    #Session Edit
    EDIT_XPATH=(By.XPATH,"//div[text()='Edit']")
    SESSION_NAME_XPATH=(By.XPATH,"//input[@value='New Session']")
    ACCEPT_BUTTON_XPATH=(By.XPATH,"//button[@id='hs-eu-confirmation-button']")



