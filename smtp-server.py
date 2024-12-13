#!/usr/bin/env python3

from aiosmtpd.controller import Controller

class CustomHandler:
    async def handle_DATA(self, server, session, envelope):
        # Print message exactly as you specified
        print("---------- MESSAGE FOLLOWS ----------")
        print(envelope.content.decode('utf-8', errors='ignore'))
        print("------------ END MESSAGE ------------")
        return '250 OK'

def main():
    controller = Controller(CustomHandler(), hostname='0.0.0.0', port=25)
    controller.start()
    
    print("SMTP server started. Waiting for messages...")
    
    try:
        # Keep the server running
        input("Press Enter to stop the server\n")
    except KeyboardInterrupt:
        pass
    finally:
        controller.stop()

if __name__ == '__main__':
    main()
