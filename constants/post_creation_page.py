class PostCreationPageConstants:
    # Hello page
    INVITATION_TEXT_XPATH = ".//p[@class='lead text-muted']"
    INVITATION_TEXT_MESSAGE_PART = "Your feed displays"
    SIGN_OUT_BUTTON_XPATH = ".//button[text()='Sign Out']"

    # Post creation
    CREATE_POST_BUTTON_XPATH = ".//a[@class='btn btn-sm btn-success mr-2']"
    POST_TITLE_XPATH = ".//input[@id='post-title']"
    POST_BODY_XPATH = ".//textarea[@id='post-body']"
    UNIQUE_POST_CHECKBOX_XPATH = ".//input[@id='”UniquePost”']"
    SAVE_NEW_POST_BUTTON_XPATH = ".//button[@Class='btn btn-primary']"
