my_varible = '''
    <html>
        <head>
            <title>testing</title>
        </head>
            <body>
                <h1>Can't believe I'm doing this</h1>
            </body>    

    </html>
'''

my_html_file = open("/Users/gsteffen/Documents/Projects/Python/my_html_file.html", "w")


my_html_file.write(my_varible)
my_html_file.close()