from processamento import segmentar_roi, detectar_bordas_hough
import cv2
import os

def executar_checkpoint():
    # Caminho da pasta de imagens
    pasta_input = "imagens"
    
    print("🚀 Iniciando Pipeline do Checkpoint 2...")

    # 1. Processamento das Imagens 2, 3 e 5
    for img_name in ["img2.png", "img3.png", "img5.jpg"]:
        caminho = os.path.join(pasta_input, img_name)
        _, res = segmentar_roi(caminho)
        if res is not None:
            cv2.imwrite(f"output_{img_name}", res)
            print(f"✅ {img_name} processada.")

    # 2. Imagem 4 (Os dois resultados pedidos no PDF)
    caminho_4 = os.path.join(pasta_input, "img4.png")
    _, res_flores = segmentar_roi(caminho_4, modo="flores")
    _, res_folhas = segmentar_roi(caminho_4, modo="folhas")
    
    if res_flores is not None:
        cv2.imwrite("output_img4_apenas_flores.png", res_flores)
        cv2.imwrite("output_img4_com_folhas.png", res_folhas)
        print("✅ img4 processada (2 versões).")

    # 3. Imagens 6 e 7 (Hough)
    for img_name in ["img6.jpg", "img7.jpg"]:
        caminho = os.path.join(pasta_input, img_name)
        _, res = detectar_bordas_hough(caminho)
        if res is not None:
            cv2.imwrite(f"output_{img_name}", res)
            print(f"✅ {img_name} processada (Hough).")

    print("\n🏁 Finalizado! Resultados salvos na raiz do projeto.")

if __name__ == "__main__":
    executar_checkpoint()
