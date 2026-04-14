# Checkpoint 2 - Visão Computacional 👁️

## 📌 Descrição do Projeto
Este projeto consiste em um pipeline de processamento de imagem para segmentação e destaque de Regiões de Interesse (ROI) em diferentes contextos (médico, botânico e eletrônico). O sistema utiliza técnicas de equalização histogrâmica, segmentação por limiarização e morfologia matemática para isolar elementos específicos, além de detecção de bordas e linhas para identificação de componentes de hardware.

## Autores - 4ESPW
- Breno Silva (RM99275)
- Gabriela Trevisan (RM99500)

## 🧠 Parte Conceitual (CP2)

### 1. Qual o papel da equalização histogrâmica neste pipeline?
A equalização aumenta o contraste global da imagem, distribuindo melhor as intensidades dos pixels. Isso é fundamental para destacar regiões de interesse que possuem brilho similar ao fundo, como a lesão na imagem 3 ou as pétalas na imagem 4, facilitando a segmentação posterior.

### 2. Como a morfologia auxilia no isolamento das ROIs?
Operações como o fechamento (`MORPH_CLOSE`) são usadas para eliminar ruídos internos e conectar partes de uma mesma estrutura que foram fragmentadas durante a segmentação. No caso da calota craniana (img 2) ou do gato (img 5), ela garante que a máscara final seja sólida e contínua.

### 3. Por que utilizar a Transformada de Hough nas imagens 6 e 7?
Diferente da segmentação por cor, a Transformada de Hough busca padrões geométricos (linhas). Para as placas de vídeo, isso permite projetar as bordas externas de forma precisa, identificando o formato retangular dos componentes mesmo com fundos complexos.

### 4. Cenário Real de Aplicação
Este sistema de segmentação pode ser aplicado no **Auxílio ao Diagnóstico Médico por Imagem**. Algoritmos que isolam automaticamente lesões (como na img 3) ou estruturas ósseas (img 2) ajudam radiologistas a identificar anomalias com maior rapidez e precisão diagnóstica.

## 🚀 Como Executar
1. Instale as dependências: `pip install opencv-python numpy`
2. Garanta que as imagens `img2` a `img7` estejam na raiz do projeto.
3. Execute o arquivo principal:

   ```bash
   python main.py

---

## 🛠️ Tecnologias Utilizadas
- Python 3.x
- OpenCV (Processamento de Imagem)
- NumPy (Manipulação de Matrizes)
