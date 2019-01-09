import socket
import pygame
from pygame.locals import *

def client_conn():
    
    ## Initialize socket
    bot_ip = "192.168.4.1"
    port = 8080
    
    try:
        print("[+] Attempting conn to bot: " + bot_ip)
        sock = socket.socket()
        sock.connect((bot_ip,port))
        print("[+] Connection to bot successful!")
        return sock
    except:
        print("[-] Connection to bot terminated.")
        
def main():
    
    ## Initialize pygame/screen
    pygame.init()
    dispWH = (1280,720)
    
    gameDisplay = pygame.display.set_mode(dispWH)
    pygame.display.set_caption("Treadwell Client")
    
    clock = pygame.time.Clock()
    
    ## Get bot connection
    print("in")
    conn = client_conn()
    print("out")
    
    ## Control loop
    
    ## Part 1 sends a command to the server
    ## Part 2 parses the response
    ## Part 3 will update the screen
    
    done = False
    key_stack = []
    
    keyReleased = True

    
    while not done:
        print(key_stack)
        message = "idle"
        ## Part 1 - Send command
        ## Update the stack
        for event in pygame.event.get():
            
            ## Quit
            if event.type == QUIT:
                done = True
                message = "quit"
                conn.send(message.encode('utf-8'))
                conn.close()
                pygame.quit()
                sys.exit()
                
            ## Add to stack
            elif event.type == KEYDOWN:
                keyReleased = False
                
                key_stack.append(event.key)
                
            ## Remove from stack
            elif event.type == KEYUP:
                if event.key in key_stack:
                    key_stack.pop(key_stack.index(event.key))
         
        ## Define message
        if key_stack:
            ## Speed control
            if key_stack[-1] == K_UP:
                message = "speed_up"
            elif key_stack[-1] == K_DOWN:
                message = "speed_down"
                
            ## Stop movement
            elif key_stack[-1] == K_SPACE:
                message = "stop"
            
            ## Movement control
            elif key_stack[-1] == K_w:
                message = "forward"
            elif key_stack[-1] == K_s:
                message = "backward"
            elif key_stack[-1] == K_a:
                message = "rot_left"
            elif key_stack[-1] == K_d:
                message = "rot_right"
                
            ## Quitting
            elif key_stack[-1] == K_q:
                message = "quit"
                
            else:
                message = "idle"
                
        ## Send the message
        conn.send(message.encode('utf-8'))
        
        ## Part 2 - Parse Response
        response = conn.recv(1024).decode('utf-8')
        print(response) # Currently the speed of the robot
        
        ## Part 3 - Update the Screen
                
            
                    
if __name__ == '__main__':     
    main()                    
                    
            
            
            
            
                
                
                
                
            
            
            
            
            
            
    
    
    
    
    
    
    
    
    
    