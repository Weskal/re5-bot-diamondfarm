import time
import win32gui
import win32con
import win32api
import math
import ctypes
from ctypes import wintypes
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
import ctypes
from ctypes import wintypes

try:
    from pynput.keyboard import Key, Listener, Controller as KeyboardController
    from pynput.mouse import Button, Listener as MouseListener, Controller as MouseController
    PYNPUT_AVAILABLE = True
except ImportError:
    PYNPUT_AVAILABLE = False

try:
    import pyautogui
    PYAUTOGUI_AVAILABLE = True
except ImportError:
    PYAUTOGUI_AVAILABLE = False

def find_re5_window():
    """Encontra especificamente a janela do RE5"""
    def enum_windows_callback(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):
            window_text = win32gui.GetWindowText(hwnd)
            # Busca exata pelo título
            if window_text == "RESIDENT EVIL 5":
                windows.append(hwnd)
        return True
    
    windows = []
    win32gui.EnumWindows(enum_windows_callback, windows)
    return windows[0] if windows else None

def activate_game_window(hwnd):
    """Ativa a janela do jogo de forma mais agressiva"""
    try:
        # Força a janela para frente
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, 
                             win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, 
                             win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        win32gui.SetForegroundWindow(hwnd)
        
        time.sleep(1)
        
        return True
    except:
        return False

def simulate_camera_movement():
    """Versão otimizada - sem ctypes pesado"""
    try:
        # Movimento simples e rápido
        for i in range(30):
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 3, 0, 0, 0)
            time.sleep(0.005)
        
        time.sleep(0.2)
        
        # Movimento circular simples
        hwnd = win32gui.GetForegroundWindow()
        rect = win32gui.GetWindowRect(hwnd)
        center_x = rect[0] + (rect[2] - rect[0]) // 2
        center_y = rect[1] + (rect[3] - rect[1]) // 2
        
        for angle in range(0, 45, 5):
            rad = math.radians(angle)
            offset_x = int(25 * math.cos(rad))
            offset_y = int(25 * math.sin(rad))
            win32api.SetCursorPos((center_x + offset_x, center_y + offset_y))
            time.sleep(0.02)  # Reduzido de 0.05 para 0.02
            
    except Exception as e:
        # Fallback ainda mais simples
        try:
            for i in range(20):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 2, 0, 0, 0)
                time.sleep(0.005)
        except:
            pass

def send_key_2():
    """Envia a tecla 2 usando apenas pynput - versão otimizada"""
    try:
        keyboard = KeyboardController()
        
        # Pressiona e solta a tecla '2'
        keyboard.press('2')
        keyboard.release('2')
        
        print("Tecla 2 enviada!")
        
    except Exception as e:
        print(f"Erro ao enviar tecla 2: {e}")

def disparo():
    """Clique esquerdo mais longo enquanto segura direito"""
    try:
        mouse = MouseController()
        
        print("Iniciando disparo...")
        
        # Pressiona botão direito
        mouse.press(Button.right)
        
        # Clique esquerdo mais longo após 1s
        time.sleep(1.0)
        mouse.press(Button.left)
        time.sleep(0.2)  # Mantém por 200ms (mais tempo)
        mouse.release(Button.left)
        
        # Completa os 3s e solta botão direito
        time.sleep(2.0)
        mouse.release(Button.right)
        
        print("Disparo concluído!")
        
    except Exception as e:
        print(f"Erro no disparo: {e}")

def movimentar(duracao):
    """Movimenta com Shift+W usando apenas pynput"""
    try:
        keyboard = KeyboardController()
        
        print(f"Iniciando movimento por {duracao} segundos...")
        
        # Pressiona as teclas
        keyboard.press('w')
        keyboard.press(Key.shift)
        
        # Mantém pressionado
        time.sleep(duracao)
        
        # Libera as teclas
        keyboard.release(Key.shift)
        keyboard.release('w')
        
        print("Movimento concluído!")
        
    except Exception as e:
        print(f"Erro na movimentação: {e}")

