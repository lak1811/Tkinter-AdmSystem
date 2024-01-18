from tkinter import *
import mysql.connector

#README!
#vindunr er basert på oppgavene i arbkravet og delvinduene er numerert systematisk
#f.eks vindunr=112 deles opp i tre deler der første tall er oppgavenr
#andre nummer er basert på delvinduet til et vindu. Som f.eks 11, som er vindu 1, ajoureholde studenter
#tredje nummer er basert på delvinduet til et delvindu til et vindu.
#f.eks 111 som er vindu 1, ajourholdestudenter, og første del-del side lagd som er lagring av studenter
#alle andre oppgaver er nummerert som vindu_1,vindu_2 osv osv for oppgavenr

#og for oppdatering av studenter og eksamen, så er det essensielt at du fyller ut alle felt og ikke lar noen felt være
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
mindatabase=mysql.connector.connect(host='localhost',port=3306,user='Eksamenssjef',passwd='oblig2022',db='oblig2022')

def vindu_1():
    vindu1=Toplevel()
    vindu1.title ('Ajoureholde')
    def ajoureholdestudenter():
        vindu11=Toplevel()
        vindu11.title('ajourhold av studenter')
        

        def lagre111():
            

            vindu111=Toplevel()
            
            vindu111.title('Registrering')
            std_markor111ekstra=mindatabase.cursor()

            def lagre111def():
                std_markor111=mindatabase.cursor()
                

                
                
                settinnstd111=('INSERT INTO Student'
                            '(studentnr,fornavn,etternavn,epost,telefon)'
                            'VALUES(%s,%s,%s,%s,%s)')
                data_std111=(studentnr.get(),fornavn.get(),etternavn.get(),epost.get(),tlf.get())
                std_markor111.execute(settinnstd111,data_std111)
                mindatabase.commit()
                settinnstd111ekstra=('''SELECT max(studentnr) FROM STUDENT''')
                std_markor111ekstra.execute(settinnstd111ekstra)
                for row in std_markor111ekstra:
                    temp=(int(row[0]))

                temp=temp+1

                studentnr.set(temp)


                std_markor111.close()
                
                
                
            lbl_studentnr=Label(vindu111,text='oppgi Studentnr: ')
            lbl_studentnr.grid(row=0,column=1,padx=5,pady=5,sticky=E)
            

            lbl_fornavn=Label(vindu111,text='oppgi Fornavn: ')
            lbl_fornavn.grid(row=1,column=1,padx=5,pady=5,sticky=E)

            lbl_etternavn=Label(vindu111,text='oppgi Etternavn: ')
            lbl_etternavn.grid(row=2,column=1,padx=5,pady=5,sticky=E)

            lbl_epost=Label(vindu111,text='oppgi Epost: ')
            lbl_epost.grid(row=3,column=1,padx=5,pady=5,sticky=E)

            lbl_tlf=Label(vindu111,text='oppgi Telefon: ')
            lbl_tlf.grid(row=4,column=1,padx=5,pady=5,sticky=E)
            

            studentnr=StringVar()
            ent_studentnr=Entry(vindu111,width=10,state='readonly',textvariable=studentnr)
            ent_studentnr.grid(row=0,column=2,padx=5,pady=5,sticky=W)

            

            settinnstd111ekstra=('''SELECT max(studentnr) FROM STUDENT''')
            std_markor111ekstra.execute(settinnstd111ekstra)
            for row in std_markor111ekstra:
                temp=(int(row[0]))

                
            temp=temp+1
            studentnr.set(temp)
            fornavn=StringVar()
            ent_fornavn=Entry(vindu111,width=10,textvariable=fornavn)
            ent_fornavn.grid(row=1,column=2,padx=5,pady=5,sticky=W)

            

            etternavn=StringVar()
            ent_etternavn=Entry(vindu111,width=10,textvariable=etternavn)
            ent_etternavn.grid(row=2,column=2,padx=5,pady=5,sticky=W)

            epost=StringVar()
            ent_epost=Entry(vindu111,width=15,textvariable=epost)
            ent_epost.grid(row=3,column=2,padx=5,pady=5,sticky=W)

            tlf=StringVar()
            ent_tlf=Entry(vindu111,width=15,textvariable=tlf)
            ent_tlf.grid(row=4,column=2,padx=5,pady=5,sticky=W)

            btn_save=Button(vindu111,text='Lagre',command=lagre111def)
            btn_save.grid(row=7,column=6,padx=5,pady=25,sticky=E)
            
  
        

            btn_out=Button(vindu111,text='Tilbake',command=vindu111.destroy)
            btn_out.grid(row=7,column=7,padx=5,pady=25,sticky=E)
            



        
            

        def endre111():
            

            vindu112=Toplevel()
            
            vindu112.title('lagre')

            def endre111def():
                markor112=mindatabase.cursor()
                settinnvare112=('''UPDATE STUDENT
                                SET fornavn=%s,etternavn=%s,
                                epost=%s,telefon=%s
                                WHERE studentnr=%s''')
                data_vare112=(fornavn.get(),etternavn.get(),epost.get(),tlf.get(),studentnr.get())
                markor112.execute(settinnvare112,data_vare112)
                mindatabase.commit()
                markor112.close()
                
                
            lbl_info=Label(vindu112,text='Her skal du oppgi studentnr og informasjon du ønsker å ha for studenten')
            lbl_info.grid(row=0,column=3,padx=5,pady=5,sticky=W)
            lbl_studentnr=Label(vindu112,text='oppgi Studentnr: ')
            lbl_studentnr.grid(row=1,column=1,padx=5,pady=5,sticky=W)

            lbl_fornavn=Label(vindu112,text='oppgi Fornavn: ')
            lbl_fornavn.grid(row=2,column=1,padx=5,pady=5,sticky=W)

            lbl_etternavn=Label(vindu112,text='oppgi Etternavn: ')
            lbl_etternavn.grid(row=3,column=1,padx=5,pady=5,sticky=W)

            lbl_epost=Label(vindu112,text='oppgi Epost: ')
            lbl_epost.grid(row=4,column=1,padx=5,pady=5,sticky=W)

            lbl_tlf=Label(vindu112,text='oppgi Telefon: ')
            lbl_tlf.grid(row=5,column=1,padx=5,pady=5,sticky=W)

            studentnr=StringVar()
            ent_studentnr=Entry(vindu112,width=10,textvariable=studentnr)
            ent_studentnr.grid(row=1,column=2,padx=5,pady=5,sticky=W)

            fornavn=StringVar()
            ent_fornavn=Entry(vindu112,width=20,textvariable=fornavn)
            ent_fornavn.grid(row=2,column=2,padx=5,pady=5,sticky=W)

            etternavn=StringVar()
            ent_etternavn=Entry(vindu112,width=20,textvariable=etternavn)
            ent_etternavn.grid(row=3,column=2,padx=5,pady=5,sticky=W)

            epost=StringVar()
            ent_epost=Entry(vindu112,width=20,textvariable=epost)
            ent_epost.grid(row=4,column=2,padx=5,pady=5,sticky=W)

            tlf=StringVar()
            ent_tlf=Entry(vindu112,width=19,textvariable=tlf)
            ent_tlf.grid(row=5,column=2,padx=5,pady=5,sticky=W)

            btn_save=Button(vindu112,text='Lagre',command=endre111def)
            btn_save.grid(row=7,column=6,padx=5,pady=25,sticky=E)

            btn_out=Button(vindu112,text='Tilbake',command=vindu112.destroy)
            btn_out.grid(row=7,column=7,padx=5,pady=25,sticky=E)

        def slette111():
            vindu113=Toplevel()
            vindu113.title('sletting')

            def slette111def():
                markor113=mindatabase.cursor()

                settinnvare113=('''DELETE FROM STUDENT
                                WHERE studentnr=%s''')
                data_vare113=studentnr.get()
                
                markor113.execute(settinnvare113%data_vare113)
                
                
                mindatabase.commit()
                markor113.close()


            lbl_studentnr=Label(vindu113,text='oppgi Studentnr ')
            lbl_studentnr.grid(row=1,column=1,padx=5,pady=5,sticky=W)

            studentnr=StringVar()
            ent_studentnr=Entry(vindu113,width=10,textvariable=studentnr)
            ent_studentnr.grid(row=1,column=2,padx=5,pady=5,sticky=W)


            btn_save=Button(vindu113,text='Utfør',command=slette111def)
            btn_save.grid(row=7,column=6,padx=5,pady=25,sticky=E)

            btn_out=Button(vindu113,text='Tilbake',command=vindu113.destroy)
            btn_out.grid(row=7,column=7,padx=5,pady=25,sticky=E)
            


        btn_lagre=Button(vindu11,bg='#0be881',text='Registrer',command=lagre111)
        btn_lagre.grid(row=3,column=0,padx=5,pady=25,sticky=E)
        btn_endre=Button(vindu11,bg='#ffc048',text='Endre',command=endre111)
        btn_endre.grid(row=3,column=3,padx=5,pady=25,sticky=W)
        btn_slette=Button(vindu11,bg='#ff3f34',text='Slette',command=slette111)
        btn_slette.grid(row=3,column=5,padx=5,pady=25,sticky=W)

        
            


        

        
        btn_avslutt11=Button(vindu11,text='Avslutt',command=vindu11.destroy)
        btn_avslutt11.grid(row=7,column=7,padx=5,pady=25,sticky=E)
        









    def ajoureholdeeksamen():
        vindu12=Toplevel()
        vindu12.title('ajourhold av eksamen')



        def lagre121():
            

            vindu121=Toplevel()
            
            vindu121.title('Registrering')

            def lagre121def():
                
                #note fjern ved innlevering. Grunnlag=dårligtestdata
                advarsel.set(' ')

                
                
                flag=[]

                xmarkor=mindatabase.cursor()
                xstatement=('''SELECT dato,romnr
                                    from eksamen
                                    WHERE dato=%s
                                    AND romnr=%s''')
                xmangler=(dato.get(),romnr.get())
                xmarkor.execute(xstatement,xmangler)
                print('1')
                for rowss in xmarkor:
                    flag+=[rowss]
                xmarkor.close()

                print('2')
                if flag:
                    advarsel.set('Rommet er dessverre reservert')
                else:
                    print ('3')
                
                    
                    
                
                    std_markor121=mindatabase.cursor()
                    settinnstd121=('INSERT INTO Eksamen'
                                '(emnekode,dato,romnr)'
                                'VALUES(%s,%s,%s)')
                    data_std121=(emnekode.get(),dato.get(),romnr.get())
                    std_markor121.execute(settinnstd121,data_std121)
                    
                    mindatabase.commit()
                    std_markor121.close()
                    
                
                
            lbl_emnekode=Label(vindu121,text='oppgi Emnekode: ')
            lbl_emnekode.grid(row=0,column=1,padx=5,pady=5,sticky=E)

            lbl_dato=Label(vindu121,text='oppgi Dato: ')
            lbl_dato.grid(row=1,column=1,padx=5,pady=5,sticky=E)

            lbl_rom=Label(vindu121,text='oppgi Romnr: ')
            lbl_rom.grid(row=2,column=1,padx=5,pady=5,sticky=E)
            

            emnekode=StringVar()
            ent_emnekode=Entry(vindu121,width=10,textvariable=emnekode)
            ent_emnekode.grid(row=0,column=2,padx=5,pady=5,sticky=W)

            dato=StringVar()
            ent_dato=Entry(vindu121,width=10,textvariable=dato)
            ent_dato.grid(row=1,column=2,padx=5,pady=5,sticky=W)

            romnr=StringVar()
            ent_romnr=Entry(vindu121,width=10,textvariable=romnr)
            ent_romnr.grid(row=2,column=2,padx=5,pady=5,sticky=W)

            advarsel=StringVar()
            ent_advarsel=Entry(vindu121,width=30,state='readonly',textvariable=advarsel)
            ent_advarsel.grid(row=7,column=2,padx=5,pady=5,sticky=E)


            btn_save=Button(vindu121,text='Lagre',command=lagre121def)
            btn_save.grid(row=7,column=6,padx=5,pady=25,sticky=E)

            btn_out=Button(vindu121,text='Tilbake',command=vindu121.destroy)
            btn_out.grid(row=7,column=7,padx=5,pady=25,sticky=E)



        
            

        def endre122():
            

            vindu122=Toplevel()
            
            vindu122.title('lagre')

            def endre122def():
                markor122=mindatabase.cursor()
                
                settinnvare122=('''UPDATE EKSAMEN
                                SET emnekode=%s,dato=%s,romnr=%s
                                WHERE emnekode=%s and dato=%s''')
                data_vare122=(emnekode.get(),dato.get(),romnr.get(),emnekodex.get(),datox.get())
                markor122.execute(settinnvare122,data_vare122)
               
                mindatabase.commit()
               
                
                
            lbl_info=Label(vindu122,text='Her skal du oppgi dato og emnekode for å legge oppdatert informasjon i eksamenen du endrer. Viktig alle felt er fylt*')
            lbl_info.grid(row=0,column=2,padx=5,pady=5,sticky=W)

            lbl_emnekode=Label(vindu122,text='oppgi ny Emnekode: ')
            lbl_emnekode.grid(row=1,column=1,padx=5,pady=5,sticky=W)

            lbl_dato=Label(vindu122,text='oppgi ny dato: ')
            lbl_dato.grid(row=2,column=1,padx=5,pady=5,sticky=W)

            lbl_romnr=Label(vindu122,text='oppgi ny romnr: ')
            lbl_romnr.grid(row=3,column=1,padx=5,pady=5,sticky=W)

            lbl_split=Label(vindu122,text='Her skal du oppgi informasjon til å registrere hvilken eksamen du vil endre : ')
            lbl_split.grid(row=4,column=2,padx=5,pady=5,sticky=W)

            lbl_emnekodex=Label(vindu122,text='oppgi emnekode: ')
            lbl_emnekodex.grid(row=5,column=1,padx=5,pady=5,sticky=W)

            lbl_datox=Label(vindu122,text='oppgi dato: ')
            lbl_datox.grid(row=6,column=1,padx=5,pady=5,sticky=W)

            emnekode=StringVar()
            ent_emnekode=Entry(vindu122,width=10,textvariable=emnekode)
            ent_emnekode.grid(row=1,column=2,padx=5,pady=5,sticky=W)

            dato=StringVar()
            ent_dato=Entry(vindu122,width=20,textvariable=dato)
            ent_dato.grid(row=2,column=2,padx=5,pady=5,sticky=W)

            romnr=StringVar()
            ent_romnr=Entry(vindu122,width=20,textvariable=romnr)
            ent_romnr.grid(row=3,column=2,padx=5,pady=5,sticky=W)

            emnekodex=StringVar()
            ent_emnekodex=Entry(vindu122,width=20,textvariable=emnekodex)
            ent_emnekodex.grid(row=5,column=2,padx=5,pady=5,sticky=W)

            datox=StringVar()
            ent_datox=Entry(vindu122,width=19,textvariable=datox)
            ent_datox.grid(row=6,column=2,padx=5,pady=5,sticky=W)

            btn_save=Button(vindu122,text='Lagre',command=endre122def)
            btn_save.grid(row=7,column=6,padx=5,pady=25,sticky=E)

            btn_out=Button(vindu122,text='Tilbake',command=vindu122.destroy)
            btn_out.grid(row=7,column=7,padx=5,pady=25,sticky=E)

        def slette123():
            vindu123=Toplevel()
            vindu123.title('sletting')

            def slette123def():
                markor123=mindatabase.cursor()

                settinnvare123=('''DELETE FROM EKSAMEN
                                WHERE emnekode=%s and dato=%s''')
                data_vare123=(emnekode.get(),dato.get())
                
                markor123.execute(settinnvare123,data_vare123)
                
                
                mindatabase.commit()
                markor123.close()


            lbl_emnekode=Label(vindu123,text='oppgi emnekode')
            lbl_emnekode.grid(row=1,column=1,padx=5,pady=5,sticky=W)

            lbl_dato=Label(vindu123,text='oppgi dato')
            lbl_dato.grid(row=2,column=1,padx=5,pady=5,sticky=W)

            emnekode=StringVar()
            ent_emnekode=Entry(vindu123,width=10,textvariable=emnekode)
            ent_emnekode.grid(row=1,column=2,padx=5,pady=5,sticky=W)

            dato=StringVar()
            ent_dato=Entry(vindu123,width=10,textvariable=dato)
            ent_dato.grid(row=2,column=2,padx=5,pady=5,sticky=W)


            btn_save=Button(vindu123,text='Utfør',command=slette123def)
            btn_save.grid(row=7,column=6,padx=5,pady=25,sticky=E)

            btn_out=Button(vindu123,text='Tilbake',command=vindu123.destroy)
            btn_out.grid(row=7,column=7,padx=5,pady=25,sticky=E)
            


        btn_lagre=Button(vindu12,bg='#0be881',text='Registrer',command=lagre121)
        btn_lagre.grid(row=3,column=0,padx=5,pady=25,sticky=E)
        btn_endre=Button(vindu12,bg='#ffc048',text='Endre',command=endre122)
        btn_endre.grid(row=3,column=3,padx=5,pady=25,sticky=W)
        btn_slette=Button(vindu12,bg='#ff3f34',text='Slette',command=slette123)
        btn_slette.grid(row=3,column=5,padx=5,pady=25,sticky=W)

        
            


        


        btn_avslutt12=Button(vindu12,text='Avslutt',command=vindu12.destroy)
        btn_avslutt12.grid(row=7,column=7,padx=5,pady=25,sticky=E)
        
    


    btn_studenter=Button(vindu1,text='Studenter',command=ajoureholdestudenter)
    btn_studenter.grid(row=3,column=6,padx=5,pady=25,sticky=E)
    btn_eksamen=Button(vindu1,text='Eksamen',command=ajoureholdeeksamen)
    btn_eksamen.grid(row=3,column=1,padx=5,pady=25,sticky=W)
    
    
        
    btn_avslutt1=Button(vindu1,text='Avslutt',command=vindu1.destroy)
    btn_avslutt1.grid(row=7,column=7,padx=5,pady=25,sticky=E)


    




