import collections, sys, os
from logic import *

############################################################
"""
Yazdiginiz kodlari denemek icin, python 3.x' i kurarak asagidaki kod satirlarini
yazabilirsiniz. 
Eger yazdiginiz kod dogru ise cikarima gore yes ya da no cevabini alacaksiniz.
I don't know cevabı bilgi tabanına yeterli bilgi ve kural girmediğinizi gösterir.
## ile gösterilen yerlere kodlarınızı yazmalisiniz.

problem11 ve problem21'i örnek olarak kullanabilirsiniz.

>>> from homework import *
>>> problem11()
Yes.

"""
############################################################

# Problem 1: Onermeler Mantigi

# Gorev1-1: "Eger Koku alamiyorsan ve Oksuruk var ise Covid hastasisindir."

def problem11():

    # Bilgi tabani ve cikarim metodu

    kb=createResolutionKB()

    # Onermeleri tanimlayin

    Koku = Atom('Koku')              # Koku onermesi            
    Oksuruk =Atom('Oksuruk')         # Oksuruk onermesi
    Covid = Atom ('Covid')  	     # Covid onermesi
    
    # Gercekleri ve Kurallari bilgi tabanina ogretin
    
    #Kurallar
    kb.tell(Implies(And(Not(Koku),Oksuruk),Covid))      # Koku alamiyorsan ve Oksuruk var ise Covidsindir. 
    
    #Gercekler
    kb.tell(Not(Koku))  # Koku yok
    kb.tell(Oksuruk)    # Oksuruk var
 
    #Sorgu
    print(kb.ask(Covid)) #Covid miyim


# Gorev1-2: " Cimler islaktir ancak ve ancak yagmur yagiyorsa veya fiskiyeler acik ise"

def problem12():

    # Bilgi tabani ve cikarim metodu

    kb=createResolutionKB()
    
    # Onermeleri tanimlayin

    Islaktir=Atom('Islaktir')   #Cimler islaktir      
    Yagmur=Atom('Yagmur')    #Yagmur yagar
    Fiskiye=Atom('Fiskiye')    #Fiskiye calisir
    
    # Gercekleri ve Kurallari bilgi tabanina ogretin
    #Kural
    kb.tell(Equiv(Islaktir,Or(Yagmur,Fiskiye)))  #Equiv (Ancak ve Ancak).Cimler islaktir ancak ve ancak (Equiv())yagmur yagiyorsa veya fiskiyeler acik ise

    
    #Gercekler
    
    kb.tell(Not(Yagmur)) #Yagmur yagmiyor
    kb.tell(Islaktir)    # Cimler islak

    #Sorgu
    
    print(kb.ask(Fiskiye))


# Gorev1-3: " Hava sicakligi pozitif ve hava basinci yuksek degilse veya ruzgar var ise Firtina yaklasiyordur"

def problem13():
    # Bilgi tabani ve cikarim metodu

    kb=createResolutionKB()

    # Onermeleri tanimlayin

    SicakligiPozitif = Atom('SicakligiPozitif') #  Hava Sicakligi pozitif
    Basinci = Atom('Basinci') #  Hava basinci yuksek
    Ruzgar = Atom('Ruzgar') #  Ruzgar
    Firtina = Atom('Firtina')#  Firtina 
    # Gercekleri ve Kurallari bilgi tabanina ogretin
    
    #Kurallar
    kb.tell(Implies(Or(And(SicakligiPozitif, Not(Basinci)),Ruzgar), Firtina)), #  Hava sicakligi pozitif ve hava basinci yuksek degilse veya ruzgar var ise Firtina yaklasiyordur"
    
    #Gerçekler
    
    kb.tell(Not(Ruzgar))      #ruzgar yok
    kb.tell(SicakligiPozitif) #sicaklik pozitif
    kb.tell(Not(Basinci))# hava basinci dusuk

    #Sorgu
    
    print(kb.ask(Firtina)) #Firtina ? 


############################################################

# Problem 2: first-order logic

# Örnek1: "Peker bir eve sahip degildir"
#   kb=createResolutionKB()
#   peker=Constant('peker')           # peker sabit
#   def Ev(x): return Atom('Ev',x)    # Ev bir önermedir
#   def EveSahiptir(x,y): return Atom('EveSahiptir',x,y) # x ye diye bir eve sahiptir
   
#   kb.tell(Not(Exists('$x',And(EveSahiptir(peker,'$x'),Ev('$x')))))
#  x bi evdir ve peker x evine sahiptir diye bir x vardır doğru değildir.


# Örnek2: " Dis cephesi olan evler kis mevsiminde soguk olmaz"

#   kb=createResolutionKB()
#   def Ev(x) : return Atom('Ev',x)
#   def Discephevardir(x): return Atom('Discephevardir',x)

#   Kismevsimi=Atom('Kismevsimi')
#   def Sogukolur(x):  return Atom('Sogukolur',x)
#   benimevim = Constant('benimevim')
    
#!!Tum operantlar 2 bilesen alirlar.