def pressionar_c():
    """Pressiona a tecla C usando múltiplas estratégias com tempo reduzido - VERSÃO OTIMIZADA"""
    try:
        # Estratégia 1: pynput (se disponível)
        if PYNPUT_AVAILABLE:
            keyboard = KeyboardController()
            keyboard.press('c')
            time.sleep(0.025)
            keyboard.release('c')
            time.sleep(0.1)
        
        # Estratégia 2: pyautogui (se disponível)
        if PYAUTOGUI_AVAILABLE:
            pyautogui.press('c')
            time.sleep(0.1)
        
        # Estratégia 3: win32api com código virtual
        win32api.keybd_event(0x43, 0, 0, 0)  # C down (código virtual 0x43)
        time.sleep(0.05)
        win32api.keybd_event(0x43, 0, win32con.KEYEVENTF_KEYUP, 0)  # C up
        time.sleep(0.1)
        
        # Estratégia 4: SendMessage direto para a janela
        hwnd = win32gui.GetForegroundWindow()
        win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x26, 0)
        time.sleep(0.05)
        win32gui.SendMessage(hwnd, win32con.WM_KEYUP, 0x26, 0)
        time.sleep(0.15)
        
        # Estratégia 5: Múltiplas tentativas para garantir
        for _ in range(2):
            win32api.keybd_event(0x26, 0, 0, 0)
            time.sleep(0.02)
            win32api.keybd_event(0x26, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(0.05)
            
    except Exception as e:
        pass

def pressionar_enter_repetido(duracao=3.0):
    """Pressiona Enter repetidamente por X segundos"""
    try:
        start_time = time.time()
        
        while (time.time() - start_time) < duracao:
            # Estratégia 1: pynput (se disponível)
            if PYNPUT_AVAILABLE:
                try:
                    keyboard = KeyboardController()
                    keyboard.press(Key.enter)
                    time.sleep(0.05)
                    keyboard.release(Key.enter)
                except:
                    pass
            
            # Estratégia 2: pyautogui (se disponível)
            if PYAUTOGUI_AVAILABLE:
                try:
                    pyautogui.press('enter')
                except:
                    pass
            
            # Estratégia 3: win32api com código virtual
            win32api.keybd_event(0x0D, 0, 0, 0)  # Enter down (código virtual 0x0D)
            time.sleep(0.05)
            win32api.keybd_event(0x0D, 0, win32con.KEYEVENTF_KEYUP, 0)  # Enter up
            
            # Estratégia 4: SendMessage direto para a janela
            hwnd = win32gui.GetForegroundWindow()
            win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x0D, 0)
            time.sleep(0.05)
            win32gui.SendMessage(hwnd, win32con.WM_KEYUP, 0x0D, 0)
            
            # Pausa entre os pressionamentos
            time.sleep(0.15)
            
    except Exception as e:
        pass

def pressionar_esc():
    """Pressiona a tecla ESC usando múltiplas estratégias - VERSÃO OTIMIZADA"""
    try:
        # Estratégia 1: pynput (se disponível)
        if PYNPUT_AVAILABLE:
            keyboard = KeyboardController()
            keyboard.press(Key.esc)
            time.sleep(0.05)
            keyboard.release(Key.esc)
        
        # Estratégia 2: pyautogui (se disponível)
        if PYAUTOGUI_AVAILABLE:
            pyautogui.press('esc')
        
        # Estratégia 3: win32api com código virtual
        win32api.keybd_event(0x1B, 0, 0, 0)  # ESC down (código virtual 0x1B)
        time.sleep(0.05)
        win32api.keybd_event(0x1B, 0, win32con.KEYEVENTF_KEYUP, 0)  # ESC up
        
        # Estratégia 4: SendMessage direto para a janela
        hwnd = win32gui.GetForegroundWindow()
        win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x1B, 0)
        time.sleep(0.05)
        win32gui.SendMessage(hwnd, win32con.WM_KEYUP, 0x1B, 0)
        time.sleep(0.15)
        
        # Estratégia 5: Múltiplas tentativas para garantir
        for _ in range(2):
            win32api.keybd_event(0x1B, 0, 0, 0)
            time.sleep(0.02)
            win32api.keybd_event(0x1B, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(0.05)
            
    except Exception as e:
        pass

def simulate_camera_movement_left():
    """Versão otimizada - movimento para esquerda sem ctypes pesado"""
    try:
        # Movimento simples e rápido para esquerda
        for i in range(100):
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -8, 0, 0, 0)
            time.sleep(0.005)
        
        # Movimento circular simples para esquerda
        hwnd = win32gui.GetForegroundWindow()
        rect = win32gui.GetWindowRect(hwnd)
        center_x = rect[0] + (rect[2] - rect[0]) // 2
        center_y = rect[1] + (rect[3] - rect[1]) // 2
        
        for angle in range(0, -240, -5):
            rad = math.radians(angle)
            offset_x = int(140 * math.cos(rad))
            offset_y = int(140 * math.sin(rad))
            win32api.SetCursorPos((center_x + offset_x, center_y + offset_y))
            time.sleep(0.02)  # Reduzido de 0.05 para 0.02
            
    except Exception as e:
        # Fallback ainda mais simples
        try:
            for i in range(140):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -8, 0, 0, 0)
                time.sleep(0.005)
        except:
            pass

