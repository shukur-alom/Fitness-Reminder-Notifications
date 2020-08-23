import win10toast,time
def nofiar(massage,icon):
    toaster = win10toast.ToastNotifier()
    toaster.show_toast("IMPORTANT UPDATE",
    massage,icon_path=f"{icon}.ico",
    duration=10)
time.sleep(3)#1800
nofiar("Drink a Glass W#ater",'water')
time.sleep(2)#600
nofiar("Colse Your eye",'eye')
time.sleep(2)#600
nofiar("Exercise for 10 s",'exercise')