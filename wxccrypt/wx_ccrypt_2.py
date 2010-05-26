#!/usr/bin/env python
from wxPython.wx import *
from wxPython.lib.stattext import wxGenStaticText
import os
import gettext
# we want a unique identifiers to associate with each menu
# option. I use the convention of all (menu) identifiers begin
# with 'ID', followed by the menu the option belongs to, then
# the option name. It's a bit wordy, but I like it.
ID_FILE_CRYPT = wxNewId()
ID_FILE_DECRYPT = wxNewId()
ID_FILE_EXIT = wxNewId()
ID_HELP_ABOUT = wxNewId()
ID_LANG_US  = wxNewId()
ID_LANG_CZ =wxNewId()
ID_DIR_CRYPT=wxNewId()
ID_DIR_DECRYPT=wxNewId()
ID_HELP_MANUAL=wxNewId()
ID_OPTION=wxNewId()

[wxID_WXFRAME1, wxID_WXFRAME1BUTTON1, wxID_WXFRAME1BUTTON2, 
 wxID_WXFRAME1BUTTON3, wxID_WXFRAME1BUTTON4, wxID_WXFRAME1GENSTATICTEXT1, 
 wxID_WXFRAME1STATICBOX1, wxID_WXFRAME1STATICBOX2, wxID_WXFRAME1STATICBOX3, 
 wxID_WXFRAME1STATICBOX4, wxID_WXFRAME1STATICTEXT1, wxID_WXFRAME1STATICTEXT2, 
 wxID_WXFRAME1STATICTEXT3, wxID_WXFRAME1STATICTEXT4, wxID_WXFRAME1STATICTEXT5, 
 wxID_WXFRAME1TEXTCTRL1, 
] = map(lambda _init_ctrls: wxNewId(), range(16))
class myFrame(wxFrame):
    def __init__(self, parent, id, title):
        # create a frame for our demo
        wxFrame.__init__(self, parent, id, title)
        self.SetClientSize(wxSize(545, 436))
        # create the 'File' menu, then add the 'open',
        # 'close', and 'exit' options. Notice that we use
        # the identifiers created above to associate an id
        # to each menu item (we will use the id again when
        # we want to 'tell' the program what to do when the
        # user selects a menu item).  We didn't mention
        # the 'AppendSeparator()', but you should be able
        # to figure out what it does :-)
        #
        file_menu = wxMenu()
        file_menu.Append(ID_FILE_CRYPT, 'Crypt File')
        file_menu.Append(ID_FILE_DECRYPT, 'Decrypt File')
        file_menu.AppendSeparator()
        file_menu.Append(ID_DIR_CRYPT, 'crypt directory')
        file_menu.Append(ID_DIR_DECRYPT, 'decrypt directory')
        file_menu.AppendSeparator()
        file_menu.Append(ID_FILE_EXIT, 'Exit Program')
        # create the 'Help' menu
        help_menu = wxMenu()
        help_menu.Append(ID_HELP_ABOUT, 'About')
        help_menu.Append(ID_HELP_MANUAL, 'Manual')
        # we now need a menu bar to hold the 2 menus just created
        menu_bar = wxMenuBar()
      
        pref_menu = wxMenu()
       
        pref_menu.Append(ID_OPTION, 'Options')
        menu_bar.Append(file_menu, 'File')
        menu_bar.Append(pref_menu, "Options")
        menu_bar.Append(help_menu, 'Help')
        
        # set the menu bar (tells the system we're done)
        self.SetMenuBar(menu_bar)
        # that's great! Now let's make the menu options do something!
        # Using EVT_MENU, we associate the identifier for each menu
        # item to a method to be called when the menu item is selected.
        # Most of these items will call the 'ToDo' function; essentially
        # a small stub method to tell the user something will happen,
        # but we have not got around to programming it, yet.
        #
        EVT_MENU(self, ID_FILE_CRYPT, self.file_encrypt)
        EVT_MENU(self, ID_FILE_DECRYPT, self.de_file)
        EVT_MENU(self, ID_FILE_EXIT, self.OnFileExit)
        EVT_MENU(self, ID_HELP_ABOUT, self.ToDo)
        EVT_MENU(self, ID_DIR_CRYPT, self.adr_encrypt)
        EVT_MENU(self, ID_DIR_DECRYPT, self.adr_de_crypt)
        EVT_MENU(self, ID_OPTION, self.ToDo)
        #-----------------------------------------Zacatek -----------------------------------------------
        
        self.button1 = wxButton(id=wxID_WXFRAME1BUTTON1, label='vyber',
              name='button1', parent=self, pos=wxPoint(408, 56), size=wxSize(80,
              22), style=0)
        EVT_BUTTON(self.button1, wxID_WXFRAME1BUTTON1, self.file_encrypt)

        self.staticText1 = wxStaticText(id=wxID_WXFRAME1STATICTEXT1,
              label='vyber s\xfabor  kter\xfd chce\xb9 zakryptovat',
              name='staticText1', parent=self, pos=wxPoint(24, 56),
              size=wxSize(384, 32), style=0)

        self.staticBox1 = wxStaticBox(id=wxID_WXFRAME1STATICBOX1, label='',
              name='staticBox1', parent=self, pos=wxPoint(8, 48),
              size=wxSize(528, 32), style=0)

        self.genStaticText1 = wxGenStaticText(ID=wxID_WXFRAME1GENSTATICTEXT1,
              label='WX CCRYPT v0.2', name='genStaticText1', parent=self,
              pos=wxPoint(152, 8), size=wxSize(202, 27), style=0)
        self.genStaticText1.SetFont(wxFont(24, 77, wxNORMAL, wxBOLD, False,
              'helvetica'))

        self.textCtrl1 = wxTextCtrl(id=wxID_WXFRAME1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wxPoint(8, 272), size=wxSize(528, 136),
              style=wxTE_MULTILINE | wxVSCROLL | wxTE_READONLY, value='')

        self.staticText2 = wxStaticText(id=wxID_WXFRAME1STATICTEXT2,
              label='status', name='staticText2', parent=self, pos=wxPoint(8,
              248), size=wxSize(48, 32), style=0)

        self.staticBox2 = wxStaticBox(id=wxID_WXFRAME1STATICBOX2, label='',
              name='staticBox2', parent=self, pos=wxPoint(9, 183),
              size=wxSize(528, 42), style=0)

        self.staticText3 = wxStaticText(id=wxID_WXFRAME1STATICTEXT3,
              label='vyber adres\xe1r kter\xfd chce\xb9 zakrypovat',
              name='staticText3', parent=self, pos=wxPoint(24, 152),
              size=wxSize(232, 72), style=0)

        self.button2 = wxButton(id=wxID_WXFRAME1BUTTON2, label='vyber',
              name='button2', parent=self, pos=wxPoint(408, 144),
              size=wxSize(80, 22), style=0)
        EVT_BUTTON(self.button2, wxID_WXFRAME1BUTTON2, self.adr_encrypt)

        self.staticBox3 = wxStaticBox(id=wxID_WXFRAME1STATICBOX3, label='',
              name='staticBox3', parent=self, pos=wxPoint(8, 88),
              size=wxSize(528, 40), style=0)

        self.staticText4 = wxStaticText(id=wxID_WXFRAME1STATICTEXT4,
              label='vyber s\xfabor kter\xfd chce\xb9 rozkryptovat',
              name='staticText4', parent=self, pos=wxPoint(24, 104),
              size=wxSize(208, 16), style=0)

        self.button3 = wxButton(id=wxID_WXFRAME1BUTTON3, label='vyber',
              name='button3', parent=self, pos=wxPoint(408, 96), size=wxSize(80,
              22), style=0)
        EVT_BUTTON(self.button3, wxID_WXFRAME1BUTTON3, self.de_file)

        self.staticBox4 = wxStaticBox(id=wxID_WXFRAME1STATICBOX4, label='',
              name='staticBox4', parent=self, pos=wxPoint(8, 136),
              size=wxSize(528, 40), style=0)

        self.staticText5 = wxStaticText(id=wxID_WXFRAME1STATICTEXT5,
              label='vyber adres\xe1r kter\xfd chce\xb9 rozkryptovat',
              name='staticText5', parent=self, pos=wxPoint(21, 194),
              size=wxSize(488, 32), style=0)

        self.button4 = wxButton(id=wxID_WXFRAME1BUTTON4, label='vyber',
              name='button4', parent=self, pos=wxPoint(411, 188),
              size=wxSize(80, 22), style=0)
        EVT_BUTTON(self.button4, wxID_WXFRAME1BUTTON4, self.adr_de_crypt)
        
        
        
    def OnFileExit(self, evt):
        """
        This is executed when the user clicks the 'Exit' option
        under the 'File' menu.  We ask the user if they *really*
        want to exit, then close everything down if they do.
        """
        dlg = wxMessageDialog(self, 'Exit Program?', 'I Need To Know!',
                              wxYES_NO | wxICON_QUESTION)
        if dlg.ShowModal() == wxID_YES:
            dlg.Destroy()
            self.Close(true)
        else:
            dlg.Destroy()
    def ToDo(self, evt):
        """
        A general purpose "we'll do it later" dialog box
        """
        dlg = wxMessageDialog(self, 'Not Yet Implimented!', 'ToDo',
                             wxOK | wxICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
    def file_encrypt2(self, event):
        event.Skip()
        dlg = wxFileDialog(self, "Choose a file", ".", "", "*.*", wxOPEN)
        try:
            if dlg.ShowModal() == wxID_OK:
                filename = dlg.GetPath()
                # Your code
            self.textCtrl1.AppendText("vybral si %s" % filename)
            os.system("xterm  -e ccencrypt %s" % filename)
            konecny= filename + '.cpt'
            self.textCtrl1.AppendText(" \n zakryptoval sem  %s " % konecny)
            self.textCtrl1.AppendText("\n Ukol splnen na 100 %")
        
        finally:
            dlg.Destroy()
    
    
    
    
    
    def decryptujHO(self, filename):
        #funkce decryptuj adresar
        self.textCtrl1.AppendText("\n rozkryptovavam %s" % filename)
        self.textCtrl1.AppendText("\n Budete dotazany na heslo")
        os.system("xterm -e ccdecrypt %s" % filename)
        nazev=filename[:-4]
        self.textCtrl1.AppendText("\n rozkryptoval sem %s" % nazev)
        os.system("tar -xPf %s" % nazev)
        self.textCtrl1.AppendText("\n Ukol splnen na 100%")
        Kde=os.getcwd()
        vypis=os.system("ls -la %s" % Kde)
        self.textCtrl1.AppendText("\n %s" % vypis)
    def decryptujHO2(self, filename):
        self.textCtrl1.AppendText("\n rozkryptovavam %s" % filename)
        self.textCtrl1.AppendText("\n Budete dotazany na heslo")
        os.system("xterm -e ccdecrypt -d %s" % filename)
        #nazev=filename[:-4]
        self.textCtrl1.AppendText("\n rozkryptoval sem %s" % filename)
        #os.system("tar -xvvf %s" % nazev)
        self.textCtrl1.AppendText("\n Ukol splnen na 100%")
        #Kde=os.getcwd()
      #  vypis=os.system("ls -la %s" % Kde)
        #self.textCtrl1.AppendText("\n %s" % vypis)
    def  de_file(self, event):
       
        event.Skip()
        dlg = wxFileDialog(self, "Choose a file", ".", "", "*.cpt", wxOPEN)
        try:
            if dlg.ShowModal() == wxID_OK:
                filename = dlg.GetPath()
                # Your code
                self.textCtrl1.AppendText("vybraly ste %s" % filename)
                dlg = wxMessageDialog(self, 'Chcete rozkryptovat  %s. ??? \n ' % (filename),
                  'Potvrzeni', wxYES_NO | wxICON_INFORMATION)
                try:
                 dlg.ShowModal()
                        
                finally:
                  #dlg.Destroy()
                  if dlg.ShowModal() == wxID_YES:
                         self.decryptujHO2(filename)
        finally:
            dlg.Destroy
        
        
    def cryptujHO(self, dir):
        # metoda zakryptuj adresar priamo funkce
        #print "a sme tu a chceme zakryptovat  %s" %dir
        self.textCtrl1.AppendText("potvril si zakryptovat adresar  %s " % dir)
        nazev= dir + '.tar'
        os.system("tar -cPvf  %s %s" % (nazev, dir))
        os.system("rm -r -f %s" % (dir))
        self.textCtrl1.AppendText("\n zapakoval sem  %s " % nazev)
        os.system("xterm  -e ccencrypt %s" % nazev)
        konecny= nazev + '.cpt'
        self.textCtrl1.AppendText(" \n zakryptoval sem  %s " % konecny)
        self.textCtrl1.AppendText("\n Ukol splnen na 100 %")
    def cryptujHO3(self, dir):
        # metoda zakryptuj adresar priamo funkce
        #print "a sme tu a chceme zakryptovat  %s" %dir
        self.textCtrl1.AppendText("potvril si zakryptovat subor  %s " % dir)
        #nazev= dir + '.tar'
        #os.system("tar -cvvf %s " % (nazev))
        #self.textCtrl1.AppendText("\n zapakoval sem  %s " % nazev)
        os.system("xterm  -e ccencrypt %s" % dir)
        konecny= dir + '.cpt'
        self.textCtrl1.AppendText(" \n zakryptoval sem  %s " % konecny)
        self.textCtrl1.AppendText("\n Ukol splnen na 100 %")
            
    def adr_encrypt(self, event):
        event.Skip()
        dlg = wxDirDialog(self, "Choose a file",  ".")
        try:
            if dlg.ShowModal() == wxID_OK:
                dir = dlg.GetPath()

                self.textCtrl1.AppendText("vybral si adresar %s \n" % dir)
                #kolik = os.popen("du -ch %s" % dir , 'r' ).readline()
                kde=os.getcwd()
                #self.textCtrl1.AppendText("Bude se kryptovat %s" % kolik)
                dlg = wxMessageDialog(self, 'Vybral si adresar %s. \n Vytvoreny zakryptovany subor bude ulozen do \n %s  .\n Opravdu ho chces zakryptovat ? \n' % (dir, kde),
                  'Potvrzeni', wxYES_NO | wxICON_INFORMATION)
                  
                try:
                    dlg.ShowModal()
                    
                finally:
                    if dlg.ShowModal() == wxID_YES:
                        self.cryptujHO(dir)
                    
                           
                    dlg.Destroy()
                
                
                # Your code
        finally:
            dlg.Destroy()
    def file_encrypt(self, event):
        
        event.Skip()
        dlg = wxFileDialog(self)
        try:
            if dlg.ShowModal() == wxID_OK:
                dir = dlg.GetPath()
                self.textCtrl1.AppendText("vybral si subor %s \n" % dir)
               # kolik = os.popen("du -ch %s" % dir , 'r' ).readline()
                kde=os.getcwd()
               # self.textCtrl1.AppendText("Bude se kryptovat %s" % kolik)
                dlg = wxMessageDialog(self, 'Vybral si subor %s. \n Vytvoreny zakryptovany subor bude ulozen do \n %s  .\n Opravdu ho chces zakryptovat ? \n' % (dir, kde),
                  'Potvrzeni', wxYES_NO | wxICON_INFORMATION)
                  
                try:
                    dlg.ShowModal()
                    
                finally:
                    if dlg.ShowModal() == wxID_YES:
                        self.cryptujHO3(dir)
                    
                           
                    dlg.Destroy()
                
                
                # Your code
        finally:
            dlg.Destroy()
   

    def adr_de_crypt(self, event):
        event.Skip()
        dlg = wxFileDialog(self, "Choose a file", ".", "", "*.cpt", wxOPEN)
        try:
            if dlg.ShowModal() == wxID_OK:
                filename = dlg.GetPath()
                # Your code
                self.textCtrl1.AppendText("vybraly ste %s" % filename)
                dlg = wxMessageDialog(self, 'Chcete rozkryptovat  %s. ??? \n ' % (filename),
                  'Potvrzeni', wxYES_NO | wxICON_INFORMATION)
                try:
                 dlg.ShowModal()
                        
                finally:
                  #dlg.Destroy()
                  if dlg.ShowModal() == wxID_YES:
                         self.decryptujHO(filename)
        finally:
            dlg.Destroy

    def konec(self, event):
        event.Skip()

    def OnMenu1Items0Menu(self, event):
        event.Skip()
    def options(self, event):
        event.Skip()  
class myMenuApp(wxApp):
    def OnInit(self):
        frame = myFrame(NULL, -1, 'WX CCRYPT , encrytpt your file or directory')
        
        
        
        
        frame.Show(true)
        self.SetTopWindow(frame)
        return true
##########################################################################
### Test Code ############################################################
##########################################################################
app=myMenuApp(0)
app.MainLoop()
