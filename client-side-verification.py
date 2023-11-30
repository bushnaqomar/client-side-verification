import mechanize

browser = mechanize.Browser()

browser.set_handle_robots(False) #to see if the user is a robot

url = input("Enter the URL: ") #user input for the url for dummy website

#set some of the parameters to True
browser.set_handle_equiv(True)
browser.set_handle_gzip(True)
browser.set_handle_redirect(True)
browser.set_handle_referer(True)

browser.open(url)
for form in browser.form():
    print(form)

#this will bypass the validations on the given fields 
browser.select_form(nr = 0)
browser.form['name'] = ''
browser.form['gender'] = ''
browser.submit()
'''this script will bypass the the name and gender section which should not be able to be 
left blank'''