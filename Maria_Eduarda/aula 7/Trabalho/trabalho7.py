import threading,time,os,webcolors,random,keyboard
from googletrans import Translator
from datetime import datetime
class Dispositivo (threading.Thread):
    def __init__(self,idExp,idt,TempoSessao,TempInicialON,TempoON,RGB_red,RGB_green,RGB_blue,eletrodos,language):
        threading.Thread.__init__(self)
        self.idExp=idExp
        self.idt=idt
        self.TempoSessao=TempoSessao
        self.TempInicialON=TempInicialON
        self.TempoON=TempoON
        self.RGB_red=RGB_red
        self.RGB_green=RGB_green
        self.RGB_blue=RGB_blue
        self.eletrodos=eletrodos
        self.language=language
    def run(self):
        tradutor=Translator()
        TXT=tradutor.translate("inicio da sessão:", dest=self.language)
        print(TXT.text+" %s" % ((self.idExp)+1)+"-",self.idt)
        TXT=tradutor.translate("#Em caso de erros no experimento apertar a tecla 'esc'!", dest=self.language)
        print(TXT.text)
        procThread(self.idExp,self.idt,self.TempoSessao,self.TempInicialON,self.TempoON,self.RGB_red,self.RGB_green,self.RGB_blue,self.language)
        TXT=tradutor.translate("Fim da sessão: ", dest=self.language)
        print(TXT.text+"%s" % ((self.idExp)+1))

def procThread(idExp,idt,TempoSessao,TempoInicialON,TempoON,red,green,blue,lang):
    tradutor=Translator()
    RGB=webcolors.rgb_to_name((red,green,blue))
    Cor=tradutor.translate(RGB, dest=lang)
    Estimulo=tradutor.translate("Estímulo com led da cor: ",dest=lang)
    temporizador=tradutor.translate("Tempo:",dest=lang)
    Desligada=tradutor.translate("Desligada!",dest=lang)
    Session=tradutor.translate("Dispositivo: ",dest=lang)
    experimento=tradutor.translate("**Experimento:",dest=lang)
    now=datetime.now()
    aux=int(now.second+TempoSessao.second)//60
    SegundoFinal=int(now.second+TempoSessao.second-(aux*60))
    SegundoAgora=int(now.second)
    minutoFinal=int(now.minute+TempoSessao.minute+aux)
    minutoAgora=int(now.minute)
    ligada=[]
    Sinal_eletrodo=[]
    for i in range(0,len(TempoInicialON)):
       aux=int(now.second+TempoInicialON[i].second)//60
       SegundoFinal_ligada=int(now.second+TempoInicialON[i].second-(aux*60))
       minutoFinal_ligada=int(now.minute+TempoInicialON[i].minute+aux)
       datatxt=str(minutoFinal_ligada)+':'+str(SegundoFinal_ligada)
       Tempo=datetime.strptime(datatxt,'%M:%S')
       ligada.append(Tempo)
  
    
    while((minutoAgora!=minutoFinal) or (SegundoAgora!=SegundoFinal)):
        if keyboard.is_pressed('esc'):
            TXT=tradutor.translate("Experimento finalizado:", dest=lang)
            print(TXT.text)
            break

        for j in ligada:
            if keyboard.is_pressed('esc'):
                TXT=tradutor.translate("Experimento finalizado:", dest=lang)
                print(TXT.text)
                break

            if((j.minute==minutoAgora)):
                for i in range (0,TempoON):
                    print("\r{6}:{7}.{4}:{5}. {2}:{0}. {3}:{1}".format(Cor.text,i,Estimulo.text,temporizador.text,Session.text,idt+1,experimento.text,idExp+1))
                    #os.system("cls")
                    for w in range (0,1000):
                        now=datetime.now()
                        SegundoAgora=now.second
                        minutoAgora=now.minute
                        if keyboard.is_pressed('esc'):
                            TXT=tradutor.translate("Experimento Finalizado:", dest=lang)
                            print(TXT.text)
                            break

                        #print("Entrnado",minutoAgora,minutoFinal,SegundoAgora,SegundoFinal)
                        if ((minutoAgora==minutoFinal) and (SegundoAgora==SegundoFinal)):
                            break
                        else:
                            sinal=round(random.uniform(-500,500),6)
                            Sinal_eletrodo.append(sinal)
                        time.sleep(0.001)
                    """now=datetime.now()
                    SegundoAgora=now.second
                    minutoAgora=now.minute"""
            else:
                print("\r {3}:{4}. {0}:{1}.{2}".format(Session.text,idt+1,Desligada.text,experimento.text,idExp+1))
                #os.system("cls")
                for w in range (0,1000):
                        now=datetime.now()
                        SegundoAgora=now.second
                        minutoAgora=now.minute
                        if keyboard.is_pressed('esc'):
                            TXT=tradutor.translate("Experimento finalizado:", dest=lang)
                            print(TXT.text)
                            break
                        #print("Entrnado",minutoAgora,minutoFinal,SegundoAgora,SegundoFinal)
                        if ((minutoAgora==minutoFinal) and (SegundoAgora==SegundoFinal)):
                            break
                        else:
                            sinal=round(random.uniform(-500,500),6)
                            Sinal_eletrodo.append(sinal)
                        time.sleep(0.001)
            """now=datetime.now()
            SegundoAgora=now.second
            minutoAgora=now.minute"""
        now=datetime.now()
        SegundoAgora=now.second
        minutoAgora=now.minute
    print((idExp+1),"Sinais captados",Sinal_eletrodo)