def vindu_2():
    markoremne=mindatabase.cursor()
    vindu2=Toplevel()
    vindu2.title('dagseksamener og rom')

    def vindu_2def1(event):
        valgt=lst_std.get(lst_std.curselection())
        markor=mindatabase.cursor()
        markor.execute('SELECT emnekode,dato,romnr FROM eksamen')
        for row in markor:
            if valgt==row[0]:
                dato.set(row[1])
                romnr.set(row[2])
        markor.close()
    def vindu_2def():
        
        markor2=mindatabase.cursor()
        kode=('''select dato,eksamen.emnekode,rom.romnr,rom.antallplasser
                    from eksamen,rom
                    WHERE dato=%s
                    and rom.romnr=eksamen.romnr''')
        settinn=dato1.get()
        markor2.execute(kode%settinn)
        emnekoder=[]
        for row in markor2:
            emnekoder+=[row[1]]
        innhold_i_lst_emne.set(tuple(emnekoder))
        markor2.close()

            

    def tilbakestill():
        markor=mindatabase.cursor()
        markor.execute('''SELECT emnekode,dato,romnr FROM eksamen''')
        emnekoder=[]
        for row in markor:
            emnekoder+=[row[0]]
              
        innhold_i_lst_emne.set(tuple(emnekoder))
        markor.close()
        
    
       
    markoremne.execute('''SELECT * FROM EKSAMEN''')
    emnekoder=[]
    for row in markoremne:
        emnekoder+=[row[0]]
    innhold_i_lst_emne=StringVar()       
    lst_std=Listbox(vindu2,width=50,height=10,listvariable=innhold_i_lst_emne)
    lst_std.grid(row=0,column=1,rowspan=10,padx=(100,0),pady=5,sticky=E)
    innhold_i_lst_emne.set(tuple(emnekoder))


    
    lbl_dato1=Label(vindu2,text='oppgi dato')
    lbl_dato1.grid(row=0,column=0,padx=5,pady=5,sticky=E)

    dato1=StringVar()
    ent_dato1=Entry(vindu2,width=10,textvariable=dato1)
    ent_dato1.grid(row=1,column=0,padx=5,pady=5,sticky=E)



    lbl_dato=Label(vindu2,text='dato er:')
    lbl_dato.grid(row=0,column=3,padx=5,pady=5,sticky=E)

    lbl_romnr=Label(vindu2,text='romnr er')
    lbl_romnr.grid(row=1,column=3,padx=5,pady=5,sticky=E)

    dato=StringVar()
    ent_dato=Entry(vindu2,width=10,state='readonly',textvariable=dato)
    ent_dato.grid(row=0,column=4,padx=5,pady=5,sticky=W)
    romnr=StringVar()
    ent_romnr=Entry(vindu2,width=10,state='readonly',textvariable=romnr)
    ent_romnr.grid(row=1,column=4,padx=5,pady=5,sticky=W)

    lst_std.bind('<<ListboxSelect>>',vindu_2def1)

    btn_lagre=Button(vindu2,text='Utfør',command=vindu_2def)
    btn_lagre.grid(row=5,column=3,padx=5,pady=5,sticky=W)

    
    btn_avslut2=Button(vindu2,text='Avslutt',command=vindu2.destroy)
    btn_avslut2.grid(row=5,column=5,padx=5,pady=25,sticky=E)
    

    btn_restart=Button(vindu2,text='Tilbakestill',command=tilbakestill)
    btn_restart.grid(row=5,column=4,padx=5,pady=5,sticky=W)

    markoremne.close()


