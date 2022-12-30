# Display Image & text on I2C driven ssd1306 OLED display 
from machine import Pin, I2C, PWM
from ssd1306 import SSD1306_I2C
from imu import MPU6050
import random
import octitle
import emojis
import framebuf
import machine
import utime
import notes
import math
import freesans20
import writer
from time import sleep
 
modebutton = Pin(14, Pin.IN, Pin.PULL_DOWN)             # modebutton pin with pull-up resistor
actionbutton = Pin(12, Pin.IN, Pin.PULL_DOWN)           # modebutton pin with pull-up resistor 
 
WIDTH  = 128                                            # oled display width
HEIGHT = 64                                             # oled display height
 
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)       # Init I2C using pins GP0 & GP1 (default I2C0 pins)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display
imu = MPU6050(i2c)

buzzer = PWM(Pin(17))
buzzer.freq(500)

blue = Pin(20, Pin.OUT)
red = Pin(22, Pin.OUT)
green = Pin(21, Pin.OUT)

lights = [
    blue,
    red,
    green,
]

def redLight():
    red.on()
    blue.off()
    green.off()

def blueLight():
    red.off()
    blue.on()
    green.off()
    
def greenLight():
    red.off()
    blue.off()
    green.on()
    
def purpleLight():
    red.on()
    blue.on()
    green.off()
    
def tealLight():
    red.off()
    blue.on()
    green.on()
    
def yellowLight():
    red.on()
    blue.off()
    green.on()



song = ["E5","G5","A5","P","E5","G5","B5","A5","P","E5","G5","A5","P","G5","E5"]
song2 = ["A5","C5","D5","P","D5","P","D5","E5","F5","P","F5","P","F5","G5","E5","P","E5","D5","C5","P","C5","D5"]
song3 = ["C4","C4","A4","A4","G4","G4","A4","A4","C4","C4","A4","G4","G4","G4","A4","A4","DS4","DS4","C5","C5","AS5","AS5","C5","C5","DS4","DS4","C5","AS5","AS5","AS5","C4","C4","F4", "F4", "F5", "F5", "DS5", "DS5","F4", "F4", "GS5", "GS5", "F5", "DS5", "DS5", "DS5","F4", "F4","C4","P","C4","P","AS4","C4"]
song4 = ["D4","D4","G4","A5","A5","CS5","CS5","B5","B5","A5","A5","G4","G4","P","G4","D4","D4","A5","A5","P","A5","A5",
         "D4","D4","G4","G4","A5","A5","CS5","CS5","B5","B5","A5","G4","G4","P","G4","G4","CS5","CS5","B5","B5","A5","G4","DS5"]
song5 = ["D4","D4","E4","E4","F4","F4","F4","F4","E4","E4","E4","E4","D4","D4","D4","D4","D4","D4","E4","E4","F4","F4","A5","A5","E4","E4","F4","F4","D4","D4"]

def playtone(frequency):
    buzzer.duty_u16(1000)
    buzzer.freq(frequency)

def bequiet():
    buzzer.duty_u16(0)

def playsong(mysong):
    for i in range(len(mysong)):
        if (mysong[i] == "P"):
            bequiet()
        else:
            playtone(notes.tones[mysong[i]])
        sleep(0.2)
    bequiet()

icons = [
    bytearray(emojis.tile003),
	bytearray(emojis.EightBall),
    bytearray(emojis.coin),
    bytearray(emojis.tetrahedron),
	bytearray(emojis.Hexahedron),
    bytearray(emojis.Octahedron),
    bytearray(emojis.deltohedron),
    bytearray(emojis.Dodecahedron),
	bytearray(emojis.Icosahedron),
	bytearray(emojis.OneHundred),
    bytearray(emojis.coin)
]

obeyTheCube = [
    framebuf.FrameBuffer(bytearray(octitle.obeyCube), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(octitle.obeyCube), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(octitle.obeyCube), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(octitle.obeyCube), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(octitle.obeyCube), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(octitle.obeyCube2), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(octitle.obeyCube4), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(octitle.obeyCube6), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(octitle.obeyCube8), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(octitle.obeyCube8), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(octitle.obeyCube8), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(octitle.obeyCube8), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(octitle.obeyCube8), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(octitle.obeyCube8), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(octitle.obeyCube8), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(octitle.obeyCube8), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(octitle.obeyCube8), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(octitle.obeyCube8), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(octitle.obeyCube8), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(octitle.obeyCube8), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(octitle.obeyCube6), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(octitle.obeyCube4), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(octitle.obeyCube2), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(octitle.obeyCube), 128, 64, framebuf.MONO_HLSB),
]

