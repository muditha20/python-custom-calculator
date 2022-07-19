import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QWidget
from PyQt5 import uic 
import linecache

class Dialog(QDialog):
    def __init__(self): 
        super().__init__()
        uic.loadUi("gui.ui", self)
        self.cal.clicked.connect(self.cement_cal)  
        self.save_button.clicked.connect(self.save_in)
        self.read_data()
#==========================================write data=========================================================       
    def save_in(self):
        s_text = self.sand_in.text()
        m_text = self.Metal_in.text()
        ce_text = self.Cement_in.text()
        print(str(s_text))
        data_file=open('data.txt',"w")
        data_file.write(str(s_text)+"\n")
        data_file.write(str(m_text)+"\n")
        data_file.write(str(ce_text))
        data_file.close()
        
#===========================================Text data get====================================================  
    def read_data(self):
        try:   
            self.sand_r=linecache.getline("data.txt",1)
            self.metal_r=linecache.getline("data.txt",2)
            self.cement_r=linecache.getline("data.txt",3)
                      
        except:
            self.cement.setText("00")
            self.sand.setText("00")
            self.metal.setText("00")
            self.metal_2.setText("00")
            self.sand_2.setText("00")
            
#============================================cement cal button==============================================
    def cement_cal(self):
        load_txt_cem=self.cement_r
        load_txt_met=self.metal_r
        load_txt_san=self.sand_r
    
        try:  
            input_int=int(self.input.text())      
            cem=round((input_int*int(load_txt_cem)/1000),2)
            san=round((input_int*int(load_txt_san)/1000),2)
            met=round((input_int*int(load_txt_met)/1000),2)         
            san_cu=round(san/2.8,2)
            met_cu=round(met/2.8,2)

            self.cement.setText(str(cem))
            self.sand.setText(str(san))
            self.metal.setText(str(met))
            self.metal_2.setText(str(met_cu))
            self.sand_2.setText(str(san_cu))
        except:    
            self.cement.setText("Please enter numbers only")
            self.sand.setText("Please enter numbers only")
            self.metal.setText("Please enter numbers only")
            self.metal_2.setText("Please enter numbers only")
            self.sand_2.setText("Please enter numbers only")
        #===============================================display=====================================================        

if __name__ == '__main__':
    caldia = QApplication(sys.argv)

    demo = Dialog()
    demo.show()

    try:
        sys.exit(caldia.exec_())
    except SystemExit:
        print("closing window")

      