def vindu_3():
    vindu3=Toplevel()
    vindu3.title('Eksamener for tider')
    markoremne=mindatabase.cursor()
    def vindu_3def1(event):
        valgt=lst_std.get(lst_std.curselection())
        markor=mindatabase.cursor()
        markor.execute('SELECT emnekode,dato,romnr FROM eksamen')
        for row in markor:
            if valgt==row[0]:
                dato.set(row[1])
                romnr.set(row[2])
        markor.close()
    def vindu_3def():
        
        markor2=mindatabase.cursor()
        kode=('''select emnekode,dato,romnr
                from eksamen
                WHERE dato BETWEEN %s and %s
                ORDER BY dato ASC''')
        
        settinn=(dato1.get(),dato2.get())
        markor2.execute(kode,settinn)
        emnekoder=[]
        for row in markor2:
            emnekoder+=[row[0]]
        innhold_i_lst_emne.set(tuple(emnekoder))
        markor2.close()

    

    def tilbakestill():
        markor=mindatabase.cursor()
        markor.execute('''SELECT emnekode,dato,romnr FROM eksamen''')
        emnekoder=[]
        for row in markor:
            emnekoder+=[row[0]]
              
        innhold_i_lst_emne.set(tuple(emnekoder))
        markor.close()
        
    
       
    markoremne.execute('''SELECT * FROM EKSAMEN''')
    emnekoder=[]
    for row in markoremne:
        emnekoder+=[row[0]]
    innhold_i_lst_emne=StringVar()       
    lst_std=Listbox(vindu3,width=50,height=10,listvariable=innhold_i_lst_emne)
    lst_std.grid(row=0,column=1,rowspan=10,padx=(100,0),pady=5,sticky=E)
    innhold_i_lst_emne.set(tuple(emnekoder))


    
    lbl_dato1=Label(vindu3,text='oppgi fra dato')
    lbl_dato1.grid(row=0,column=0,padx=5,pady=5,sticky=E)



    dato1=StringVar()
    ent_dato1=Entry(vindu3,width=10,textvariable=dato1)
    ent_dato1.grid(row=1,column=0,padx=5,pady=5,sticky=E)

    dato2=StringVar()
    ent_dato2=Entry(vindu3,width=10,textvariable=dato2)
    ent_dato2.grid(row=3,column=0,padx=5,pady=5,sticky=E)

    lbl_dato2=Label(vindu3,text='oppgi til dato')
    lbl_dato2.grid(row=2,column=0,padx=5,pady=5,sticky=E)



    lbl_dato=Label(vindu3,text='dato er:')
    lbl_dato.grid(row=0,column=3,padx=5,pady=5,sticky=E)

    lbl_romnr=Label(vindu3,text='romnr er')
    lbl_romnr.grid(row=1,column=3,padx=5,pady=5,sticky=E)

    dato=StringVar()
    ent_dato=Entry(vindu3,width=10,state='readonly',textvariable=dato)
    ent_dato.grid(row=0,column=4,padx=5,pady=5,sticky=W)
    romnr=StringVar()
    ent_romnr=Entry(vindu3,width=10,state='readonly',textvariable=romnr)
    ent_romnr.grid(row=1,column=4,padx=5,pady=5,sticky=W)

    lst_std.bind('<<ListboxSelect>>',vindu_3def1)

    btn_lagre=Button(vindu3,text='Utfør',command=vindu_3def)
    btn_lagre.grid(row=5,column=3,padx=5,pady=5,sticky=W)

    
   
    

    btn_restart=Button(vindu3,text='Tilbakestill',command=tilbakestill)
    btn_restart.grid(row=5,column=4,padx=5,pady=5,sticky=W)





    
    btn_avslutt3=Button(vindu3,text='Avslutt',command=vindu3.destroy)
    btn_avslutt3.grid(row=5,column=5,padx=5,pady=25,sticky=E)
    markoremne.close()


    



