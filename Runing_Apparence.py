#Importando Arquivos Py
import Variaveis
import pushyb
import Conversor

#Importando Librearias
import time

Captar_Valor_Final = Variaveis.Valor_Final_pix

if __name__ == "__main__":
    import Nivelador_de_Processos

    #Executando Módulo de Inicialização
    for i in Variaveis.inciando_list:
        print(i)
        time.sleep(Variaveis.Sleep_time) # Atraso configurado em Variaveis
    

    
    #Captando Valor Final1
    Captar_Valor_Final = pushyb.Captar_Valor_Final(Captar_Valor_Final)
    Captar_Valor_Final = Conversor.tratar_valor_fina_input(Captar_Valor_Final)
    Variaveis.log.append(f"Valor Final: R$ {Captar_Valor_Final / 100:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    #Atualizando Valor Final
    Variaveis.Valor_Final_pix = Captar_Valor_Final

    #Executando Nivelador de Processos
    Variaveis.ID_NivelamentoContrl = 2
    Nivelador_de_Processos.Nivelamento_de_Solo()
  

    for log_atual in Variaveis.log:
        print(log_atual)
        time.sleep(Variaveis.Sleep_time) # Atraso configurado em Variaveis

    print(Variaveis.log_org)
    print(Variaveis.Status_QRCode)
    print(Variaveis.log_org)

    def finish():
        Variaveis.ID_NivelamentoContrl = 2
        print(f"Nivel: {Variaveis.ID_NivelamentoContrl}")
        print("Ultima Fase!")
        Nivelador_de_Processos.Nivelamento_de_Solo()

    finish()
 







#Atualizando Valor Final
Variaveis.Valor_Final_pix = Captar_Valor_Final