#   kb.tell(Forall('$x',Implies(And(And(Ev('$x'),Discephevardir('$x')),Kismevsimi),Not(Sogukolur('$x')))))

#!!Tüm x ler için x bir ev ise ve bu x'in Dis cephesi var ise ve Kismevsimi dogru ise Soguk olur yanlistir
#   kb.tell(And(Ev(benimevim),Discephevardir(benimevim)))
#   kb.tell(Kismevsimi)
#   print(kb.ask(Sogukolur(benimevim)))


# Gorev 2-1:"Mavi Arabalar hizlidir, Benim arabam mavidir. Benim Arabam hizli midir?"

def problem21():

    # Bilgi tabani ve cikarim metodu

    kb=createResolutionKB()
    
    # Nesneler Onermeler ve fonksiyonlar
    
    benim_arabam = Constant('benim_arabam')

    def Araba(x): return Atom('Araba',x)
    def Mavi(x): return Atom('Mavi',x)      
    def Hizlidir(x): return Atom('Hizlidir',x)
    
    # Gercekleri ve Kurallari bilgi tabanina ogretin
    #Kural 
    
    kb.tell(Forall('$x',Implies(And(Araba('$x'),Mavi('$x')),Hizlidir('$x'))))
    
    #Gercekler
    kb.tell(And(Araba(benim_arabam),Mavi(benim_arabam)))
  
    #Sorgu    
    print(kb.ask(Hizlidir(benim_arabam)))
    

# Gorev 2-2: "Birisi gitar kursu almış ise gitar calabilir"

def problem22():

    # Bilgi tabani ve cikarim metodu

    kb=createResolutionKB()
    
    # Onermeler icin fonksiyonlar
    ahmet=Constant('ahmet')
    zeynep =Constant('zeynep')
    
    def GitarCalar(x): return Atom('GitatCalar', x) #Gitar calar     
    def KursAlmis(x): return Atom('KursAlmis', x)   #Kurs almis

    # Gercekleri ve Kurallari bilgi tabanina ogretin

    #Kural
    kb.tell(Forall('$x', Equiv(KursAlmis('$x'), GitarCalar('$x'))))  #"Birisi gitar kursu almış ise gitar calabilir"
    
    kb.tell(KursAlmis(zeynep))
    kb.tell(Not(KursAlmis(ahmet)))
    
    #Sorgu
    print(kb.ask(GitarCalar(ahmet)))




# Gorev 2-3 "x,y nin cocugu ise ve x kadin ise, x y'nin kizidir".

def problem23():

    # Bilgi tabani ve cikarim metodu

    kb=createResolutionKB()
    
    # Onermeler icin fonksiyonlar
    
    zeynep =Constant('zeynep')
    ahmet=Constant('ahmet')
    
    def Kadin(x): 
        return Atom('Kadin', x)            # x kadin dir
    def Cocugu(x, y): 
        return Atom('Cocugudur', y, x)            # y x'in cocugudur
    def Kizi(x, y): 
        return Atom('Kizi', y, x)           # y x'in kizidir

    # Gercekleri ve Kurallari bilgi tabanina ogretin
    
    #Kural
    kb.tell(Forall('$x',Forall('$y',Implies(And(Cocugu('$y','$x'), Kadin('$x')), Kizi('$y', '$x')))))   # x,y nin cocugu ise ve x kadin ise, x yenin kizidir
    
    #Gercekler
    
    kb.tell(Kadin(zeynep))
    kb.tell(Cocugu(ahmet,zeynep))
    
    #Sorgu
    print(kb.ask(Kizi(ahmet,zeynep)))

# Yes

    
# Gorev 2-4 "Hastanin tansiyon degeri 13'ten yuksek ise Hasta risklidir ve 
# riskli hastalar önceliklidir."


def problem24():
   
    # Bilgi tabani ve cikarim metodu

    kb=createResolutionKB()
    
    # Onermeler icin fonksiyonlar ve sabitler
    
    riza=Constant('riza')
    ece=Constant('ece')
        
    def Onceliklidir(x): return Atom('Öncelikli', x)    #Öncelikli x ler vardır
    def Risklidir(x): return Atom('Riskli', x)    #Riskli x ler vardir      
    
    def Tansiyon(x,y):   #x 'in tansiyonu y ise ve y>13 ise x Risklidir
        if y>13:
            return Risklidir(x)
        else:
            return Not(Risklidir(x))

    # Gercekleri ve Kurallari bilgi tabanina ogretin
    
    #Kurallar
    kb.tell(Forall('$x', Equiv(Risklidir('$x'), Onceliklidir('$x'))))  #Tüm Riskliler Önceliklidir.
    
    #Gercekler
    kb.tell(Tansiyon(riza, 16))  #Riza nin tansiyonu 16 dir
    kb.tell(Tansiyon(ece, 13))  # Ece'nin tansiyonu 13'tür 
     
    #Sorgu
    print(kb.ask(Onceliklidir(riza))) # Riza öncelikli midir? 
    print(kb.ask(Onceliklidir(ece))) # Riza öncelikli midir? 


############################################################