def vindu_4():
    vindu4=Toplevel()
    vindu4.title('sette karakter')
    markorstudent=mindatabase.cursor()
    markor=mindatabase.cursor()
    markor2=mindatabase.cursor()
    def settekarakter(event):
        
        valgt=lst_std.get(lst_std.curselection())
        
        
        markor.execute('SELECT  studentnr FROM student')
        for row in markor:
            if valgt==row[0]:
                studentnr1.set(row[0])
        
                



    def settekarakter1():
        markorx=mindatabase.cursor()
        kode=('''INSERT INTO eksamensresultat
                VALUES(%s,%s,%s,%s)''')
        settinn=(studentnr1.get(),emne.get(),dato.get(),karakter.get())
        
        markorx.execute(kode,settinn)
        mindatabase.commit()
        markorx.close()
        
        
        
    markorstudent.execute ('''SELECT * FROM student''')
    studentnr=[]
    for row in markorstudent:
        studentnr+=[row[0]]


    y_scroll=Scrollbar(vindu4,orient=VERTICAL)
    y_scroll.grid(row=0,column=2,rowspan=10,padx=(0,100),pady=5,sticky=NS)
    innhold_i_lst_std=StringVar()

    lst_std=Listbox(vindu4,width=50,height=10,listvariable=innhold_i_lst_std,
    yscrollcommand=y_scroll.set)
    lst_std.grid(row=0,column=1,rowspan=10,padx=(100,0),pady=5,sticky=E)
    innhold_i_lst_std.set(tuple(studentnr))
    y_scroll['command']=lst_std.yview


    lbl_dato=Label(vindu4,text='Emnekode')
    lbl_dato.grid(row=0,column=0,padx=5,pady=5,sticky=E)
    lbl_romnr=Label(vindu4,text='Studentnr')
    lbl_romnr.grid(row=1,column=0,padx=5,pady=5,sticky=E)
    lbl_karakter=Label(vindu4,text='Karakter')
    lbl_karakter.grid(row=2,column=0,padx=5,pady=5,sticky=E)
    lbl_Dato=Label(vindu4,text='Dato')
    lbl_Dato.grid(row=3,column=0,padx=5,pady=5,sticky=E)

    emne=StringVar()


    ent_emne=Entry(vindu4,width=10,textvariable=emne)
    ent_emne.grid(row=0,column=1,padx=5,pady=5,sticky=W)
    studentnr1=StringVar()


    ent_dato=Entry(vindu4,width=10,state='readonly',textvariable=studentnr1)
    ent_dato.grid(row=1,column=1,padx=5,pady=5,sticky=W)
    dato=StringVar()
    ent_dato=Entry(vindu4,width=10,textvariable=dato)
    ent_dato.grid(row=3,column=1,padx=5,pady=5,sticky=W)
    karakter=StringVar()


    ent_karakter=Entry(vindu4,width=10,textvariable=karakter)
    ent_karakter.grid(row=2,column=1,padx=5,pady=5,sticky=W)
    lst_std.bind('<<ListboxSelect>>',settekarakter)
    btn_avslutt4=Button(vindu4,text='Avslutt',command=vindu4.destroy)
    btn_avslutt4.grid(row=8,column=6,padx=5,pady=25,sticky=E)
    btn_lagre=Button(vindu4,text='Utfør',command=settekarakter1)
    btn_lagre.grid(row=8,column=4,padx=5,pady=5,sticky=W)
    markorstudent.close()

          
                
       

     
