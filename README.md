# docxToPng
Um amigo me pediu pra fazer.

### Como utilizar
1- Baixe a última versão do [Poppler](https://blog.alivate.com.au/poppler-windows/).

2- Descompacte a pasta na pasta raiz do projeto e renomeie-a para apenas "Poppler".

3- Abra o terminal do windows na pasta raiz e crie um ambiente virtual.
```
python -m venv venv
```
4- Digite o comando abaixo para ativar o ambiente virtual.
```
.\venv\scripts\activate
```

5- Instale as dependências no ambiente virtual.
```
pip install -r requirements.txt
```

6- Crie uma pasta chamada input na raiz e adicione os seus arquivos .docx lá.

7- Rode o arquivo main.py no terminal.
```
python main.py
```
8- Abra a pasta output para ver seus arquivos.

Obs.: Caso queira também a versão pdf do documento é só apagar a última linha.
