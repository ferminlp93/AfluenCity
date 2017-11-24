from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream



##Mis claves de twitter
consumer_key = "Dbk9K4825bR3BgaHjhuIMDdKr"
consumer_secret = "WkxFXFiRh8bdacO4fReF83yJV06aD3BEUWsMPQlzLLZ1fllPtm"
 
access_token  = "840639055-KWRYNG45l1jgSJjlwngg10ePVHwxwmr5zpMwYqjc"
access_token_secret  = '36i928WMor6fYbbtUnr6fyxB1zz0DGlw0ankonrMAPeaD'

#Streaming de twitter en tiempo real
class StdOutListener(StreamListener):
    
    def on_data(self, data):
        print(data)
        #sacar a fichero los datos para procesarlos
        with open("output.txt", "a") as text_file:
            text_file.write(data.strip())
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    #LLamamos a la api con nuestras claves
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #Filtramos la zona levante, joder lo que ha costado esta puta linea.
stream.filter(locations=[-1.06,38.3,3.48,40.56])