emojiBits = [
    bytearray(emojis.tile003),
    bytearray(emojis.tile005),
    bytearray(emojis.tile007),
    bytearray(emojis.tile009),
    bytearray(emojis.tile020),
    bytearray(emojis.tile032),
    bytearray(emojis.tile081),
    bytearray(emojis.eggplant)
]

loadBar = [
    framebuf.FrameBuffer(bytearray(emojis.LoadingBar_00001), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(emojis.LoadingBar_00003), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(emojis.LoadingBar_00005), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(emojis.LoadingBar_00007), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(emojis.LoadingBar_00001), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(emojis.LoadingBar_00003), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(emojis.LoadingBar_00005), 128, 64, framebuf.MONO_HLSB),
    framebuf.FrameBuffer(bytearray(emojis.LoadingBar_00007), 128, 64, framebuf.MONO_HLSB)
]

magicEightBall = [
    'As I see it, yes',
    'Ask again later',
    'Better not tell you now',
    'Cannot predict now',
    'Concentrate and ask again',
    'Dont count on it',
    'It is certain',
    'It is decidedly so',
    'Most likely',
    'My reply is no',
    'My sources say no',
    'Outlook good',
    'Outlook not so good',
    'Reply hazy try again',
    'Signs point to yes',
    'Very doubtful',
    'Without a doubt',
    'Yes',
    'Yes, definitely',
    'You may rely on it',
    'Beware of small children',
    'Doesnt matter cuz you are lookin fine!',
]


mode = [
    'Mood',
    'Magic 8 Ball',
    'D2-Coin Flip',
    'D4-Tetrahedron',
    'D6-Hexahedron',
    'D8-Octahedron',
    'D10-Deltohedron',
    'D12-Dodecahedron',
    'D20-Icosahedron',
    'D100-Zocchihedron'
]

def prettyEightBall(msg):
    theMessage = list(msg)
    firstString = theMessage[:15]
    firstMessage = ''
    for x in firstString:
        firstMessage += x
    secondString = theMessage[15:28]
    secondMessage = ''
    for y in secondString:
        secondMessage += y
    thirdString = theMessage[28:41]
    thirdMessage = ''
    for z in thirdString:
        thirdMessage += z
    fourthString = theMessage[41:54]
    fourthMessage = ''
    for w in fourthString:
        fourthMessage += w
    fifthString = theMessage[41:54]
    fifthMessage = ''
    for v in fifthString:
        fifthMessage += v
    oled.fill(0)
    oled.text(modeText, 0, 0)
    oled.text(firstMessage, 0, 25)
    oled.text(secondMessage, 0, 35)
    oled.text(thirdMessage, 0, 45)
    oled.text(fourthMessage, 0, 55)
    oled.show()


modeNum = 9
modeText = str(mode[modeNum])

loadBarLength = len(loadBar)
magicEightBallLength = len(magicEightBall)
emojiBitsLength = len(emojiBits)

randomEmoji = random.randrange(0, emojiBitsLength)
thisEmoji = bytearray(emojiBits[randomEmoji])
emojiIcon = framebuf.FrameBuffer(thisEmoji, 96, 48, framebuf.MONO_HLSB)

greenLight()

def blk():
    oled.fill(0)
    oled.show()

for image in obeyTheCube:
    oled.fill(0)
    oled.blit(image, 0, 0)
    oled.show()

playsong(song5)

