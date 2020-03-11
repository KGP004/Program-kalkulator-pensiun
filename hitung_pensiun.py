import math
from tkinter import *
from tkinter import messagebox

class MyWindow:
	def __init__(self,win):
		self.lbl1=Label(win, text='Umur Sekarang (misal = 20)')
		self.lbl2=Label(win, text='Umur Pensiun (misal = 45)')
		self.lbl3=Label(win, text='Masa Pensiun (berapa lama durasi penerimaan pembayaran pensiun)')
		self.lbl4=Label(win, text='Suku Bunga (misal = 0.5)')
		self.lbl5=Label(win, text='Besaran (P, pembayaran yang diterima dlm Rp.)')
		self.lbl6=Label(win, text='Berapa kali pembayaran dalam setahun (misal 2 = 6 bulan sekali)')


		#self.lbl7=Label(win, text='Bunga Perbulan')
		#self.lbl8=Label(win, text='Lama Mencicil')
		#self.lbl9=Label(win, text='PA(r,n)')
		#self.lbl10=Label(win, text='P')
		self.lbl11=Label(win, text='Cicilan')
		self.lbl12=Label(win, text='Estimasi Dana Pensiun')
		#self.lbl13=Label(win, text='')
	

		self.t1=Entry()
		self.t2=Entry()
		self.t3=Entry()
		self.t4=Entry()
		self.t5=Entry()
		self.t6=Entry()
		#self.t7=Entry()
		#self.t8=Entry()
		#self.t9=Entry()
		#self.t10=Entry()
		self.t11=Entry()
		self.t12=Entry()
	

		self.btn1 = Button(win, text='Hitung')

		self.lbl1.place(x=100, y=50)
		self.t1.place(x=480, y=50)
		self.lbl2.place(x=100, y=100)
		self.t2.place(x=480, y=100)
		self.lbl3.place(x=100, y=150)
		self.t3.place(x=480, y=150)
		self.lbl4.place(x=100, y=200)
		self.t4.place(x=480, y=200)
		self.lbl5.place(x=100, y=250)
		self.t5.place(x=480, y=250)
		self.lbl6.place(x=100, y=300)
		self.t6.place(x=480, y=300)


		self.b1=Button(win, text='Hitung', command=self.hitung)
		self.b1.place(x=480, y=350)

		#self.lbl7.place(x=100, y=400)
		#self.t7.place(x=480, y=400)
		#self.lbl8.place(x=100, y=450)
		#self.t8.place(x=480, y=450)
		#self.lbl9.place(x=100, y=500)
		#self.t9.place(x=480, y=500)
		#self.lbl10.place(x=100, y=550)
		#self.t10.place(x=480, y=550)
		self.lbl11.place(x=100, y=400)
		self.t11.place(x=480, y=400)
		self.lbl12.place(x=100, y=450)
		self.t12.place(x=480, y=450)

		



	def hitung(self):
		#self.t7.delete(0, 'end')
		#self.t8.delete(0, 'end')
		#self.t9.delete(0, 'end')
		#self.t10.delete(0, 'end')
		self.t11.delete(0, END)
		self.t12.delete(0, END)


		sekarang=int(self.t1.get())
		pensiun=int(self.t2.get())
		masa=int(self.t3.get())
		r=float(self.t4.get())
		besaran=int(self.t5.get())
		m = int(self.t6.get())
		bulan=12
		
		#bunga=r/bulan
		#self.t7.insert(END,str(bunga))

		
		#self.t8.insert(END,str(tahuncicilan))

		#A=1+bunga
		#B=m*masa
		#pa_rn=(1-pow(A,-B))/bunga
		#self.t9.insert(END,str(pa_rn))

		#pokok=besaran*masa*bulan
		#self.t10.insert(END,str(pokok))

		if pensiun>sekarang:
			tahuncicilan=pensiun-sekarang
			bunga=r/bulan
			A=1+bunga
			B=m*tahuncicilan
			pa_rn=(1-pow(A,-B))/bunga
			pokok=besaran*masa*bulan
			tahuncicilan=pensiun-sekarang
			cicil_awal=pokok/pa_rn
			Estimasi_dana_pensiun = cicil_awal * masa * bulan
			self.t11.insert(END,"Rp." + str(cicil_awal))
			self.t12.insert(END,"Rp." + str(Estimasi_dana_pensiun))
		else:
			messagebox.showerror("Eror", "Inputan usia anda salah, mohon inputkan kembali")
			self.t11.insert(END,"Rp." + str(0))
			self.t12.insert(END,"Rp." + str(0))

		#cicil_awal=pokok/pa_rn
		#self.t11.insert(END,"Rp." + str(cicil_awal))

		#Estimasi_dana_pensiun = cicil_awal * masa * bulan
		#self.t12.insert(END,"Rp." + str(Estimasi_dana_pensiun))

	

window=Tk()
mywin=MyWindow(window)
window.title('Hitung Pensiun')
window.geometry("700x700+10+10")
window.mainloop()