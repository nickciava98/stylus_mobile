from java.awt.event import KeyEvent
from java.awt import *
from java.awt import Dimension
from java.lang import System
from javax.swing import ImageIcon
from javax.swing import JFrame
from javax.swing import JMenu
from javax.swing import JMenuBar
from javax.swing import JMenuItem
from javax.swing import JPanel
from javax.swing import JButton
from javax.swing.filechooser import FileNameExtensionFilter
from javax.swing import *
from datetime import *
from java.lang import *
from java.util import *
import time
import photoViewer 
import calculator 
import bg 
import pingpong 
import d2048 
import calendarP 
import editor

class PyOS(JFrame):
    fc = JFileChooser("/")
    fc.setFileFilter(FileNameExtensionFilter("Images (*.jpg; *.jpeg; *.bmp; *.dib; *.png; *.jfif; *.jpe; *.gif; *.tif; *.tiff; *.wdp)", ["jpg", "jpeg", "bmp", "dib", "png", "jfif", "jpe", "gif", "tif", "tiff", "wdp"]))
        
    def __init__(self):
       self.initUI()

    def initUI(self):          
        menubar = JMenuBar()
	
        start = JMenu("Start")
        start.setMnemonic(KeyEvent.VK_S)

        apps = JMenu("Applications")
        apps.setPreferredSize(Dimension(200, 35))
        apps.setToolTipText("Stylus Applications")
        web = JMenuItem("Internet", actionPerformed = self.internet)
        web.setPreferredSize(Dimension(200, 35))
        web.setToolTipText("Stylus Web Browser")
        apps.add(web)
        image = JMenuItem("Image Viewer", actionPerformed = self.photos)
        image.setPreferredSize(Dimension(200, 35))
        image.setToolTipText("Stylus Image Viewer")
        apps.add(image)
        start.add(apps)
        
        utility = JMenu("Utility")
        utility.setPreferredSize(Dimension(200, 35))
        utility.setToolTipText("Stylus Utility")
        voice = JMenuItem("Anna", actionPerformed = self.vocal)
        voice.setPreferredSize(Dimension(200, 35))
        voice.setToolTipText("Anna Vocal Assistant")
        utility.add(voice)
        clc = JMenuItem("Calculator", actionPerformed = self.calc)
        clc.setPreferredSize(Dimension(200, 35))
        clc.setToolTipText("Stylus Calculator")
        utility.add(clc)
        fman = JMenuItem("File Manager", actionPerformed = self.file_manager)
        fman.setPreferredSize(Dimension(200, 35))
        fman.setToolTipText("Stylus File Manager")
        utility.add(fman)
        txted = JMenuItem("Notepad", actionPerformed = self.notepad)
        txted.setPreferredSize(Dimension(200, 35))
        txted.setToolTipText("Stylus Notepad")
        utility.add(txted)
        terminal = JMenuItem("Terminal (as root)", actionPerformed = self.lxterminal)
        terminal.setPreferredSize(Dimension(200, 35))
        terminal.setToolTipText("Stylus Terminal")
        utility.add(terminal)
        start.add(utility)
        
        games = JMenu("Games")
        games.setPreferredSize(Dimension(200, 35))
        games.setToolTipText("PyOS Games")
        g1 = JMenuItem("2048", actionPerformed = self.d2048)
        g1.setPreferredSize(Dimension(200, 35))
        g1.setToolTipText("Play 2048 Game")
        games.add(g1)
        
        g2 = JMenuItem("Ping Pong", actionPerformed = self.ppong)
        g2.setPreferredSize(Dimension(200, 35))
        g2.setToolTipText("Play Ping Pong Game")
        games.add(g2)
        
        start.add(games)   
        
        start.addSeparator()    

        exit = JMenuItem("Exit", actionPerformed = self.onExit)
        exit.setPreferredSize(Dimension(200, 35))
        exit.setToolTipText("Stylus Exit")
        start.add(exit)
    
        menubar.add(start)
        
        file = JMenu("File")
        file.setMnemonic(KeyEvent.VK_F)
        
        tk = Toolkit.getDefaultToolkit()
        xSize = (int(tk.getScreenSize().getWidth()))
        ySize = (int(tk.getScreenSize().getHeight()))
        
        self.setSize(xSize, ySize)
        
        filebg = open("/icons/background.txt", "r")
        path = filebg.readline()
        
        filebg.close()
        
        panel2 = bg.background(path, self.getWidth(), self.getHeight() - 100)

        theme = JMenuItem("Change background", actionPerformed = lambda e: self.bg(panel2, e))
        theme.setPreferredSize(Dimension(200, 35))
        theme.setToolTipText("Stylus Background")

        file.add(theme)

        menubar.add(file)
        
        info = JMenu("?")
        info.setMnemonic(KeyEvent.VK_I)

        inf = JMenuItem("Info", actionPerformed = self.onInfo)
        inf.setToolTipText("Stylus Information")

        info.add(inf)

        menubar.add(info)
        
        menubar.add(Box.createHorizontalGlue())
        
        timedate = JMenu(time.strftime("%a, %Y %b %d, %H:%M"))
        timedate.setMnemonic(KeyEvent.VK_C)
        calendar = JMenuItem("Calendar", actionPerformed = self.calendar)
        calendar.setPreferredSize(Dimension(200, 35))
        timedate.add(calendar)
        
        menubar.add(timedate)
        menubar.add(JLabel("  "))
        
        menubar.setPreferredSize(Dimension(200, 35))

        self.setJMenuBar(menubar)

        self.setTitle("Stylus OS")
        self.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        #self.setSize(1360, 768)
        self.setLocationRelativeTo(None)
        
        """time = JPanel()
        time.setBorder(BorderFactory.createEtchedBorder())
        time.setBackground(Color(153, 203, 255))
        time.setLayout(GridLayout(0, 1))
        
        f = Font("", Font.PLAIN, 60)
        t = JLabel("11:51")
        t.setHorizontalAlignment(JLabel.CENTER)
        t.setFont(f)
        time.add(t)
        
        f2 = Font("", Font.PLAIN, 50)
        d = JLabel("Tuesday, 2016/07/12")
        d.setHorizontalAlignment(JLabel.CENTER)
        d.setFont(f2)
        time.add(d)
        
        self.getContentPane().add(time)
        self.add(time, BorderLayout.NORTH)"""
        
        panel = JPanel()
        self.getContentPane().add(panel)
        
        b0 = JButton(ImageIcon("/icons/file-manager.png"), actionPerformed = self.file_manager)
        b0.setToolTipText("File Manager")
        panel.add(b0)
        b1 = JButton(ImageIcon("/icons/internet.png"), actionPerformed = self.internet)
        b1.setToolTipText("Internet")
        panel.add(b1)
        b2 = JButton(ImageIcon("/icons/mail.png"))
        b2.setToolTipText("Mail")
        #panel.add(b2)
        b3 = JButton(ImageIcon("/icons/music.png"))
        b3.setToolTipText("Music")
        #panel.add(b3)
        b4 = JButton(ImageIcon("/icons/video.png"))
        b4.setToolTipText("Video")
        #panel.add(b4)
        b5 = JButton(ImageIcon("/icons/photos.png"), actionPerformed = self.photos)
        b5.setToolTipText("Photos")
        panel.add(b5)
        b6 = JButton(ImageIcon("/icons/calculator.png"), actionPerformed = self.calc)
        b6.setToolTipText("Calculator")
        panel.add(b6)
        b7 = JButton(ImageIcon("/icons/notepad.png"), actionPerformed = self.notepad)
        b7.setToolTipText("Notepad")
        panel.add(b7)
        b8 = JButton(ImageIcon("/icons/settings.png"))
        b8.setToolTipText("Settings")
        #panel.add(b8)
        b9 = JButton(ImageIcon("/icons/trash.png"))
        b9.setToolTipText("Trash")
        #panel.add(b9)
        
        #panel.setBackground(Color(153, 203, 255))
    
        self.add(panel, BorderLayout.SOUTH)
        
        self.getContentPane().add(panel2)
        
        #panel2.setBorder(BorderFactory.createEtchedBorder())
        #panel2.setLayout(GridLayout(0, 1))
        #panel.setLayout(None)
        #panel2.setBackground(Color(153, 203, 255))
        
        #panel2.add(JLabel(ImageIcon("logo.png")))
        
        #panel2.add(JButton("Icon 0"))
        #panel2.add(JButton("Icon 1"))
        #panel2.add(JButton("Icon 2"))
        #panel2.add(JButton("Icon 3"))
        #panel2.add(JButton("Icon 4"))
        #panel2.add(JButton("Icon 5"))
        #panel2.add(JButton("Icon 6"))
        #panel2.add(JButton("Icon 7"))
        #panel2.add(JButton("Icon 8"))
        #panel2.add(JButton("Icon 9"))
        
             
        self.add(panel2)
        
        self.setExtendedState(JFrame.MAXIMIZED_BOTH) 
        self.setUndecorated(True)
        self.setVisible(True)
        
        #Thread.sleep(1000)
        
    def calendar(self, e):
        calendarP.CalendarProgram.main()
        
    def browse(self, path2, e):
        self.fc.setMultiSelectionEnabled(False)
        self.fc.setDialogTitle("Select background" )
        
        if(self.fc.showOpenDialog(self.getContentPane()) == JFileChooser.APPROVE_OPTION):        
            try: 
                path2.setText(self.fc.getSelectedFile().getAbsolutePath())
            
            except:
                print("")
    
    def change(self, path, panel2, e):
        panel2.revalidate()
        
        panel2 = bg.background(path, self.getWidth(), self.getHeight() - 100)
        self.getContentPane().add(panel2)
        
        self.add(panel2)
        
        file = open("/icons/background.txt", "w")
        
        file.write(path)
        file.close()
    
    def bg(self, panel2, e):
        bground = JFrame()
        bground.setTitle("Change Background")
        bground.setDefaultCloseOperation(JFrame.HIDE_ON_CLOSE)
        bground.setSize(350, 100)
        bground.setLocationRelativeTo(None)
        bground.setVisible(True)
        bground.setResizable(False)
        
        panel = JPanel()
        #panel.setBackground(Color(46, 64, 96))
        bground.getContentPane().add(panel)
        
        path = JLabel("File:")
        panel.add(path)
        
        path2 = JTextField()
        path2.setPreferredSize(Dimension(180, 20))
        panel.add(path2)
        
        browse = JButton("Browse file", actionPerformed = lambda e: self.browse(path2, e))
        panel.add(browse)
        
        change = JButton("Change", actionPerformed = lambda e: self.change(path2.getText(), panel2, e))
        panel.add(change)
        
        bground.add(panel)

    def onExit(self, e):
        exit = JFrame()
        exit.setTitle("Exit Stylus")
        exit.setDefaultCloseOperation(JFrame.HIDE_ON_CLOSE)
        exit.setSize(250, 225)
        exit.setLocationRelativeTo(None)
        exit.setVisible(True)
        exit.setResizable(False)
        
        panel = JPanel()
        panel.setBorder(BorderFactory.createEtchedBorder())
        panel.setLayout(GridLayout(0, 1))
        exit.getContentPane().add(panel)
        
        icon1 = ImageIcon("/icons/shutdown.png")        
        poweroff = JButton("Shutdown", icon1, actionPerformed = self.shutdown)
        panel.add(poweroff)
        
        icon2 = ImageIcon("/icons/reboot.png")
        reboot = JButton("  Reboot    ", icon2, actionPerformed = self.reboot)
        panel.add(reboot)
        
        exit.add(panel)
        #System.exit(0)
        
    def onInfo(self, e):
        info = JFrame()
        info.setTitle("Info")
        info.setDefaultCloseOperation(JFrame.HIDE_ON_CLOSE)
        info.setSize(410, 400)
        info.setLocationRelativeTo(None)
        info.setResizable(False)
        info.setVisible(True)
        
        panel = JPanel()
        #panel.setBackground(Color(46, 64, 96))
        #panel.setLayout(GridLayout(0, 2))
        
        logo = JLabel(ImageIcon("/icons/logo.jpg"))
        panel.add(logo)
        
        f = Font("", Font.ITALIC, 40)
        title = JLabel("Stylus OS 1.0 beta")
        title.setFont(f)
        panel.add(title)
        
        info.getContentPane().add(panel)      
        info.add(panel)

    def lxterminal(self, e):
        Runtime.getRuntime().exec("sudo lxterminal")
    
    def autoclean(self, e):
        Runtime.getRuntime().exec("sudo lxterminal --command='sudo apt-get autoclean'")

    def d2048(self, e):
        d2048.Main.main()
    
    def ppong(self, e):
        pingpong.Finestra.main()
    
    def file_manager(self, e):
        Runtime.getRuntime().exec("sudo java -jar /home/stylus/OS/fmanager/jfm.jar")
    
    def internet(self, e):
        Runtime.getRuntime().exec("java -jar /home/stylus/OS/browser/demo/jxbrowserdemo.jar")
    
    def photos(self, e):
        photoViewer.ImageViewer.main()
    
    def vocal(self, e):
        Runtime.getRuntime().exec("sudo lxterminal -e python3.5 /home/stylus/Anna/Anna.py")

    def calc(self, e):
        calculator.calc.main()
    
    def notepad(self, e):
        editor.Main.main()
    
    def shutdown(self, e):
        Runtime.getRuntime().exec("sudo poweroff")
        
    def reboot(self, e):
        Runtime.getRuntime().exec("sudo reboot")

if __name__ == '__main__':
    PyOS()
