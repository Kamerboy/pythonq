import smtplib

server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login ( 'contactluke247@gmail.com', 'Toolbox2.0' )

server.sendmail( "Luke W.", "8152070489@vtext.com", "ZCH 384'6, ZSH 997'4" )
