#Weather Forecaster  
  
Get Yahoo weather forecast from the command line  

##Installation  
Requires python 2.5+

I recommend you put the script into the directory you use for user created
executables. I use the directory `~/.bin` for this.  
  
If you don't have such a directory create on like so.

    mkdir ~/.bin ; cd ~/.bin

Then clone this repository into your `~/.bin` directory.

    git clone https://github.com/cmcdowell/Weather-Forecaster.git

You can use the script like this, but it might be a good idea to add it to the
PATH in your .bashrc, you can do that by adding this to your .bashrc

    export PATH=$PATH:$HOME/.bin
    alias weather='weather.py'

And changing the mode of the script to executable with `chmod +x weather.py`

Finally you need to add the WOEID of your location to the script. Open up
weather.py in your text editor and change the WOEID variable to reference your
location, you can find your WOIED [here](http://woeid.rosselliot.co.nz/lookup).

##Usage 

If installed properly you can get the current weather by just typing `weather`
in the command line. By default Weather Forecaster displays temperatures in
degrees Celsius, if you want to have temperatures in Fahrenheit you can do
that by adding the -f flag  
  
    weather -f

You can get a more detailed forecast, covering several days, by adding the -d
flag  

    weather -d
