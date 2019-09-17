#   --------------------------------------------------------------------------   #
#   -                          CLASSE EXCLUSIVA PARA FUNÇÕES DE USO GERAL    -   #
#   --------------------------------------------------------------------------   #
from util.collection import *

class funcoesGlobais():
    
    def PegaCaminhoRelativo(self, caminho):
        #observação: o caminho q for passado deve estar com as barras iguais as de data, ou seja, para a direita
        #import glob
        globei = glob.glob(caminho, recursive=True)
        for i in globei:
            return(i)
    # PegaCaminhoRelativo
    
    def RemoveAcentos(self, palavra):
        #No terminal de o comando...   pip install unidecode
        #fazer a importação...         from unidecode import unidecode
        return unidecode(palavra)
    # RemoveAcentos
    
    def GeraLog(self, caminhoDoLog, nomeDoArquivo, valorAInserir = ''):
        if(valorAInserir != ''):    
            #cria o diretorio 
            if(self.CriaDiretorio(caminhoDoLog.strip()) == False):
                return False
            #cria o arquivo 
            try:
                try:
                    insere = open(caminhoDoLog + '/' + nomeDoArquivo, 'a')
                    
                    #inserir valor no arquivo
                    insere.writelines( valorAInserir.strip() + '\n')
                finally:
                    insere.close()
            except Exception:
                return False
            return True
        else:
            return False
    # GeraLog
    
    def VerificaDiretorioExiste(self, caminhoDiretorio=""):
        #fazer a importação...         import os
        if(r"{}".format(caminhoDiretorio.strip()) != ""):
            if(os.path.isdir(caminhoDiretorio.strip()) == True):
                return True
        return False
    # VerificaDiretorioExiste
       
    def VerificaArquivoExiste(self, caminhoArquivo=""):
        #fazer a importação...         import os
            if(r"{}".format(caminhoArquivo.strip()) != ""):
                if(os.path.isfile(caminhoArquivo.strip()) == True):
                    return True
            return False
    # VerificaArquivoExiste
    
    def ListarArquivosNoDiretorio(self, caminhoDiretorio, optionalExtensaoDoArquivo = ''):
        arquivos = []
        if(self.VerificaDiretorioExiste(caminhoDiretorio)== True):
            
            #esse if traz todos os arquivos que existirem no diretório e nos subdiretórios do mesmo
            if(optionalExtensaoDoArquivo == ""):
                for p, _, files in os.walk(os.path.abspath(caminhoDiretorio)):
                    for file in files:
                        arquivos.append(os.path.join(p, file))
                        
            #esse else traz apenas os arquivos que contém exatamente a mesma extensão passada por parametro
            else:
                for p, _, files in os.walk(os.path.abspath(caminhoDiretorio)):
                    for file in files:
                        extensaoDoArquivo = file[file.index("."):len(str(file))]
                        if(optionalExtensaoDoArquivo in str(file) and len(optionalExtensaoDoArquivo) == len(str(extensaoDoArquivo)) ):
                            arquivos.append(os.path.join(p, file))
        else:
            return "Diretório Inválido"
        return arquivos
    # ListarArquivosNoDiretorio
    
    def CriaDiretorio(self, caminhoDiretorio = ""):
        if(caminhoDiretorio.strip() != ""):
            if(self.VerificaDiretorioExiste(caminhoDiretorio.strip()) != True):
                
                #tentando criar um diretório...
                try:
                    os.mkdir(caminhoDiretorio.strip());
                    
                #caso não consiga retorna uma mensagem de erro
                except:
                    raise Exception ("Processo de criação do diretorio " + caminhoDiretorio.strip() + " falhou.")
                
                #verirficando de o diretório realmente foi criado...
                if (self.VerificaDiretorioExiste(caminhoDiretorio.strip()) == True):
                    return True
            else:
                return True
        else:
            raise Exception("Caminho para criar o diretorio raiz, não foi informado!")
        return False
    # CriaDiretorio

    def ExcluiDiretorio(self, caminhoDiretorio=""):
        #fazer import shutil
        if(caminhoDiretorio.strip() != ""):
            if (self.VerificaDiretorioExiste(caminhoDiretorio.strip()) == True):
                try:
                    shutil.rmtree(caminhoDiretorio.strip(), ignore_errors=True)
                except:
                    raise Exception ("Processo de exclusão do diretorio " + caminhoDiretorio.strip() + " falhou.")
                if (self.VerificaDiretorioExiste(caminhoDiretorio.strip())):
                    return False
                else:
                    return True
        else:
            raise Exception ("Caminho para excluir o diretorio raiz, não foi informado!")
        return False
    # ExcluiDiretorio

    def ExcluiArquivo(self, caminhoDiretorio, nomeArquivo):
        try:
            if (caminhoDiretorio.strip() == ""):
                return False
            if (nomeArquivo.strip() == ""):
                return False
            if (self.VerificaDiretorioExiste(caminhoDiretorio) == False):
                return False
            if (self.VerificarArquivoContemDiretorio(caminhoDiretorio, nomeArquivo) == False):
                return False
            os.remove(caminhoDiretorio.upper() +'/'+ nomeArquivo.upper())
            return True
        except:
            return False
    # ExcluiArquivo

    def VerificarArquivoContemDiretorio(self, caminhoDiretorio, nomeArquivo):
        if(self.VerificaDiretorioExiste(caminhoDiretorio)== True):
            if(nomeArquivo != ""):
                for p, _, files in os.walk(os.path.abspath(caminhoDiretorio)):
                    for file in files:
                        if(str(file).upper() == nomeArquivo.upper()):
                            return True
        return False
    # VerificarArquivoContemDiretorio
    
    def RetornaDataHoraSemCaracteres(self):
        dataAtual = datetime.datetime.now()
        return(str(dataAtual)[:str(dataAtual).index(".")].replace("-", "").replace(":", "").replace(" ", ""))
    # RetornaDataHoraSemCaracteres

    def RetornaMesPorEscrito(self, mesInformado):
        if (mesInformado == 1):
            mesPorEscrito = "JANEIRO"
        elif (mesInformado == 2):
            mesPorEscrito = "FEVEREIRO"
        elif (mesInformado == 3):
            mesPorEscrito = "MARÇO"
        elif (mesInformado == 4):
            mesPorEscrito = "ABRIL"
        elif (mesInformado == 5):
            mesPorEscrito = "MAIO"
        elif (mesInformado == 6):
            mesPorEscrito = "JUNHO"
        elif (mesInformado == 7):
            mesPorEscrito = "JULHO"
        elif (mesInformado == 8):
            mesPorEscrito = "AGOSTO"
        elif (mesInformado == 9):
            mesPorEscrito = "SETEMBRO"
        elif (mesInformado == 10):
            mesPorEscrito = "OUTUBRO"
        elif (mesInformado == 11):
            mesPorEscrito = "NOVEMBRO"
        elif (mesInformado == 12):
            mesPorEscrito = "DEZEMBRO"
        else:
            return "Mês informado inválido"
        return mesPorEscrito
    # RetornaMesPorEscrito

    def RetornaIndiceMes(self, mesInformado):
        if (mesInformado.upper() == 'JANEIRO'):
            idxMesSelecionado = 1
        elif (mesInformado.upper() == 'FEVEREIRO'):
            idxMesSelecionado = 2
        elif (mesInformado.upper() == 'MARÇO'):
            idxMesSelecionado = 3
        elif (mesInformado.upper() == 'ABRIL'):
            idxMesSelecionado = 4
        elif (mesInformado.upper() == 'MAIO'):
            idxMesSelecionado = 5
        elif (mesInformado.upper() == 'JUNHO'):
            idxMesSelecionado = 6
        elif (mesInformado.upper() == 'JULHO'):
            idxMesSelecionado = 7
        elif (mesInformado.upper() == 'AGOSTO'):
            idxMesSelecionado = 8
        elif (mesInformado.upper() == 'SETEMBRO'):
            idxMesSelecionado = 9
        elif (mesInformado.upper() == 'OUTUBRO'):
            idxMesSelecionado = 10
        elif (mesInformado.upper() == 'NOVEMBRO'):
            idxMesSelecionado = 11
        elif (mesInformado.upper() == 'DEZEMBRO'):
            idxMesSelecionado = 12
        else:
            return 'Mês informado inválido'
        return idxMesSelecionado
    # RetornaMesPorEscrito
    
    def GeradorAutomaticoCpf(self):
        # Gera os numeros randonomicos ;)
        n1 = random.randrange(10)
        n2 = random.randrange(10)
        n3 = random.randrange(10)
        n4 = random.randrange(10)
        n5 = random.randrange(10)
        n6 = random.randrange(10)
        n7 = random.randrange(10)
        n8 = random.randrange(10)
        n9 = random.randrange(10)

        # Contas e mais contas, dividi pra fica mais bonitinho
        a1 = n9 * 2
        a2 = n8 * 3
        a3 = n7 * 4
        a4 = n6 * 5
        a5 = n5 * 6
        a6 = n4 * 7
        a7 = n3 * 8
        a8 = n2 * 9
        a9 = n1 * 10

        d1 = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9
        d1 = 11 - round(d1 % 11)

        # Caso d1 seja maior que 10, o que não pode, ele deve ser
        # igualado a 0
        if d1 >= 10:
            d1 = 0

        a1 = d1 * 2
        a2 = n9 * 3
        a3 = n8 * 4
        a4 = n7 * 5
        a5 = n6 * 6
        a6 = n5 * 7
        a7 = n4 * 8
        a8 = n3 * 9
        a9 = n2 * 10
        a10 = n1 * 11

        d2 = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10
        d2 = 11 - round(d2 % 11)

        if d2 >= 10:
            d2 = 0

        return "{}{}{}{}{}{}{}{}{}{}{}".format(n1, n2, n3,  n4, n5, n6,  n7, n8, n9,  d1, d2)
    
#   Fim da função Gera CPF     

#   Objetivo: Cria/Edita arquivos Json
    def EditarJason(self, path, texto, modo):
        arq = open(path, modo)
        arq.write(str(texto))
        arq.close()