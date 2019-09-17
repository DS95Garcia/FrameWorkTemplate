#   --------------------------------------------------------------------------   #
#   -                          DEFINIÇÕES INICIAIS                           -   #
#   --------------------------------------------------------------------------   #
from util.collection import *

class fSelenium():
    def __init__(self):
        super().__init__()
   
#   --------------------------------------------------------------------------   #
#   -                    DOCUMENTAÇÃO DAS FUNCIONALIDADES                    -   #
#   --------------------------------------------------------------------------   #

    def SelecionarItemDaLista(self, by, elemento, SelectType, options, optionalElemento = None, optionalPararAplicacaoNoErro = True, optionalNumeroDeTentativas = 30):
        # Este método é usado para selecionar um item de uma lista
        # dropdown list ou um combobox */
        checkDeObjeto = False
        numeroTentativas = optionalNumeroDeTentativas
        while(numeroTentativas >= 0):
            try:
                if (optionalElemento != None):
                    elementoSelecionado = optionalElemento.find_element(by,elemento)
                else:
                    elementoSelecionado = self.driver.find_element(by,elemento)
                    
                if (SelectType.value == 1):
                    try:
                        Select(elementoSelecionado).select_by_index(options)
                       
                    except Exception:
                        raise Exception("[Por favor, informe um indice valido do combo para selecionar o item.]")
                    break
                elif (SelectType.value == 2):
                    Select(elementoSelecionado).select_by_visible_text(str(options))
                    break
                elif (SelectType.value == 3):
                    Select(elementoSelecionado).select_by_value(options)
                    
                    break
                else:
                    raise Exception("[Não foi possível selecionar o item na lista.]")
                    break

                numeroTentativas = -2
                checkDeObjeto = True
            except Exception:
                pass
            
            if (checkDeObjeto == False):
                time.sleep(1)
                numeroTentativas = numeroTentativas - 1
                
        if (numeroTentativas == -1):
            if (optionalPararAplicacaoNoErro == True):
                if (optionalElemento != None):
                    raise Exception("[Não foi possível interar com o objeto: (Name:"+optionalElemento.GetAttribute("name") + ", ID: "+ optionalElemento.GetAttribute("id") + ", Class: "+ optionalElemento.GetAttribute("class") +")]")
                else:
                    raise Exception("[Não foi possível interar com o objeto: " + elemento +" ]")
    # Fim função SelecionarItemdaLista
    
    # Função DigitarTexto
    def DigitarTexto(self,by,nomeObjeto,text,optionalElemento = None,optionalPararAplicacaoNoErro = True,optionalNumeroDeTentativas = 30):
        elemento = None
        checkDeObjeto = False
        numeroTentativas = optionalNumeroDeTentativas
        
        while(numeroTentativas >= 0):
            try:
                if(optionalElemento is None):
                    elemento = self.driver.find_element(by,nomeObjeto)                                  
                else:
                    elemento = optionalElemento.find_element(by,nomeObjeto)
                    
                if(elemento.is_displayed and elemento.is_enabled()):
                    elemento.clear()    
                    elemento.send_keys(text.strip())

                numeroTentativas = -2
                checkDeObjeto = True
            except Exception:
                pass
            
            if (checkDeObjeto == False):
                time.sleep(1)
                numeroTentativas = numeroTentativas -1               
                    
        if (checkDeObjeto == False):
                if (optionalPararAplicacaoNoErro == True):
                    if(optionalElemento != None):
                        raise Exception("Não foi possível interar com o objeto: (Name: " + optionalElemento.get_atribute("name") + ", ID: "+ optionalElemento.get_atribute("id") + ", Class: "+ optionalElemento.get_atribute("class") +")]")
                    else:
                        raise Exception("[ Não foi possível interagir com o objeto: " + nomeObjeto +" ]\n")
    # Fim da função digitarTexto
    
    # Função click                    
    def Click(self, by, nomeObjeto, optionalElemento = None, optionalPararAplicacaoNoErro = True, optionalNumeroDeTentativas = 30):
        elemento = None
        checkDeObjeto = False
        numeroTentativas = optionalNumeroDeTentativas
        
        action = ActionChains(self.driver)

        while (numeroTentativas >= 0):
            try: 
                if (optionalElemento == None):
                    elemento = self.driver.find_element(by,nomeObjeto)                    
                else:
                    elemento = optionalElemento.find_element(by,nomeObjeto)

                if(elemento != None and elemento.is_displayed and elemento.is_enabled()):                    
                    action.move_to_element(elemento).perform()
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", elemento)
                    elemento.click()
                    
                    numeroTentativas = -2
                    checkDeObjeto = True
            except Exception:
                pass  
                            
            if (checkDeObjeto == False):
                time.sleep(1)
                numeroTentativas = numeroTentativas -1
        
        if(numeroTentativas == -1):
            if(optionalPararAplicacaoNoErro == True):
                if(optionalElemento != None):
                    try:
                        raise Exception("[Não foi possível interar com o objeto: (Name: " + optionalElemento.get_attribute("name") + ", ID: "+ optionalElemento.get_attribute("id") + ", Class: "+ optionalElemento.get_attribute("class") +")]")
                    except Exception:
                        raise Exception("[ Não foi possível interagir com o objeto: " + nomeObjeto +" ]\n")
                else:
                    raise Exception("[ Não foi possível Manipular com o objeto: " + nomeObjeto +" ]")
    # Fim da função click

    # Função encontrar element ( executar pagedown até achar)
    def encontrarElemento(self,by, nomeObjeto,optionalElemento):
        nTentativas = 30
        
        if (optionalElemento == None):
            elemento = self.driver.find_element(by,nomeObjeto)     
        else:
            elemento = optionalElemento.find_element(by,nomeObjeto)    
                    
        while (nTentativas > 0):
            try:
                if (elemento.is_displayed() and elemento.is_enabled()):
                    return True
                else:
                    action = ActionChains(self.driver)
                    action.send_keys(Keys.PAGE_DOWN).perform()
                    nTentativas = nTentativas - 1
            except:
                pass
        
        return False
    # fim da função EncontrarElemento
    
    def TrocaFrame(self, nomeFrame, optionalPararAplicacaoNoErro = True, optionalNumeroDeTentativas = 30):
        numeroTentativas = optionalNumeroDeTentativas
        
        while(numeroTentativas >= 0):
            try:
                self.driver.switch_to.frame(str(nomeFrame))
                numeroTentativas = -2
            except:
                time.sleep(1)
                numeroTentativas = numeroTentativas - 1

        if (numeroTentativas == -1):
            if (optionalPararAplicacaoNoErro == True):
                raise("[Não foi possível realizar a troca do frame para: " + str(nomeFrame) + "]")
    # TrocaFrame
    
    def ElementoEstaVisivel(self, By, elemento, optionalNumeroDeTentativas = 30):
        # Este método tem como função, fazer um numero determinado de tentativas e verificar se o objeto está visivel na tela

        numeroTentativas = optionalNumeroDeTentativas;

        if(self.ElementoEstaHabilitado(By, elemento)):
            while (numeroTentativas >= 0):
                try:
                    if (self.driver.find_element(By, elemento) != None):
                        return self.driver.find_element(By, elemento).is_displayed                    
                except:
                    pass

                if(numeroTentativas >= 0):
                    time.Sleep(1000)

                numeroTentativas = numeroTentativas - 1

        return False
    # ElementoEstaVisivel    
    
    def ElementoEstaHabilitado(self, By, elemento, optionalNumeroDeTentativas = 30):
        numeroTentativas = optionalNumeroDeTentativas;

        while (numeroTentativas >= 0):
            try:
                if (self.driver.FindElements(By, elemento) != None):
                    return self.driver.find_element(By, elemento).is_enabled()                
            except:
                pass

            time.sleep(1000);
            numeroTentativas = numeroTentativas - 1

        return False;
    # ElementoEstaHabilitado   
    
    def VerificaElemento(self, By, elemento, optionalNomeFrame = "", optionalNumeroDeTentativas = 30):
        # Este método tem como função, fazer um numero determinado de tentativas em busca do objeto dentro do site
        #    em caso em que o objeto é encontrado retorna true, caso contrário false.

        numeroTentativas = optionalNumeroDeTentativas

        while (numeroTentativas >= 0):
            try:
                if (optionalNomeFrame == ""):
                    self.driver.switch_to.default_content()
                else:
                    self.driver.SwitchTo().frame(optionalNomeFrame.Trim())

                return self.driver.find_element(By, elemento)
            except:
                pass

            time.sleep(1)
            numeroTentativas = numeroTentativas - 1        

        return None;
    # VerificaElemento 
    
    def AguardarElementoParaClicar(self, By, locatorValue, optionalElemento = None, optionalPararAplicacaoNoErro = True, optionalNumeroDeTentativas = 30):
        # Este método é usado para aguardar o elemento estar pronto para clicar 

        elemento = None
        checkDeObjeto = False
        numeroTentativas = optionalNumeroDeTentativas

        while (numeroTentativas >= 0):
            try:
                if (optionalElemento == None):
                    elemento = self.find_element(By, locatorValue)
                else:
                    elemento = optionalElemento.find_element(By, locatorValue)

                if(elemento != None and elemento.is_displayed and elemento.is_enabled()): 
                    numeroTentativas = numeroTentativas - 2
                    checkDeObjeto = True
            except:
                pass

            if (checkDeObjeto == False):
                time.sleep(1);
                numeroTentativas = numeroTentativas - 1

        if (checkDeObjeto == False):
            if (optionalPararAplicacaoNoErro == True):
                if(optionalElemento != None):
                    raise("[Não foi possível interar com o objeto: (Name: " + optionalElemento.GetAttribute("name") + ", ID: "+ optionalElemento.GetAttribute("id") + ", Class: "+ optionalElemento.GetAttribute("class") +")]")
                else:
                    raise("[Não é possível manipular o objeto: (" + str(locatorValue) +")]")
    # AguardarElementoParaClicar  
    
    def AguardarEnquantoPaginaCarrega(self, optionalPararAplicacaoNoErro = False):
        page_state = self.driver.execute_script('return document.readyState;')
        return page_state == 'complete'    
    # AguardarEnquantoPaginaCarrega      