def vindu_5():
                    
    vindu5=Toplevel()
    vindu5.title('eksamensresultat i et emne')
    markorstd=mindatabase.cursor()
    std=[]
    

    def vindu_5def1(event):
        valgt=lst_std.get(lst_std.curselection())
        markor5=mindatabase.cursor()
        
        
        markor5.execute('''SELECT emnekode,dato
                        FROM Eksamensresultat
                        order by studentnr asc''')
        
        
        for row in markor5:
            
            
            if str(valgt[0])== str (row[0]) and str(valgt[1])==str(row[1]):
                
                emnekode.set(row[0])
                dato.set(row[1])
        
                
                
                
    def vindu_5def():
        
        markorx=mindatabase.cursor()
        valgt=lst_std.get(lst_std.curselection())
        std=[]
        kode=('''SELECT studentnr,emnekode,dato,karakter
                FROM Eksamensresultat
                WHERE Emnekode=%s
                and dato=%s
                order by studentnr asc''')
        settinn=(emnekode.get(),dato.get())
        markorx.execute(kode,settinn)

        for row in markorx:
            std+=[row]
            if valgt==row[0]:
                
                studentnr.set(row[0])
                emnekode.set(row[1])
                karakter.set(row[3])
                dato.set(row[2])
        
        
          
                
        innhold_i_lst_std.set(tuple(std))
        markorx.close()
                
        
        
            
    def tilbakestill5():
        markor1=mindatabase.cursor()
        markor1.execute('''SELECT DISTINCT emnekode,dato
                        FROM Eksamensresultat
                        order by studentnr asc''')
        std=[]
        for row in markor1:
            std+=[row]
        innhold_i_lst_std.set(tuple(std))
        markor1.close()
        
        
    
       
    markorstd.execute('''SELECT DISTINCT emnekode,dato
                        FROM Eksamensresultat
                        order by studentnr asc''')
    std=[]
    for row in markorstd:
        std+=[row]
    innhold_i_lst_std=StringVar()       
    lst_std=Listbox(vindu5,width=50,height=10,listvariable=innhold_i_lst_std)
    lst_std.grid(row=0,column=3,rowspan=10,padx=(100,0),pady=5,sticky=E)
    innhold_i_lst_std.set(tuple(std))



    emnekode=StringVar()
    ent_emnekode=Entry(vindu5,width=10,textvariable=emnekode)
    ent_emnekode.grid(row=2,column=1,padx=5,pady=5,sticky=E)

    dato=StringVar()
    ent_dato=Entry(vindu5,width=10,textvariable=dato)
    ent_dato.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    lbl_dato=Label(vindu5,text='Klikk på emnet og dato du ønsker å se karakterer for og klikk deretter utfør:')
    lbl_dato.grid(row=0,column=4,padx=5,pady=5,sticky=W)


    lbl_dato=Label(vindu5,text='dato er:')
    lbl_dato.grid(row=1,column=0,padx=5,pady=5,sticky=E)
    


    lbl_emnekode=Label(vindu5,text='emnekode:')
    lbl_emnekode.grid(row=2,column=0,padx=5,pady=5,sticky=E)



    



    lst_std.bind('<<ListboxSelect>>',vindu_5def1)

    btn_lagre=Button(vindu5,text='Utfør',command=vindu_5def)
    btn_lagre.grid(row=7,column=6,padx=5,pady=5,sticky=W)

    
    btn_avslut2=Button(vindu5,text='Avslutt',command=vindu5.destroy)
    btn_avslut2.grid(row=7,column=8,padx=5,pady=25,sticky=E)
    

    btn_restart=Button(vindu5,text='Tilbakestill',command=tilbakestill5)
    btn_restart.grid(row=7,column=7,padx=5,pady=5,sticky=W)
    markorstd.close()

    


    



