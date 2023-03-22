# README


IMPORTANT!

This API uses OAuth aunhtentication.

After enable the user and get the required credential, you must to store a file named 'credential.json' containing the credential data downloade on your Google workspace https://developers.google.com/workspace/guides/create-credentials?hl=en


### __auth()

    

    This function authenticate and generate the token for accessing the api
    This is a private function, so it will not be available for direct accessing, being used as an access provider for the public functions

    Requirements

    This function requires the credential information to generate a token access, make sure that you already had confugured the API activation on the Google workspace 
    
    The credential can be taken on your Google workspace 'https://developers.google.com/workspace/guides/create-credentials?hl=en'
    
    Important: You must rename your credential file to 'credentials.json' and move it to the same path of your execution file.
    
    On that specific case to the same path of the file 'gmail_api.ipynb'


### __mymail()

    This function get the user email address
    This is a private function, so it will not be available for direct accessing, being used as an access provider for the public functions

### gmail_send_message(param=0)

    This function sends an email
    To works properly it requires a set of parameters as shown below

    param = {
        'from': email_from, 
        'to': email_to,
        'subject': text_subject,
        'body': text_body
        }

    from - the sender email address
    to -  the recipient email address
    subject - the title of the email message
    body - the content of the email message

### generate_sample(num_sample=10)

    This function generates a user defined number of email samples to provide a real world perspective of the API usability.

### gmail_search_message(word_search='')

    This function search for email messages that fits the predefined word desired

    The samples were generated based on a list of job roles
    job roles list
    ['Data engineer', 'Data analyst', 'Data scientist', 'BI analyst', 'Product Owner', 'Product Manager', 'Tech Lead']

    Pick one of these job roles and test it
    Also, if you just want to take a list of all emails, you can run it without filling the variable 'word_search'
    
### read_message(id_message=0)

    Each email has its own ID number, to use this function first you need to get a specific email ID number

    In that case the ID number can be found using the function gmail_search_message()

### welcome()

    This function shows a message when the api is fully connected and read to use.

