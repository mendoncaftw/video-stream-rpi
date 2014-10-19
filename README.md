video-stream-rpi
================

Simple **Flask** application for the **Raspberry Pi** that allows you to **stream** from the **camera** to any browser through the **RTMP** protocol.

For the full installation just follow the instructions available at http://www.raspberrypi.org/forums/viewtopic.php?f=43&t=45368.

This solution uses [ffmpeg](https://www.ffmpeg.org/), [crtmpserver](http://www.rtmpd.com/) and both flash players: [jwplayer](http://www.jwplayer.com/) and [strobe media player](http://sourceforge.net/projects/smp.adobe/files/).

*If you wish to access the streams outside of your LAN you need to do some port forwarding on your router and change the RPi's address on both HTML files.*

I decided to provide two different players because while JWPlayer is the recomended one, for me and many other users, it provided some delay that just kept increasing over time, while Strobe Media Player keeps the delay a 1 / 1,5 seconds.

To use this solution you just need to follow the tutorial up until you start *raspivid*. After that just go to the root folder of the Flask project and run:
```
sudo python stream.py
```
Then just open a browser and type your RPi's address followed by the name of the player you wish to use, ex: http://rpi_address/strobemediaplayer