def vindu_6():
    
    vindu6=Toplevel()
    vindu6.title('Karakterstatestikk')
    markoremne=mindatabase.cursor()

    def vindu_6def1(event):
        valgt=lst_std.get(lst_std.curselection())
        markor=mindatabase.cursor()
        markor.execute('SELECT DISTINCT emnekode,dato FROM eksamensresultat')
        for row in markor:
            if valgt==row[0]:
                emnekode.set(row[0])
                dato.set(row[1])
        markor.close()
    def vindu_6def():
        
        markora=mindatabase.cursor()
        markorb=mindatabase.cursor()
        markorc=mindatabase.cursor()
        markord=mindatabase.cursor()
        markore=mindatabase.cursor()
        markorf=mindatabase.cursor()
        kodea=('''SELECT distinct emnekode,karakter, count(*) as antallkandidater
                FROM eksamensresultat
                where emnekode=%s
                 and dato=%s
                 and karakter='a'
                order by karakter asc''')
        settinna=(emnekode.get(),dato.get())
        markora.execute(kodea,settinna)
        recordsa=markora.fetchall()
        
        a.set(recordsa[0][2])
        
        kodeb=('''SELECT distinct emnekode,karakter, count(*) as antallkandidater
                FROM eksamensresultat
                where emnekode=%s
                 and dato=%s
                 and karakter='b'
                order by karakter asc''')
        settinnb=(emnekode.get(),dato.get())
        markorb.execute(kodeb,settinnb)
        recordsb=markorb.fetchall()
        
        b.set(recordsb[0][2])

        kodec=('''SELECT distinct emnekode,karakter, count(*) as antallkandidater
                FROM eksamensresultat
                where emnekode=%s
                 and dato=%s
                 and karakter='c'
                order by karakter asc''')
        settinnc=(emnekode.get(),dato.get())
        markorc.execute(kodec,settinnc)
        recordsc=markorc.fetchall()
        
        c.set(recordsc[0][2])


        koded=('''SELECT distinct emnekode,karakter, count(*) as antallkandidater
                FROM eksamensresultat
                where emnekode=%s
                 and dato=%s
                 and karakter='d'
                order by karakter asc''')
        settinnd=(emnekode.get(),dato.get())
        markord.execute(koded,settinnd)
        recordsd=markord.fetchall()
        
        d.set(recordsd[0][2])

        kodee=('''SELECT distinct emnekode,karakter, count(*) as antallkandidater
                FROM eksamensresultat
                where emnekode=%s
                 and dato=%s
                 and karakter='e'
                order by karakter asc''')
        settinne=(emnekode.get(),dato.get())
        markore.execute(kodee,settinne)
        recordse=markore.fetchall()
        
        e.set(recordse[0][2])

        kodef=('''SELECT distinct emnekode,karakter, count(*) as antallkandidater
                FROM eksamensresultat
                where emnekode=%s
                 and dato=%s
                 and karakter='f'
                order by karakter asc''')
        settinnf=(emnekode.get(),dato.get())
        markorf.execute(kodef,settinnf)
        recordsf=markorf.fetchall()
        
        f.set(recordsf[0][2])



        markora.close()
        markorb.close()
        markorc.close()
        markord.close()
        markore.close()
        markorf.close()

            
    def tilbakestill6():
        markor1=mindatabase.cursor()
        markor1.execute('''SELECT DISTINCT emnekode FROM eksamensresultat''')
        emnekodelist=[]
        for row in markor1:
            emnekodelist+=[row[0]]
        markor1.close()
              
        innhold_i_lst_emne.set(tuple(emnekodelist))
        a.set(0)
        b.set(0)
        c.set(0)
        d.set(0)
        e.set(0)
        f.set(0)
        
    
       
    markoremne.execute('''SELECT DISTINCT EMNEKODE FROM EKSAMENsresultat''')
    emnekodelist=[]
    for row in markoremne:
        emnekodelist+=[row[0]]
    innhold_i_lst_emne=StringVar()       
    lst_std=Listbox(vindu6,width=50,height=10,listvariable=innhold_i_lst_emne)
    lst_std.grid(row=0,column=3,rowspan=10,padx=(100,0),pady=5,sticky=E)
    innhold_i_lst_emne.set(tuple(emnekodelist))



    emnekode=StringVar()
    ent_emnekode=Entry(vindu6,width=10,textvariable=emnekode)
    ent_emnekode.grid(row=2,column=1,padx=5,pady=5,sticky=E)



    dato=StringVar()
    ent_dato=Entry(vindu6,width=10,textvariable=dato)
    ent_dato.grid(row=1,column=1,padx=5,pady=5,sticky=W)
    

    lbl_dato=Label(vindu6,text='dato er:')
    lbl_dato.grid(row=1,column=0,padx=5,pady=5,sticky=E)




    lbl_emnekode=Label(vindu6,text='emnekode:')
    lbl_emnekode.grid(row=2,column=0,padx=5,pady=5,sticky=E)


    

    lbl_a=Label(vindu6,text='A')
    lbl_a.grid(row=1,column=5,padx=5,pady=5,sticky=E)

    lbl_b=Label(vindu6,text='B')
    lbl_b.grid(row=2,column=5,padx=5,pady=5,sticky=E)

    lbl_c=Label(vindu6,text='C')
    lbl_c.grid(row=3,column=5,padx=5,pady=5,sticky=E)

    lbl_d=Label(vindu6,text='D')
    lbl_d.grid(row=4,column=5,padx=5,pady=5,sticky=E)

    lbl_e=Label(vindu6,text='E')
    lbl_e.grid(row=5,column=5,padx=5,pady=5,sticky=E)

    lbl_f=Label(vindu6,text='F')
    lbl_f.grid(row=6,column=5,padx=5,pady=5,sticky=E)


    a=StringVar()
    ent_karakter=Entry(vindu6,width=10,state='readonly',textvariable=a)
    ent_karakter.grid(row=1,column=6,padx=5,pady=5,sticky=E)

    b=StringVar()
    ent_karakter=Entry(vindu6,width=10,state='readonly',textvariable=b)
    ent_karakter.grid(row=2,column=6,padx=5,pady=5,sticky=E)

    c=StringVar()
    ent_karakter=Entry(vindu6,width=10,state='readonly',textvariable=c)
    ent_karakter.grid(row=3,column=6,padx=5,pady=5,sticky=E)

    d=StringVar()
    ent_karakter=Entry(vindu6,width=10,state='readonly',textvariable=d)
    ent_karakter.grid(row=4,column=6,padx=5,pady=5,sticky=E)

    e=StringVar()
    ent_karakter=Entry(vindu6,width=10,state='readonly',textvariable=e)
    ent_karakter.grid(row=5,column=6,padx=5,pady=5,sticky=E)

    f=StringVar()
    ent_karakter=Entry(vindu6,width=10,state='readonly',textvariable=f)
    ent_karakter.grid(row=6,column=6,padx=5,pady=5,sticky=E)
    

    lst_std.bind('<<ListboxSelect>>',vindu_6def1)

    btn_lagre=Button(vindu6,text='Utfør',command=vindu_6def)
    btn_lagre.grid(row=7,column=6,padx=5,pady=5,sticky=W)

    
    btn_avslut2=Button(vindu6,text='Avslutt',command=vindu6.destroy)
    btn_avslut2.grid(row=7,column=8,padx=5,pady=25,sticky=E)
    

    btn_restart=Button(vindu6,text='Tilbakestill',command=tilbakestill6)
    btn_restart.grid(row=7,column=7,padx=5,pady=5,sticky=W)

    a.set(0)
    b.set(0)
    c.set(0)
    d.set(0)
    e.set(0)
    f.set(0)

    markoremne.close()


    





