import cv2
import numpy as np

def segmentar_roi(img_path, modo="padrao"):
    """
    Pipeline para Imagens 2, 3, 4 e 5: 
    Equalização + Segmentação + Morfologia.
    """
    img = cv2.imread(img_path)
    if img is None: return None
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 1. Equalização para destacar áreas claras (ROIs)
    equalized = cv2.equalizeHist(gray)
    
    # 2. Segmentação (Thresholding) ajustada por imagem
    if "img2" in img_path: # Borda TC
        _, thresh = cv2.threshold(equalized, 250, 255, cv2.THRESH_BINARY)
    elif "img3" in img_path: # Lesão
        _, thresh = cv2.threshold(equalized, 240, 255, cv2.THRESH_BINARY)
    elif "img4_flores" in modo: # Apenas flores brancas
        _, thresh = cv2.threshold(equalized, 250, 255, cv2.THRESH_BINARY)
    elif "img4_folhas" in modo: # Flores + Folhas
        _, thresh = cv2.threshold(equalized, 180, 255, cv2.THRESH_BINARY)
    else: # Gato (img5)
        _, thresh = cv2.threshold(equalized, 220, 255, cv2.THRESH_BINARY)

    # 3. Morfologia para limpar ruído e fechar a ROI
    kernel = np.ones((5,5), np.uint8)
    morf = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    
    return img, morf

def detectar_bordas_hough(img_path):
    """
    Pipeline para Imagens 6 e 7: Canny + Hough para as GPUs.
    """
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Redução de ruído e Canny
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    edges = cv2.Canny(blur, 50, 150)
    
    # Transformada de Hough Probabilística
    linhas = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)
    
    res = img.copy()
    if linhas is not None:
        for linha in linhas:
            x1, y1, x2, y2 = linha[0]
            cv2.line(res, (x1, y1), (0, 255, 0), 3) # Linha Verde
            
    return img, res
