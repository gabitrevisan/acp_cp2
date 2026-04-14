from processamento import segmentar_roi, detectar_bordas_hough
import cv2

def executar_checkpoint():
    print("🚀 Iniciando Processamento do Checkpoint 2...")

    # --- PROCESSAMENTO IMAGENS 2, 3 e 5 ---
    for img_name in ["img2.png", "img3.png", "img5.jpg"]:
        orig, res = segmentar_roi(img_name)
        cv2.imwrite(f"output_{img_name}", res)
        print(f"✅ {img_name} processada.")

    # --- PROCESSAMENTO IMAGEM 4 (DOIS RESULTADOS) ---
    _, res_flores = segmentar_roi("img4.png", modo="img4_flores")
    cv2.imwrite("output_img4_apenas_flores.png", res_flores)
    
    _, res_folhas = segmentar_roi("img4.png", modo="img4_folhas")
    cv2.imwrite("output_img4_com_folhas.png", res_folhas)
    print("✅ img4 processada (2 versões).")

    # --- PROCESSAMENTO IMAGENS 6 e 7 ---
    for img_name in ["img6.jpg", "img7.jpg"]:
        orig, res = detectar_bordas_hough(img_name)
        cv2.imwrite(f"output_{img_name}", res)
        print(f"✅ {img_name} processada (Hough).")

    print("\n🏁 Processamento concluído! Verifique os arquivos 'output_'.")

if __name__ == "__main__":
    executar_checkpoint()