def vindu_7():
    
    vindu7=Toplevel()
    vindu7.title('Eksamen i et emne')
    markoremne=mindatabase.cursor()

    def vindu_7def1(event):
        valgt=lst_std.get(lst_std.curselection())
        markor=mindatabase.cursor()
        markor.execute('SELECT studentnr FROM student')
        for row in markor:
            if valgt==row[0]:
                studentnr.set(row[0])
                
        markor.close()
    def vindu_7def():
        
        markor2=mindatabase.cursor()
        markorekstra=mindatabase.cursor()
        kode=('''SELECT distinct dato,Studentnr,eksamensresultat.Emnekode,emne.emnenavn
                ,karakter,emne.Studiepoeng
                FROM Eksamensresultat inner join emne
                on eksamensresultat.emnekode=emne.emnekode 
                where studentnr=%s
                order by dato asc''')
        settinn=studentnr.get()
        markor2.execute(kode%settinn)
        std=[]
        for row in markor2:
            std+=[row]
        innhold_i_lst_std.set(tuple(std))

        kodeekstra=('''select SUM(studiepoeng) as stdpoengg 
                    from eksamensresultat 
                    inner join emne 
                    on eksamensresultat.emnekode=emne.emnekode 
                    where karakter!='F'
                    and studentnr=%s''')
        settinnekstra=studentnr.get()
        markorekstra.execute(kodeekstra%settinnekstra)
        
        for roww in markorekstra:
            stdpoeng.set(roww)
        markor2.close()
        markorekstra.close()

            

    def tilbakestill7():
        markor=mindatabase.cursor()
        markor.execute('''SELECT studentnr FROM student''')
        std=[]
        for row in markor:
            std+=[row[0]]
            stdpoeng.set('0')
        innhold_i_lst_std.set(tuple(std))
        markor.close()
        
    
       
    markoremne.execute('''SELECT studentnr FROM student''')
    std=[]
    for row in markoremne:
        std+=[row[0]]
    innhold_i_lst_std=StringVar()       
    lst_std=Listbox(vindu7,width=50,height=10,listvariable=innhold_i_lst_std)
    lst_std.grid(row=0,column=1,rowspan=10,padx=(100,0),pady=5,sticky=E)
    innhold_i_lst_std.set(tuple(std))
    







    lbl_std=Label(vindu7,text='studentnr er:')
    lbl_std.grid(row=0,column=0,padx=5,pady=5,sticky=E)


    studentnr=StringVar()
    ent_std=Entry(vindu7,width=10,textvariable=studentnr)
    ent_std.grid(row=0,column=1,padx=5,pady=5,sticky=W)




    stdpoeng=StringVar()
    ent_stdpoeng=Entry(vindu7,width=5,state='readonly',textvariable=stdpoeng)
    ent_stdpoeng.grid(row=0,column=4,padx=5,pady=5,sticky=W)

    lbl_stdpoeng=Label(vindu7,text='Totale studiepoeng:')
    lbl_stdpoeng.grid(row=0,column=3,padx=5,pady=5,sticky=E)
    stdpoeng.set('0')



    lst_std.bind('<<ListboxSelect>>',vindu_7def1)

    btn_lagre=Button(vindu7,text='Utfør',command=vindu_7def)
    btn_lagre.grid(row=7,column=3,padx=5,pady=5,sticky=E)

    
    btn_restart=Button(vindu7,text='Tilbakestill',command=tilbakestill7)
    btn_restart.grid(row=7,column=4,padx=5,pady=5,sticky=E)        
        
        
    btn_avslutt7=Button(vindu7,text='Avslutt',command=vindu7.destroy)
    btn_avslutt7.grid(row=7,column=5,padx=5,pady=25,sticky=E)
    markoremne.close()


    



