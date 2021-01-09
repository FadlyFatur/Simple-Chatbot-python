from nltk.chat.util import Chat, reflections
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog
from PyQt5.uic import loadUi
import sys

class CB (QMainWindow):
    def __init__(self):
        super(CB,self).__init__()
        loadUi('chatbot.ui',self)
        self.kirimButton.clicked.connect(self.ngobrolClicked)
        self.clearButton.clicked.connect(self.clearClicked)

    def clearClicked(self):
        self.listWidget.clear()
        self.listWidget.addItem("Chatbot.v1")

    def ngobrolClicked(self):
        pairs = [
                    [
                        r"hai|hi|hey|hello|Apa Kabar|Ada orang?|apakah ada orang?|hola",
                        ["Hello", "Hey, ada yang bisa dibantu?","Selamat Datang", "Hi, Kaka", "Hi, Apakah ada yang bisa saya bantu?"]
                    ],
                    [
                        r"Dah|Sampai bertemu lagi|Selamat Tinggal|Terima kasih|Trims|Oke",
                        ["Semoga harimu menyenangkan!!!", "Senang berbincang dengan kamu", "Senang bisa membantu"]
                    ],
                    [
                        r"Berapa usiamu?|Berapa umur kamu?|Umur?",
                        ["Usia hanya sebuah angka","Aku robot aku tak mengenal umur", "umur 2 hari", "Umur saya tak terhingga"]
                    ],
                    [
                        r"Siapa Namamu?|Siapa Namamu|Nama",
                        ["Panggil saya Chatbot","Chatbot, itu namaku"]
                    ],
                    [
                        r"Sedang apa?|Nanya|Chatbot",
                        ["Saya disini siap membantu anda"]
                    ],
                    [
                        r"Saya ingin membeli sesuatu|Apa saja yang kamu rekomendasikan?|Mau beli",
                        ["Silahkan pilih : 1. KYT 2. HRC 3. Hiu", "Tergantung kamu ingin helm seperti apa? 1. KYT 2. HRC 3. Hiu", "1. KYT 2. HRC 3. Hiu"]
                    ],
                    [
                        r"Kapan toko mulai buka?|Apakah ini buka?|Berapa lama toko ini buka?",
                        ["Kami buka pukul 7 pagi", "Kami buka dari hari senin hingga senin lagi!", "07.00 sampai 19.00"]
                    ],
                    [
                        r"Berapa harga helm?|Saya mau tau harganya|harga",
                        ["Merk apa kaka?", "Tolong sebutkan merknya :)", "Hmmm tolong sebutkan merknya :)", "mulai dari 50rb anda sudah mendapat helm kaka"]
                    ],
                    [
                        r"Apa ini?",
                        ["Ini adalah layanan chatbot penjualan helm","Saya robot kaka"]
                    ],
                    [
                        r"Merk NHK|NHK",
                        ["Harganya mulai dari Rp.300rb","300rb saja sudah bisa dibeli :)"]
                    ],
                    [
                        r"Merk KYT|KYT",
                        ["Untuk itu harganya 330rb, ukuran berapa?","Cukup 330rb saja, Ukuran berapa?"]
                    ],
                    [
                        r"Merk Hiu|Hiu",
                        ["Itu sangat terjangkau harganya, hanya 50rb, Ukuran berapa?","50rb saja, Ukuran berapa?"]
                    ],
                    [
                        r"Saya ambil itu|ambil itu|mau yang itu|beli yang itu|pesan yang itu|pesan|beli",
                        ["Oke kaka lanjutkan ke pembayaran","Siap :) setelah bayar helm akan langsung dikemas", "Silahkan lanjutkan ke kasir kaka"]
                    ],
                    [
                        r"ukuran(.*)",
                        ["ukuran %1, oke segera dikirim setelah pembayaran :)"]
                    ],
                    [
                        r"(.*)",
                        ["Saya tidak mengerti", "Bisa katakan hal lain?", "Aduh bingung, saya tidak mengerti"]
                    ],
                ]

        chat = Chat(pairs, reflections)
        print('=' * 72)
        s = ""
        while s != "quit":
            s = "quit"
            try:
                inp = self.le.text()
                print(inp)
                # self.ngobrolClicked(inp, None)
                user = "You > "+inp
                self.listWidget.addItem(user)
                s = inp.lower()
            except EOFError:
                print(s)
                self.listWidget.addItem(s)
                # self.ngobrolClicked(None, s)
            if s:
                respond = chat.respond(s)
                print(respond)
                bot = "Bot > " + respond
                # self.ngobrolClicked(respond, None)
                self.listWidget.addItem(bot)
                s = "quit"
        # self.le.setText('')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CB()
    window.setWindowTitle('Chatbot - Bahasa Alamiah')
    window.show()
    sys.exit(app.exec())