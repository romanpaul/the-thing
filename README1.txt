To run the code:

Download and install Python3:
https://www.python.org/downloads/

Run the following code in your console of choice to install dependancy libraries for the project:
pip3 install Flask
pip3 install connexion[swagger-ui]
pip3 install pytest
pip3 install requests

Navigate to the folder where you downloaded the project and start the server by entering the following in your console:
python3 server.py

The server will be active on http://localhost:5000, so you will see the test homepage by entering that into your browser. To visit the current page for the documentation, go to http://localhost:5000/api/ui/. From here you can test each API call. Once you press "try it out", two ways to obtain the results will appear. Curl is a Linux based command line tool that you can use to make http requests from the console. If you would rather view the data in your browser, copy the line under "Request URL" and paste it in your address bar. 
