
import Variaveis




if __name__ != "__main__":# apenas para evitar execução direta
    import inspect
    import Variaveis
    import time
 

 
    def deuruim():
        caller = inspect.stack()[1].filename.split("\\")[-1]
        origem = inspect.stack()[-1].filename.split("\\")[-1]

        ##print(f"[Nox] Chamador: {caller}")
        ##print(f"[Nox] Origem final: {origem}")
        

        if caller != "Nivelador_de_Processos.py" or Variaveis.ID_NivelamentoContrl != 3:  

            Variaveis.log.append("[Nox] Finalizando com Sucesso!")  
            return        
        
        for Log_Erro_atual in Variaveis.log_Erros:
            print(Log_Erro_atual)
            time.sleep(Variaveis.Sleep_time) # Atraso configurado em Variaveis
     