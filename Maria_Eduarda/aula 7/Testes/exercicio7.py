import time,sys,webcolors,threading
from datetime import datetime
from googletrans import Translator
class Experimento (threading.Thread):
    def __init__(self,idt,TempoSessao,TempInicialON=list,TempoON=list,RGB_red,RGB_green,RGB_blue):
        threading.Thread.__init__(self)
        self.idt=idt
        self.TempoSessao=TempoSessao
        self.TempInicialON=TempInicialON
        self.TempoON
        self.RGB_red=RGB_red
        self.RGB_green=RGB_green
        self.RGB_blue=RGB_blue
    def run(self):
        print("Inicio da sessão: %s" % (self.id))
        procThread(self.id,self.TempoSessao,self.TempInicialON,self.Tempo_On,self.RGB_red,self.RGB_green,self.RGB_blue)
        print("Fim da sessão%s" % (self.id))
def procThread (cod,Tempo_Sessao,Tempo_Inicia_On=list,Tempo_On=list,red,green,blue):
    now = datetime.now()
    x=now.minute+Tempo_Sessao
    y=now.minute
    tradutor=Translator()
    RGB=webcolors.rgb_to_name((red,green,blue))
    Cor=tradutor.translate(RGB, dest='pt')
    print(b.text)
    while (y!=x):
         for i in range(0, Tempo_On):
             sys.stdout.write("\r a led da cor{}"+str(b).format(i))
             sys.stdout.flush()
             time.sleep(1)
         else:
             sys.stdout.write("\rDesligada{}".format(j))
             sys.stdout.flush()
             time.sleep(1)
         y=now.minute
  
ThreadTest=Experimento(1,2,[1],[30],1,0,0,0)
ThreadTest2=Experimento(1,2,[1],[30],1,0,0,0)
ThreadTest.start()
ThreadTest2.start()
print("Fim")