def StartThread():
    print("****Welcome Optogenetics Prime***")
    tradutor=Translator()
    Detector=input("#To start the system write 'Start the system' in your native language: ")
    Lang=tradutor.detect(Detector)
    Txt=tradutor.translate('Digite a quantidade de Experimentos simultâneos: ', dest=Lang.lang)
    num=int(input(Txt.text))
    Dispositivos=[]
    for i in range(0,num,1):
        Exp=i
        Txt=tradutor.translate('***Informações do experimento {}: ***'.format(i+1), dest=Lang.lang)
        print(Txt.text)
        Txt=tradutor.translate('Digite a quantidade de Dispositivos Utlizados no experimento {}:'.format(i+1), dest=Lang.lang)
        Num_Dispositivosint=int(input(Txt.text))
        Txt=tradutor.translate('Digite o tempo (Minutos) de sessão do experimento {} (Ex.02:30, ou seja, 2min e 30s): '.format(i+1), dest=Lang.lang)
        TempoSessaoTxt=input(Txt.text)
        TempoSessao=datetime.strptime(TempoSessaoTxt,'%M:%S')
        for j in range (0,Num_Dispositivosint,1):
            idt= j
            Txt=tradutor.translate('Digite q quatidade de vezes que o dispositivo {} será ligado: '.format(j+1), dest=Lang.lang)
            qtd=int(input(Txt.text))
            Txt=tradutor.translate('Digite as 32 posições do dispositivo {}. Da seguinte forma 1,23,45,6,...:'.format(j+1), dest=Lang.lang)
            eletrodos=input(Txt.text)
            eletrodos=str(eletrodos).split(',')
            Txt=tradutor.translate('Digite por quanto, tempo em Segundos, que a luz deve permanecer ligada :', dest=Lang.lang)
            TempoON=int(input(Txt.text))
            TempoInicialON=[]
            for z in range(0,qtd,1):
                Txt=tradutor.translate('Digite em que tempo o dispositivo {0} será ligado na interação {1}. Ex. 0:30, isto é, após de 30 segundos que o dispositivo foi ligado:'.format(j+1,z+1), dest=Lang.lang)
                TempoInicialTxt=input(Txt.text)
                TempoInicialDT=datetime.strptime(TempoInicialTxt,'%M:%S')
                TempoInicialON.append(TempoInicialDT)     
            Txt=tradutor.translate('Digite o Primeiro valor RGB (0 a 255):', dest=Lang.lang)
            RGB_red=int(input(Txt.text))
            Txt=tradutor.translate('Digite o segundo valor RGB (0 a 255):', dest=Lang.lang)
            RGB_green=int(input(Txt.text))
            Txt=tradutor.translate('Digite o Terceiro valor RGB (0 a 255):', dest=Lang.lang)
            RGB_blue=int(input(Txt.text))
            Dispositivos.append(Dispositivo(Exp,idt,TempoSessao,TempoInicialON,TempoON,RGB_red,RGB_green,RGB_blue,eletrodos,Lang.lang))
    for w in range (0,len(Dispositivos)):
        Dispositivos[w].start()
    for t in Dispositivos:
        t.join()    
            


StartThread()


