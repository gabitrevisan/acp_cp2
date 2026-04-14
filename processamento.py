import cv2
import numpy as np

def segmentar_roi(img_path, modo="padrao"):
    img = cv2.imread(img_path)
    if img is None:
        print(f"❌ Erro: Não foi possível carregar {img_path}")
        return None, None
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 1. Equalização para destacar áreas de interesse
    equalized = cv2.equalizeHist(gray)
    
    # 2. Segmentação (Thresholding)
    if "img2" in img_path:
        _, thresh = cv2.threshold(equalized, 250, 255, cv2.THRESH_BINARY)
    elif "img3" in img_path:
        _, thresh = cv2.threshold(equalized, 240, 255, cv2.THRESH_BINARY)
    elif "img4" in img_path:
        limiar = 250 if modo == "flores" else 180
        _, thresh = cv2.threshold(equalized, limiar, 255, cv2.THRESH_BINARY)
    else: # Gato (img5)
        _, thresh = cv2.threshold(equalized, 220, 255, cv2.THRESH_BINARY)

    # 3. Morfologia Matemática (Fechamento)
    kernel = np.ones((5,5), np.uint8)
    morf = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    
    return img, morf

def detectar_bordas_hough(img_path):
    img = cv2.imread(img_path)
    if img is None: return None, None
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    edges = cv2.Canny(blur, 50, 150)
    
    # Hough Probabilístico
    linhas = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)
    
    res = img.copy()
    if linhas is not None:
        for linha in linhas:
            x1, y1, x2, y2 = linha[0]
            cv2.line(res, (x1, y1), (x2, y2), (0, 255, 0), 3)
            
    return img, res