while True:
    if modebutton.value():
        if modeNum < 9:
            modeNum +=1
            modeText = str(mode[modeNum])
            thisIcon = bytearray(icons[modeNum])
            modeIcon = framebuf.FrameBuffer(thisIcon, 96, 48, framebuf.MONO_HLSB)
            oled.fill(0)
            oled.blit(modeIcon, 0, 15)
            oled.text(modeText, 0, 0)
            oled.show()
            if modeNum == 1:
                blueLight()
            elif modeNum == 2:
                redLight()
            elif modeNum == 3:
                purpleLight()
            elif modeNum == 4:
                yellowLight()
            elif modeNum == 5:
                tealLight()
            elif modeNum == 6:
                purpleLight()
            elif modeNum == 7:
                yellowLight()
            elif modeNum == 8:
                tealLight()
            elif modeNum == 9:
                purpleLight()
            elif modeNum == 10:
                yellowLight()
            else:
                greenLight()
        else:
            greenLight()
            modeNum = 0
            modeText = str(mode[modeNum])
            thisIcon = bytearray(icons[modeNum])
            modeIcon = framebuf.FrameBuffer(thisIcon, 96, 48, framebuf.MONO_HLSB)
            oled.fill(0)
            oled.blit(modeIcon, 0, 15)
            oled.text(modeText, 0, 0)
            oled.show()
        sleep(.5)
        
    if (abs(imu.accel.x) > 0.75 and abs(imu.gyro.x) > 5) or (abs(imu.accel.y) > 0.75 and abs(imu.gyro.y) >5):
        for loadFrame in loadBar:
            oled.fill(0)
            oled.blit(loadFrame, 0, 0)
            oled.show()
            for color in lights:
                color.toggle()
                sleep(.025)
                color.toggle()
                sleep(.025)
        if modeNum == 0:
            greenLight()
            randomEmoji = random.randrange(0, emojiBitsLength)
            thisEmoji = bytearray(emojiBits[randomEmoji])
            emojiIcon = framebuf.FrameBuffer(thisEmoji, 96, 48, framebuf.MONO_HLSB)
            modeText = str(mode[modeNum])
            oled.fill(0)
            oled.blit(emojiIcon, 0, 15)
            oled.text(modeText, 0, 0)
            oled.show()
        elif modeNum == 1:
            blueLight()
            randomEightBall = random.randrange(0, magicEightBallLength)
            msg = str(magicEightBall[randomEightBall])
            prettyEightBall(msg)

        elif modeNum == 2:
            redLight()
            def randomNum():
                return str(random.randrange(1, 3))
            modeText = str(mode[modeNum])
            font_writer = writer.Writer(oled, freesans20)
            oled.fill(0)
            font_writer.set_textpos(45, 40)
            font_writer.printstring(randomNum())
            oled.text(modeText, 0, 0)
            oled.show()
        elif modeNum == 3:
            purpleLight()
            def randomNum():
                return str(random.randrange(1, 5))
            modeText = str(mode[modeNum])
            font_writer = writer.Writer(oled, freesans20)
            oled.fill(0)
            font_writer.set_textpos(45, 40)
            font_writer.printstring(randomNum())
            oled.text(modeText, 0, 0)
            oled.show()
        elif modeNum == 4:
            yellowLight()
            def randomNum():
                return str(random.randrange(1, 7))
            modeText = str(mode[modeNum])
            font_writer = writer.Writer(oled, freesans20)
            oled.fill(0)
            font_writer.set_textpos(45, 40)
            font_writer.printstring(randomNum())
            oled.text(modeText, 0, 0)
            oled.show()
        elif modeNum == 5:
            tealLight()
            def randomNum():
                return str(random.randrange(1, 9))
            modeText = str(mode[modeNum])
            font_writer = writer.Writer(oled, freesans20)
            oled.fill(0)
            font_writer.set_textpos(45, 40)
            font_writer.printstring(randomNum())
            oled.text(modeText, 0, 0)
            oled.show()
        elif modeNum == 6:
            purpleLight()
            def randomNum():
                return str(random.randrange(1, 11))
            modeText = str(mode[modeNum])
            font_writer = writer.Writer(oled, freesans20)
            oled.fill(0)
            font_writer.set_textpos(45, 40)
            font_writer.printstring(randomNum())
            oled.text(modeText, 0, 0)
            oled.show()
        elif modeNum == 7:
            yellowLight()
            def randomNum():
                return str(random.randrange(1, 13))
            modeText = str(mode[modeNum])
            font_writer = writer.Writer(oled, freesans20)
            oled.fill(0)
            font_writer.set_textpos(45, 40)
            font_writer.printstring(randomNum())
            oled.text(modeText, 0, 0)
            oled.show()
        elif modeNum == 8:
            tealLight()
            def randomNum():
                return str(random.randrange(1, 21))
            modeText = str(mode[modeNum])
            font_writer = writer.Writer(oled, freesans20)
            oled.fill(0)
            font_writer.set_textpos(45, 40)
            font_writer.printstring(randomNum())
            if int(randomNum()) > 9:
                oled.rect(33, 33, 55, 30, 1)
            else:
                oled.rect(33, 33, 33, 30, 1)
                oled.text(modeText, 0, 0)
                oled.text(modeText, 0, 0)
            oled.show()
        elif modeNum == 9:
            purpleLight()
            def randomNum():
                return str(random.randrange(1, 101))
            modeText = str(mode[modeNum])
            font_writer = writer.Writer(oled, freesans20)
            oled.fill(0)
            font_writer.set_textpos(45, 40)
            font_writer.printstring(randomNum())
            oled.text(modeText, 0, 0)
            oled.show()
        sleep(.5)
        