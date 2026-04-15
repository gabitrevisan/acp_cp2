from processamento import segmentar_roi, detectar_bordas_hough
import cv2
import os

def executar_checkpoint():
    pasta_input = "imagens"
    pasta_output = "output"

    # Cria a pasta de output se ela não existir
    if not os.path.exists(pasta_output):
        os.makedirs(pasta_output)
        print(f"📁 Pasta '{pasta_output}' criada com sucesso.")

    print("🚀 Iniciando Pipeline do Checkpoint 2...")

    # 1. Processamento das Imagens 2, 3 e 5
    for img_name in ["img2.png", "img3.png", "img5.png"]:
        caminho = os.path.join(pasta_input, img_name)
        _, res = segmentar_roi(caminho)
        if res is not None:
            cv2.imwrite(os.path.join(pasta_output, f"resultado_{img_name}"), res)
            print(f"✅ {img_name} processada.")

    # 2. Imagem 4 (Dois resultados pedidos)
    caminho_4 = os.path.join(pasta_input, "img4.png")
    _, res_flores = segmentar_roi(caminho_4, modo="flores")
    _, res_folhas = segmentar_roi(caminho_4, modo="folhas")
    
    if res_flores is not None:
        cv2.imwrite(os.path.join(pasta_output, "resultado_img4_flores.png"), res_flores)
        cv2.imwrite(os.path.join(pasta_output, "resultado_img4_com_folhas.png"), res_folhas)
        print("✅ img4 processada (2 versões).")

    # 3. Imagens 6 e 7 (Hough)
    for img_name in ["img6.png", "img7.png"]:
        caminho = os.path.join(pasta_input, img_name)
        _, res = detectar_bordas_hough(caminho)
        if res is not None:
            cv2.imwrite(os.path.join(pasta_output, f"resultado_{img_name}"), res)
            print(f"✅ {img_name} processada (Hough).")

    print(f"\n🏁 Finalizado! Verifique os resultados na pasta '{pasta_output}'.")

if __name__ == "__main__":
    executar_checkpoint()