def pressionar_f():
    """Pressiona a tecla F usando múltiplas estratégias"""
    try:
        # Estratégia 1: pynput (se disponível)
        if PYNPUT_AVAILABLE:
            keyboard = KeyboardController()
            keyboard.press('f')
            time.sleep(0.05)
            keyboard.release('f')
            time.sleep(0.15)
        
        # Estratégia 2: pyautogui (se disponível)
        if PYAUTOGUI_AVAILABLE:
            pyautogui.press('f')
            time.sleep(0.15)
        
        # Estratégia 3: win32api com código virtual
        win32api.keybd_event(0x46, 0, 0, 0)  # F down (código virtual 0x46)
        time.sleep(0.05)
        win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)  # F up
        time.sleep(0.15)
        
        # Estratégia 4: SendMessage direto para a janela
        hwnd = win32gui.GetForegroundWindow()
        win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x46, 0)
        time.sleep(0.05)
        win32gui.SendMessage(hwnd, win32con.WM_KEYUP, 0x46, 0)
        time.sleep(0.15)
        
        # Estratégia 5: Múltiplas tentativas para garantir
        for _ in range(2):
            win32api.keybd_event(0x46, 0, 0, 0)
            time.sleep(0.02)
            win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(0.05)
            
    except Exception as e:
        pass