def vindu_8():
    vindu8=Toplevel()
    vindu8.title('Vitnemål')

    markoremne=mindatabase.cursor()

    def vindu_8def1(event):
        valgt=lst_std.get(lst_std.curselection())
        markor=mindatabase.cursor()
        markor.execute('SELECT studentnr FROM student')
        for row in markor:
            if valgt==row[0]:
                studentnr.set(row[0])
                
        markor.close()
    def vindu_8def():
        
        markor2=mindatabase.cursor()
        markorekstra=mindatabase.cursor()
        kode=('''SELECT distinct dato,Studentnr,eksamensresultat.Emnekode,emne.emnenavn
            ,min(karakter),emne.Studiepoeng
            FROM Eksamensresultat inner join emne
            on eksamensresultat.emnekode=emne.emnekode 
            where studentnr=%s
            group by emnekode 
            order by (SELECT SUBSTR(eksamensresultat.emnekode,4,4))asc''')
        settinn=studentnr.get()
        markor2.execute(kode%settinn)
        std=[]
        for row in markor2:
            std+=[row]
        innhold_i_lst_std.set(tuple(std))

        kodeekstra=('''select SUM(studiepoeng) as stdpoengg 
                    from eksamensresultat 
                    inner join emne 
                    on eksamensresultat.emnekode=emne.emnekode 
                    where karakter!='F'
                    and studentnr=%s''')
        settinnekstra=studentnr.get()
        markorekstra.execute(kodeekstra%settinnekstra)
        for roww in markorekstra:
            stdpoeng.set(roww)
        markor2.close()


            

    def tilbakestill8():
        markor=mindatabase.cursor()
        markor.execute('''SELECT studentnr FROM student''')
        std=[]
        for row in markor:
            std+=[row[0]]
              
        innhold_i_lst_std.set(tuple(std))

        markor.close()
        
    markoremne.execute('''SELECT studentnr FROM student''')
    std=[]
    for row in markoremne:
        std+=[row[0]]
    innhold_i_lst_std=StringVar()       
    lst_std=Listbox(vindu8,width=50,height=10,listvariable=innhold_i_lst_std)
    lst_std.grid(row=0,column=1,rowspan=10,padx=(100,0),pady=5,sticky=E)
    innhold_i_lst_std.set(tuple(std))







    lbl_std=Label(vindu8,text='studentnr er:')
    lbl_std.grid(row=0,column=0,padx=5,pady=5,sticky=E)


    studentnr=StringVar()
    ent_std=Entry(vindu8,width=10,textvariable=studentnr)
    ent_std.grid(row=0,column=1,padx=5,pady=5,sticky=W)




    stdpoeng=StringVar()
    ent_stdpoeng=Entry(vindu8,width=5,state='readonly',textvariable=stdpoeng)
    ent_stdpoeng.grid(row=0,column=4,padx=5,pady=5,sticky=W)

    lbl_stdpoeng=Label(vindu8,text='Totale studiepoeng:')
    lbl_stdpoeng.grid(row=0,column=3,padx=5,pady=5,sticky=E)

    lst_std.bind('<<ListboxSelect>>',vindu_8def1)

    btn_lagre=Button(vindu8,text='Utfør',command=vindu_8def)
    btn_lagre.grid(row=7,column=3,padx=5,pady=5,sticky=E)

    
    btn_restart=Button(vindu8,text='Tilbakestill',command=tilbakestill8)
    btn_restart.grid(row=7,column=4,padx=5,pady=5,sticky=E)        
        
    btn_avslutt8=Button(vindu8,text='Avslutt',command=vindu8.destroy)
    btn_avslutt8.grid(row=7,column=5,padx=5,pady=25,sticky=E)
    markoremne.close()


    

root=Tk()
root.title('Hovedvindu')
root.configure(background="cyan")
btn_vindu1=Button(root,text='Ajourholding av eksamen/studenter',command=vindu_1)
btn_vindu1.grid(row=0,column=0,padx=5,pady=5,sticky=W,)

btn_vindu2=Button(root,text='Utskrift av eksamener på en dag',command=vindu_2)
btn_vindu2.grid(row=1,column=0,padx=5,pady=5,sticky=W)

btn_vindu3=Button(root,text='Utskrift av eksamener i en periode',command=vindu_3)
btn_vindu3.grid(row=0,column=1,padx=5,pady=5,sticky=W)

btn_vindu4=Button(root,text='Registrere karakterer',command=vindu_4)
btn_vindu4.grid(row=1,column=1,padx=5,pady=5,sticky=W)

btn_vindu5=Button(root,text='Utskrift av eksamensresultater for et emne',command=vindu_5)
btn_vindu5.grid(row=0,column=2,padx=5,pady=5,sticky=W)

btn_vindu6=Button(root,text='Karakterkstatestikk',command=vindu_6)
btn_vindu6.grid(row=1,column=2,padx=5,pady=5,sticky=W)

btn_vindu7=Button(root,text='Eksamensresultater med emnenavn/dato',command=vindu_7)
btn_vindu7.grid(row=0,column=3,padx=5,pady=5,sticky=W)

btn_vindu8=Button(root,text='Vitnemål',command=vindu_8)
btn_vindu8.grid(row=1,column=3,padx=5,pady=5,sticky=W)

btn_avslutt=Button(root,text='Avslutt',bg='#ff3f34',command=root.destroy)
btn_avslutt.grid(row=5,column=5,padx=5,pady=25,sticky=E)

root.mainloop()