def pressionar_arrow_up():
    """Pressiona a tecla seta para cima usando múltiplas estratégias"""
    try:
        # Estratégia 1: pynput (se disponível)
        if PYNPUT_AVAILABLE:
            keyboard = KeyboardController()
            keyboard.press(Key.up)
            time.sleep(0.05)
            keyboard.release(Key.up)
            time.sleep(0.15)
        
        # Estratégia 2: pyautogui (se disponível)
        if PYAUTOGUI_AVAILABLE:
            pyautogui.press('up')
            time.sleep(0.15)
        
        # Estratégia 3: win32api com código virtual
        win32api.keybd_event(0x26, 0, 0, 0)  # Arrow Up down (código virtual 0x26)
        time.sleep(0.05)
        win32api.keybd_event(0x26, 0, win32con.KEYEVENTF_KEYUP, 0)  # Arrow Up up
        time.sleep(0.15)
        
        # Estratégia 4: SendMessage direto para a janela
        hwnd = win32gui.GetForegroundWindow()
        win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x26, 0)
        time.sleep(0.05)
        win32gui.SendMessage(hwnd, win32con.WM_KEYUP, 0x26, 0)
        time.sleep(0.15)
        
        # Estratégia 5: Múltiplas tentativas para garantir
        for _ in range(2):
            win32api.keybd_event(0x26, 0, 0, 0)
            time.sleep(0.02)
            win32api.keybd_event(0x26, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(0.05)
            
    except Exception as e:
        pass
  
def pressionar_arrow_down():
    """Pressiona a tecla seta para baixo usando múltiplas estratégias"""
    try:
        # Estratégia 1: pynput (se disponível)
        if PYNPUT_AVAILABLE:
            keyboard = KeyboardController()
            keyboard.press(Key.down)
            time.sleep(0.05)
            keyboard.release(Key.down)
            time.sleep(0.15)
        
        # Estratégia 2: pyautogui (se disponível)
        if PYAUTOGUI_AVAILABLE:
            pyautogui.press('down')
            time.sleep(0.15)
        
        # Estratégia 3: win32api com código virtual
        win32api.keybd_event(0x28, 0, 0, 0)  # Arrow Down down (código virtual 0x28)
        time.sleep(0.05)
        win32api.keybd_event(0x28, 0, win32con.KEYEVENTF_KEYUP, 0)  # Arrow Down up
        time.sleep(0.15)
        
        # Estratégia 4: SendMessage direto para a janela
        hwnd = win32gui.GetForegroundWindow()
        win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x28, 0)
        time.sleep(0.05)
        win32gui.SendMessage(hwnd, win32con.WM_KEYUP, 0x28, 0)
        time.sleep(0.15)
        
        # Estratégia 5: Múltiplas tentativas para garantir
        for _ in range(2):
            win32api.keybd_event(0x28, 0, 0, 0)
            time.sleep(0.02)
            win32api.keybd_event(0x28, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(0.05)
            
    except Exception as e:
        pass

def pressionar_arrow_left():
    """Pressiona a tecla seta para esquerda usando múltiplas estratégias"""
    try:
        # Estratégia 1: pynput (se disponível)
        if PYNPUT_AVAILABLE:
            keyboard = KeyboardController()
            keyboard.press(Key.left)
            time.sleep(0.05)
            keyboard.release(Key.left)
            time.sleep(0.15)
        
        # Estratégia 2: pyautogui (se disponível)
        if PYAUTOGUI_AVAILABLE:
            pyautogui.press('left')
            time.sleep(0.15)
        
        # Estratégia 3: win32api com código virtual
        win32api.keybd_event(0x25, 0, 0, 0)  # Arrow Left down (código virtual 0x25)
        time.sleep(0.05)
        win32api.keybd_event(0x25, 0, win32con.KEYEVENTF_KEYUP, 0)  # Arrow Left up
        time.sleep(0.15)
        
        # Estratégia 4: SendMessage direto para a janela
        hwnd = win32gui.GetForegroundWindow()
        win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x25, 0)
        time.sleep(0.05)
        win32gui.SendMessage(hwnd, win32con.WM_KEYUP, 0x25, 0)
        time.sleep(0.15)
        
        # Estratégia 5: Múltiplas tentativas para garantir
        for _ in range(2):
            win32api.keybd_event(0x25, 0, 0, 0)
            time.sleep(0.02)
            win32api.keybd_event(0x25, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(0.05)
            
    except Exception as e:
        pass  

def main():
    """Executa a sequência completa conforme especificado"""
    hwnd = find_re5_window()
    
    if hwnd:
        if activate_game_window(hwnd):
            # PRIMEIRA PARTE (entrar na fase)
            for i in range(1):
                time.sleep(1)
                pressionar_enter_repetido(1.0)
                time.sleep(1)
                pressionar_enter_repetido(1.0)
                time.sleep(1)
                pressionar_enter_repetido(1.0)
                time.sleep(1)
                pressionar_arrow_down()
                time.sleep(0.5)
                pressionar_arrow_left()
                time.sleep(0.5)
                pressionar_arrow_up()
                time.sleep(1)
                pressionar_enter_repetido(1.0)
                time.sleep(1)
                pressionar_arrow_up()
                time.sleep(1)
                pressionar_enter_repetido(1.0)
                time.sleep(3.0)
                pressionar_esc()
                time.sleep(0.020)  
                
                # SEGUNDA PARTE (Ativar Wesker)
                send_key_2()
                time.sleep(0.020)  
                simulate_camera_movement()  
                time.sleep(1)  
                disparo()  
                time.sleep(1)  
                movimentar(6)  # Era 7 segundos (padrão)
                time.sleep(1)  
                pressionar_esc()  
                #time.sleep(1.5)  
                
                # TERCEIRA PARTE (Correr e pegar diamante)
                time.sleep(1)    
                pressionar_c()
                movimentar(6.0)  # Move com Shift+W por 6 segundos
                pressionar_esc()
                time.sleep(0.2)  
                pressionar_esc()  # Pressiona ESC novamente
                simulate_camera_movement_left()
                movimentar(2.0)  # Move com Shift+W por 2 segundos
                pressionar_f()  
                movimentar(1.0)  # Move com Shift+W por 1 segundo
                pressionar_f()  
                movimentar(2.0)  # Move com Shift+W por 2 segundos
                pressionar_f()  
                time.sleep(0.5)
                pressionar_esc() 
                pressionar_arrow_up()  # Pressiona seta para cima
                pressionar_enter_repetido(3.5)  # Pressiona Enter repetidamente por 3.5 segundos
                
                i = i+1

if __name__ == "__main__":
    main()